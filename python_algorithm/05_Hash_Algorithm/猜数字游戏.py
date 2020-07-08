"""
有一种猜数字游戏规则是这样的：一个人写下几个数字让另外一人猜，当每次答题方猜完之后，出题方会给答题方一个提示，
告诉他刚才的猜测中有多少位数字和
确切位置都猜对了，这种情况为全对的情况；还会告诉他多少位数字猜对了但是位置不对，这种情况为只是数字对的情况。
"""

# 猜数字游戏
def guessgame(secret, guess):
    secret_dict = {}
    guess_dict = {}
    count1 = 0
    count2 = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            count1 += 1
        else:
            if secret[i] in secret_dict:
                secret_dict[secret[i]] = secret_dict[secret[i]] + 1
            else:
                secret_dict[secret[i]] = 1
                if guess[i] in guess_dict:
                    guess_dict[guess[i]] = guess_dict[guess[i]] + 1
                else:
                    guess_dict[guess[i]] = 1
    for digit in secret_dict:
        if digit in guess_dict:
            count2 += min(secret_dict[digit], guess_dict[digit])
    return str(count1) + ',' + str(count2)


