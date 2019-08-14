

def count_swaps(a):
    swaps = 0
    for i in a:
        for j in range(0, len(a)-1):
            if a[j] > a[j+1]:
                swaps += 1
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    print(a)


count_swaps([1, 2, 3])