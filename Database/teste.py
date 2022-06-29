from multiprocessing.connection import wait


a = ["abc","def","ghi"]
b = ["xyz"]

print(b)
b += [item for item in a]
print(b)
