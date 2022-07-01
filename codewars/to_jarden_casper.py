def cap(word):
    return word.capitalize()
def to_jaden_case(string):
    wl = string.split(' ')
    wl = list(map(cap, wl))
    return ' '.join(wl)