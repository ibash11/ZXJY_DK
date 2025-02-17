from bs4 import BeautifulSoup
import requests
import pushMessage

def AppVersion(pushKey):
    AdaptedVersion = 'v1.4.1'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url = "https://www.yuque.com/huaji-kiyl5/kb/br0dfuykwe7ryku3"
    response = requests.get(url, headers=header).content
    description = BeautifulSoup(response, 'html.parser').find('meta', attrs={'name': 'description'})['content']
    result = float(description.split('#')[0].replace(' ', ''))
    if result <= 0.41:
        url = 'https://app.mi.com/details?id=com.wyl.exam'
        try:
            response = requests.get(url, headers=header)
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'html.parser')
            version = soup.select('.main .float-left')[1].find('div', {'style': 'float:right;'}).get_text().strip()
            if version == AdaptedVersion:
                return True
            else:
                pushMessage.pushMessage('职校家园版本',
                                        f'此版本适配{AdaptedVersion} 当前版本{version}',pushKey)
                print(f'此版本适配{AdaptedVersion} 当前版本{version}')
                return False, "职校家园版本获取失败"
        except requests.exceptions.RequestException as error:
            pushMessage.pushMessage('职校家园版本',
                                    f'职校家园版本获取错误{error}', pushKey)
            print(f'职校家园版本获取错误{error}')
            return False, f'职校家园版本获取失败{error}'
    else:
        print(f"代码有更新请前往 https://github.com/huajien/ZXJY_DK 更新代码")
