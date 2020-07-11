from selenium import webdriver
import time
from dialogflow import reply_with_ai
sent = ""
flag = False
driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://web.whatsapp.com')
input('press anything to start')
search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.send_keys('Deepaaaaa')
time.sleep(5)
name = driver.find_element_by_class_name('_325lp')
name.click()
time.sleep(5)
msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
msg.send_keys("hey im indu's assistant")
time.sleep(5)
button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
button.click()
time.sleep(5)
imsgelement = driver.find_elements_by_class_name('_274yw')
lamsg = imsgelement[len(imsgelement) - 1]
res = lamsg.text


def send_msg(mymsg):
    global sent
    global flag
    time.sleep(2)
    print("msg is :"+str(mymsg))
    msg1 = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg1.send_keys(mymsg)
    time.sleep(2)
    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    button.click()
    time.sleep(5)
    sent = mymsg
    print("sending:"+str(sent))
    flag = False


while True:
    time.sleep(2)
    imsgelement = driver.find_elements_by_class_name('eRacY')
    lamsg = imsgelement[len(imsgelement) - 1].text
    print("last :"+str(lamsg))
    print("sent msg is :"+str(sent))
    if lamsg != sent:
        flag = True
    if flag:
        output = reply_with_ai(lamsg)
        send_msg(output)
        '''if 'hi' in lamsg:
            send_msg('hello')
        elif 'class' in lamsg:
            send_msg('no class')
        elif 'lunch' in lamsg:
            send_msg('ha nuv')
        elif 'ssup' in lamsg:
            send_msg('roof')
        else:
            send_msg('sorry')'''

