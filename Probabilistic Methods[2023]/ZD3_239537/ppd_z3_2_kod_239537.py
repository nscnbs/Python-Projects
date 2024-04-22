import secrets
import random

def insertion_sort(arr):
    comp_count = 0
    swap_count = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            comp_count += 1
            arr[j + 1] = arr[j]
            swap_count += 1
            j = j - 1

        arr[j + 1] = key
        swap_count += 1

    return comp_count, swap_count

def main():
    with open("results.txt", "a") as outfile:
        for n in range(100, 10001, 100):
            for k in range(50):
                arr = random.sample(range(2 * n), n)
                comp_count, swap_count = insertion_sort(arr)
                outfile.write(f"{n}\t{comp_count}\t{swap_count}\n")

if __name__ == "__main__":
    main()
