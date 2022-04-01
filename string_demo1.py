#list_Oper_demo1.py
# Demo on lists

def main():
    name = "Julian"
    for char in name:
        print(char)

    print(name[0], name[2], name [5])

    # name[4] = "e" strings are immutable but can be concatenated because concatenation 
    # actually creates a new string and assigns the new string to the previously used variable
    last_name = " Brown"
    name += last_name


    print(name * 3)
    print(name)

    print("Brow" in name)

main()