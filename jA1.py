def overlapping(claim1, claim2):
    #Wenn die linke x-Koordinate von claim größer ist als die rechte von claim2 oder die rechte von claim kleiner ist als die linke von claim2, überlappen die Rechtecke nicht
    #Wenn die untere y-Koordinate von claim größer ist als die ober von claim2 oder die ober von claim kleiner ist als die untere von claim2, überlappen die Rechtecke nicht
    #Ansonsten, überlappen sie
    return not (claim[0] >= claim2[2] or claim[2] <= claim2[0]) and not (claim[1] >= claim2[3] or claim[3] <= claim2[1])

claims = [(2, 3, 5, 5), (1, 2, 4, 4), (3, 1, 6, 3)]
accepted_claims = []

for claim in claims:
    if not any([overlapping(claim, claim2) for claim2 in accepted_claims]):
        accepted_claims.append(claim)
        print(claim, "accepted")
    else:
        print(claim, "not accepted")
