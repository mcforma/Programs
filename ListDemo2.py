# ListDemo2.py
# Demo of lists contd.

def main():
    odd_num = [1,3,5,7,9]
    even_num = [2,4,6,8]

    print(len(odd_num))
    print(len(even_num))

    print(odd_num)
    print(even_num)

    num_list = odd_num + even_num

    print(num_list)
    print(len(num_list))

    print(num_list[0:5]) # splicing / substring(ish): indices 0 TO EXCLUSIVE 3
    print(num_list[2:5])
    print(num_list[:4]) # 0 through 3. If first value unspecified default start is 0
    print(num_list[0:])
    print(num_list[::2])
    print(num_list[::3])

    for num in num_list:
        print(num)


main()