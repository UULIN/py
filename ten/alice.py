from ten.word_count import count_words

filenames = ['alice', 'pi_digits', 'programming', 'pi']

for file in filenames:
    filename = "./source/" + file + ".txt"
    count_words(filename)