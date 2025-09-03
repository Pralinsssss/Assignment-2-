def shift_char(char, shift1, shift2, encrypt=True):
    s1, s2 = (shift1, shift2) if encrypt else (-shift1, -shift2)
    if char.islower():
        if 'a' <= char <= 'm':
            shift = s1 * s2
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'n' <= char <= 'z':
            shift = s1 + s2
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char.isupper():
        if 'A' <= char <= 'M':
            return chr((ord(char) - ord('A') + s1) % 26 + ord('A'))
        elif 'N' <= char <= 'Z':
            shift = s2 * s2
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    return char