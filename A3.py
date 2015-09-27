def ways_to_arrange(number_of_bottles, buckets):
    if number_of_bottles < 0:
        return 0
    if not buckets:
        if number_of_bottles == 0:
            return 1
        else:
            return 0
    bucket = buckets[0]
    return sum([ways_to_arrange(number_of_bottles-filllevel, buckets[1:]) for filllevel in range(bucket+1)])

text = """7
2
3 5"""
lines = text.split("\n")

number_of_bottles = int(lines[0])
buckets = [int(b) for b in lines[2].split(" ")]

print(ways_to_arrange(number_of_bottles, buckets))
