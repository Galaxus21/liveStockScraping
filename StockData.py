import requests
from bs4 import BeautifulSoup
import time


def StockInfo(company):
    urlList={'Nvidia':'https://www.investing.com/equities/nvidia-corp',
             'Google':'https://www.investing.com/equities/google-inc',
             'Microsoft':'https://www.investing.com/equities/microsoft-corp',
             'Apple':'https://www.investing.com/equities/apple-computer-inc',
             'Tesla':'https://www.investing.com/equities/tesla-motors',
             'Tata Motors':'https://www.investing.com/equities/tata-motors-ltd',
             'Adani Enterprises':'https://www.investing.com/equities/adani-enterprises',
             'TCS':'https://www.investing.com/equities/tata-consultancy-services',
             'Dominos':'https://www.investing.com/equities/dominos-pizza-inc',
             'AMD':'https://www.investing.com/equities/adv-micro-device'}
    
    url=urlList[company]

    # 1: Get the HTML

    htmlcontent=requests.get(url).text

    # 2: Parse the HTML

    soup = BeautifulSoup(htmlcontent, 'html5lib')

    # 3: HTML Tree Traversal

    Info1=soup.find('div', class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6')
    change=Info1.find_all('span')

    price=Info1.find('div', class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]').text
    diff=change[0].text
    changepercent=change[1].text[1:-1]

    Info2=soup.find('div', class_='flex flex-wrap items-center justify-between border-t border-t-[#e6e9eb] pt-2.5 sm:pb-2.5 pb-2.5')

    prevcloseval=Info2.dd.span.contents[1].text

    print(price,prevcloseval,diff,changepercent)

    return ({'price':price,'prevcloseval':prevcloseval,'change':diff,'changepercent':changepercent})

if __name__=='__main__':

    urlList={'Nvidia':'https://www.investing.com/equities/nvidia-corp',
             'Google':'https://www.investing.com/equities/google-inc',
             'Microsoft':'https://www.investing.com/equities/microsoft-corp',
             'Apple':'https://www.investing.com/equities/apple-computer-inc',
             'Tesla':'https://www.investing.com/equities/tesla-motors',
             'Tata Motors':'https://www.investing.com/equities/tata-motors-ltd',
             'Adani Enterprises':'https://www.investing.com/equities/adani-enterprises',
             'TCS':'https://www.investing.com/equities/tata-consultancy-services',
             'Dominos':'https://www.investing.com/equities/dominos-pizza-inc',
             'AMD':'https://www.investing.com/equities/adv-micro-device'}
    
    while True:
        for company in urlList.keys():
            StockInfo(company)
        time.sleep(10)
        
    

