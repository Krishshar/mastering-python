def is_palindrome_permutation(string):
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    odds = 0
    for c in string:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if(table[x] % 2):
                odds += 1
            else:
                odds -= 1

    return odds <= 1


def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if(a <= val <= z):
        return val - a
    elif(A <= val <= Z):
        return val - A
    return -1


if __name__ == '__main__':
    print(is_palindrome_permutation(input("Enter a string: ")))
