import facebook_page_scraper
import json
import unittest
import json



class Test_json(unittest.TestCase):

    def is_name_empty(self,dictionary):
        for key in dictionary:
            if dictionary[key]['name'] == "":
                return True
        return False

        
    def test_scraper_for_json(self): 
        facebook_ai = facebook_page_scraper.Facebook_scraper("facebookai",10,"firefox")
        json_data = facebook_ai.scrap_to_json()
        data_dictionary = json.loads(json_data)
        
        self.assertEqual(len(data_dictionary),10)
        self.assertFalse(self.is_name_empty(data_dictionary),"Getting empty strings on name attribute")
        
             

class Test_csv_output(unittest.TestCase):
    
    def test_csv(self):
        facebook_ai = facebook_page_scraper.Facebook_scraper("facebookai",10,"firefox")
        was_saved = facebook_ai.scrap_to_csv("fbai","E:\Programming")
        self.assertEqual(was_saved,True)



if __name__ == "__main__":
    unittest.main()