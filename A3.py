def ways_to_arrange(number_of_bottles, buckets):
    print(number_of_bottles, buckets)
    if number_of_bottles < 0 or number_of_bottles > sum(buckets):
        return 0
    if not buckets:
        if number_of_bottles == 0:
            return 1
        else:
            return 0
    bucket = buckets[0]
    return sum([ways_to_arrange(number_of_bottles-filllevel, buckets[1:]) for filllevel in range(bucket+1)])

with open(r".\Flaschenzug\flaschenzug3.txt") as d:
    STRING = d.read()
    while STRING.rsplit("\n", 1)[1] == "": #leere letzte Zeile löschen
        STRING = STRING.rsplit("\n", 1)[0]

lines = STRING.split("\n")

number_of_bottles = int(lines[0])
buckets = sorted([int(b) for b in lines[2].split(" ")], reverse=True)
print(number_of_bottles)
print(buckets)

print(ways_to_arrange(number_of_bottles, buckets))
