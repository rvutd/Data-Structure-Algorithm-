# Bubble Sort -
# fuction to swap elements -
def swapValue(firstElement, adjacentElement, arrToSort):
    (arrToSort[firstElement], arrToSort[adjacentElement]) = (arrToSort[adjacentElement], arrToSort[firstElement])
    
    # return value
    return arrToSort

# function to bubble sort list -
def bubbleSort(arrToSort):
    
    # 2 loops with till lenght of list -
    # loop one carries firstElement
    for firstElement in range(0, len(arrToSort)):
    # loop two carries adjacentElement (Next Element in List)
        for adjacentElement in range(0, len(arrToSort)):
        # if firstElement value < adjacentElement 
            if arrToSort[firstElement] < arrToSort[adjacentElement]:
                # swap those digits and save to list -
                swapValue(firstElement, adjacentElement, arrToSort)
    # return sorted list
    return arrToSort

# Take Data In -
arrToSort = list(map(int, input().split(',')))[:]

# print(len(arrToSort))
print('Unsorted List = ', arrToSort, '\nSorted List =' ,bubbleSort(arrToSort))