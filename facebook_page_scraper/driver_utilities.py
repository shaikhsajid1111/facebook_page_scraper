#!/usr/bin/env python3
try:
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException,WebDriverException
    import time
    import sys
except Exception as ex:
    print(ex)
    
class Utilities:

    @staticmethod
    def __close_driver(driver):
        """expects driver's instance, closes the driver"""
        try:
            driver.close()
            driver.quit()
        except Exception as ex:
            print("error at close_driver method : {}".format(ex))
    
    @staticmethod
    def __close_error_popup(driver):
        '''expects driver's instance as a argument and checks if error shows up 
        like "We could not process your request. Please try again later" ,
        than click on close button to skip that popup.'''
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a.layerCancel'))) #wait for popup to show
            button = driver.find_element_by_css_selector("a.layerCancel") #grab that popup's close button
            button.click()  #click "close" button
        except WebDriverException:
            #it is possible that even after waiting for given amount of time,modal may not appear
            pass
        except NoSuchElementException:
            pass  #passing this error silently because it may happen that popup never shows up
        
        except Exception as ex:
            #if any other error occured except the above one
            print("error at close_error_popup method : {}".format(ex))

    @staticmethod
    def __scroll_down(driver):
        """expects driver's instance as a argument, and it scrolls down page to the most bottom till the height"""
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        except Exception as ex:
            #if any error occured than close the driver and exit
            Utilities.__close_driver(driver)
            print("error at scroll_down method : {}".format(ex))
            
    @staticmethod
    def __close_popup(driver):
        """expects driver's instance and closes modal that ask for login, by clicking "Not Now" button """
        try:
            Utilities.__scroll_down(driver)  #try to scroll
            #wait for popup to show
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'expanding_cta_close_button')))
            #grab "Not Now" button
            popup_close_button = driver.find_element_by_id('expanding_cta_close_button')
            popup_close_button.click()  #click the button
        except WebDriverException:
            #modal may not popup, so no need to raise exception in case it is not found
            pass
        except NoSuchElementException:
            pass  #passing this exception silently as modal may not show up
        except Exception as ex:
            print("error at close_popup method : {}".format(ex))
        
    @staticmethod
    def __wait_for_element_to_appear(driver):
        """expects driver's instance, wait for posts to show.
        post's CSS class name is userContentWrapper
        """
        try:
            #wait for page to load so posts are visible
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.userContentWrapper')))
        except WebDriverException:
            #if it was not found,it means either page is not loading or it does not exists
            print("No posts were found!")
            Utilities.__close_driver(driver)
            sys.exit(1)  #exit the program, because if posts does not exists,we cannot go further
        except Exception as ex:
            print("error at wait_for_element_to_appear method : {}".format(ex))
            Utilities.__close_driver(driver) 
            
        

    @staticmethod
    def __click_see_more(driver,content):
        """expects driver's instance and selenium element, click on "see more" link to open hidden content"""
        try:
            #find element and click 'see more' button
            element = content.find_element_by_css_selector('span.see_more_link_inner')
            driver.execute_script("arguments[0].click();", element) #click button using js    
        
        except NoSuchElementException:
            #if it doesn't exists than no need to raise any error
            pass
        except AttributeError:
            pass
        except IndexError:
            pass
        except Exception as ex:
            print("error at click_see_more method : {}".format(ex))