def reverse(a):
    b = ""
    c = ""
    for i in a:
        if i != " ":
            b += i
        else:
            c = b + " " + c
            b = ""
    c = b + " " + c
    return c

print(reverse("This is awesome"))
