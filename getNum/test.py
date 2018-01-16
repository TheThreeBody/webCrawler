# coding=utf-8
import re
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path="F:/work/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver.get("http://www.miaopai.com/u/mob_49878220")

# get video blocks
lis = driver.find_elements_by_class_name('videoCont')
videolist = []

for each in lis:

    # match number and unit, convert into raw number
    numeric_const_pattern = '[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'
    rx = re.compile(numeric_const_pattern, re.VERBOSE)
    num = each.find_element_by_class_name('red').text
    name = each.find_elements_by_tag_name('p')[0].text
    title = each.find_elements_by_tag_name('p')[2].text
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
print(videolist)
