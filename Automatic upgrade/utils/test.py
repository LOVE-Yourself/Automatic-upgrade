# s = '2.0.1'
# s1 = s.split('.')[2]
# print(s1)
# s_1 = '2.0.1'


# class my(object):
#     @classmethod
#     def hah(cls):
#         print('--->')
#
#     def ni(self):
import requests,json
url = 'http://192.168.192.141:8000/operation/chance_change/1?isupdate=no'
response = requests.get(url)
req = json.loads(response.content.decode('utf-8'))
r1 = req['status']
print(r1)