#!/usr/bin/env python3
try:
    import facebook_page_scraper
    from selenium.common.exceptions import NoSuchElementException
    import json
    import csv
    import os
except Exception as ex:
    print(ex)

class Facebook_scraper:
    data_dict = {}  #this dictionary stores all post's data 
    
    #when we scroll and extract all posts,it may happens that we extract same posts over and over,so this lead to too much iteration
    #and waste time to iterate over and over the same post, to solve that,
    # problem I needed a data structure which 
    # 1) removes duplicates from itself automatically,
    # 2) provides search of element,
    # 3) compatible with list's unpacking to quickly add element inside itself from list 
    #  set() seems to be doing the work properly
    extracted_post = set() 
    #extracted_post contains all the posts that have been scraped before to avoid post duplication.
    
    retry = 10

    def __init__(self,page_name,posts_count="10",browser="chrome"):
        self.page_name = page_name
        self.posts_count = int(posts_count)
        self.URL = "https://www.facebook.com/pg/{}/posts".format(self.page_name)
        self.browser = browser
        self.driver = facebook_page_scraper.Initializer(self.browser).init()

    def scrap_to_json(self):
        
        self.driver.get(self.URL)
        
        facebook_page_scraper.Utilities._Utilities__close_error_popup(self.driver)
        facebook_page_scraper.Utilities._Utilities__wait_for_element_to_appear(self.driver)
        facebook_page_scraper.Utilities._Utilities__scroll_down(self.driver)
        facebook_page_scraper.Utilities._Utilities__close_popup(self.driver)
        
        while len(self.data_dict) <= self.posts_count:
        
            facebook_page_scraper.Utilities._Utilities__close_error_popup(self.driver)
            facebook_page_scraper.Utilities._Utilities__close_popup(self.driver)
            
            self.__find_elements()

            if self.__close_after_retry() is True:
                break
            
            
        
        facebook_page_scraper.Utilities._Utilities__close_driver(self.driver)
        
        self.data_dict = dict(list(self.data_dict.items())[0:int(self.posts_count)])
        
        return json.dumps(self.data_dict)    

    def __json_to_csv(self,filename,json_data,directory):
        
        os.chdir(directory)

        fieldnames = ['id','name','shares','likes','loves','wow','cares','sad','angry','haha','reactions_count','comments','content','video'
                    ,'image','post_url']
        with open("{}.csv".format(filename),'w',newline='') as data_file:
            writer = csv.DictWriter(data_file,fieldnames=fieldnames)

            writer.writeheader()

            for key in json_data:
                row = {'id': key,'name' : json_data[key]['name'],'shares':json_data[key]['shares'],
                'likes' : json_data[key]['reactions']['likes'],'loves' :  json_data[key]['reactions']['loves'],
                'wow' : json_data[key]['reactions']['wow'],'cares' : json_data[key]['reactions']['cares'],
                'sad' : json_data[key]['reactions']['sad'],'angry' : json_data[key]['reactions']['angry'],
                'haha' : json_data[key]['reactions']['haha'],'reactions_count' : json_data[key]['reaction_count'],
                'comments'  : json_data[key]['comments'],'content' : json_data[key]['content'],
                'video' : json_data[key]['video'],'image':json_data[key]['image'],'post_url' : json_data[key]['post_url']
                }   
                writer.writerow(row)

            data_file.close()

    def scrap_to_csv(self,filename,directory = os.getcwd()):
        data = self.scrap_to_json()
        self.__json_to_csv(filename,json.loads(data),directory)
        

    def __remove_duplicates(self,all_posts):
        """takes a list of posts and removes duplicates from it and returns the list"""
        if len(self.extracted_post) == 0:  #if self.extracted_post is empty that means it is first extraction
            self.extracted_post.update(all_posts) #if it does than just add all the elements from the lists to extracted_post set()
            return all_posts #return the all_posts without any changes as it is first time and no duplicate is present
        else:
            #if self.extracted posts have some element than compare it with all_posts's element and return a new list containing new element
            removed_duplicated =  [post for post in all_posts if post not in self.extracted_post] 
            self.extracted_post.update(all_posts)  #after removing duplicates, add all those new element to extracted_posts, as it  
            return removed_duplicated               #is set() it won't have duplicate elements
    
    def __close_after_retry(self):
        return self.retry <= 0


    def __no_post_found(self,all_posts):
        if len(all_posts) == 0:
            self.retry -= 1
        
    def __find_elements(self):
        all_posts = facebook_page_scraper.Finder._Finder__find_all_posts(self.driver)
        all_posts = self.__remove_duplicates(all_posts)

        name = facebook_page_scraper.Finder._Finder__find_name(self.driver)
        
        self.__no_post_found(all_posts)
        
        for post in all_posts:
            try:
                
                status = facebook_page_scraper.Finder._Finder__find_status(post)
                
                shares = facebook_page_scraper.Finder._Finder__find_share(post)
                
    
                reactions_all = facebook_page_scraper.Finder._Finder__find_reactions(post)

                all_hrefs_in_react = reactions_all.find_elements_by_tag_name("a") if type(reactions_all) != str else ""
                
                if type(all_hrefs_in_react) == list:
                    l = [i.get_attribute("aria-label") for i in all_hrefs_in_react]  
                else:
                    l = []
                
                likes = facebook_page_scraper.Scraping_utilities._Scraping_utilities__exists_in_list(l,"Like")
                likes = facebook_page_scraper.Scraping_utilities._Scraping_utilities__extract_numbers(likes[0]) if len(likes) > 0 else 0

                loves = facebook_page_scraper.Scraping_utilities._Scraping_utilities__exists_in_list(l,"Love") 
                loves = facebook_page_scraper.Scraping_utilities._Scraping_utilities__extract_numbers(loves[0]) if len(loves) > 0 else 0

                wow = facebook_page_scraper.Scraping_utilities._Scraping_utilities__exists_in_list(l,"Wow")
                wow = facebook_page_scraper.Scraping_utilities._Scraping_utilities__extract_numbers(wow[0]) if len(wow) > 0 else 0

                cares = facebook_page_scraper.Scraping_utilities._Scraping_utilities__exists_in_list(l,"Care")
                cares = facebook_page_scraper.Scraping_utilities._Scraping_utilities__extract_numbers(cares[0]) if len(cares) > 0 else 0

                sad = facebook_page_scraper.Scraping_utilities._Scraping_utilities__exists_in_list(l,"Sad")
                sad = facebook_page_scraper.Scraping_utilities._Scraping_utilities__extract_numbers(sad[0]) if len(sad) > 0 else 0

                angry = facebook_page_scraper.Scraping_utilities._Scraping_utilities__exists_in_list(l,"Angry")
                angry = facebook_page_scraper.Scraping_utilities._Scraping_utilities__extract_numbers(angry[0]) if len(angry) > 0 else 0
                
                haha = facebook_page_scraper.Scraping_utilities._Scraping_utilities__exists_in_list(l,"Haha")
                haha = facebook_page_scraper.Scraping_utilities._Scraping_utilities__extract_numbers(haha[0]) if len(haha) > 0 else 0
        
                reactions = {"likes" : likes,"loves" : loves,"wow":wow,"cares" : cares,"sad":sad,"angry":
                angry,"haha" : haha}

                total_reaction_count = facebook_page_scraper.Scraping_utilities._Scraping_utilities__count_reaction(reactions)
                
                comments = facebook_page_scraper.Finder._Finder__find_comments(post)
                
                post_content = facebook_page_scraper.Finder._Finder__find_content(post,self.driver)
                
                posted_time = facebook_page_scraper.Finder._Finder__find_posted_time(post)
                posted_time = facebook_page_scraper.Scraping_utilities._Scraping_utilities__convert_time(posted_time)
                               
                video = facebook_page_scraper.Finder._Finder__find_video_url(post,self.page_name,status)
                
                image = facebook_page_scraper.Finder._Finder__find_image_url(post)
                
                post_url = "https://www.facebook.com/{}/posts/{}".format(self.page_name,status)
                
                self.data_dict[status] = {
                    "name" : name,
                    "shares" : shares,
                    "reactions" : reactions,
                    "reaction_count" : total_reaction_count,
                    "comments" : comments,
                    "content" : post_content,
                    "posted_on" : posted_time,
                    "video" : video,
                    "image" : image,
                    "post_url" :post_url
                
                }
        
            except Exception as ex:
                print("error at find_elements method : {}".format(ex))


