def count_words(filename):
    """计算一个文件中包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
        # print("not found" + filename + "'s file")
        pass
    else:
        """计算文件大致包含多少个单词"""
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + "has about " + str(num_words) + " words")