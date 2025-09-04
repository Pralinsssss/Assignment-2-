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

def process_file(infile, outfile, shift1, shift2, encrypt=True):
    try:
        with open(infile, 'r') as f_in, open(outfile, 'w') as f_out:
            for line in f_in:
                f_out.write(''.join(shift_char(c, shift1, shift2, encrypt) for c in line))
        print(f"{'Encryption' if encrypt else 'Decryption'} completed. Output to {outfile}")
    except FileNotFoundError:
        print(f"Error: {infile} not found")
    except Exception as e:
        print(f"{'Encryption' if encrypt else 'Decryption'} error: {e}")

def verify_decryption():
    try:
        with open('raw_text.txt', 'r') as orig, open('decrypted_text.txt', 'r') as dec:
            print("Verification " + ("successful: Decrypted text matches original" if orig.read() == dec.read() else "failed: Decrypted text does not match original"))
    except FileNotFoundError:
        print("Error: One or both files not found")
    except Exception as e:
        print(f"Verification error: {e}")

def main():
    try:
        shift1 = int(input("Enter shift1 (integer): "))
        shift2 = int(input("Enter shift2 (integer): "))
        process_file('raw_text.txt', 'encrypted_text.txt', shift1, shift2)
        process_file('encrypted_text.txt', 'decrypted_text.txt', shift1, shift2, False)
        verify_decryption()
    except ValueError:
        print("Error: Enter valid integers for shifts")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
