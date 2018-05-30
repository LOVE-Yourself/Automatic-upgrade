from lxml import etree
import requests
import json
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
headers ={'User-Agent':user_agent}
response = requests.get('http://seputu.com/',headers=headers)
mulu_xpath = "/html/body/div[@class='body']/div[@class='bg']/div[@class='mulu']"
html = etree.HTML(response.text)
content = []
for mulu in html.xpath(mulu_xpath):
    list = []
    title = mulu.xpath( "div[@class='mulu-title']/center/h2/text()")
    if title != []:
        li_lsit = mulu.xpath("div[@class='box']/ul/li")
        for li in li_lsit:

            a_text = li.xpath("a/text()")
            a_href = li.xpath("a/@href")
            list.append({'href':a_href,'box_title':a_text})

        content.append({'title':title[0],'content':list})

#以二进制写入json文件
with open('DMBJ.json','w+b') as fp:
    print(type(content))
    fp.write(json.dumps(content,indent=4,ensure_ascii=False).encode('utf-8'))
    # python---》json   dict --》object    tuple,list -----》array


#写入csv



print(content)



