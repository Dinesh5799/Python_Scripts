import csv
import urllib.error,urllib.error,urllib.parse
from selenium import webdriver
import getpass
import time

profile_links = list()


def sending_connectionrequest():
    try:
        connect_checker = browser.find_element_by_xpath(
            'html/body/div[5]/div[5]/div[3]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/div[2]/div/span[1]/button/span[1]')
        text_conmes = connect_checker.text
        print(text_conmes)
        if 'More actions' in text_conmes:
            connect = browser.find_element_by_class_name('pv-s-profile-actions--connect')
            connect.click()
            # ml1  button-primary-large
            send_now = browser.find_element_by_class_name('ml1')
            send_now.click()
        elif 'Message' in text_conmes:
            connect_checker = browser.find_element_by_xpath(
                '/html/body/div[5]/div[5]/div[3]/div/div/div/div[2]/div[1]/div[2]/section/div[3]/div[1]/div[2]/div/button/span[1]')
            text_conmes = connect_checker.text
            print('text_conmes: ', text_conmes)
            connect = browser.find_element_by_class_name('pv-s-profile-actions--connect')
            connect.click()
            send_now = browser.find_element_by_class_name('ml1')
            send_now.click()
    except Exception as e:
        print('Failed to send Connection Request')


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

try:
    email = input('Enter email: ')
    #email = 'dineshchunduspecial@gmail.com'
    password = input('Enter pass: ')
    #password = ''
    print('No Problem With User Credentials')#chromedriver.exe
    browser = webdriver.Chrome(executable_path=r"C:/chromedriver.exe")
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
        print(i)
        browser.get(i)
        time.sleep(2)
        sending_connectionrequest()
        time.sleep(2)
    time.sleep(30)

except Exception as e:
    print('Exception with selenium',e)
