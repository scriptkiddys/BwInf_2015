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

def convert_to_direction(field1, field2): #Position von field1 relativ zu field2 als Richtung
    if field1[0] < field2[0]:
        return "N"
    elif field1[1] > field2[1]:
        return "O"
    elif field1[0] > field2[0]:
        return "S"
    elif field1[1] < field2[1]:
        return "W"
    else:
        raise RuntimeError()


with open(r".\Kassopeia\kassopeia0.txt") as d:
    STRING = d.read()


#Macht den String zu einer zweidimensionalen Liste
#True: weisses Feld (oder Kassopeia)
#False: schwarzes Feld
fields = []
for i, row in enumerate(STRING.split("\n")[1:]): #ignoriere die erste Zeile
    fields_row = []
    for j, field in enumerate(row):
        if field == "K":
            fields_row.append(True)
            kassopeia_field = (i,j) #Alle Koordinaten gehen von der linken oberen Ecke als Ursprung aus. Der erste Teil ist die Reihe, der zweite die Spalte
        elif field == " ":
            fields_row.append(True)
        elif field == "#":
            fields_row.append(False)
    fields.append(fields_row)

def find_path(previous_path):
    if all([field == ((i, j) in previous_path) for i, row in enumerate(fields) for j, field in enumerate(row)]): #Wenn alle weißen Felder abgedeckt sind.
        return previous_path #ist dies der richtige Weg und er wird zurück gegeben
    for field in find_neighbours(previous_path[-1], fields):
        if field in previous_path: #Felder auf denen Kassopeia bereits war können nicht erneut betreten werden
            continue #deshalb wird dieses Feld übersprungen
        path = find_path(previous_path+[field])
        if path:
            return path
    return False #kein passender Weg konnte gefunden werden

path = find_path([kassopeia_field])

if path:
    print("".join([convert_to_direction(path[i], path[i-1]) for i in range(1, len(path))]))
else:
    print("Es gibt keinen Weg für Kassopeia jedes weisse Feld genau einmal zu betreten.")
