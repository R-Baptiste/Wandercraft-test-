# Baptiste ROUQUETTE

# Exercise 3
import re


multiplication = 0
with open("Exercise_3/data_ex_3.txt", "r") as f:
    for line in f:
        line = line.strip()
        for pos in range(len(line)):
            if (line[pos] == 'm' and 
                pos+3 < len(line) and 
                line[pos+1] == 'u' and 
                line[pos+2] == 'l' and 
                line[pos+3] == '('):
                
                try:
                    end_paren = line.index(")", pos)       
                    inside = line[pos+4:end_paren]         
                    x, y = map(int, inside.split(","))
                    multiplication += x * y
                except:
                    pass

print("Résultat final 1 =", multiplication)


multiplication = 0
tmp = True
with open("Exercise_3/data_ex_3.txt", "r") as f:
    for line in f:
        line = line.strip()
        for pos in range(len(line)):
            if (line[pos] == 'm' and 
                pos+3 < len(line) and 
                line[pos+1] == 'u' and 
                line[pos+2] == 'l' and 
                line[pos+3] == '('):
                
                try:
                    end_paren = line.index(")", pos)       
                    inside = line[pos+4:end_paren]         
                    x, y = map(int, inside.split(","))
                    if tmp == True :
                        multiplication += x * y
                except:
                    pass
            elif (line[pos:pos+7] == "don't()"):
                tmp = False

            elif (line[pos:pos+4] == "do()"):
                tmp = True


                try:
                    end_paren = line.index(")", pos)       
                    inside = line[pos+4:end_paren]         
                    x, y = map(int, inside.split(","))
                    if tmp == True :
                        multiplication -= x * y
                except:
                    pass

print("Résultat final 2 =", multiplication)


