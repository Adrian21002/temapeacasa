"""
Nota trecătoare la un test.
Presupunem că pentru a avea o notă trecătoare la un test,
elevii trebuie să obţină minim 15 puncte.
Scrieţi un program care citeşte de la tastatură punctajul obţinut de un elev şi
afişează dacă elevul are o notă trecătoare sau va trebui să mai susţină încă o dată testul.
"""
punctaj_acumulat = int(input("Introduceți punctajul acumulat: "))

if punctaj_acumulat >= 15:
    print("Felicitări! Aveți o notă trecătoare.")
else:
    print("Nu aveți o notă trecătoare. Va trebui să susțineți testul din nou.")
