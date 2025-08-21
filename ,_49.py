# a = 1
# b = 2

# print(id(a))
# print(id(b))

# print(a is b)
# a += 1
# b = a
# print(a is b)
# print(id(a))
# print(id(b))

# name = "Arek"
# print(dir(name))
# print(name.upper())

# int_data = 1
# print(int_data.bit_length())
# print(dir(int_data))
# print(int_data.conjugate())


a, b = 10, 3
print("ARYTMETYKA:", a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
print("BITY:", a & b, a | b, a ^ b, a << 2, a >> 1, ~a)
print("PORÓWNANIA:", a == b, a > b, a <= b)
print("FORMAT:", format(a, "b"), format(a, "#x"))
print("BIT LEN/COUNT:", a.bit_length(), a.bit_count())
by = a.to_bytes(2, "big")
print("BYTES:", by, int.from_bytes(by, "big"))
print("RATIO/REAL/IMAG:", a.as_integer_ratio(), a.real, a.imag)
