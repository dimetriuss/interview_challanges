from re import sub


def rle_encode_re(text: str) -> str:
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), text)


def rle_decode_re(text: str) -> str:
    if len(text) < 2:
        raise ValueError("Input text should contains at least 2 characters")
    if not text[0].isdigit() or text[-1].isdigit():
        raise ValueError("Input text should be started with digit and should be ended with non-digit")
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), text)


def rle_encode_native(text: str) -> str:
    counter = 1
    result = []
    if len(text) == 1:
        result.append(counter)
        result.append(text)
    elif len(text) >= 2:
        for i in range(1, len(text)):
            if text[i] == text[i-1]:
                counter += 1
            else:
                result.append(counter)
                result.append(text[i-1])
                counter = 1
        if text[-1] != text[-2]:
            result.append(counter)
            result.append(text[-1])
    return ''.join(map(str, result))


def rle_decode_native(text: str) -> str:
    if len(text) < 2:
        raise ValueError("Input text should contains at least 2 characters")
    if not text[0].isdigit() or text[-1].isdigit():
        raise ValueError("Input text should be started with digit and should be ended with non-digit")
    result = []
    temp = []
    for char in text:
        if char.isdigit():
            temp.append(char)
        else:
            decode = int(''.join(temp)) * char
            result.append(decode)
            temp = []
    return ''.join(result)
