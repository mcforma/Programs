def main():
    l1 = [7, 6, 1, 2, 3, 4]
    l2 = [1, 3, 5 ,7 , 8]

    l3, list_sum = intersection_lists(l1, l2)
    print(f" The new list formed from the common elements of lists l1 and l2 is list l3: {l3} and the sum of l3 is: {list_sum}.")

def intersection_lists(list1, list2):
    i = 0
    j = 0
    list3 = []

    while i < len(list1):
        j = 0
        while j < len(list2):
            if list2[j] == list1[i]:
                list3.append(list2[j])
            j += 1
        i += 1
    
    list_sum = sum(list3)
    return list3, list_sum

main()