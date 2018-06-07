#sadsadasdsadsdsafaffqewwewqerqwrqweqwewqeqw



import requests

headers = {
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Referer': 'https://www.zhihu.com/people/excited-vczh/following',
    # 'X-UDID': 'AJBCD9iXpgyPTl5cmXmohBKioOd6n52PRnU=',
    'Cookie': 'q_c1=7c06d6dda147464085a9e25545326917|1505752805000|1505752805000; _zap=9a01aa65-3b12-4040-a492-13f0aa3ad5ad; d_c0="ABACYKw3qQyPThyVtc2P0vvIbINGwHqRfGE=|1510294422"; aliyungf_tc=AQAAAHcr4EKk8gMA510OfC7UV3qACuYg; q_c1=7c06d6dda147464085a9e25545326917|1513234275000|1505752805000; _xsrf=cdb68050e7b02faea68077cfbb93bfb1; r_cap_id="ODVmNjk5ZTQ3MWIyNDA4Njk1Y2ZlNDFiN2RkYzRhMDY=|1513234275|7b22624c60286c862f20847107c38f1ce0b5ed9d"; cap_id="M2NhOTI5ODkxM2NmNGMzN2I4NDBkMDdhN2RmMjc3NDI=|1513234275|7354cb7a537ed2a24f3b64b0accf60b2f98d2e62"; __utma=51854390.2146445833.1513234277.1513234277.1513234277.1; __utmc=51854390; __utmz=51854390.1513234277.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20170919=1; z_c0=Mi4xSzMtTEF3QUFBQUFBRUFKZ3JEZXBEQmNBQUFCaEFsVk5oMjBmV3dDamNtQ0tHcTdFbVdXNjdSbHA1Z3ZzLTlrcWt3|1513234311|2611237ee0c767bec5a65afe634703278cee274b; _xsrf=cdb68050e7b02faea68077cfbb93bfb1'
}
cookies = {
    'aliyungf_tc': 'AQAAAHcr4EKk8gMA510OfC7UV3qACuYg',
    'q_c1': '7c06d6dda147464085a9e25545326917|1505752805000|1505752805000',
    '_xsrf': 'cdb68050e7b02faea68077cfbb93bfb1',
    'r_cap_id': "ODVmNjk5ZTQ3MWIyNDA4Njk1Y2ZlNDFiN2RkYzRhMDY=|1513234275|7b22624c60286c862f20847107c38f1ce0b5ed9d",
    'cap_id': "M2NhOTI5ODkxM2NmNGMzN2I4NDBkMDdhN2RmMjc3NDI=|1513234275|7354cb7a537ed2a24f3b64b0accf60b2f98d2e62",
    'd_c0': "ABACYKw3qQyPThyVtc2P0vvIbINGwHqRfGE=|1510294422",
    '_zap': '9a01aa65-3b12-4040-a492-13f0aa3ad5ad',
    '__utma': '51854390.2146445833.1513234277.1513234277.1513234277.1',
    '__utmb': '51854390.0.10.1513234277',
    '__utmc': '51854390',
    '__utmz': '51854390.1513234277.1.1.utmcsr = (direct) | utmccn = (direct) | utmcmd = (none)',
    '__utmv': '51854390.000--| 3 = entry_date = 20170919 = 1',
    'z_c0': 'Mi4xSzMtTEF3QUFBQUFBRUFKZ3JEZXBEQmNBQUFCaEFsVk5oMjBmV3dDamNtQ0tHcTdFbVdXNjdSbHA1Z3ZzLTlrcWt3 | 1513234311 | 2611237ee0c767bec5a65afe634703278cee274b',
    'n_c': '1',

}

respones = requests.get('https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20',headers=headers,)
str1 = respones.text
print(str1)
