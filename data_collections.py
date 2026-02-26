## Saraksti ar 5+ skaitļiem
skaitli = [5, 7, 8, 10, 15]
print("Sakotnējais skaitlis:", skaitli)
# Pievieno elementu ar .append(beigu skaitlis)
skaitli.append (65)
print("Pēc appment()",skaitli)
# Dzēš pēdējo elementu ar .pop()                
dzestais = skaitli.pop()
print("Dzēstais elements:", dzestais)
print("Pēc pop():", skaitli)

# Saraksti: summa un vidējo vērtību ar for ciklu

summa = 0 #sākums sākas ar 0 un sāk krāties
skaits = 0 # mainīgais elements, nav sākuma skaitīts

for sk in skaitli: #cikls iziet katram elementam
    summa += sk  #pieskaits katru skaitli
    skaits += 1 #saskaits cik elementu un palielina par 1

videja = summa / skaits

print("summa:", summa)
print("vidējā vērtība:", videja)

#Filtrē sarakstu: pāra skaitļiem (for + if)

para_skaitli = []  # jauns saraksts pāra skaitļiem
for p_skaitlis in skaitli: 
    if p_skaitlis % 2 ==0: # %dalīšanasn vai dalās ar 2
        para_skaitli.append(p_skaitlis)
print("para_skaitli:", para_skaitli)

#Demonstrē (slice): pirmie 3, pēdējie 2, katrs otrais elements

print("Pirmie 3:", skaitli[:3])      # pirmie 3 jeb :3
print("Pēdējie 2:", skaitli[-2:])    # pēdējie 2, jeb -2:
print("katrs otrais:", skaitli[::2]) # ņem katru otro solis 2, jeb  ::2

## - Vārdnica

#saraksts ar 3+ studenti {atver un aizver vārdnīcu}
studenti = {
    "Anna": 85,
    "Jānis": 75,
    "Līga": 95
}
# saraksts
print("saraksts:")
for name, grade in studenti.items():
    print(f"{name} → {grade} punkti")

# Lietotājs ievada jaunu studenta vārdu un atzīmi  \n jauna rinda break 

jauns_vards = input("\nIevadi jaunā studenta vārdu: ")
# Lietotājs ievada jaunu atzīmi 
jauna_atzime = int(input("Ievadi jaunā studenta atzīmi: "))  #int ievada veselu skaitli 
# Pievieno vārdnīcā 
studenti[jauns_vards] = jauna_atzime 
print("Atjaunināt sarakstu:", studenti) #
# Iterējam caur vārdnīcu (atkārtot) 
for name, grade in studenti.items(): 
    print(f"{name} → {grade}, punkti")

# 1Atrod studentu ar augstāko atzīmi
labakais_vards = ""
labaka_atzime = 0
for name, grade in studenti.items():
    if grade > labaka_atzime:
        labaka_atzime = grade
        labakais_vards = name
print(f"Labākais students: {labakais_vards} ({labaka_atzime})\n")
# Studenti ar atzīmi >= 80
print("Studenti ar atzīmi >= 80:")
skaits = 1
for name, grade in studenti.items():
    if grade >= 80:
        print(f"{skaits}. {name} — {grade}")
        skaits += 1