# list_functions_demo2.py
# Continuing with functions

def main():
    odd_list = [1,3,5,7,9]
    even_list = [2,4,6,8]
    
    num_list = odd_list + even_list

    print(num_list)

    print(max(num_list))
    print(min(num_list))

    num_list.sort()
    print(num_list)

    num_list.reverse()
    print(num_list)

    reptiles = ["Lizard", "Crocodile", "Chamelion", "komodo Dragon"]
    print(max(reptiles))
    print(min(reptiles))

    reptiles[3] = "Komodo Dragon"
    print(max(reptiles))

    reptiles.sort()
    print(reptiles)

    reptiles.reverse()
    print(reptiles)

    print(reptiles[-1])


main()