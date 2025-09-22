# Baptiste ROUQUETTE

# Exercise 5


rules = []
liste_sol = []
total_sol = []

with open("Exercise_5/data_ex_5_rules.txt", "r") as g:
    for line in g:
        line = line.strip()
        left, right = map(int, line.split("|"))
        rules.append((left, right))


with open("Exercise_5/data_ex_5_sol.txt", "r") as f:
    for line in f:
        line = line.strip()
        liste_sol = [int(x) for x in line.split(",")]
        total_sol.append(liste_sol)

res = 0
final_value = 0
new_list = []
new_res = 0
new_final_value = 0

for i, update in enumerate(total_sol, 1):
    tmp = True
    for a, b in rules:
        if a in update and b in update:
            if update.index(a) >= update.index(b):
                tmp = False
                break
    if tmp:
        res += 1
        n = len(update)
        if n % 2 == 1:
            value = update[n//2]
        else:
            value = update[n//2 - 1]
        final_value += value
    
    else:
        fixed = update.copy()
        changed = True
        while changed:
            changed = False
            for a, b in rules:
                if a in fixed and b in fixed:
                    idx_a = fixed.index(a)
                    idx_b = fixed.index(b)
                    if idx_a > idx_b:
                        fixed.pop(idx_a)
                        fixed.insert(idx_b, a)
                        changed = True
        new_list.append(fixed)

        new_res += 1
        new_n = len(fixed)
        if new_n % 2 == 1:
            new_value = fixed[new_n//2]
        else:
            new_value = fixed[new_n//2 - 1]
        new_final_value += new_value




print("Nombre de mises à jour correctes :", res)
print("Somme des valeurs centrales :", final_value)

print("Nombre de mises à jour correctes sur new liste :", new_res)
print("Somme des valeurs centrales sur new liste :", new_final_value)
