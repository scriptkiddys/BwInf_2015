def overlapping(claim1, claim2):
    return not (
        claim[1] >= claim2[3] or #die untere y-Koordinate von claim1 ist groesser als die obere von claim2 -> claim1 liegt über claim2
        claim[3] <= claim2[1] or #die obere y-Koordinate von claim1 ist kleiner als die untere von claim2 -> claim1 liegt unter claim2
        claim[2] <= claim2[0] or #die rechte x-Koordinate von claim1 ist kleiner als die linke von claim2 -> claim1 liegt links neben claim2
        claim[0] >= claim2[2]) #die linke x-Koordinate von claim1 ist groesser als die rechte von claim2 -> claim1 liegt rechts neben claim2

claims = [(2, 3, 5, 5), (1, 2, 4, 4), (3, 1, 6, 3)]
accepted_claims = []

for claim in claims:
    if not any([overlapping(claim, claim2) for claim2 in accepted_claims]):
        accepted_claims.append(claim)
        print(claim, "accepted")
    else:
        print(claim, "not accepted")
