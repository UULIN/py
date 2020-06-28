"""
递推法，就是递增法，时间复杂度是 O(n)，呈线性增长，如果数据量巨大，速度会越拖越慢
"""

def feb(n):
    a,b = 0, 1
    for _ in range(n + 1):
        a, b = b, a+b
    return a

if __name__ == '__main__':
    for _ in range(20):
        print(feb(_))