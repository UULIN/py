import re

def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    result =  re.split('[，。]', poem)
    if '' in result:
        result.remove('')
    print(result)

main()