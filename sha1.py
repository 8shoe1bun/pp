import hashlib
# data = input("")
# sha1 = hashlib.sha1()
# sha1.update(data.encode('utf-8'))
# hashed_data = sha1.hexdigest()
# print("The hashed data using SHA1 is: ", hashed_data)
# print(len(hashed_data))

# import hashlib
data = input("")
sha = hashlib.sha512()
sha.update(data.encode('utf-8'))
datai = sha.hexdigest()

print("The hashed data using SHA512 is: ", datai)
print(len(datai))