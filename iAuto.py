from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import schedule
import os
import datetime

x = 0

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
p = os.getcwd()
browser = webdriver.Firefox(executable_path=p + "/geckodriver.exe", options=chrome_options)
browser.set_window_size(600, 800)
browser.get('https://www.instagram.com/accounts/login/')
usernames = [
"user 1",
"user 2",
]  # usernames whom you will send the message


def iauto():
    print("Firing iAuto")
    global x
    global usernames
    time.sleep(5)
    username_bar = browser.find_element_by_name('username')
    password_bar = browser.find_element_by_name('password')

    username = 'Your username'  # Enter your username here
    password = 'Your password'  # Enter your password here

    username_bar.send_keys(username)
    password_bar.send_keys(password + Keys.ENTER)
    print("Logging in")
    time.sleep(10)
    print("Removing Popup 1")
    try:
        browser.find_element_by_xpath("//a[contains(text(),'Not Now')]").click()
    except:
        try:
            browser.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        except:
            try:
                browser.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
            except:
                pass

    time.sleep(5)
    print("Removing Popup 2")
    try:
        browser.find_element_by_xpath("//a[contains(text(),'Not Now')]").click()
    except:
        try:
            browser.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        except:
            try:
                browser.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
            except:
                pass

    def send_msg(usernames):
        print("Messenger Called")
        print("Spamming Started")
        popup = 0
        browser.get('https://www.instagram.com/direct/new/')
        time.sleep(5)
        to_btn = browser.find_element_by_name('queryBox')
        to_btn.send_keys(usernames)
        time.sleep(5)
        if popup == 0:
            print("Removing Popup 3")
            popup += 1
            try:
                browser.find_element_by_xpath("//a[contains(text(),'Not Now')]").click()
                pass
            except:
                try:
                    browser.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
                    pass
                except:
                    try:
                        browser.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
                        pass
                    except:
                        pass
        chk_mrk = browser.find_element_by_class_name('dCJp8')
        chk_mrk.click()
        time.sleep(5)
        nxt_btn = browser.find_element_by_xpath('//div[@class="rIacr"]')
        nxt_btn.click()
        time.sleep(5)
        txt_box = browser.find_element_by_tag_name('textarea')
        txt_box.send_keys(
            f"Hey {usernames}, I love what you do and your images have inspired me. I’d love to connect; what do you think? Do follow back & lets support each others Journey. Feel free to Join our Team for Freelancing Project works. The Pr0tagonists : https://pr0tagonists.github.io . Myself I am Mastermindx33 : https://github.com/Mastermindx33 . I'll be looking forward for your reply mate ! Feel free to ping me .")  # Customize your message
        time.sleep(5)
        snd_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF')
        snd_btnn = snd_btn[len(snd_btn) - 1]
        snd_btnn.click()
        time.sleep(5)

    count = 0
    try:
        for usernamex in usernames:
            send_msg(usernamex)
            count += 1
            print("Message spammed Successfully")
            print("Spamming again in 10 secs")
            time.sleep(10)  # Enter wait secs here
            print("Calling Spam")
    except TypeError:
        print('Failed!')
    x += 1
    browser.quit()
    print(f'''
    Successfully Sent {count} Massages
    ''')
    x += 1


# time = datetime.datetime.now()  # Specific Time When The message will be send

# try:
#     print("Starting up")
#     schedule.every().day.at(time).do(iauto)
# except TypeError:
#     print("I call 0")
#     pass

# try:
#     print("I call 1")
#     while True and x != 1:
# print("I call 2")
# schedule.run_pending()
# time.sleep(1)
# except UnboundLocalError:
#     print("I call 3")
#     pass

iauto()
