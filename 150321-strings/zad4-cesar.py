import string # dla caesar_encode3


def caesar_encode(message, key):
    res = []
    for c in message:
        if 'A' <= c <= 'Z':
            idx = ord(c) - ord('A')
            idx = (idx + key) % 26
            res.append(chr(ord('A') + idx))
        else:
            res.append(c)
    return "".join(res)


def caesar_encode2(message, key):
    def letter(x):
        if 'A' <= x <= 'Z':
            idx = ord(x) - ord('A')
            idx = (idx + key) % 26
            return chr(ord('A') + idx)
        return x
    return "".join([letter(x) for x in message])
            

def caesar_encode3(message, key):
    alphabet = string.ascii_uppercase # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = []
    for c in message:
        idx = alphabet.find(c)
        if idx == -1:
            res.append(c)
            continue
        idx = (idx + key) % len(alphabet)
        res.append(alphabet[idx])
    return "".join(res)


def caesar_decode(message, key):
    return caesar_encode(message, -key)

if __name__ == "__main__":
    print(caesar_encode("THIS IS A VERY, VERY SECRET MESSAGE!", 7))
    print(caesar_encode2("THIS IS A VERY, VERY SECRET MESSAGE!", 7))
    print(caesar_encode3("THIS IS A VERY, VERY SECRET MESSAGE!", 7))
    print(caesar_decode(caesar_encode("THIS IS A VERY, VERY SECRET MESSAGE!", 50), 50))
