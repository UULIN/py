favorite_languanges ={
    'tom' : 'python',
    'jack': 'C',
    'phil': 'Java',
    'lili': 'shell'
}

friend=['tom', 'liming']

for name in friend:

    if name in favorite_languanges.keys():
        print(name + favorite_languanges[name])
    else:
        print("sorry , ", name, "is not in this people")

for name in sorted(favorite_languanges.keys()):
    print("keys  is " + name + "    value is  " + favorite_languanges[name])
