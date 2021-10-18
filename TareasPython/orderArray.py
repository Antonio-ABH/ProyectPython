def run():
    
    print()
    print('Program that order a list and remove repeated data')
    print()
    print('First Method using sets')
    print()
    list1 = [9,7,1,2,3,4,3,5,5,1,6,7,8,9,1,2,3,4]
    print(list1)
    
    #Set method converts the list to set and remove repeated data
    removeNumbers = set(list1)
    print()
    print(removeNumbers)
    print()
    
    # Use method list to converts set to a list again and order by self
    list1 = list(removeNumbers)
    print(list1)
    print()
    print('Second method using cycle for')
    print()
    list2 = [9,7,1,2,3,4,3,5,5,1,6,7,8,9,1,2,3,4]
    print(list2)
    print()
    
    # make 2 var
    notRepeatedNumbers = []
    repeatedNumbers = []
    
    # We need to loop the list2 with cycle for
    for n in list2:
        if n not in notRepeatedNumbers:
            notRepeatedNumbers.append(n)
        else:
            repeatedNumbers.append(n)
    print(notRepeatedNumbers)
    print()
    
    # reassing original value to list2
    list2 = notRepeatedNumbers
    
    # order the list2 with sort method
    list2.sort()
    print(list2)

    
    




if __name__ == '__main__':
    run()