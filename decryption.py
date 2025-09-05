import os

def decrypt_char(char, shift1, shift2):
    if char.islower():
        temp = (ord(char) - ord('a') - (shift1 * shift2)) % 26 + ord('a')
        if 'a' <= chr(temp) <= 'm':
            return chr(temp)
        return chr((ord(char) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))
    elif char.isupper():
        temp = (ord(char) - ord('A') + shift1) % 26 + ord('A')
        if 'A' <= chr(temp) <= 'M':
            return chr(temp)
        return chr((ord(char) - ord('A') - (shift2 * shift2)) % 26 + ord('A'))
    return char

def decrypt_file(input_filename, output_filename, shift1, shift2):
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
        
        decrypted_text = ''.join(decrypt_char(char, shift1, shift2) for char in text)
        
        output_path = os.path.join(os.path.dirname(__file__), output_filename)
        
        with open(output_path, 'w') as f:
            f.write(decrypted_text)
        
        print(f"Decryption successful: Output written to '{output_path}'")
        return True
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_path}' or writing to '{output_path}'")
        return False
    except Exception as e:
        print(f"Decryption error: {e}")
        return False

def main():
    try:
        shift1 = int(input("Enter the shift1 value: "))
        shift2 = int(input("Enter the shift2 value: "))
        
        if not decrypt_file("encrypted_text.txt", "decrypted_text.txt", shift1, shift2):
            print("Decryption failed")
            return
        
    except ValueError:
        print("Error: Please enter the valid integer values for shift1 and shift2")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
