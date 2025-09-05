import os

def encrypt_char(char, shift1, shift2):
    if char.islower():
        if 'a' <= char <= 'm':
            shift = shift1 * shift2
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'n' <= char <= 'z':
            shift = shift1 + shift2
            return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    elif char.isupper():
        if 'A' <= char <= 'M':
            return chr((ord(char) - ord('A') - shift1) % 26 + ord('A'))
        elif 'N' <= char <= 'Z':
            shift = shift2 * shift2
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    return char

def encrypt_file(input_filename, output_filename, shift1, shift2):
    try:
        input_path = os.path.join(os.path.dirname(__file__), input_filename)
        if not os.path.exists(input_path):
            print(f"Error: Input file '{input_path}' not found.")
            return False
        
        with open(input_path, 'r') as f:
            text = f.read()
        
        if not text:
            print(f"Warning: Input file '{input_path}' is empty.")
            return False
        
        encrypted_text = ''.join(encrypt_char(char, shift1, shift2) for char in text)
        
        output_path = os.path.join(os.path.dirname(__file__), output_filename)
        
        with open(output_path, 'w') as f:
            f.write(encrypted_text)
        
        print(f"Encryption successful: Output written to '{output_path}'")
        return True
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_path}' or writing to '{output_path}'")
        return False
    except Exception as e:
        print(f"Encryption error: {e}")
        return False

def main():
    try:
        shift1 = int(input("Entre shift1 value: "))
        shift2 = int(input("Entre shift2 value: "))
        
        if not encrypt_file("raw_text.txt", "encrypted_text.txt", shift1, shift2):
            print("Encryption failed")
            return
        
    except ValueError:
        print("Error: Please entre the valid integer values for shift1 and shift2")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
