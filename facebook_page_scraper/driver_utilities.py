#!/usr/bin/env python3

import logging
import sys
import time
from random import randint

from selenium.common.exceptions import (NoSuchElementException,
                                        WebDriverException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Utilities:

    @staticmethod
    def __close_driver(driver):
        """expects driver's instance, closes the driver"""
        try:
            driver.close()
            driver.quit()
        except Exception as ex:
            logger.exception("Error at close_driver method : {}".format(ex))

    @staticmethod
    def __close_error_popup(driver):
        '''expects driver's instance as a argument and checks if error shows up
        like "We could not process your request. Please try again later" ,
        than click on close button to skip that popup.'''
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a.layerCancel')))  # wait for popup to show
            # grab that popup's close button
            button = driver.find_element(By.CSS_SELECTOR, "a.layerCancel")
            button.click()  # click "close" button
        except WebDriverException:
            # it is possible that even after waiting for given amount of time,modal may not appear
            pass
        except NoSuchElementException:
            pass  # passing this error silently because it may happen that popup never shows up

        except Exception as ex:
            # if any other error occured except the above one
            logger.exception(
                "Error at close_error_popup method : {}".format(ex))

    @staticmethod
    def __scroll_down_half(driver):
        try:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight / 2);")
        except Exception as ex:
            # if any error occured than close the driver and exit
            Utilities.__close_driver(driver)
            logger.exception(
                "Error at scroll_down_half method : {}".format(ex))

    @staticmethod
    def __close_modern_layout_signup_modal(driver):
        try:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            close_button = driver.find_element(
                By.CSS_SELECTOR, '[aria-label="Close"]')
            close_button.click()
        except NoSuchElementException:
            pass
        except Exception as ex:
            logger.exception(
                "Error at close_modern_layout_signup_modal: {}".format(ex))

    @staticmethod
    def __scroll_down(driver, layout):
        """expects driver's instance as a argument, and it scrolls down page to the most bottom till the height"""
        try:
            if layout == "old":
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
            elif layout == "new":
                body = driver.find_element(By.CSS_SELECTOR, "body")
                for _ in range(randint(1, 3)):
                    body.send_keys(Keys.PAGE_UP)
                time.sleep(randint(5, 6))
                for _ in range(randint(5, 8)):
                    body.send_keys(Keys.PAGE_DOWN)
                #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # Utilities.__close_modern_layout_signup_modal(driver)
        except Exception as ex:
            # if any error occured than close the driver and exit
            Utilities.__close_driver(driver)
            logger.exception("Error at scroll_down method : {}".format(ex))

    @staticmethod
    def __close_popup(driver):
        """expects driver's instance and closes modal that ask for login, by clicking "Not Now" button """
        try:
            # Utilities.__scroll_down_half(driver)  #try to scroll
            # wait for popup to show
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.ID, 'expanding_cta_close_button')))
            # grab "Not Now" button
            popup_close_button = driver.find_element(
                By.ID, 'expanding_cta_close_button')
            popup_close_button.click()  # click the button
        except WebDriverException:
            # modal may not popup, so no need to raise exception in case it is not found
            pass
        except NoSuchElementException:
            pass  # passing this exception silently as modal may not show up
        except Exception as ex:
            logger.exception("Error at close_popup method : {}".format(ex))

    @staticmethod
    def __wait_for_element_to_appear(driver, layout, timeout):
        """expects driver's instance, wait for posts to show.
        post's CSS class name is userContentWrapper
        """
        try:
            if layout == "old":
                # wait for page to load so posts are visible
                body = driver.find_element(By.CSS_SELECTOR, "body")
                for _ in range(randint(3, 5)):
                    body.send_keys(Keys.PAGE_DOWN)
                WebDriverWait(driver, timeout).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.userContentWrapper')))
                return True
            elif layout == "new":
                WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-posinset]")))
                print("new layout loaded")

                return True

        except WebDriverException:
            # if it was not found,it means either page is not loading or it does not exists
            logger.critical("No posts were found!")
            return False
            # (optional) exit the program, because if posts does not exists,we cannot go further
            # Utilities.__close_driver(driver)
            # sys.exit(1)
        except Exception as ex:
            logger.exception(
                "Error at wait_for_element_to_appear method : {}".format(ex))
            return False
            # Utilities.__close_driver(driver)

    @staticmethod
    def __click_see_more(driver, content, selector=None):
        """expects driver's instance and selenium element, click on "see more" link to open hidden content"""
        try:
            if not selector:
                # find element and click 'see more' button
                element = content.find_element(
                    By.CSS_SELECTOR, 'span.see_more_link_inner')
            else:
                element = content.find_element(By.CSS_SELECTOR,
                                               selector)
            # click button using js
            driver.execute_script("arguments[0].click();", element)

        except NoSuchElementException:
            # if it doesn't exists than no need to raise any error
            pass
        except AttributeError:
            pass
        except IndexError:
            pass
        except Exception as ex:
            logger.exception("Error at click_see_more method : {}".format(ex))

    @staticmethod
    def __close_cookie_consent_modern_layout(driver):
        # To avoid the cookie consent prompt
        try:
          allow_span = driver.find_element(
             By.XPATH, '//div[contains(@aria-label, "Allow")]/../following-sibling::div')
          allow_span.click()
        except Exception as ex:
            #if not found, that's fine silently just log thing do not stop
            logger.info('The Cookie Consent Prompt was not found!: ', ex)