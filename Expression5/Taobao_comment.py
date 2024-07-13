# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 9:41
# @Author  : jianjian
# @File    : Taobao_comment.py
# @Software: PyCharm
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException
from urllib.parse import quote
from pyquery import PyQuery as pq
import time
sleeptime=5
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222") #此处端口保持和命令行启动的端口一致
driver = Chrome(options=chrome_options)
driver.implicitly_wait(10)  # 隐式等待
wait = WebDriverWait(driver, 15)  # 显示等待

# 模拟淘宝登录
def login_taobao():
    print('开始登录...')
    try:
        login_url='https://login.taobao.com/member/login.jhtml'
        driver.get(login_url)
        check_login_type()
        input_login_id = wait.until(EC.presence_of_element_located((By.ID, 'fm-login-id')))
        input_login_password = wait.until(EC.presence_of_element_located((By.ID, 'fm-login-password')))
        input_login_id.send_keys('')#渐渐_moment
        input_login_password.send_keys('Gsv@1979512177')
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

# 判断登录模式，如果是扫描登录则切换到用户名密码登录模式
def check_login_type():
    print('判断登录模式')
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'fm-login-id')))
    except TimeoutException:
        change_type = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.iconfont.icon-password')))
        change_type.click()  # 切换到用户密码模式登录
        print('切换到用户密码模式登录...')

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
        item_href=item.attr('href') # 得到商品的详情访问页面
        if item_href.find('https:')>=0:
            item_url =item_href
            print(item_url)
        else:
            item_url = "https:" + item.attr('href')
            # 爬取商品评价
            get_prod_comments(item_url)
            time.sleep(sleeptime)

# 爬取商品评价
def get_prod_comments(item_url):
    driver.get(item_url)
    print('跳转至详情页.......'+item_url)
    ele = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Tabs--title--1Ov7S5f ']/span")))
    time.sleep(sleeptime)
    # 向下滚动至目标元素可见
    js = "arguments[0].scrollIntoView();"
    driver.execute_script(js, ele)
    print('向下滚动至-宝贝评价-元素可见.......')
    driver.execute_script("arguments[0].click();", ele)
    print('点击-宝贝评价.......')
    ele_comments=driver.find_elements(By.CSS_SELECTOR,".Comment--content--15w7fKj")
    print('提取宝贝评价信息.......')
    for ele_comment in ele_comments:
        print(ele_comment.text)


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
        KEYWORD = 'iPad'
        url = 'https://s.taobao.com/search?page=1&q=' + quote(KEYWORD) + '&tab=all'
        max_page=1
        index_page(url,1,max_page)
