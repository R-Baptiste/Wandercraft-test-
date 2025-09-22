# Baptiste ROUQUETTE

# Exercise 1 

liste1 = []
liste2 = []

with open("Exercise_1/data_ex_1.txt", "r") as f:
    for line in f:
        cols = line.split()
        if len(cols) == 2:   
            liste1.append(int(cols[0]))
            liste2.append(int(cols[1]))




def distance(L1,L2):

    L1 = sorted(L1)
    L2 = sorted(L2)
    tmp = 0
    if len(L1) <= len(L2):
        x = len(L1)
    else:
        x = len(L2)
    for i in range(x):
        tmp += abs(L1[i] - L2[i])
    return tmp


L1 = [3, 4, 2, 1, 3, 3]
L2 = [4, 3, 5, 3, 9, 3]

print(distance(L1,L2))  # Expected output : 11 (by hand calculation)
print(distance(liste1,liste2))  # Expected output : 1992864 (by hand calculation)




liste1_part2 = []
liste2_part2 = []

with open("Exercise_1/data_ex_1.txt", "r") as f:
    for line in f:
        cols = line.split()
        if len(cols) == 2:   
            liste1_part2.append(int(cols[0]))
            liste2_part2.append(int(cols[1]))


L1 = [3, 4, 2, 1, 3, 3]
L2 = [4, 3, 5, 3, 9, 3]

def distance_v2(L1,L2):
    res = 0 
    tmp = 0
    for i in L1:
        tmp = 0
        for j in L2:
            if i == j:
                tmp += 1
        res += i * tmp
    return res

print(distance_v2(L1,L2)) 
print(distance_v2(liste1_part2,liste2_part2))