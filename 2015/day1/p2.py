with open('puzzle.in')  as f:
    s,l = f.read(), 0
    for c in range(len(s)):
        if s[c] == '(':
            l += 1
        else:
            l -= 1
        if l < 0:
            print(c + 1)
            break
