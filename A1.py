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
        print("Big problem:", field1, field2)


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

#Finde Kassopeias Feld
i, j = find_in_2d_list(fields, "K") #Alle Koordinaten gehen von der linken oberen Ecke als Ursprung aus. Der erste Teil ist die Reihe, der zweite die Spalte
fields[i][j] = True

def find_path(previous_path):
    if all([field == ((i, j) in previous_path) for i, row in enumerate(fields) for j, field in enumerate(row)]): #Wenn alle weißen Felder abgedeckt sind.
        return previous_path #ist dies der richtige Weg und er wird zurück gegeben
    for field in find_neighbours(previous_path[-1], fields):
        if field in previous_path: #Felder auf denen Kassopeia bereits war können nicht erneut betreten werden
            continue #deshalb wird dieses Feld übersprungen
        path = find_path(previous_path+[field])
        if path:
            return path

path = find_path([(i, j)])

if path:
    print("".join([convert_to_direction(path[i], path[i-1]) for i in range(1, len(path))]))
else:
    print("Es gibt keinen Weg für Kassopeia jedes weisse Feld genau einmal zu betreten.")
