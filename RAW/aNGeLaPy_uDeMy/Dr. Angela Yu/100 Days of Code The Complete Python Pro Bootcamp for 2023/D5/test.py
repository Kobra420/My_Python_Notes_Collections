# l = [156, 178, 165, 171, 187]
# for i in l:
#     i = i + 1
# print(type(i))

# Max integer value ValueError:
# Exceeds the limit (4300) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

# i = 2**14284
# print(f"Max. integer value:{i}")
# l = i
# l1 = str(l)
# print(f"max int length:{len(l1)}")

# # max range----------- OverflowError: Python int too large to convert to C ssize_t

# print(list(range(2 ** 100)))
marks = input("Enter numbers obtained:").split()
for i in range(0, len(marks)):
    marks[i] = float(marks[i])
print(marks[3], type(marks[3]))
