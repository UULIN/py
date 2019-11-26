import json


def set_stored_username():
    """提示输入用户名"""
    username = input("First please input you username: ")
    filename = "./source/username.json"
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return  username


def get_stored_username():
    """如果存储了用户，就获取他"""
    filename = './source/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Nice to meet you , " + username)
    else:
        username = set_stored_username()
        print("remember you , " + username)
