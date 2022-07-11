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

        cleaned_word = [x.lower() for x in word if x.isalnum()]
        mid = len(cleaned_word) // 2
        if mid < len(cleaned_word)/2:
            mid+=1

        left,right = cleaned_word[0:mid],cleaned_word[mid:]
        right.reverse()

        for x in range(len(right)):
            if left[x] != right[x]:
                answer = False
                break
            else:
                answer = True
        print(answer)
    return answer

if __name__ == '__main__':
    palindrome()