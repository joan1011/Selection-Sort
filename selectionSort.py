#selection sort algorthm
#array[8,5,2,9,5,6,3]
#define two seperate lists with in this array.One sublist with sorted numbers and others with unsorted numbers
#find the smallest number in this sublist of unsorted numbers and append to the sublist of sorted numbers


def selectionSort(array):
    currentIndex = 0
    while currentIndex < len(array)-1: #when current index gets to the Last number in the final position in the index.
        smallestIndex = currentIndex
        for i in range(currentIndex+1,len(array)):
            if array[smallestIndex] > array[i]:
                smallestIndex = i
        swap(currentIndex,smallestIndex,array)
        currentIndex +=1
	return array
 
def swap(i,j,array):
    array[i],array[j] = array[j],array[i]

selectionSort([-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8])
