def find_in_2d_list(list_, element):
    #Findet ein Element in einer zweidimensionalen Liste
    for i, row in enumerate(list_):
        try:
            j = row.index(element)
        except ValueError:
            pass
        else:
            return i, j
    raise ValueError(str(elem)+" is not in list")

def find_neighbours(position, fields):
    #Findet alle Indizes von weissen Nachbarfelder
    x, y = position
    result = []
    if 0 < x and fields[x-1][y]:
        result.append((x-1, y))
    if x < len(fields)-1 and fields[x+1][y]:
        result.append((x+1, y))
    if 0 < y and fields[x][y-1]:
        result.append((x, y-1))
    if y < len(fields[x])-1 and fields[x][y+1]:
        result.append((x, y+1))
    return set(result)

fields = """6 9
#########
#  #    #
#  # #  #
#  K #  #
#    #  #
#########"""

#Macht den String zu einer zweidimensionalen Liste
#True: weisses Feld
#False: schwarzes Feld
#K: Kassopeia
fields = [[field==" " if field != "K" else "K" for field in row] for row in fields.split("\n")[1:]]

checked_fields = set() #Die Felder, die von Kassopeia aus erreichbar sind und dessen Nachbarn auch schon ueberprueft wurden
unchecked_fields = set() #Die Felder, die von Kassopeia aus erreichbar sind, dessen Nachbarn aber noch nicht ueberprueft wurden
new_fields = set() #Felder, die von Kassopeia aus erreichbar sind, die erst in diesem Durchlauf hinzugefuegt wurden (Nachbarfelder von unchecked_fields)

#Finde Kassopeias Feld
i, j = find_in_2d_list(fields, "K")
fields[i][j] = True
unchecked_fields.add((i, j)) #Kassopeias Feld ist der Ausgangspunkt

#Ziel: alle Felder, die von Kassopeias Feld aus erreichbar sind zu checked_fields hinzufuegen
first = True
while new_fields or first: #Solange es noch Felder gibt, die neu dazu gekommen sind, koennten die Nachbar dieser Felder noch nicht registriert werden sein
    first = False
    new_fields = set() #new_fields wird zurueckgesetzt
    for cell in unchecked_fields: #Für alle Felder, deren Nachbarn noch nicht geprueft wurden, wird dies jetzt gemacht
        new_fields |= find_neighbours(cell, fields) #Die weissen Nachbarfelder werden zu new_fields hinzugefuegt
    checked_fields |= unchecked_fields #Da die Nachbarn aller Felder in unchecked_fields jetzt ueberprueft wurden, werden sie zu checked_fields hinzugefuegt
    unchecked_fields = new_fields-checked_fields #Es werden alle neuen Felder, die noch nicht registriert wurden zu unchecked_fields

#Wenn alle weissen Felder inf fields auch in checked_fields sind, dann sind alle Felder von Kassopeia aus erreichbar
if all([field == ((i, j) in checked_fields) for i, row in enumerate(fields) for j, field in enumerate(row)]):
    print("Kassopeia kann alle Felder erreichen.")
else:
    print("Kassopeia sind einige Felder versperrt.")
