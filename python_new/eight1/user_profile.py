def build_profile(username , password, **info):
    profile ={}
    profile['username'] = username
    profile['password'] = password

    for key, value in info.items():
        profile[key] = value
    return profile


print(build_profile('xu', '123', age='12', p = '1111'))
