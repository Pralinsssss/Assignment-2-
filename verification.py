import os

def compare_files(raw_filename, decrypted_filename):
    try:
        raw_path = os.path.join(os.path.dirname(__file__), raw_filename)
        decrypted_path = os.path.join(os.path.dirname(__file__), decrypted_filename)
        
        if not os.path.exists(raw_path):
            print(f"Error: '{raw_filename}' not found.")
            return False
        if not os.path.exists(decrypted_path):
            print(f"Error: '{decrypted_filename}' not found.")
            return False
        
        with open(raw_path, 'r') as f:
            raw_text = f.read().strip()
        with open(decrypted_path, 'r') as f:
            decrypted_text = f.read().strip()
        
        is_match = raw_text == decrypted_text
        print(f"Comparison result: {'Match' if is_match else 'Mismatch'}")
        print(f"Raw text preview: {raw_text[:100] + '...' if len(raw_text) > 100 else raw_text}")
        print(f"Decrypted text preview: {decrypted_text[:100] + '...' if len(decrypted_text) > 100 else decrypted_text}")
        
        if not is_match:
            print("Differences found. Check full files for details.")
            for i, (r, d) in enumerate(zip(raw_text, decrypted_text)):
                if r != d:
                    print(f"First difference at position {i}: raw='{r}', decrypted='{d}'")
                    break
        
        return is_match
    
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    if not compare_files("raw_text.txt", "decrypted_text.txt"):
        print("Comparison failed. Ensure files exist and are correct.")

if __name__ == "__main__":
    main()