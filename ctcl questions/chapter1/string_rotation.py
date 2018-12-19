def is_string_rotation(*args):
    str1, str2 =  args[0]
    return str2 in str1 + str1


if __name__ == '__main__':
    print(is_string_rotation(input("Input two space seperated strings: ").split()))
