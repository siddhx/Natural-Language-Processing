def wordfreq (mystring):
    '''
    Function to generate the frequency distribution of the given text
    '''
    print(mystring)
    word_freq={}
    for token in mystring.split():
        if token in word_freq:
            word_freq[token] += 1
        else:
            word_freq[token] = 1
    print(word_freq)


def main():
    str = "This is my first python program"
    wordfreq(str)


if __name__ == '__main__':
    main()
