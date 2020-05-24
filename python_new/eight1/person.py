def build_person(first_name, last_name, age=''):
    """返回一个字典，存储关于人的信息"""
    person = {'first_name': first_name, 'last_name': last_name}

    if age:
        person['age'] = age
    return person


print(build_person('xu', 'yulin', '22'))
print(build_person('a', 'lin'))


