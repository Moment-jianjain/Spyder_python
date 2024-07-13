# -*- coding: utf-8 -*-
# @Time    : 2024/7/3 15:33
# @Author  : jianjian
# @File    : Taobao_Chromedriver_DL.py
# @Software: PyCharm
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from urllib.parse import quote
from pyquery import PyQuery as pq

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222") #此处端口保持和命令行启动的端口一致
driver = Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# 模拟淘宝登录
def login_taobao():
    print('开始登录...')
    try:
        login_url='https://login.taobao.com/member/login.jhtml'
        driver.get(login_url)
        input_login_id = wait.until(EC.presence_of_element_located((By.ID, 'fm-login-id')))
        input_login_password = wait.until(EC.presence_of_element_located((By.ID, 'fm-login-password')))
        input_login_id.send_keys('18340557566') # 用你自己的淘宝账号替换
        input_login_password.send_keys('wx18340557566') # 用你自己的密码替换
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fm-button.fm-submit.password-login')))
        submit.click()
        is_loging = wait.until(EC.url_changes(login_url))
        return is_loging
    except TimeoutException:
        print('login_taobao TimeoutException')
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fm-button.fm-submit')))
        submit.click()
        is_loging = wait.until(EC.url_changes(login_url))
        if is_loging:
            return is_loging
        else:
            login_taobao()


# 解析获取商品信息
def get_products():
    """提取商品数据"""
    html = driver.page_source
    doc = pq(html)
    items = doc('.Card--doubleCardWrapper--L2XFE73').items()
    for item in items:
        product = {'url': item.attr('href'),
            'price': item.find('.Price--priceInt--ZlsSi_M').text(),
            'realsales': item.find('.Price--realSales--FhTZc7U-cnt').text(),
            'title': item.find('.Title--title--jCOPvpf').text(),
            'shop': item.find('.ShopInfo--TextAndPic--yH0AZfx').text(),
            'location': item.find('.Price--procity--_7Vt3mX').text()}
        print(product)

# 自动获取商品信息并自动翻页
def index_page(url,cur_page,max_page):
    print(' 正在爬取：'+url)
    try:
        driver.get(url)
        get_products()
        next_page_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button/span[contains(text(),"下一页")]')))
        next_page_btn.click()
        do_change = wait.until(EC.url_changes(url))
        if do_change and cur_page<max_page:
            new_url=driver.current_url
            cur_page = cur_page + 1
            index_page(new_url,cur_page,max_page)
    except TimeoutException:
        print('---index_page TimeoutException---')




if __name__ == '__main__':
    is_loging=login_taobao()
    if is_loging:
        print('已经登录')
        KEYWORD = 'vivo'
        url = 'https://s.taobao.com/search?page=1&q=' + quote(KEYWORD) + '&tab=all'
        max_page=10
        index_page(url,1,max_page)
