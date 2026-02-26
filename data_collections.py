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