favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
# 遍历所有人喜欢的语言

for name,languages in favorite_languages.items():
    print(name.title() + '\'s favorite languages is:')
    if len(languages) > 1:
        for language in languages:
            print("\t" + language)