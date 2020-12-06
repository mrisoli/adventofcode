def get_seat(s):
    t = s.translate(s.maketrans('FBLR', '0101'))
    return (int(t[:7], 2) << 3) + int(t[7:], 2)
