HEXDIGITS = "0123456789ABCDEF"
hextobyte = {
    (i + j).encode(): bytes.fromhex(i + j) for i in HEXDIGITS for j in HEXDIGITS
}


def unquote(url: str):
    url_byte = url.encode()
    bits = url_byte.split(b'%')
    if len(bits) == 1:
        return url
    
    result = bytearray(bits[0])
    append = result.extend

    for i in range(1, len(bits)):
        item = bits[i][0:2]
        if item in hextobyte:
            append(hextobyte[item])
            append(bits[i][2:])
        else:
            append(b'%')
            append(bits[i])
    return result.decode()


while True:
    try:
        print(unquote(input()))
    except EOFError:
        break
