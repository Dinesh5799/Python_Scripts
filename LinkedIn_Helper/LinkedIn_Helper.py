import csv
import urllib.error,urllib.error,urllib.parse
from selenium import webdriver
import getpass
import time
import pyautogui as pyt
import os

profile_links = list()


def copy_csvfiles(n):
    co = -1
    try:
        with open('result.csv', 'r',encoding='utf-8') as inp, open('result1.csv', 'w', newline='',encoding='utf-8') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                co += 1
                if co > n:
                    #print(row)
                    writer.writerow(row)
            inp.close()
            out.close()

    except Exception as e:
        print("Exception in opening csv file", e)


def delete_csvfile():
    try:
      os.remove('result.csv')
      os.rename('result1.csv','result.csv')
      print('Sucessfully Done With Saving Current State')
    except Exception as e:
        print('Error Deleting csv file',e)


def sending_connectionrequest():
    try:
        connect_checker = browser.find_element_by_class_name('pv-s-profile-actions')
        text_conmes = connect_checker.text
        print('First text_conmes: ',text_conmes)
        country = browser.find_element_by_class_name('pv-top-card-section__location')
        country = country.text
        print('country: ',country)
        if not 'india' and 'India' and 'INDIA' in country:
            print('---Returning---')
            return
        if 'Message' in text_conmes:
            print('Return As You Are Connected Already')
            return
        elif 'Connect' in text_conmes:
            print('Sending Connect Request')
            connect = browser.find_element_by_class_name('pv-s-profile-actions--connect')
            connect.click()
            send_now = browser.find_element_by_class_name('ml1')
            send_now.click()
            time.sleep(5)
            print('Connect Request Sent')
    except Exception as e:
        print('Failed to send Connection Request',e)
try:
    with open("result.csv",encoding="utf8") as fn:
        data = csv.reader(fn, delimiter=',')
        for row in data:
            #print(row[0])
            profile_links.append(row[0])
    fn.close()
    print(profile_links)
except Exception as e:
    print('Exception',e)

n = 0
try:
    email = input('Enter email: ')
    #email = ''
    password = input('Enter pass: ')
    #password = ''
    print('No Problem With User Credentials')#chromedriver.exe
    browser = webdriver.Chrome(executable_path=r"C:/Users/KIT9059/Desktop/chromedriver.exe")
    print('Found Chrome Driver')
    browser.get('https://www.linkedin.com/')
    time.sleep(2)
    email_id = browser.find_element_by_id('login-email')
    email_id.send_keys(email)
    pass_fill = browser.find_element_by_id('login-password')
    pass_fill.send_keys(password)
    login = browser.find_element_by_id('login-submit')
    login.click()
    for i in profile_links:
        if i == 'profileLink':
            continue
        n += 1
        print(i)
        browser.get(i)
        time.sleep(2)
        sending_connectionrequest()
        time.sleep(2)
    copy_csvfiles(n)
    delete_csvfile()
    time.sleep(30)

except Exception as e:
    copy_csvfiles(n)
    delete_csvfile()
    print('Exception with selenium',e)
