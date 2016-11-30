vowels = ["a", "i", "e", "o", "u", "A", "I", "E", "O", "U"]


def rem_v(s, n):
    if n == len(vowels):
        return s
    if vowels[n] in s:
        s = s.replace(vowels[n], "")
        return rem_v(s, n+1)
    else:
        return rem_v(s, n+1)
print(rem_v("Beautiful", 0))
