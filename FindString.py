string = "isisii"
substring = "is"

def find_string(string, substring):
    c = 0
    d = 0

    while True:
        position = string.find(substring, c)
        if position >= 0:
            c = position + 1
            d = d + 1
        else:
            break

    return d

print find_string(string, substring)
