from selenium import webdriver as w
from sys import argv as a
from sys import stderr as r

user = a[1]
password = a[2]
options = w.ChromeOptions()

options.add_argument('--incognito')

browser = w.Chrome('path to chromedriver download',options = options)

browser.get("https://cupertino.schoolloop.com")
try:
    firstInp = browser.find_element_by_xpath('''//*[@id="login_name"]''')
    firstInp.send_keys(user)
    secondInp = browser.find_element_by_xpath('''//*[@id="password"]''')
    secondInp.send_keys(password)
    buttClick = browser.find_element_by_xpath('''//*[@id="login_form"]/a[1]''')
    buttClick.click()
    assignments = browser.find_element_by_xpath('''//*[@id="container_content"]/div/div[1]/div[1]/div[4]/div''').text
    writeList = open("assignments.txt","w")
    writeList.write(assignments)
    writeList.seek(0)
    tempList = []

    finalDict = {}
    with open("assignments.txt","r") as d:
        for i in d:
            tempList.append(i.rstrip())
    tempList.pop(0)
    for i in tempList:
        finalDict[i[:-12].rstrip()] = i[-7:-1].lstrip()
    print(finalDict)
except Exception as e:
    r.write("Error - Incorrect User Id and Password ")
    print(str(e))
    r.flush()


browser.quit()
