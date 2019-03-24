from selenium import webdriver as wd
from datetime import datetime
from selenium.webdriver.support.ui import Select
import re

import time

if __name__ == '__main__':
    try:
        year, month, day = input('yyyy mm dd : ').split()

        if not (1900 <= int(year) <= datetime.today().year + 15):
            print("Can't calculate Lunar date")
            exit()
        driver = wd.Chrome('C:/tools/chromedriver.exe')
        site = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='
        site += year + '년' + month + '월' + day + '일+음력'
        driver.get(site)
        select = Select(driver.find_element_by_css_selector('.sel_trans'))
        select.select_by_index(0)
        time.sleep(0.2)
        driver.find_element_by_xpath('// *[ @ id = "direct_calendar"] / div / div[3] / div[1] / div[1] / dl / dd[3] / a[1] / img').click()
        time.sleep(0.2)
        lunar_data = driver.find_element_by_css_selector('#direct_calendar > div > div.con_area > div.trans_sun_lunar > div:nth-child(2) > dl > dd:nth-child(2) > strong').text
        driver.close()

        lunar_data = lunar_data.split()

        lunar_year = lunar_data[0][0:4]
        lunar_month = lunar_data[1][0:-1]
        lunar_day = re.compile('[\d]+').match(lunar_data[2]).group()

        print()
        print('*********Solar Calendar***********')
        print(f'Year  : {year}')
        print(f'Month : {month}')
        print(f'Day   : {day}')
        print()
        print('****Translate to Lunar Calendar***')
        print(f'Year  : {lunar_year}')
        print(f'Month : {lunar_month}')
        print(f'Day   : {lunar_day}')

    except ValueError:
        print('You have to enter yyyy mm dd form. ex) 2000 10 10')

