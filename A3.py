from functools import lru_cache

@lru_cache(None)
def ways_to_arrange(number_of_bottles, buckets): 
    if number_of_bottles < 0 or number_of_bottles > sum(buckets):
        return 0
    elif number_of_bottles == 0:
        return 1
    elif len(buckets) == 1 and number_of_bottles <= buckets[0]:
        return 1
    elif not buckets: #number_of_bottles > 0
        return 0
    else:
        bucket = buckets[0]
        return sum([ways_to_arrange(number_of_bottles-fillnumber, buckets[1:]) for fillnumber in range(min(bucket, number_of_bottles)+1)])

with open(r".\Flaschenzug\flaschenzug0.txt") as d:
    STRING = d.read()
    while STRING.rsplit("\n", 1)[1] == "": #leere letzte Zeile löschen
        STRING = STRING.rsplit("\n", 1)[0]

lines = STRING.split("\n")

number_of_bottles = int(lines[0])
buckets = [int(b) for b in lines[2].split(" ")]

##print(number_of_bottles)
##print(buckets)
##print()
print(ways_to_arrange(number_of_bottles, tuple(buckets)), "Moeglichkeiten")

