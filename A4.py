import math
import random

def shuffled(l): #Gibt die Liste l zufaellig gemischt zurueck
    r = list(l)[:]
    random.shuffle(r) #Dies ist noetig, weil random.shuffle in-place mischt
    return r

def print_key(key): #Gibt den den Schluessel key formatiert als Schluesselkarte aus (debugging)
    for i in range(5):
        for j in range(5):
            print("x" if key[i*5+j] else ".", end="") #Gestanzte Loecher werden als "x" dargestellt, nicht-gestanzte als "."
        print()

def key_difference(key1, key2): #Gibt die Anzahl unterschiedlicher Loecher von key1 und key2 zurueck, dies wird als Mass fuer die Unterschiedlichkeit von Schluesselkarten betrachtet. Ein Rueckgabewert von 0 bedeutet, dass die Schluessel identisch sind.
    return sum([key1[i]^key2[i] for i in range(25)])

#"Mindestabstand"
def key_differences(key, other_keys):
    return min([key_difference(key, key2) for key2 in other_keys])

def next_key(keys): #Gibt einen Schluessel zurueck, der sich von den schon vorhandenen moeglichst stark unterscheidet
    #Starte mit einem Schluessel, der an jeder Stelle mit der Mehrheit, der schon vorhandenen Schluessel uebereinstimmt, der sich also zunaechst moeglichst wenig unterscheidet
    r = [sum(key[i] for key in keys) > len(keys)/2. for i in range(25)]
    first = True
    while first or (r in keys or key_differences(r, keys) < 12-(len(keys)-2)//12): #Solange r schon vorhanden ist (soll mindestens einmal ausgefuehrt werden)
        first = False
        for i in shuffled(range(25)):
            sim_key = min([(key_difference(key, r), key) for key in keys])[1] #Es wird der zu r aehnlichste vorhandene Schluessel gesucht
            r[i] = not sim_key[i] #An der Stelle i wird r auf das Gegenteil des aehnlichsten Schluessel an der Stelle i gesetzt, wenn der aehnlichste Schluessel dort gestanzt ist, ist r es nicht und umgekehrt
    return r
    
N = 25

keys = [[True]*25, [False]*25] #Da alles gestanzt und nichts gestantzt sich am meisten unterscheiden, werden sie als Startpunkt genutzt

for i in range(N):
    nk = next_key(keys) #Der naechste Schluessel wird mit next_key gesucht
    print_key(nk)
    print("Abstand zum aehnlichsten Schluessel:", key_differences(nk, keys))
    print()
    keys.append(nk) #und zu den vorhandenen Schluesseln hinzugefuegt

#Das Problem: Wie kann die Guete der Loesung ueberprueft werden?
#Wieviele Schluessel kann es maximal mit einem Mindestabstand von 12 geben? (Durch Ausprobieren: mind. 12)
#Wieviele Schluessel kann es danach maximal mit einem Mindestabstand von 11 geben? (Durch Ausprobieren: mind. 12
#Vermutung: Es gibt zu jedem Mindestabstand 11 verschiedene Schlüssel
#Ein Schluessel, der von next_key generiert wurde kann also nicht der bestmoegliche sein, wenn nicht key_differences(r, keys) >= 12-(len(keys)-2)//12 erfuellt ist
