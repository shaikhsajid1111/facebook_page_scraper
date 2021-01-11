#!/usr/bin/env python3
try:
    from .driver_initialization import Initializer
    from .driver_utilities import Utilities
    from .element_finder import Finder
    from .scraping_utilities import Scraping_utilities
    from selenium.common.exceptions import NoSuchElementException
    import json
    import csv
    import os

except Exception as ex:
    print(ex)

class Facebook_scraper:
    __data_dict = {}  #this dictionary stores all post's data 
    
    #when we scroll and extract all posts,it may happens that we extract same posts over and over,so this lead to too much iteration
    #and waste time to iterate over and over the same post, to solve that,
    # problem I needed a data structure which 
    # 1) removes duplicates from itself automatically,
    # 2) provides search of element,
    # 3) compatible with list's unpacking to quickly add element inside itself from list 
    #  set() seems to be doing the work properly
    
    #__extracted_post contains all the post's ID that have been scraped before and as it set() it avoids post's ID duplication.
    __extracted_post = set() 
    

    #condition,
    #1) if we reach bottom of the page and post is not longer available, and we don't meet the number of posts that we need to find
    #2) if we were given wrong page_name, and it does not exists in fb than no post will exist.
    #with above condition being true, the crawler will keep on scrolling the page to find posts 
    # and it will stuck in infinite loop, which may cause machine to crash
    #to solve the problem, I have declared a class member "retry",assigned it value 10.
    #it checks 'retry' times if posts does not exists.
    # __no_post_found method subtracts -1 every time the if post is not found.
    #on each iteration __close_after_retry is called to check if retry have turned to 0
    # if it returns true,it will break the loop. After coming out of loop,driver will be closed and it will return post whatever was found
    
    retry = 10

    def __init__(self,page_name,posts_count=10,browser="chrome"):
        self.page_name = page_name
        self.posts_count = int(posts_count)
        self.URL = "https://www.facebook.com/pg/{}/posts".format(self.page_name)
        self.browser = browser
        self.__driver = ''

    def __start_driver(self):
        """changes the class member __driver value to driver on call"""
        self.__driver = Initializer(self.browser).init()

    def scrap_to_json(self):
        #call the __start_driver and override class member __driver to webdriver's instance
        self.__start_driver()
        #navigate to URL
        self.__driver.get(self.URL)
        #sometimes we get popup that says "your request couldn't be processed", however
        #posts are loading in background if popup is closed, so call this method in case if it pops up.
        Utilities._Utilities__close_error_popup(self.__driver) 
        #wait for post to load 
        Utilities._Utilities__wait_for_element_to_appear(self.__driver)
        #scroll down to bottom most
        Utilities._Utilities__scroll_down(self.__driver)
        #while scrolling, wait for login popup to show, it can be skipped by clicking "Not Now" button
        Utilities._Utilities__close_popup(self.__driver)
        
        while len(self.__data_dict) <= self.posts_count:

            #if during scrolling any of error or signup popup shows 
            Utilities._Utilities__close_error_popup(self.__driver)
            Utilities._Utilities__close_popup(self.__driver)
            
            self.__find_elements()

            if self.__close_after_retry() is True:
                #keep a check if posts are available, if retry is 0, than it breaks loop
                break
        #close the browser window after job is done.
        Utilities._Utilities__close_driver(self.__driver)
        #dict trimming, might happen that we find more posts than it was asked, so just trim it
        self.__data_dict = dict(list(self.__data_dict.items())[0:int(self.posts_count)])
        
        return json.dumps(self.__data_dict)    

    def __json_to_csv(self,filename,json_data,directory):
        
        os.chdir(directory) #change working directory to given directory
        #headers of the CSV file
        fieldnames = ['id','name','shares','likes','loves','wow','cares','sad','angry','haha','reactions_count','comments','content','video'
                    ,'image','post_url']
        #open and start writing to CSV files
        with open("{}.csv".format(filename),'w',newline='',encoding="utf-8") as data_file:
            writer = csv.DictWriter(data_file,fieldnames=fieldnames) #instantiate DictWriter for writing CSV file 

            writer.writeheader() #write headers to CSV file
            #iterate over entire dictionary, write each posts as a row to CSV file
            for key in json_data:
                #parse post in a dictionary and write it as a single row
                row = {'id': key,'name' : json_data[key]['name'],'shares':json_data[key]['shares'],
                'likes' : json_data[key]['reactions']['likes'],'loves' :  json_data[key]['reactions']['loves'],
                'wow' : json_data[key]['reactions']['wow'],'cares' : json_data[key]['reactions']['cares'],
                'sad' : json_data[key]['reactions']['sad'],'angry' : json_data[key]['reactions']['angry'],
                'haha' : json_data[key]['reactions']['haha'],'reactions_count' : json_data[key]['reaction_count'],
                'comments'  : json_data[key]['comments'],'content' : json_data[key]['content'],
                'video' : json_data[key]['video'],'image': " ".join(json_data[key]['image']) 
                ,'post_url' : json_data[key]['post_url']
                }   
                writer.writerow(row) #write row to CSV file

            data_file.close() #after writing close the file

    def scrap_to_csv(self,filename,directory = os.getcwd()):
        try:
            data = self.scrap_to_json()   #get the data in JSON format from the same class method 
            self.__json_to_csv(filename,json.loads(data),directory) #convert it and write to CSV 
            return True
        except Exception as ex:
            print(ex)
            return False

    def __remove_duplicates(self,all_posts):
        """takes a list of posts and removes duplicates from it and returns the list"""
        if len(self.__extracted_post) == 0:  #if self.__extracted_post is empty that means it is first extraction
            self.__extracted_post.update(all_posts) #if it does than just add all the elements from the lists to __extracted_post set()
            return all_posts #return the all_posts without any changes as it is first time and no duplicate is present
        else:
            #if self.extracted posts have some element than compare it with all_posts's element and return a new list containing new element
            removed_duplicated =  [post for post in all_posts if post not in self.__extracted_post] 
            self.__extracted_post.update(all_posts)  #after removing duplicates, add all those new element to extracted_posts, as it  
            return removed_duplicated               #is set() it won't have duplicate elements
    
    def __close_after_retry(self):
        """returns if class member retry is 0"""
        return self.retry <= 0


    def __no_post_found(self,all_posts):
        """if all_posts were found to be length of 0"""
        if len(all_posts) == 0:
            #if length of posts is 0,decrement retry by 1
            self.retry -= 1
        
    def __find_elements(self):
        """find elements of posts and add them to data_dict"""
        all_posts = Finder._Finder__find_all_posts(self.__driver) #find all posts
        all_posts = self.__remove_duplicates(all_posts) #remove duplicates from the list

        name = Finder._Finder__find_name(self.__driver) #find name element
        
        self.__no_post_found(all_posts)  #after removing duplicates if length is 0, retry will decrease by 1
        #iterate over all the posts and find details from the same
        for post in all_posts:
            try:
                #find post ID from post
                status = Finder._Finder__find_status(post)
                #find share from the post
                shares = Finder._Finder__find_share(post)
                #find all reactions 
                reactions_all = Finder._Finder__find_reactions(post)
                #find all anchor tags in reactions_all list
                all_hrefs_in_react = reactions_all.find_elements_by_tag_name("a") if type(reactions_all) != str else ""
                #if hrefs were found
                #all_hrefs contains elements like
                #["5 comments","54 Likes"] and so on
                if type(all_hrefs_in_react) == list:
                    l = [i.get_attribute("aria-label") for i in all_hrefs_in_react]  
                else:
                    l = []
                #extract that aria-label from all_hrefs_in_react list and than extract number from them seperately
                #if Like aria-label is in the list, than extract it and extract numbers from that text
                
                likes = Scraping_utilities._Scraping_utilities__exists_in_list(l,"Like")
                likes = Scraping_utilities._Scraping_utilities__extract_numbers(likes[0]) if len(likes) > 0 else 0

                #if Love aria-label is in the list, than extract it and extract numbers from that text
                loves = Scraping_utilities._Scraping_utilities__exists_in_list(l,"Love") 
                loves = Scraping_utilities._Scraping_utilities__extract_numbers(loves[0]) if len(loves) > 0 else 0
            
                #if Wow aria-label is in the list, than extract it and extract numbers from that text
                wow = Scraping_utilities._Scraping_utilities__exists_in_list(l,"Wow")
                wow = Scraping_utilities._Scraping_utilities__extract_numbers(wow[0]) if len(wow) > 0 else 0
                #if Care aria-label is in the list, than extract it and extract numbers from that text
                cares = Scraping_utilities._Scraping_utilities__exists_in_list(l,"Care")
                cares = Scraping_utilities._Scraping_utilities__extract_numbers(cares[0]) if len(cares) > 0 else 0
                #if Sad aria-label is in the list, than extract it and extract numbers from that text
                sad = Scraping_utilities._Scraping_utilities__exists_in_list(l,"Sad")
                sad = Scraping_utilities._Scraping_utilities__extract_numbers(sad[0]) if len(sad) > 0 else 0
                #if Angry aria-label is in the list, than extract it and extract numbers from that text
                angry = Scraping_utilities._Scraping_utilities__exists_in_list(l,"Angry")
                angry = Scraping_utilities._Scraping_utilities__extract_numbers(angry[0]) if len(angry) > 0 else 0
                #if Haha aria-label is in the list, than extract it and extract numbers from that text
                haha = Scraping_utilities._Scraping_utilities__exists_in_list(l,"Haha")
                haha = Scraping_utilities._Scraping_utilities__extract_numbers(haha[0]) if len(haha) > 0 else 0

                #converting all reactions to numbers
                #e,g reactions may contain counts like "5k","5m", so converting them to actual number
                likes = Scraping_utilities._Scraping_utilities__value_to_float(likes)
                loves = Scraping_utilities._Scraping_utilities__value_to_float(loves)
                wow = Scraping_utilities._Scraping_utilities__value_to_float(wow)
                cares = Scraping_utilities._Scraping_utilities__value_to_float(cares)
                sad = Scraping_utilities._Scraping_utilities__value_to_float(sad)
                angry = Scraping_utilities._Scraping_utilities__value_to_float(angry)
                haha = Scraping_utilities._Scraping_utilities__value_to_float(haha)
                
                reactions = {"likes" : int(likes),"loves" : int(loves),"wow":int(wow),"cares" : int(cares),"sad":int(sad),
                "angry":
                int(angry),"haha" : int(haha)}

                #count number of total reactions 
                total_reaction_count = Scraping_utilities._Scraping_utilities__count_reaction(reactions)
                
                comments = Finder._Finder__find_comments(post)
                
                post_content = Finder._Finder__find_content(post,self.__driver)
                #we get time in unix timestamp
                posted_time = Finder._Finder__find_posted_time(post)
                #convert that timestamp to ISO 8601
                posted_time = Scraping_utilities._Scraping_utilities__convert_time(posted_time)
                               
                video = Finder._Finder__find_video_url(post,self.page_name,status)
                
                image = Finder._Finder__find_image_url(post)
                
                post_url = "https://www.facebook.com/{}/posts/{}".format(self.page_name,status)
                
                self.__data_dict[status] = {
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


