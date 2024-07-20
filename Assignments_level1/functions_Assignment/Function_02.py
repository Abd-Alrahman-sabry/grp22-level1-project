def palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False


word_test = input("Enter a word: ")
print(word_test, "is a palindrome?")

word = palindrome(word_test)
print(word)
