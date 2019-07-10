def break_words(stuff):
    """This function will break up words for us."""
    # 将变量字符串拆分为词组以''分割
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the word."""
    # 对原来的列表内容进行排序，并返回新的列表
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    # 打印弹出后的第一个单词
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    # 打印弹出后的最后一个单词
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    # 输入完整的句子并返回排序后的单词
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    # 打印句子的第一个和最后一个单词
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    # 对单词进行排序，然后打印第一个和最后一个单词
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
