# bubble sort

# def bubblesort(array):
#     for i in range(len(array)):
#         for j in range(0,len(array)-i-1):
#             if array[j]>array[j+1]:
#                 x=array[j]
#                 array[i]=array[j+1]
#                 array[j+1]=x
# data=[-10,2,7,9,12]
# bubblesort(data)
# print(data)

# selection sort

# def selectionsort(array,size):
#     for step in range(size):
#         min_idx=step
#         for i in range(step+1,size):
#             if array[i]<array[min_idx]:
#                 min_idx=i
#                 (array[step],array[min_idx])=(array[min_idx],(array[step]))
# data=[-2,45,0,11,-9]
# size=len(data)
# selectionsort(data,size)
# print(data)


    
# Insertion sort in Python


# def insertionSort(array):

#     for step in range(1, len(array)):
#         key = array[step]
#         j = step - 1
        
#         # Compare key with each element on the left of it until an element smaller than it is found
#         # For descending order, change key<array[j] to key>array[j].        
#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j = j - 1
        
#         # Place key at after the element just smaller than it.
#         array[j + 1] = key


# data = [9, 5, 1, 4, 3]
# insertionSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)
