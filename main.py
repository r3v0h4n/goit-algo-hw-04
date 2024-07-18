import timeit
import random

from merge_sort import merge_sort
from insertion_sort import insertion_sort

def main():
    data_sizes = [100, 1000, 5000]
    datasets = {size: [random.randint(0, 10000) for _ in range(size)] for size in data_sizes}

    for size, data in datasets.items():        
        print(f"{size} elements:")

        t_insertion = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        t_merge = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        t_timsort = timeit.timeit(lambda: sorted(data.copy()), number=1)

        print(f"Insertion sort: {t_insertion}")
        print(f"Merge sort: {t_merge}")
        print(f"Tim sort: {t_timsort}")
        print("----------")


if __name__ == "__main__":
    main()