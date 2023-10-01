import random
import game_data

def data_format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

for item in game_data.data:
    print(data_format(item))
    print("-----")
# 🚨 Don't change the code below 👇
# account1 = {
#     "name": "John",

#     "follower_count": 78,

#     "description": "Python",

#     "country": "United States"
# }

# account2 = {
    
#     "name": "Rolf",

#     "follower_count": 98,

#     "description": "JavaScript",

#     "country": "Sweden"

# }

# account3 = {
    
#     "name": "Anna",

#     "follower_count": 80,

#     "description": "Go",

#     "country": "United States"

# }

# print(data_format(account1))
# print(data_format(account2))
# print(data_format(account3))



