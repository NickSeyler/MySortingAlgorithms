# Author:       Nick Seyler
# Date:         07/02/2020
# Description:  Sort an array by iterating through it and finding the minimum value


from BubbleSort import bubble_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSort import quick_sort
from SelectionSort import selection_sort


def main():
    arr = [9, 3, 4, 2, 6, 10, 1, 8, 7, 5]
    print(arr)  # before the array is sorted
    quick_sort(arr)  # replace this with any sorting method
    print(arr)  # after the array is sorted


if __name__ == "__main__":
    main()
