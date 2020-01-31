# instagram_crawling_1-2(txt_version).py
# 인스타그램 셀레니움으로 크롤링
# 1. 각자가 쓴 인스타그램 게시글로 들어갈 수 있는 url 받기       : instagram_crawling_1-1(txt_version).py
# 2. 각 url로 들어가 그곳에서 아이디, 태그 or 글 뽑기            : instagram_crawling_1-1(txt_version).py
# 3. 뽑은 태그 or 글을 txt파일로 저장하기.                       : instagram_crawling_1-1(txt_version).py

# 4. 뽑은 아이디로 각자의 프로필화면으로 들어가 프로필 다운받기. : instagram_crawling_1-2(txt_version).py

import requests
import urllib.request
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# 검색어
search = '오늘의훈남'
# url
url = 'https://www.instagram.com/explore/tags/' + search + '/?h1=ko'

driver = webdriver.Chrome(executable_path="D:\\python_D\\chromedriver.exe")
driver.implicitly_wait(2)
driver.get(url)

# 1. 각자가 쓴 인스타그램 게시글로 들어갈 수 있는 url 받기.
body = driver.find_element_by_tag_name("body")

num_of_pagedowns = 30
i = 0
count = 0
arr_href = []   # 게시글 주소들 담김.

# 게시글이 파일로 저장되어있으면 그걸 arr_href 에 넣는다.
f = open(".\\instagrampost.txt", "r")
for line in f:
    arr_href.append(line)

print("게시글 개수 : %d"%len(arr_href))

# 2. 각 url로 들어가 그곳에서 아이디, 태그 or 글 뽑기.
arr_profile = []                                                                        # 프로필 화면 주소들 담김.
arr_id = []                                                                             # 아이디 담김.
arr_hash = []                                                                           # 해시태그, 내용 저장.
count = 0
for h in arr_href:
    url = arr_href[count]                                                               # 게시글 주소 담겨있음.(200개 이상)
    driver.implicitly_wait(2)
    driver.get(url)

    # id부분 찾아서 아이디, 프로필주소 저장
    try:   
        href = driver.find_elements_by_xpath('//*[@class="e1e1d"]')                     # <div class="e1e1d"> <a href="/아이디/"> 형식.
        print("id 클래스 검색성공", len(href))
        print("id[%d]" % count)
    except:
        print("id 클래스 검색실패")
        continue

    try:
        href_profile = href[0].find_element_by_css_selector('a').get_attribute('href')      # 프로필주소 검색
        arr_profile.append(href_profile)
    
        id = href[0].find_element_by_css_selector('a').text                                 # 아이디 검색.
        arr_id.append(id)
        print("id : %s" %id)
    except:
        print("아이디, 프로필주소 검색 실패, none으로 초기화")
        arr_profile.append("none")
        arr_id.append("none")
        
        print("-------------------------")
    
    count += 1

print("=================================================================")
print("id 수 : %d, 프로필주소 수 : %d, 해시태그, 내용 수 : %d" %(len(arr_id), len(arr_profile), len(arr_hash)))
print(arr_id)
print(arr_profile)

count = 0
count_img = 0
# 4. 뽑은 아이디로 각자의 프로필화면으로 들어가 프로필 다운받기.
for profile in arr_profile:
    
    if(arr_id[count] != "none"):
        driver.implicitly_wait(2)
        driver.get(profile)     # 프로필화면으로 들어감

        # 프로필 들어가서 이미지 검색
        try:   
            href = driver.find_elements_by_xpath('//*[@class="_2dbep "]')                     # <div class="e1e1d"> <a href="/아이디/"> 형식.
            print("프로필 클래스 검색성공", len(href))
            print(" profile[%d]" % count)
        except:
            print("프로필 클래스 검색실패")

        # 이미지 저장.
        try:
            full_name = ".\\크롤러\\" + search + "\\" + arr_id[count] + ".jpg"
            print("저장될 이미지 : ",full_name)
            href_profile = href[0].find_element_by_css_selector('img').get_attribute('src')      # 프로필 사진 검색
            print("href_profile : ", href_profile)
#            urllib.request.urlretrieve(item.get_attribute('src'), full_name) # src를 받는다.
            urllib.request.urlretrieve(href_profile, full_name)                                  # full_name에 받아온 이미지 저장.
        
            print("img[%d] : %s" %(count, arr_id[count]+".jpg"))
        except:
            print("이미지 저장 실패")
            
        count_img += 1    
        print("-------------------------")
        
    count += 1
    
driver.quit()
print("이미지 개수 : %d"%count_img)
print("Saved!")
