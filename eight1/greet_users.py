def greet_users(names):
    """像列表中的每位用户都发出简单的问候"""
    for name in names:
        print("Hello " + name.title())

usernames = ['alin', 'ylin', 'xulin']
# test
greet_users(usernames)