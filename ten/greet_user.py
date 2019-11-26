import json
filename = './source/username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Hello, " + username)
