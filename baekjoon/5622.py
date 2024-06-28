alp_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
alp = input()
result = 0

for i in alp:
    for j in alp_list:
        if i in str(j):
            num = alp_list.index(j) + 3
            result += num
print(result)