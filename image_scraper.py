import os
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

def main(argv):
    keywords = input("input words, e.g.'cat,dog,small kitty' : ").split(",")
    url = "https://www.google.co.jp/imghp?hl=en&tab=wi&authuser=0"

    dir = os.getcwd()
    d = webdriver.Chrome("./chromedriver")
    d.implicitly_wait(10)

    d.get(url)

    parser = argparse.ArgumentParser(description='Options for scraping Google images')
    parser.add_argument('-n', '--num_images', default=10, type=int, help='num of images to scrape')
    parser.add_argument('-o', '--directory', default='images', type=str, help='output directory')
    args = parser.parse_args()

    for keyword in keywords:
        save_directory = args.directory + '/' + keyword.replace(" ", "_")
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        search_blank = d.find_element_by_id("lst-ib")
        search_blank.send_keys(keyword)
        search_blank.send_keys(Keys.ENTER)

        # scroll bottom
        target = d.find_element(By.XPATH, "//input[@value='Show more results']");

        actions = ActionChains(d)
        actions.move_to_element(target)
        actions.click(target)
        actions.perform()
        print(target.get_attribute("value"))

        # img_elements = d.find_elements_by_class_name("rg_ic")
        # for i, img_ele in enumerate(img_elements):
        #     print(i, img_ele.get_attribute("src"))


    # d.close()
    # d.quit()

if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    # sys.exit()
