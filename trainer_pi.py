import math
import keyboard
import time

# Fonction pour obtenir un caractère sans appui sur "Entrée"
def get_char():
    event = keyboard.read_event(suppress=True)
    return event.name if event.event_type == keyboard.KEY_DOWN else ''

# Obtiens le nombre de décimales à vérifier
n_decimales = 223846264385000
# Calcul des décimales de pi
decimales_pi = "14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999"
# Convertit pi en chaîne et prend n_decimales+2 caractères (3. inclus)
time.sleep(0.220)
# Demande et vérifie les décimales
for i in range(n_decimales):
    decimale_entree = ''
    while decimale_entree == '':
        decimale_entree = get_char()
    print(decimale_entree)
    if decimale_entree != decimales_pi[i]:
        print("Erreur à la décimale #{}: Tu as entré '{}', la bonne décimale est '{}'.".format(i+1, decimale_entree, decimales_pi[i]))
        break
else:
    print("Bravo, toutes les décimales sont correctes!")

def space_pi():
    for i in range(len(decimales_pi)//2):
        print(decimales_pi[2*i]+decimales_pi[2*i+1], end = " ")
        
#35028space_pi()