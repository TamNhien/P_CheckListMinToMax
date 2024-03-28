def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

lst = list(map(int, input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ").split(',')))
print(is_sorted(lst))
