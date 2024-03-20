def bsort(list1):
    Sorted = False
    IndexLength = len(list1) -1

    while not Sorted:
        Sorted = True
        for i in range(0, IndexLength):
            if list1[i] > list1[i+1]:
                Sorted= False
                list1[i], list1[i+1] = list1[i+1], list1[i]
    
    return list1


print(bsort([16,4,88,2,9,74,22,3]))
