import requests
import json

payload = {"needQueryPoint": "true", "mainOfferId": "820048", "subscriberId": "2202834738", "groupId": ""}
headers = {
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  "Connection": "keep-alive",
  "Content-Length": "74",
  "Content-Type": "application/json",
  "Cookie": "echannelweb_route=ce6f6b07b4bff662742279b4571e5f06; echannelapp_route=6fe0a41fa57d9f791d257f566994ea66; route=f5c30e31371d7eb1b46500a8c446bfe9; indiv_login_token=469095A69C35AE49A2E70A7ACED304800027755D4ED3F382; TS01bba117=010aa23b1d3852ea6382c2574c434db3938bba9aed7d84a784fdebec31173d0f4e295b1c46791011084c314625f9be6ce11b3e9b2297f4bb088fec8366f6a6de2edeeb6671e0d25a19fbd1f502e218636bf7b17ace9e98328308c481eb1e910a62d431daa522f8cedcd0256beb5f2b9841b062b11f; TS01fa9144=010aa23b1d707a08cc1469bcc1e9ef5a1106817ca5a2b8104532de68c9bd77188979a66468fd51f49ef58d859729e859493785fc9e74841884725a07f278ec46664e64bde5c1a52bdd2ab5718bc304400588902b9b2f8f06db91d9bc31384e98394d66cd15",
  "Host": "my.te.eg",
  "Origin": "https://my.te.eg",
  "Referer": "https://my.te.eg/echannel/",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
  "channelId": "702",
  "csrftoken": "A6E8779789A25CC88C75B1F09EB59EC3F2B5ABAD8424424B",
  "delegatorSubsId": "",
  "isCoporate": "false",
  "isMobile": "false",
  "isSelfcare": "frue",
  "languageCode": "en-US",
  "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Linux\""
}

result = requests.post(data=json.dumps(payload),url="https://my.te.eg/echannel/service/besapp/base/rest/busiservice/cz/cbs/bb/queryFreeUnit",headers=headers)
print(result.status_code)
print(result.content)