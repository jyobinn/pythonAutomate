import time

from selenium import webdriver

# 这里指定谷歌driver的路径
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = r"C:\Users\jyo\AppData\Local\Programs\Python\Python37\Lib\chromedriver.exe"
browser = webdriver.Chrome(url)
# browser.maximize_window()
# 打开网页
# openUrl = "https://vip.qq.com/jf/?ADTAG=CLIENT.QQ.5635_.0&SNO=1563002483079"
openUrl = "https://vip.qq.com/growtask/index?ADTAG=CLIENT.QQ.5635_.0&SNO=1563002483079"
browser.get(openUrl)
browser.implicitly_wait(8)
# 切换到默认frame
# browser.switch_to.default_content()
print(browser.find_element_by_id("menu-login-btn").text)
browser.find_element_by_id("menu-login-btn").click()
browser.implicitly_wait(10)
# .click()
# 找到弹框的id
frameId = browser.find_element_by_id("ui_ptlogin")
# 切换到弹框
browser.switch_to.frame(frameId)
# 登录方式切换账号密码登录
browser.find_element_by_id("switcher_plogin").click()
browser.implicitly_wait(3)
browser.find_element_by_id('u').clear()
# 填写qq账号
browser.find_element_by_id('u').send_keys('1103596419')
browser.find_element_by_id('p').clear()
# 填写qq密码
browser.find_element_by_id('p').send_keys('jyobinn')
browser.find_element_by_id('login_button').click()
browser.implicitly_wait(3)
# 切换到默认frame
browser.switch_to.default_content()
print(browser.find_elements_by_class_name("ui-btn-basic-s")[1].text)
print(browser.find_elements_by_class_name("ui-btn-basic-s")[1].get_attribute("data-url"))

element = browser.find_elements_by_class_name("ui-btn-basic-s")[1]

# browser.execute_script("arguments[0].click();", element)
# browser.execute_script("arguments[0].click();", element)
js = 'document.getElementsByClassName("ui-btn-basic-s")[1].click();'
browser.execute_script(js)
# element.click()
print(browser.find_element_by_css_selector('[href="https://vip.qq.com/life.html?ADTAG=CLIENT.QQ.5635_.0&SNO=1563002483079"]').text)
print(browser.find_element_by_css_selector('[href="https://vip.qq.com/life.html?ADTAG=CLIENT.QQ.5635_.0&SNO=1563002483079"]').location)
# browser.find_element_by_css_selector('[data-idx="3"]').click()
browser.find_element_by_css_selector('[href="https://vip.qq.com/life.html?ADTAG=CLIENT.QQ.5635_.0&SNO=1563002483079"]').send_keys(Keys.ENTER)
# webdriver.ActionChains(webdriver).move_to_element(element ).click(element ).perform()