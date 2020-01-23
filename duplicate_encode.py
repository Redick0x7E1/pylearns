def duplicate_encode(word):
    word.lower()
    s = list(word)
    count = 0
    i = 0
    found = []
    new_s = []
    for i in range(len(s)):

        if s[i] not in found:
            found.append(s[i])

    for letter in found:
        for x in range(len(s)):

            if s[x] == letter:
                count += 1
        if count >= 2:
            new_s.append("(")
        if count == 1:
            new_s.append(")")
        count = 0
    return new_s

a = "abbccc"

print(duplicate_encode(a))