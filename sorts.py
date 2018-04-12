#listaaa = [3, 5, 8, 3, 4, 9, 10, -2, 1]
listaaa = [3, 1, 8, 4]

def bublesort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - 1 - i):
            if(list[j] > list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]


def quicksort(list, low, high):
    if(low >= high):
        return
    print(list)
    pivot = list[high]
    y = low - 1
    #Placing the low values behind
    for x in range(low, high):
        if(list[x] <= pivot):
            y += 1
            list[x], list[y] = list[y], list[x]
    y += 1
    #placing the pivot next to all the alaments that are smmaller or equal to itself
    list[high], list[y] = list[y], list[high]
    quicksort(list, low, y - 1)
    quicksort(list, y + 1, high)


def mergesort(sublist):
    # We call thsi untis we get to a stackcall when atleast right or leftlist contains something
    if(len(sublist) > 1):
        midIndex = len(sublist) // 2
        leftList = sublist[:midIndex]
        rightList = sublist[midIndex:]
        #we always start from the left
        mergesort(leftList)
        mergesort(rightList)
        #and we always override our whole list from the begining
        k = 0
        while(len(leftList) > 0 and len(rightList) > 0):
            if(leftList[0] < rightList[0]):
                sublist[k] = leftList[0]
                leftList.pop(0)
                k += 1
            else:
                sublist[k] = rightList[0]
                rightList.pop(0)
                k += 1

        while(len(leftList) > 0):
            sublist[k] = leftList[0]
            leftList.pop(0)
            k += 1
        while(len(rightList) > 0):
            sublist[k] = rightList[0]
            rightList.pop(0)
            k += 1


def insertionSort(list):
    for x in range(1, len(list)):
        key = list[x]
        position = x
        while(list[position - 1] > key and position > 0):
            print(position)
            list[position] = list[position - 1]
            position -= 1        
        list[position] = key


insertionSort(listaaa)
#quicksort(listaaa, 0, len(listaaa) - 1)
print(listaaa)

