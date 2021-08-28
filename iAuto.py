from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import schedule
import os
import datetime
x = 0

def dmer():
    global x
    usrnames = ["user 1",
                "user 2",]  # usernames whom you will send the message

    chrome_options = Options()
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    p = os.getcwd()
    browser = webdriver.Chrome(executable_path= p + "/chromedriver.exe", options=chrome_options)
    browser.set_window_size(600, 1000)
    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    usrname_bar = browser.find_element_by_name('username')
    passwrd_bar = browser.find_element_by_name('password')

    username = 'Your username'  # Enter your username here
    password = 'Your password'  # Enter your password here

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)

    time.sleep(11)

    def send_msg(usrnames):
        browser.get('https://www.instagram.com/direct/new/')

        time.sleep(5)

        to_btn = browser.find_element_by_name('queryBox')
        to_btn.send_keys(usrnames)

        time.sleep(8)

        chk_mrk = browser.find_element_by_class_name('dCJp8')
        chk_mrk.click()

        time.sleep(3)

        nxt_btn = browser.find_element_by_xpath('//div[@class="mXkkY KDuQp"]')
        nxt_btn.click()

        time.sleep(6)

        txt_box = browser.find_element_by_tag_name('textarea')
        txt_box.send_keys(f"Hey {usrnames}, I love what you do and your images have inspired me. I’d love to connect; what do you think? Do follow back & lets support each others Journey. Feel free to Join our Team for Freelancing Project works. The Pr0tagonists : https://pr0tagonists.github.io . Myself I am Mastermindx33 : https://github.com/Mastermindx33 . I'll be looking forward for your reply mate ! Feel free to ping me .")  # Customize your message
        time.sleep(2)

        snd_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF')
        snd_btnn = snd_btn[len(snd_btn)-1]
        snd_btnn.click()

        time.sleep(4)

    count = 0
    try:
        for usrnamee in usrnames:
            send_msg(usrnamee)
            count += 1

    except TypeError:
        print('Failed!')

    browser.quit()

    print(f'''
    Successfully Sent {count} Massages
    ''')

    x += 1


# timee = datetime.datetime.now()  # Specific Time When The message will be send

# try:
#     print("Starting up")
#     schedule.every().day.at(timee).do(dmer)
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


dmer()
