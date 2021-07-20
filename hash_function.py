def hashing(title, content, date):
    hash_value = ''
    sum_ = 0

    for el in title:
        el = ord(el)
        sum_ += el

    sum_ = str(sum_)
    hash_value += sum_ + 'T'

    sum_ = 0
    for el in content:
        el=ord(el)
        sum_ += el


    sum_ = str(sum_)
    hash_value += sum_ + 'C'

    sum_ = 0
    for el in date:
        if el.isdigit():
            sum_ += int(el)
        else:
            el = ord(el)
            sum_ += el

    sum_ = str(sum_)
    hash_value += sum_ + 'D'

# adding some more characters to make the hash value more unique
    hash_value += str(len(title)) + 'T'
    hash_value += str(len(content)) + 'C'
    hash_value += str(len(date)) + 'D'
    date = date.split(' ')
    hash_value += date[0]

    return hash_value
