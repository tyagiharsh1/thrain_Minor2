import enc_dec
import time
import unicodedata
import os
import os.path
import Diffie_Helman

# Encryption method
def encrypt(filename, directory, public_key, private_key):
    key = Diffie_Helman.generate_secret(int(private_key), int(public_key))
    key = key[0:32]  # Ensure the key is 32 bytes long

    # Encode the key string to bytes using UTF-8 encoding
    key_bytes = key.encode('utf-8')

    file_obj = open(filename, "r")
    t = time.time()
    msg1 = enc_dec.AESCipher(key_bytes).encrypt(file_obj.read())
    s = time.time()
    outputFilename = os.path.join(directory, key[16:] + ".txt")
    file_obj = open(outputFilename, 'wb')  # Open the file in binary mode for writing bytes
    file_obj.write(msg1.encode('utf-8'))

    file_obj.close()  # Close the file after writing
    os.remove(filename)
    os.startfile(output_filename)


# Decryption Method
def decrypt(filename, directory, public_key, private_key):
    key = Diffie_Helman.generate_secret(int(private_key), int(public_key))
    key = key[0:32]

    # Encode the key string to bytes using UTF-8 encoding
    key_bytes = key.encode('utf-8')

    file_obj = open(filename, "rb")  # Open the file in binary mode for reading bytes
    msg = file_obj.read()
    file_obj.close()  # Close the file after reading
    text = enc_dec.AESCipher(key_bytes).decrypt(msg)
    outputFilename = os.path.join(directory, "DecodedFile.txt")
    file_obj = open(outputFilename, "w")
    file_obj.write(text)
    file_obj.close()  # Close the file after writing
    os.remove(filename)
    os.system("xdg-open " + directory)
# Prime Numbers
prime_ = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AAAC42DAD33170D04507A33A85521ABDF1CBA64ECFB850458DBEF0A8AEA71575D060C7DB3970F85A6E1E4C7ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261AD2EE6BF12FFA06D98A0864D87602733EC86A64521F2B18177B200CBBE117577A615D6C770988C0BAD946E208E24FA074E5AB3143DB5BFCE0FD108E4B82D120A92108011A723C12A787E6D788719A10BDBA5B2699C327186AF4E23C1A946834B6150BDA2583E9CA2AD44CE8DBBBC2DB04DE8EF92E8E