#!/usr/bin/env python3

try:
    from selenium.common.exceptions import NoSuchElementException
    from .scraping_utilities import Scraping_utilities
    from .driver_utilities import Utilities    
    import sys
except Exception as ex:
    print(ex)

class Finder():
    """
    Holds the collections of methods that finds element of the facebook's posts using selenium's webdriver's methods  
    """
    @staticmethod
    def __find_status(post):
        """finds URL of the post, then extracts link from that URL and returns it"""
        try:
            #aim is to find element that looks like <a href="URL" class="_5pcq"></a>
            #after finding that element, get it's href value and pass it to different method that extracts post_id from that href
            status_link = post.find_element_by_class_name("_5pcq").get_attribute("href")  
            #extract out post id from post's url
            status = Scraping_utilities._Scraping_utilities__extract_id_from_link(status_link)
                           
        except NoSuchElementException:
            #if element is not found
            status = "NA"
            
        except Exception as ex:
            print("error at find_status method : {}".format(ex))
            status = "NA"
        
        return status
    
    @staticmethod
    def __find_share(post):
        """finds shares count of the facebook post using selenium's webdriver's method"""
        try:
            #aim is to find element that have datatest-id attribute as UFI2SharesCount/root 
            shares = post.find_element_by_css_selector("[data-testid='UFI2SharesCount/root']").get_attribute('textContent')
            shares = Scraping_utilities._Scraping_utilities__extract_numbers(shares)
            
        except NoSuchElementException:
            #if element is not present that means there wasn't any shares
            shares = 0
            
        except Exception as ex:
            print("error at find_share method : {}".format(ex))
            shares = 0
            
        
        return shares

    @staticmethod
    def __find_reactions(post):
        """finds all reaction of the facebook post using selenium's webdriver's method"""
        try:
            #find element that have attribute aria-label as 'See who reacted to this
            reactions_all = post.find_element_by_css_selector('[aria-label="See who reacted to this"]')
        except NoSuchElementException:
            reactions_all = ""
        except Exception as ex:
            print("error at find_reactions method : {}".format(ex))
        return reactions_all
    
    @staticmethod
    def __find_comments(post):
        """finds comments count of the facebook post using selenium's webdriver's method"""
        try:
            comments = post.find_element_by_css_selector("a._3hg-").get_attribute('textContent')
            #extract numbers from text
            comments = Scraping_utilities._Scraping_utilities__extract_numbers(comments)
        except NoSuchElementException:
            comments = 0
        except Exception as ex:
            print("error at find_comments method : {}".format(ex))
            comments = 0

        return comments       
    
    @staticmethod
    def __find_content(post,driver):
        """finds content of the facebook post using selenium's webdriver's method"""
        try:
            post_content = post.find_element_by_css_selector('[data-testid="post_message"]')
            Utilities._Utilities__click_see_more(driver,post_content) #click 'see more' button to get hidden text as well
            post_content = Scraping_utilities._Scraping_utilities__extract_content(post_content)
        except NoSuchElementException:
            pass
            post_content = ""
        except Exception as ex:
            print("error at find_content method : {}".format(ex))
            post_content = ""
        return post_content

    
    @staticmethod
    def __find_posted_time(post):
        """finds posted time of the facebook post using selenium's webdriver's method"""
        try:
            #extract element that looks like <abbr class='_5ptz' data-utime="some unix timestamp"> </abbr>
            posted_time = post.find_element_by_css_selector("abbr._5ptz").get_attribute("data-utime")
        except Exception as ex:
            print("error at find_posted_time method : {}".format(ex))
            posted_time = ""
        return posted_time
    
    @staticmethod
    def __find_video_url(post,page_name,status):
        """finds video of the facebook post using selenium's webdriver's method"""
        try:
            #if video is found in the post, than create a video URL by concatenating post's id with page_name
            video_element = post.find_element_by_tag_name("video") 
            video = "https://www.facebook.com/{}/videos/{}".format(page_name,status)

        except NoSuchElementException:
            video = ""
            pass
        except Exception as ex:
            video = ""
            print("error at find_video_url method : {}".format(ex))

        return video
    
    @staticmethod
    def __find_image_url(post):
        """finds all image of the facebook post using selenium's webdriver's method"""
        try:
            #find all img tag that looks like <img class="scaledImageFitWidth img" src="">
            images = post.find_elements_by_css_selector("img.scaledImageFitWidth.img")
            #extract src attribute from all the img tag,store it in list
            sources = [image.get_attribute("src") for image in images] if len(images) > 0 else []
        except NoSuchElementException:
            sources = []
            pass
        except Exception as ex:
            print("error at find_image_url method : {}".format(ex))
            sources = []
    
        return sources

    @staticmethod
    def __find_all_posts(driver):
        """finds all posts of the facebook page using selenium's webdriver's method"""
        try:
            #find all posts that looks like <div class="userContentWrapper"> </div>
            all_posts = driver.find_elements_by_css_selector("div.userContentWrapper")
            return all_posts
        except NoSuchElementException:
            print("Cannot find any posts! Exiting!")
            #if this fails to find posts that means, code cannot move forward, as no post is found
            Utilities.__close_driver(driver)
            sys.exit(1)
        except Exception as ex:
            print("error at __find_all_posts method : {}".format(ex))
            Utilities.__close_driver(driver)
            sys.exit(1)

    @staticmethod
    def __find_name(driver):
        """finds name of the facebook page using selenium's webdriver's method"""
        try:
            name =  driver.find_element_by_class_name('_64-f').get_attribute('textContent')
            return name
        except Exception as ex:
            print("error at __find_name method : {}".format(ex))