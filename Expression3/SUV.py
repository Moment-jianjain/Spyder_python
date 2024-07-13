import requests
from bs4 import BeautifulSoup

def fetch_car_names(keyword,page):
    url = f'https://mall.autohome.com.cn/list/0-999999-0-0-0-0-0-0-0-1.html?isSearch=1&providerId=&prefix={keyword}'
    header = {
      'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36(KHTML,like Gecke) Chrome/91.0.4472.124 Safafi/537.36'
    }

    try:
        response = requests.get(url,headers=header)
        response.raise_for_status()

        soup = BeautifulSoup(response.text,'html.parser')
        car_divs = soup.find_all('div',class_='carbox-title single-line')
        car_names = [div.get_text(strip=True) for div in car_divs]
        return car_names
    except requests.exceptions.RequestException as e:
        print(f"请求异常:{e}")
        return []

def main():
    keyword = 'SUV'
    page = 1
    car_names = fetch_car_names(keyword,page)

    if car_names:
        print("搜索的车辆型号有如下")
        for name in car_names:
            print(name)
        with open('car_names.txt','w',encoding='utf-8') as f:
            for name in car_names:
                f.write(name + '\n')

    else:
        print("未能获取到车辆型号")
if __name__ == "__main__":
    main()

