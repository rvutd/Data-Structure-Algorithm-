# Bubble Sort -
# fuction to swap elements -
def swapValue(firstElement, adjacentElement, arrToSort):
    (arrToSort[firstElement], arrToSort[adjacentElement]) = (arrToSort[adjacentElement], arrToSort[firstElement])
    
    # return value
    return arrToSort

# function to bubble sort list -
def bubbleSort(arrToSort):

    # No Element Swaped Indicator - 
    swaped = False
    
    # 2 loops with till lenght of list -
    # loop one carries firstElement
    for firstElement in range(0, len(arrToSort)):
    # loop two carries adjacentElement (Next Element in List)
        # this loop runs and reduces its lenght every time -
        for adjacentElement in range(0, len(arrToSort)-firstElement-1):
        # if firstElement value > adjacentElement 
            if arrToSort[adjacentElement] > arrToSort[adjacentElement+1]:
                # swap those digits and save to list -
                swapValue(adjacentElement, adjacentElement+1, arrToSort)
                swaped = True

        # if not element's swaped means array is already sorted
        if swaped == False:
            break


    # return sorted list
    return arrToSort

# Take Data In -
arrToSort = list(map(int, input().split()))[:]

# print(len(arrToSort))
print('Unsorted List = ', arrToSort, '\nSorted List =' ,bubbleSort(arrToSort))