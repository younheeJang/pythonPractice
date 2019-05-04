def is_palindrome(word):
    reserved = ''
    i = 0
    word_list = list(word)
    print(word_list)
    while i < len(word_list):
        i += 1
        reserved += word_list[len(word_list)-i]
    if(reserved == word):
        return True
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))


def is_palindrome(word):
    for left in range(len(word) // 2):
        print(left)

        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    return True


print(is_palindrome("kayak"))
print(is_palindrome("hello"))
