def binary_search(a_list, x, y):
    first = 0
    last = len(a_list) - 1
    if x > y:
        x += y
        y = x - y  # code needs x to be smaller than y this just switches them if it isn't
        x -= y
    in_range_1 = False      # is there a value larger than x
    in_range_2 = False      # is there a value smaller than y
    while first <= last and (not in_range_1 or not in_range_2):  # loop until in range or until search finishes
        m = (first + last // 2)
        if x < a_list[m]:
            in_range_1 = True       # if larger than x
            if y > a_list[m]:
                in_range_2 = True   # if smaller than y
            else:
                last = m - 1  # larger than x but also larger than y midpoint moves down
        else:
            first = m + 1     # not larger than x then midpoint moves up
    if in_range_1 and in_range_2:   # when both true output true
        return True
    else:             # if loop finishes and both not true output false
        return False


a = [5, 22, 45, 56, 87, 123, 124, 165, 222, 245]
print(binary_search(a, 223, 246))
