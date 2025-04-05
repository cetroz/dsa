'''
    Bubble sort works by comparing two elements with each other.
    
    1) First item will be compared with second, and if first is greater it will swap places
    2) This will run till n-1 passes, and with each run the list will be "cut" by 1 (n-1-i)
    3) The cut is done, because the last element will be the greatest after each run
'''

def bubble_sort(array: list) -> list:
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array