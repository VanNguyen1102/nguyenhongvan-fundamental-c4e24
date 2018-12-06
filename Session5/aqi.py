from urllib.request import urlopen

import json

url = "https://wind.waqi.info/nsearch/full/hanoi?n=4"

#1. Open connection (tạo đường truyền)
conn = urlopen(url)

#2. Read data (gửi dữ liệu từ server về client)
raw_data = conn.read()

#3. Decode data (giải mã dữ liệu)
text = raw_data.decode("utf-8")

#4. Convert data from str to dict
data = json.loads(text)

results = data["results"]
# result = results[0]
# print(result["s"]["a"])
# print(result["s"]["n"][0])


