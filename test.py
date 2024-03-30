import json
import os
import unittest

from dotenv import load_dotenv

import facebook_page_scraper

load_dotenv()  # take environment variables from .env.


# get env password
fb_password = os.getenv('fb_password')
fb_email = os.getenv('fb_email')


class Test_json(unittest.TestCase):

    def is_name_empty(self,dictionary):
        for key in dictionary:
            if dictionary[key]['name'] == "":
                return True
        return False

        
    def test_scraper_for_json(self): 
        anime_group = facebook_page_scraper.Facebook_scraper("170918513059147",5,"firefox", isGroup=True,  headless=False, username=fb_email, password=fb_password)
        json_data = anime_group.scrap_to_json()
        data_dictionary = json.loads(json_data)
        
        self.assertEqual(len(data_dictionary),5)
        self.assertFalse(self.is_name_empty(data_dictionary),"Getting empty strings on name attribute")
        
             

class Test_csv_output(unittest.TestCase):
    
    def test_csv_group(self):
        anime_group = facebook_page_scraper.Facebook_scraper("170918513059147",5,"firefox",isGroup=True,  headless=False, username=fb_email, password=fb_password)
        was_saved = anime_group.scrap_to_csv("group_test","./")
        self.assertEqual(was_saved,True)

    def test_csv_page(self):
        meta_page = facebook_page_scraper.Facebook_scraper("Meta",5,"firefox", headless=False, username=fb_email, password=fb_password)
        was_saved = meta_page.scrap_to_csv("meta_test","./")
        self.assertEqual(was_saved,True)



if __name__ == "__main__":
    unittest.main()