#!/usr/bin/env python3
try:
    import facebook_page_scraper
    import time
    from selenium.common.exceptions import NoSuchElementException,WebDriverException,TimeoutException,StaleElementReferenceException
    import re
except Exception as ex:
    print(ex)

class Facebook_scraper:
    data_dict = {}
    
    def __init__(self,page_name,posts_count,browser="firefox"):
        self.page_name = page_name
        self.posts_count = int(posts_count)
        self.URL = "https://www.facebook.com/pg/{}/posts/?ref=page_internal".format(self.page_name)
        self.browser = browser
        self.driver = facebook_page_scraper.Initializer(self.browser).init()

    def __is_time_up(self,seconds):
        return seconds > 800

    def __close_after_timeup(self,seconds):
        if self.__is_time_up(seconds):
           facebook_page_scraper.Utilities._Utilities__close_driver(self.driver)
           return True
        return False    

    def scrap(self):
        
        self.driver.get(self.URL)
        
        execution_starts_at = time.time()
        facebook_page_scraper.Utilities._Utilities__close_error_popup(self.driver)
        facebook_page_scraper.Utilities._Utilities__wait_for_element_to_appear(self.driver)
        facebook_page_scraper.Utilities._Utilities__scroll_down(self.driver)
        facebook_page_scraper.Utilities._Utilities__close_popup(self.driver)
        current_time = time.time()

        while len(self.data_dict) <= self.posts_count:
            current_time = time.time()

            facebook_page_scraper.Utilities._Utilities__close_error_popup(self.driver)
            facebook_page_scraper.Utilities._Utilities__close_popup(self.driver)
            
            self.__find_elements()
            if self.__close_after_timeup(current_time-execution_starts_at):
                break
            facebook_page_scraper.Utilities._Utilities__scroll_down(self.driver)
        
        facebook_page_scraper.Utilities._Utilities__close_driver(self.driver)
        
        return self.data_dict    

    def __extract_id_from_link(self,link):
        status = "NA"
        if "posts/" in link:
            status = link.split('/')[5].split('?')[0]
        elif "photos/" in link:
            status = link.split("/")[-2]
        else:
            status = link.split('/')[-1].split('=')[-3].split('&')[0]
        if "/videos/" in link:
            status = link.split("/")[5]
        return status

    def extract_numbers(self,string):
        return re.findall("\d+", string)[0]

    def exists_in_list(self,li,word):
        return [substring for substring in li if word in substring]

    def __find_elements(self):
        all_posts = self.driver.find_elements_by_css_selector("div.userContentWrapper")
        for post in all_posts:
            try:
                
                try:
                    status_link = post.find_element_by_class_name("_5pcq").get_attribute("href")
                    status = self.__extract_id_from_link(status_link)               
                except NoSuchElementException:
                
                    status = "NA"
                except Exception as ex:
                    status = "NA"
                
                #finding share element in the post
                try:
                    shares = post.find_element_by_css_selector("[data-testid='UFI2SharesCount/root']").get_attribute('textContent')
                    shares = self.extract_numbers(shares)
                except NoSuchElementException:
                    shares = "0"
                except Exception as ex:
                    print(ex)
                    shares = "0"
                
                
                #finding all reactions counts of the posts
                try:
                    reactions_all = post.find_element_by_css_selector('[aria-label="See who reacted to this"]')
                except NoSuchElementException:
                    reactions_all = ""
                
                all_hrefs_in_react = reactions_all.find_elements_by_tag_name("a") if type(reactions_all) != str else ""
                
                if type(all_hrefs_in_react) == list:
                    l = [i.get_attribute("aria-label") for i in all_hrefs_in_react]  
                else:
                    l = []
                
                likes = self.exists_in_list(l,"Like")
                likes = self.extract_numbers(likes[0]) if len(likes) > 0 else "0"

                loves = self.exists_in_list(l,"Love") 
                loves = self.extract_numbers(loves[0]) if len(loves) > 0 else "0"

                wow = self.exists_in_list(l,"Wow")
                wow = self.extract_numbers(wow[0]) if len(wow) > 0 else "0"

                cares = self.exists_in_list(l,"Care")
                cares = self.extract_numbers(cares[0]) if len(cares) > 0 else "0"

                sad = self.exists_in_list(l,"Sad")
                sad = self.extract_numbers(sad[0]) if len(sad) > 0 else "0"

                angry = self.exists_in_list(l,"Angry")
                angry = self.extract_numbers(angry[0]) if len(angry) > 0 else "0"
                
                haha = self.exists_in_list(l,"Haha")
                haha = self.extract_numbers(haha[0]) if len(haha) > 0 else "0"
        
                reactions = {"likes" : likes,"loves" : loves,"wow":wow,"cares" : cares,"sad":sad,"angry":
                angry,"haha" : haha}
                
                try:
                    anchor = post.find_element_by_class_name('_4vn1')                           
                except NoSuchElementException:
                    print("Anhor not found")
                    anchor = "NA"
                
                
                try:
                    comments = anchor.find_element_by_css_selector("a._3hg-._42ft").get_attribute('textContent')
                except Exception as ex:
                    print(ex)
                    comments = "0"

                self.data_dict[status] = {
                "id" : status,
                "shares" : shares,
                "reactions" : reactions,
                "comments" : comments
                }
            except Exception as ex:
                print(ex)


