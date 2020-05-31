"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re
while True:
    def main():
        user_name = input('please input username: ')
        qq_num = input('please input qq_num: ')

        m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', user_name)
        m2 = re.match(r'^[1-9][0-9]{4,11}$', qq_num)

        if not m1:
            print(r'您输入的用户名不符合规则！')
        if not m2:
            print(r'您输入的QQ号码不符合规则！')
        if m1 and m2:
            print(r'输入信息有效')

    if __name__ == '__main__':
        main()