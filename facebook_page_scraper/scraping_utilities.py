#!/usr/bin/env python3
try:
    import re
    from datetime import datetime as dt
except Exception as ex:
    print(ex)

class Scraping_utilities:
    @staticmethod
    def __extract_numbers(string):
        """expects string and returns numbers from them as integer type,
        e.g => input = '54454 comment', than output => 54454
        """
        try:
            return string.split(" ")[0]
        except IndexError:
            return 0


    @staticmethod
    def __exists_in_list(li,word):
        """expects list and a element, returns all the occurence of element in the list.
        e.g input => li = ['sajid','sajid','sajid','d','s'] with given word = 'sajid', 
        output => ['sajid','sajid','sajid'] """
        return [substring for substring in li if word in substring]
    
    @staticmethod
    def __convert_time(unix_timestamp):
        try:
            return dt.utcfromtimestamp(float(unix_timestamp)).isoformat()        
        except Exception as ex:
            print(ex)

    @staticmethod
    def __extract_content(content):
        """returns the text content of selenium element, else if content is string than returns a empty string"""
        if type(content) is not str:
            content = content.find_element_by_tag_name("p").get_attribute('textContent')
        else:
            content = ""
        return content

    @staticmethod
    def __count_reaction(dictionary):
        """expects a dictionary and returns sum of all values of dictionary.
        e.g => 
        input dictionary = {"s":1,"d":34},
        output=> 35"""
        return sum(dictionary.values())

    @staticmethod
    def __extract_id_from_link(link):
        """expects the post's URL as a argument, and extracts out post_id from that URL"""
        status = "NA"
        #if url pattern container "/posts" 
        if "posts/" in link:
            status = link.split('/')[5].split('?')[0]
        #if url pattern container "/photos"
        elif "photos/" in link:
            status = link.split("/")[-2]
        else:
            status = link.split('/')[-1].split('=')[-3].split('&')[0]
        #if url pattern container "/videos"
        if "/videos/" in link:
            status = link.split("/")[5]
        return status
    
    @staticmethod
    def __value_to_float(x):
        try:
            x = float(x)
            return x
        except:
            pass    
        x = x.lower()
        if 'k' in x:
            if len(x) > 1:
                return float(x.replace('k', '')) * 1000
            return 1000
        if 'm' in x:
            if len(x) > 1:
                return float(x.replace('m', '')) * 1000000
            return 1000000
        if 'm' in x:
            return float(x.replace('m', '')) * 1000000000
        return 0