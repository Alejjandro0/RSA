import math

#Введите то, что хотите зашифровать в файл plaintext.txt
#Введите числа зашифрованного сообщения в ciphertext.txt через пробел для расшифрования

def prime(j):
    k = 0
    for i in range(1, j+1):
        if j % i == 0:
            k+=1
    if k<=2:
        return j

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
    test = []
    for i in range(len(phrase)):
        encrypted_list.append(((ord(phrase[i])**e) % mod))
    encrypted_text = ''
    for j in range(len(encrypted_list)):
        encrypted_text += chr(encrypted_list[j])
    return encrypted_list

def decrypt(d, mod, phrase):
    decrypted_list = []
    arr = phrase.split(' ')
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    for i in range(len(arr)):
        decrypted_list.append(((arr[i])**d) % mod)
    decrypted_text = ''
    for j in range(len(decrypted_list)):
        decrypted_text += chr(decrypted_list[j])
    return decrypted_text

def main():
    #print('Введите текст для шифрования:')
    print('0 - Шифрование, 1 - Расшифрование')
    t = int(input())
    if t == 0:
        with open('plaintext.txt') as f:
            phrase = f.read()
        print('Введите два простых числа:')
        p, q = map(int, input().split())
        if not prime(p):
            raise TypeError(f'Число {p} не простое')
        if not prime(q):
            raise TypeError(f'Число {q} не простое')
        e, mod, d = keys(p, q)
        print(f'Открытый ключ: ({e}, {mod})')
        print(f'Закрытый ключ: {d}')
        encrypted_list = encrypt(e, mod, phrase)
        print(f'Зашифрованное сообщение:\n {encrypted_list}')
    if t == 1:
        with open('ciphertext.txt', 'r') as f:
            phrase = f.read()
        print('Введите ваш закрытый ключ:')
        d = int(input())
        print('Введите N из открытого ключа:')
        mod = int(input())
        decrypted_text = decrypt(d, mod, phrase) #(13, 21583) 1637
        print(f'Расшифрованное сообщение:\n {decrypted_text}')

if __name__ == '__main__':
    main()
