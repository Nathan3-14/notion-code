from typing import Dict, Any
import time
import os


if os.path.exists("launch.log"):
    pass


users = {
    "0210": ("Nathan", "3141"),
    "0114": ("Talin", "1596")
}
auth_code_2_tmp = "5926"
auth_code_3_tmp = "53589"

user = input("Enter user id\n> ")
_auth_1 = input("Enter your auth code\n> ")
_auth_2 = input("Enter auth code 2\n> ")
_auth_3 = input("Enter auth code 3\n> ")

try:
    user_data = users[user]
    username = user_data[0]
    auth_code_1 = user_data[1]
    if auth_code_1 == _auth_1 and auth_code_2_tmp == _auth_2 and auth_code_3_tmp == _auth_3:
        print(f"\nWelcome {username}")
    else:
        raise KeyError
except KeyError:
    print("Err: incorrect login details")
    quit()


atk_types = {
    "1": "ICBM",
    "2": "Rocket",
    "3": "Airdrop"
}

print(f"Select Attack type ({', '.join([f'{id}: {type}' for id, type in atk_types.items()])})")
atk_type = ""
while atk_type not in list(atk_types.keys()):
    atk_type = input(f"{username} >> ")
atk_type = atk_types[atk_type]

print("Enter a location")
location = input(f"{username} >> ")

log_text = f"{atk_type} fired at {location}\nAuthorised by user {user}"

print("Starting Countdown...")
x = 10
while x > 0:
    print(f"Time remaining {x}s")
    x -= 1
    time.sleep(1)
print("LAUNCH")

with open("launch.log", "w") as f:
    f.write(log_text)
