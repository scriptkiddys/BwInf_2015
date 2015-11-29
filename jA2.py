def find_neighbours(position, fields):
    #Findet alle Indizes von weissen Nachbarfelder
    i, j = position
    result = []
    if 0 < i and fields[i-1][j]:
        result.append((i-1, j))
    if i < len(fields)-1 and fields[i+1][j]:
        result.append((i+1, j))
    if 0 < j and fields[i][j-1]:
        result.append((i, j-1))
    if j < len(fields[i])-1 and fields[i][j+1]:
        result.append((i, j+1))
    return set(result)

def print_visualising_fields(visualising_fields, step): #Gibt den aktuellen Zustand der Karte aus
    print("\n".join(["".join(row) for row in visualising_fields]))
    print("Schritt: "+str(step)+"\n")

with open(r".\Kassopeia\kassopeia0.txt") as d:
    STRING = d.read()

#Macht den String zu einer zweidimensionalen Liste
#True: weisses Feld (oder Kassopeia)
#False: schwarzes Feld
fields = []
visualising_fields = []
for i, row in enumerate(STRING.split("\n")[1:]): #ignoriere die erste Zeile
    fields_row = []
    visualising_fields_row = []
    for j, field in enumerate(row):
        visualising_fields_row.append(field)
        if field == "K":
            fields_row.append(True)
            kassopeia_field = (i,j) #Alle Koordinaten gehen von der linken oberen Ecke als Ursprung aus. Der erste Teil ist die Reihe, der zweite die Spalte
        elif field == " ":
            fields_row.append(True)
        elif field == "#":
            fields_row.append(False)
    fields.append(fields_row)
    visualising_fields.append(visualising_fields_row)
            
fully_checked_fields = set() #Die Felder, die von Kassopeia aus erreichbar sind und dessen Nachbarn auch schon ueberprueft wurden
checked_fields = set() #Die Felder, die von Kassopeia aus erreichbar sind, dessen Nachbarn aber noch nicht ueberprueft wurden
new_fields = set() #Felder, die von Kassopeia aus erreichbar sind, die erst in diesem Durchlauf hinzugefuegt wurden (Nachbarfelder von checked_fields)

checked_fields.add(kassopeia_field) #Kassopeias Feld ist der Ausgangspunkt
visualising_fields[kassopeia_field[0]][kassopeia_field[1]] = "A"

#Ziel: alle Felder, die von Kassopeias Feld aus erreichbar sind zu fully_checked_fields hinzufuegen
step = 0
first = True
while new_fields or first: #Solange es noch Felder gibt, die neu dazu gekommen sind, koennten die Nachbar dieser Felder noch nicht registriert werden sein
    first = False
    print_visualising_fields(visualising_fields, step) #Gibt den aktuellen Zustand der Karte und den Schritt aus, um den Vorgang anschaulicher zu machen
    new_fields = set() #new_fields wird zurueckgesetzt
    for cell in checked_fields: #Für alle Felder, deren Nachbarn noch nicht geprueft wurden, wird dies jetzt gemacht
        new_fields |= find_neighbours(cell, fields) #Die weissen Nachbarfelder werden zu new_fields hinzugefuegt
    fully_checked_fields |= checked_fields #Da die Nachbarn aller Felder in checked_fields jetzt ueberprueft wurden, werden sie zu fully_checked_fields hinzugefuegt
    checked_fields = new_fields-fully_checked_fields #Es werden alle neuen Felder, die noch nicht registriert wurden zu checked_fields
    #Aktualisiert die Daten in der Karte, die zur Veranschaulichung ausgegeben wird
    for field in fully_checked_fields: 
        visualising_fields[field[0]][field[1]] = "Z"
    for field in checked_fields: 
        visualising_fields[field[0]][field[1]] = "A"
    step += 1


#Wenn alle weissen Felder inf fields auch in fully_checked_fields sind, dann sind alle Felder von Kassopeia aus erreichbar
if all([field == ((i, j) in fully_checked_fields) for i, row in enumerate(fields) for j, field in enumerate(row)]):
    print("Kassopeia kann alle Felder erreichen.")
else:
    print("Kassopeia sind einige Felder versperrt.")
