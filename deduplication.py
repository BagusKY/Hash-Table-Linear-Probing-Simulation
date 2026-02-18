def deduplikasi(lst):
    seen = set()
    hasil = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            hasil.append(item)

    return hasil


# Contoh
data = [1, 2, 2, 3, 4, 3, 5]
print(deduplikasi(data))
