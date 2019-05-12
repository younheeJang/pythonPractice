def is_palindrome(word):
    words = list(word)
    howMany = len(words)//2
    standard = [*range(howMany)]

    counterpart_index = 0
    for index in standard:
        counterpart_index = counterpart_index - 1
        if words[index] == words[counterpart_index]:
            pass
        else:
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))