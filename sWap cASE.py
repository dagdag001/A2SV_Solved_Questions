def swap_case(s):
    res = ""
    for c in s:
        if c.isupper():
            c = c.lower()
        else:
            c = c.upper()
        res += c
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)