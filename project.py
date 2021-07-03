# question 1 --->

import hashlib
str = 'soumya'
output = hashlib.md5(str.encode())
print('the output is :) ')
print(output.hexdigest())


# question 2 ----->

import hashlib
str = hashlib.sha256()
print('the lib are :: ')
print(hashlib.algorithms_guaranteed)


str = 'soumya'
output = hashlib.sha1(str.encode())
print('the output is :) ')
print(output.hexdigest())


str = 'kolkata the city of joy'
output = hashlib.blake2b(str.encode())
print('the output is :) ')
print(output.hexdigest())


str = 'i <3 code'
output = hashlib.sha512(str.encode())
print('the output is :) ')
print(output.hexdigest())


# question 3 ----->


import hashlib , binascii
hash = hashlib.pbkdf2_hmac('sha512' , b'supersecertpassword' , b'saltthepassword' , 100000)
binascii.hexlify(hash)
print(hash)