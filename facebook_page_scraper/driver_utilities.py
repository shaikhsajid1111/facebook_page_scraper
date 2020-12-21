#!/usr/bin/env python3
try:
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import time
except Exception as ex:
    print(ex)
    
class Utilities:

    @staticmethod
    def __close_driver(driver):
        try:
            driver.quit()
            driver.close()
        except Exception as ex:
            print(ex)
    
    @staticmethod
    def __close_error_popup(driver):
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a.layerCancel')))
            button = driver.find_element_by_css_selector("a.layerCancel")
            button.click()
        except Exception as ex:
            pass

    @staticmethod
    def __scroll_down(driver):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        except Exception as ex:
            Utilities.__close_driver(driver)
            print(ex)
            
    @staticmethod
    def __close_popup(driver):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'expanding_cta_close_button')))
            popup_close_button = driver.find_element_by_id('expanding_cta_close_button')
            popup_close_button.click()
            time.sleep(2)
        except:
            pass
    
    @staticmethod
    def __wait_for_element_to_appear(driver):
        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.userContentWrapper')))
        except Exception as ex:
            Utilities.__close_driver(driver)
            print(ex)
        

