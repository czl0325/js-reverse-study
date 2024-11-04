import requests
import execjs

cookies = {
    'MEIQIA_TRACK_ID': '2oMmgjC4qKyoHsvB07s3Il7jteo',
    'MEIQIA_VISIT_ID': '2oMmgjwEAUHbqsBWCOsUSX75zq2',
}

headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'MEIQIA_TRACK_ID=2oMmgjC4qKyoHsvB07s3Il7jteo; MEIQIA_VISIT_ID=2oMmgjwEAUHbqsBWCOsUSX75zq2',
    'Origin': 'https://www.endata.com.cn',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'year': '2023',
    'MethodName': 'BoxOffice_GetYearInfoData',
}

response = requests.post('https://www.endata.com.cn/API/GetData.ashx', cookies=cookies, headers=headers, data=data)

with open("./ee-decrypt.js", "r", encoding="utf-8") as f:
    js_code = f.read()
    ctx = execjs.compile(js_code)
    res = ctx.call("enDecrypt", response.text)
    print(res)
