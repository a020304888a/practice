size = int(input("Input size:"))

print("size =", size)

print("1.")
for i in range(1, size+1, 1):
	for j in range(1, i+1, 1):
		print("*", end='')
	print()
print("\n2.")
for i in range(size, 0, -1):
	for j in range(i, 0, -1):
		print("*", end='')
	print()

print("\n3.")
for i in range(1, size+1, 1):
	for j in range(i, size, 1):
		print(" ", end='')
	for j in range(1, i+1, 1):
		print("*", end='')
	print()

print("\n4.")
for i in range(size, 0, -1):
	for j in range(i, size, 1):
		print(" ", end='')
	for j in range(i, 0, -1):
		print("*", end='')
	print()
