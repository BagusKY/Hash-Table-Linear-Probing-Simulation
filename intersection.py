def intersection(arr1, arr2):
    set2 = set(arr2)
    hasil = []

    for item in arr1:
        if item in set2:
            hasil.append(item)

    return hasil


# Contoh
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(intersection(a, b))
