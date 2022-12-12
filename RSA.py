import math

#Введите то, что хотите зашифровать в файл text.txt

def keys(p, q):
    mod = p * q
    fi = (p - 1) * (q - 1)
    while True:
        print('Выберите целое число е, взаимно простое с', fi, ':')
        e = int(input())
        if math.gcd(e, fi) == 1:
            break
        else:
            print('Попробуйте другое число.')
    d = 0
    for i in range(1, mod):
        if (e * i) % fi == 1:
            d = i
            break
    return e, mod, d

def encrypt(e, mod, phrase):
    encrypted_list = []
    for i in range(len(phrase)):
        encrypted_list.append(((ord(phrase[i])**e) % mod))
    encrypted_text = ''
    for j in range(len(encrypted_list)):
        encrypted_text += chr(encrypted_list[j])
    return encrypted_text

def decrypt(mod, d, encrypted_text):
    decrypted_list = []
    for i in range(len(encrypted_text)):
        decrypted_list.append(((ord(encrypted_text[i]))**d) % mod)
    decrypted_text = ''
    for j in range(len(decrypted_list)):
        decrypted_text += chr(decrypted_list[j])
    return decrypted_text

def main():
    #print('Введите текст для шифрования:')
    with open('text.txt') as f:
        phrase = f.read()
    print('Введите два простых числа:')
    p, q = map(int, input().split())
    e, mod, d = keys(p, q)
    print(f'Открытый ключ: ({e}, {mod})')
    print(f'Закрытый ключ: {d}')
    encrypted_text = encrypt(e, mod, phrase)
    print(f'Зашифрованное сообщение:\n {encrypted_text}')
    decrypted_text = decrypt(mod, d, encrypted_text)
    print(f'Расшифрованное сообщение:\n {decrypted_text}')

if __name__ == '__main__':
    main()
