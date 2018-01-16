# coding=utf-8
import re
from selenium import webdriver


class MiaoPai:

    url = ''

    def __init__(self, url='https://www.miaopai.com/u/mob_91912490'):
        self.url = url

    def getnum(self):

        # initial crawler
        driver = webdriver.PhantomJS(executable_path="F:/work/phantomjs-2.1.1-windows/bin/phantomjs.exe")
        driver.get(self.url)

        # get video blocks
        lis = driver.find_elements_by_class_name('videoCont')
        videolist = []

        for each in lis:
            name = each.find_elements_by_tag_name('p')[0].text
            title = each.find_elements_by_tag_name('p')[2].text
            # match number and unit, convert into raw number
            numeric_const_pattern = '[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'
            rx = re.compile(numeric_const_pattern, re.VERBOSE)
            num = each.find_element_by_class_name('red').text
            raw = (rx.findall(num)[0])
            pos_raw = num.find(raw)
            unit = num[pos_raw + len(raw)] if len(num) > pos_raw + len(raw) else ''
            raw = int(float(raw) * 10000) if unit == '万' else raw
            videolist.append(
                {
                    'name': name,
                    'title': title,
                    'num': num,
                    'raw_num': raw,
                    'source': each.find_element_by_tag_name('video').get_attribute('src')
                }
            )
        return videolist


