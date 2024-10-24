import requests
import execjs

with open('./wk-decrypt.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)

cookies = {
    'SUNWAY-ESCM-COOKIE': '950975a1-8c90-4a32-97e9-3af5c896b329',
    '__jsluid_s': '02abceab720ec8606073a60e460e4edd',
    'JSESSIONID': '5A2B2C0106104CB0C9017DFF9E08966A',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'SUNWAY-ESCM-COOKIE=950975a1-8c90-4a32-97e9-3af5c896b329; __jsluid_s=02abceab720ec8606073a60e460e4edd; JSESSIONID=5A2B2C0106104CB0C9017DFF9E08966A',
    'Origin': 'https://ec.minmetals.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ec.minmetals.com.cn/logonAction.do',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

public_key = requests.post('https://ec.minmetals.com.cn/open/homepage/public', cookies=cookies, headers=headers).text
param = ctx.call('generateParam', public_key, 1)
res = requests.post("https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page", headers=headers, cookies=cookies, json={ "param": param })
print(res.json())