def string_compression(string):
    curr_count = 1
    temp = string[0]
    for i in range(len(string) - 1):
        if(string[i] != string[i+1]):
            temp += str(curr_count) + string[i+1]
            curr_count = 1
        else:
            curr_count += 1
    final_string = temp + str(curr_count)
    return min(string, final_string, key=len)


if __name__ == '__main__':
    print(string_compression(input("Insert string to compress: ")))
