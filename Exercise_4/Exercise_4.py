# Baptiste ROUQUETTE

# Exercise 4 

texte = []
with open("Exercise_4/data_ex_4.txt", "r") as f:
    for line in f:
        cols = list(line.strip())
        i = 0
        ligne = []
        while i < len(cols):
            ligne.append(cols[i])
            i += 1
        texte.append(ligne)

for ligne in texte:
    print(ligne)


sol = "XMAS"
length = len(sol)
line = len(texte)
column = len(texte[0])

direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

res = []

for i in range(line):
    for j in range(column):
        if texte[i][j] == sol[0]:  
            for dx, dy in direction:
                x, y = i, j
                k = 0
                while k < length:
                    if not (0 <= x < line and 0 <= y < column):
                        break
                    if texte[x][y] != sol[k]:
                        break
                    x += dx
                    y += dy
                    k += 1
                if k == length:
                    res.append(((i, j), (dx, dy)))
        

print("Nombre de 'XMAS' trouvés :", len(res))





length2 = len("MAS")
line2 = len(texte)
column2 = len(texte[0])

res2 = []

for i in range(1, line2-1):
    for j in range(1, column2-1):
        if texte[i][j] == "A":
            diag1 = texte[i-1][j-1] + "A" + texte[i+1][j+1]
            diag2 = texte[i-1][j+1] + "A" + texte[i+1][j-1]

            if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                res2.append((i,j))

print("Nombre de 'X-MAS' trouvés :", len(res2))

