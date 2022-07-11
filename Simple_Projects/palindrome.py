'''
Palindrome App

App rules:
1. Checks it the word or phrase is can be read the same after reversing it.
2. Ignore capitals, whitespaces, and symbols.
3. Input can be 'str', 'int', etc.
'''
def palindrome():
    while True:
        word = input('Put phrase/word: ')
        if word == 'exit':
            break

        base_word, reversed_word = [],[]           
        for x in word:
            if x.isalnum():
                base_word.append(x.lower())
                reversed_word.insert(0,x.lower())

        for x in range(len(base_word)):
            if base_word[x] == reversed_word[x]:
                answer = True
            else:
                answer = False
                break
        print(answer)
        base_word.pop(),reversed_word.pop

if __name__ == '__main__':
    print(palindrome())