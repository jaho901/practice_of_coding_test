import sys
sys.stdin = open('practice3.txt')

def bruteForce(char, word):
    word_idx = 0
    char_idx = 0
    count = 0
    while char_idx < len(char) and word_idx < len(word):
        if word[word_idx] != char[char_idx]:
            word_idx = word_idx - char_idx
            char_idx = -1
        word_idx += 1
        char_idx += 1
        if char_idx == len(char):
            count += 1
            char_idx = 0
    return count




for _ in range(10):
    tc = int(input())
    char = input()
    word = input()
    print('#{} {}'.format(tc, bruteForce(char, word)))
