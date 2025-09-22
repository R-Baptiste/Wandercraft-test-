# Baptiste ROUQUETTE

# Exercise 2 


def main():
    total = 0
    total_phase_2 = 0
    with open("Exercise_2/data_ex_2.txt", "r") as f:
        for line in f:
            cols = line.split()
            liste = []
            for i in range(len(cols)):
                liste.append(int(cols[i]))
            increase = all(liste[i] < liste[i+1] for i in range(len(liste)-1))
            decrease = all(liste[i] > liste[i+1] for i in range(len(liste)-1))
            distance = all(abs(liste[i] - liste[i-1]) <= 3 for i in range(1, len(liste)))
            if (increase or decrease) and distance:
                total += 1

            for i in range(len(liste)):
                liste_phase_2 = liste.copy() 
                del liste_phase_2[i]
                increase = all(liste_phase_2[j] < liste_phase_2[j+1] for j in range(len(liste_phase_2)-1))
                decrease = all(liste_phase_2[j] > liste_phase_2[j+1] for j in range(len(liste_phase_2)-1))
                distance = all(abs(liste_phase_2[i] - liste_phase_2[i-1]) <= 3 for i in range(1, len(liste_phase_2)))
                if (increase or decrease) and distance:
                    total_phase_2 += 1
                    break

    print(total)
    print(total_phase_2)
    return



if __name__ == "__main__":
    main()