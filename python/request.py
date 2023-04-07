# python request.py

'''
import requests

responsOBJ=requests.reuest("GET",'http://20.194.192.246:10004/main/api/BusAPI/all/')

print(responsOBJ)


#json   request   zip
'''
import requests

url = "https://od.moi.gov.tw/api/v1/rest/datastore/301000000A-001609-001?site_id"

payload={}
headers = {
  'Cookie': 'JSESSIONID=429CEB8D072D10239FAE1B7DFD2E69EE'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

