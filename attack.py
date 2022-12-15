import math


def sqrt_n(mod):
    N = math.ceil(math.sqrt(mod))
    return N


def check(N, mod):
    for N2 in range(N, mod):
        if int(math.sqrt(abs(N2 ** 2 - mod))) == math.sqrt(abs(N2 ** 2 - mod)):
            return N2


def V(N2, mod):
    V = math.sqrt(abs(N2 ** 2 - mod))
    return V


def keys(p, q, e):
    mod = p * q
    fi = (p - 1) * (q - 1)
    while True:
        if math.gcd(e, fi) == 1:
            break
        else:
            print('Число е взаимно простое с fi, поэтому закрытый ключ посчитать не удалось')
            break
    d = 0
    for i in range(1, mod):
        if (e * i) % fi == 1:
            d = i
            break
    return d


def main():
    print('Давайте вычислим квадратный корень от n из открытого ключа и округлим его вверх к ближайшему целому значению')
    print('Введите открытый ключ:')
    e, mod = map(int, input().split())
    N = sqrt_n(mod)
    print(f'Вот что получилось: {N}')
    print('Далее давайте проверять целые числа больше N, как только значение формулы будет целым - задача факторизации решена')
    N2 = check(N, mod)
    print(f'Значение формулы целое при N = {N2}')
    print('Следовательно мы можем посчитать изначальные p и q')
    v = V(N2, mod)
    p = int(N2 + v)
    q = int(N2 - v)
    pq = p * q
    print(f'Получим, что p = {p}, q = {q}')
    print(f'Проверим, что все получилось, подставив в формулу p и q:'
          f' {p} * {q} = {pq}')
    d = keys(p, q, e)
    print(f'В итоге получаем закрытый ключ d = {d}')


if __name__ == '__main__':
    main()