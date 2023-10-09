import random


class SortArray:
    """Filling in and sorting the list"""

    def insertion_sort(unsorted, n, int_flag):
        """Sorning data in list"""
        for i in range(1, n):
            val = unsorted[i]
            hole = i
            if int_flag != 1:
                while hole > 0 and unsorted[hole - 1] > val:
                    unsorted[hole] = unsorted[hole - 1]
                    hole -= 1
            else:
                while hole > 0 and unsorted[hole - 1] < val:
                    unsorted[hole] = unsorted[hole - 1]
                    hole -= 1
            unsorted[hole] = val
        return unsorted

    def set_random_list(count=int):
        """Filling list"""
        list_main = []
        k = 1
        for i in range(array_count):
            list_internal = [random.random() for _ in range(k)]
            k += 1
            list_main.append(list_internal)
        return list_main


if __name__ == "__main__":
    """Input data"""
    print("Hi my friend! Please input int-type data")
    while True:
        array_count = int(input())
        obj = SortArray
        list_main = obj.set_random_list(array_count)
        for j in range(len(list_main)):
            len_list = len(list_main[j])
            int_flag = 0 if (len_list % 2) == 0 else 1
            list_sorted = obj.insertion_sort(list_main[j], len_list, int_flag)
            list_main[j] = list_sorted
        print(list_main)
        print("let's again?")
