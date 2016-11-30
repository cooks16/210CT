def longest_sub(lis):
    longest = [1] * len(lis)  # create list of 1's as long as the given list
    sub = []
    for i in range(len(lis)):   # for position in lis
        for j in range(0, i):   # for each position between 0 and i
            if lis[i] > lis[j]:  # check the value now being check against all other beforehand
                longest[i] = max(longest[i], longest[j] + 1)  # if larger add 1 to the largest value between i and j
    print(max(longest)) # returns the length of the string
    longest.append(None)
    for i in range(len(longest)):  # loop through longest linking the each of the lowest values
        if longest[i + 1] is None:  # furthest along in longest to the original list
            if longest[i] > longest[i-1]:
                sub.append(lis[i])
            return sub
        if longest[i] < longest[i + 1] and longest[i] != longest[i + 1]:
            sub.append(lis[i])
    return sub


a = [9, 1, 3, 7, 5, 6, 20]
print(longest_sub(a))
