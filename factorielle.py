import os, sys

# ! version 1

# if len(sys.argv) > 1 :
#     n = int(sys.argv[1])
#     res = 1
#     while n > 0 :
#         res = res*n
#         n = n - 1
# else :
#     print("Paramètre requis!!")

# print("factoriel de ",sys.argv[1],' est : ',res)

# ! Version 2

n = int(input('Donnez un nombre : '))
res = 1
if n != 0 :
    for i in range(n) :
        res = res*(i+1)
print('le factoriel de ', n, ' est : ', res )