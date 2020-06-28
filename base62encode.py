import string


def base62encode(number):
    if number < 0:
        raise ValueError("The number should be larger than 0")
    base62 = string.digits + string.ascii_uppercase + string.ascii_lowercase
    result = []
    while True:
        pos, num = divmod(number, len(base62))
        if pos > 0:
            result.append(base62[num])
        else:
            return base62[num]
        number = pos
        if number < len(base62):
            break
    result.append(pos)
    final = [str(each) for each in reversed(result)]
    return "".join(final)


print(base62encode(2147483647))
print(base62encode(1))
print(base62encode(62))