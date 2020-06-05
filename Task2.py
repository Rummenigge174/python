#1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
#Примечания:
#* в сумму не включаем пустую строку и строку целиком;
#* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.
#2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter


class Node:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def smbl_code(root, codes=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    smbl_code(root.left, codes, code + '0')
    smbl_code(root.right, codes, code + '1')

    return codes


def H_tree(string):
    freq = Counter(string)

    if len(freq) <= 1:
        node = Node(None)

        if len(freq) == 1:
            node.left = Node(string[0])
            node.right = Node(None)

        freq = {node: 1}

    while len(freq) != 1:
        node = Node(None)
        spam = freq.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])

        else:
            node.right = spam[1][0]

        del freq[spam[0][0]]
        del freq[spam[1][0]]
        freq[node] = spam[0][1] + spam[1][1]

    return list(freq.keys())[0]


def str_encode(string, codes):
    res = ''
    for symbol in string:
        res += codes[symbol]
    return res


def str_decode(string, codes):
    res = []
    enc_smbl = ''
    for symbol in string:
        enc_smbl += symbol
        for code in codes:
            if codes.get(code) == enc_smbl:
                res.append(code)
                enc_smbl = ''
                break

    return ''.join(res)


s = input('Введите строку: ')
tree = H_tree(s)
codes = smbl_code(tree)
# print('{codes}')
enc_string = str_encode(s, codes)
dec_string = str_decode(enc_string, codes)

print(f'Кодированна строка: {enc_string}')
print(f'Декодированная строка: {dec_string}')
