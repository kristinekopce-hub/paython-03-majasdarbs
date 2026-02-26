# Saraksti ar 5+ skaitļiem
skaitli = [10, 15, 20, 25, 50]
print("Sakotnējais skaitlis:", skaitli)
# Pievieno elementu ar .append(beigu skaitlis)
skaitli.append (65)
print("Pēc appment()",skaitli)
# Dzēš pēdējo elementu ar .pop()
dzestais = skaitli.pop()
print("Dzēstais elements:", dzestais)
print("Pēc pop():", skaitli)

# Saraksti: summa un vidējo vērtību ar for ciklu
skaitli = [10, 15, 20, 25, 50]
summa = 0 #sākums sākas ar 0 un sāk krāties
skaits = 0 # mainīgais elements, nav sākuma skaitīts

for sk in skaitli: #cikls iziet katram elementam
    summa += sk  #pieskaits katru skaitli
    skaits += 1 #saskaits cik elementu un palielina par 1

videja = summa / skaits

print("summa:", summa)
print("vidējā vērtība:", videja)

#Filtrē sarakstu: pāra skaitļiem (for + if)
skaitli = [10, 15, 20, 25, 50]
para_skaitli = []  # jauns saraksts pāra skaitļiem
for p_skaitlis in skaitli: 
    if p_skaitlis % 2 ==0: # %dalīšanasn vai dalās ar 2
        para_skaitli.append(p_skaitlis)
print("para_skaitli:", para_skaitli)

#Demonstrē (slice): pirmie 3, pēdējie 2, katrs otrais elements
skaitli = [10, 15, 20, 25, 50]
print("Pirmie 3:", skaitli[:3])      # pirmie 3 jeb :3
print("Pēdējie 2:", skaitli[-2:])    # pēdējie 2, jeb -2:
print("katrs otrais:", skaitli[::2]) # ņem katru otro solis 2, jeb  ::2


