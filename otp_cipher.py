import sys

def one_time_pad_encrypt(plaintext_path, pad_path, output_path):
    with open(plaintext_path, 'rb') as pt, open(pad_path, 'rb') as pad, open(output_path, 'wb') as ct:
        while True:
            pt_byte = pt.read(1)
            pad_byte = pad.read(1)
            
            if not pt_byte or not pad_byte:
                break  # Stop when the end of either file is reached

            # XOR the bytes and write to the ciphertext file
            ct_byte = bytes([pt_byte[0] ^ pad_byte[0]])
            ct.write(ct_byte)

def one_time_pad_decrypt(ciphertext_path, pad_path, output_path):
    with open(ciphertext_path, 'rb') as ct, open(pad_path, 'rb') as pad, open(output_path, 'wb') as dt:
        while True:
            ct_byte = ct.read(1)
            pad_byte = pad.read(1)
            
            if not ct_byte or not pad_byte:
                break  # Stop when the end of either file is reached

            # XOR the bytes and write to the decrypted text file
            dt_byte = bytes([ct_byte[0] ^ pad_byte[0]])
            dt.write(dt_byte)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python otp_cipher.py <mode> <input_path> <pad_path> <output_path>")
        sys.exit(1)
        
    mode = sys.argv[1]
    input_path = sys.argv[2]
    pad_path = sys.argv[3]
    output_path = sys.argv[4]
    
    if mode == "--encrypt":
        one_time_pad_encrypt(input_path, pad_path, output_path)
        print(f"Encryption complete. Ciphertext saved to {output_path}.")
    elif mode == "--decrypt":
        one_time_pad_decrypt(input_path, pad_path, output_path)
        print(f"Decryption complete. Decrypted text saved to {output_path}.")
    else:
        print("Invalid mode. Use --encrypt or --decrypt.")
