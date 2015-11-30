import math
import random

def shuffled(l): #Gibt die Liste l zufaellig gemischt zurueck
    r = list(l)[:]
    random.shuffle(r) #Dies ist noetig, weil random.shuffle in-place mischt
    return r

def print_key(key, key_number=None, min_key_difference_=None): #Gibt den den Schluessel key formatiert als Schluesselkarte aus
    if key_number is not None:
        print("Schluesselkarte {}:".format(key_number))
    for i in range(5):
        for j in range(5):
            print("x" if key[i*5+j] else ".", end="") #Gestanzte Positionen werden als "x" dargestellt, nicht-gestanzte als "."
        print()
    if min_key_difference_ is not None:
        print("Mindestabstand:", min_key_difference_)
        

#"Abstand"
def key_difference(key1, key2): #Gibt die Anzahl unterschiedlicher Stanz-Positionen (ob gestanzt oder nicht) von key1 und key2 zurueck, dies wird als Mass fuer die Unterschiedlichkeit von Schluesselkarten betrachtet. Ein Rueckgabewert von 0 bedeutet, dass die Schluessel identisch sind.
    return sum([key1[i]^key2[i] for i in range(25)])

#"Mindestabstand"
def min_key_difference(key, other_keys): #Gibt den kleinsten Abstand zwischen der Schluesselkarte key und einer Schluesselkarte aus other_keys zurueck.
    return min([key_difference(key, key2) for key2 in other_keys])

def next_key(keys, max_tries=100): #Gibt eine Schluesselkarte zurueck, die sich von den schon vorhandenen moeglichst stark unterscheidet
    if len(keys) == 2:
        target_difference = 12
    else:
        target_difference = min_key_difference(keys[-1], keys[:-1])
    #Startet mit einer Schluesselkarte, die an jeder Stelle mit der Mehrheit der schon vorhandenen Schluesselkarten uebereinstimmt, die sich also zunaechst moeglichst wenig unterscheidet
    r = [sum(key[i] for key in keys) > len(keys)/2. for i in range(25)]
    tries = 0
    #Versucht maximal max_tries einen Schlüssel mit der target_difference als Mindestabstand zu finden
    #und wenn dies nicht gelingt, wird danach ein Schlüssel mit einem Mindestabstand gesucht, der um eins niederiger ist als die target_difference, jedoch darf der Mindestabstand niemals kleiner als 1 sein, denn dann waeren die Schluesselkarten identisch
    while tries < max_tries and min_key_difference(r, keys) < target_difference \
            or min_key_difference(r, keys) < max(target_difference-1, 1):
        for i in shuffled(range(25)):
            sim_key = min([(key_difference(key, r), key) for key in keys])[1] #Es wird die zu r aehnlichste vorhandene Schluesselkarte gesucht
            r[i] = not sim_key[i] #An der Stanz-Position i wird r auf das Gegenteil der aehnlichsten Schluesselkarte an der Stanz-Position i gesetzt, wenn die aehnlichste Schluesselkarte dort gestanzt ist, ist r es nicht und umgekehrt
        tries += 1
    return r

def invert_key(key): #Gibt die inverse Schluesselkarte zu key zurueck
    return [not e for e in key]
    
N = 20

keys = [[True]*25, [False]*25] #Da alles gestanzt und nichts gestantzt sich am meisten unterscheiden, werden sie als Startpunkt genutzt

print_key(keys[0], 1, 25)
print()

print_key(keys[1], 2, 25)
print()

for i in range(3, N+1):
    if i%2 == 1:
        nk = next_key(keys) #Der naechste Schluessel wird mit next_key gesucht
        print_key(nk, i, min_key_difference(nk, keys))
        keys.append(nk) #und zu den vorhandenen Schluesseln hinzugefuegt
    else:
        nk = invert_key(nk) #Der naechste Schluessel ist die Inversion von nk
        print_key(nk, i, min_key_difference(nk, keys))
        keys.append(nk)
    print()    
