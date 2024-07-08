def pembagi_indeks(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1

vals = [100, 66, 55, 64, 41, 35, 18, 64]
hasil = pembagi_indeks(vals, 5)
print(hasil)  
