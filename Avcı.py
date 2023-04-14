def avcı_encrypt(text, key):
    # Avcı algoritması başlatılıtor...
    # Metni ASCII kodlarına dönüştürülecek (başla)...
    ascii_text = [ord(char) for char in text]
    
    # Anahtar kelimesinin ASCII toplamını hesaplanacak...
    key_sum = sum([ord(char) for char in key])
    
    # Metnin her karakterini anahtar kelimesinin ASCII toplamıyla XOR işlemine tabi tutulacak...
    encrypted = [char ^ key_sum for char in ascii_text]
    
    # Şifrelenmiş metni karakterlere dönüştürülecek..
    encrypted_text = ''.join([chr(char) for char in encrypted])
    
    return encrypted_text


def avcı_decrypt(encrypted_text, key):
    # Şifrelenmiş metni ASCII kodlarına dönüştürülecek...
    ascii_text = [ord(char) for char in encrypted_text]
    
    # Anahtar kelimesinin ASCII toplamını hesaplanacak...
    key_sum = sum([ord(char) for char in key])
    
    # Şifrelenmiş metnin her karakterini anahtar kelimesinin ASCII toplamıyla XOR işlemine tabi tutulacak...
    decrypted = [char ^ key_sum for char in ascii_text]
    
    # Şifre çözülmüş metni karakterlere dönüştürülecek...
    decrypted_text = ''.join([chr(char) for char in decrypted])
    
    return decrypted_text


# Kullanıcıdan metni ve anahtar kelimesini alınacak...
text = input("Metni girin: ")
key = input("Anahtar kelimesini girin: ")

# Metni şifreleyin ve kullanıcıya gösterilecek...
encrypted_text = avcı_encrypt(text, key)
print("Şifrelenmiş metin: ", encrypted_text)

# Şifrelenmiş metni çözün ve kullanıcıya gösterin (son)
decrypted_text = avcı_decrypt(encrypted_text, key)
print("Çözülmüş metin: ", decrypted_text)
