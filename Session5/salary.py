#1 dùng 1 biến mô tả bảng lương
#2 tính lương theo tuần: 
# lương = số tiền theo giờ * số giờ
#3 tính tổng lương

salary_list = [
    {
    "name": "Huy",
    "VNDperhour": 20,
    "hour": 25
    },
    {
    "name": "Quan",
    "VNDperhour": 30,
    "hour": 30
    },
    {
    "name": "H.Duc",
    "VNDperhour": 25,
    "hour": 15
    }
]

wage_list = [ p["VNDperhour"] * p["hour"] for p in salary_list ]
print (wage_list)
total = sum(wage_list)
print (total)

# total = 0
# for p in salary_list:
#     name = p["name"]
#     vnd = p["VNDperhour"]
#     hour = p["hour"]
#     wage = vnd * hour
#     print(name, wage)
#     total += wage

# print("Total wage:", total)

# total = 0
# for i in range(3):
#     spw = salary_list[i]["VNDperhour"] * salary_list[i]["hour"]
#     print(spw)
#     total += spw
# print(total)

