import math
import keyboard
import time
import random
from matplotlib import pyplot as plt

# Fonction pour obtenir un caractère sans appui sur "Entrée"
def get_char():
    event = keyboard.read_event(suppress=True)
    return event.name if event.event_type == keyboard.KEY_DOWN else ''

# Obtiens le nombre de décimales à vérifier
n_decimales = 1000
# Calcul des décimales de pi
decimales_pi = ("1415926535897932384626433832795028841"
               "97169399375105820974944592307816406286"
               "20899862803482534211706798214808651328"
               "23066470938446095505822317253594081284"
               "81117450284102701938521105559644622948"
               "95493038196442881097566593344612847564"
               "82337867831652712019091456485669234603"
               "48610454326648213393607260249141273724"
               "58700660631558817488152092096282925409"
               "17153643678925903600113305305488204665"
               "21384146951941511609433057270365759591"
               "95309218611738193261179310511854807446"
               "23799627495673518857527248912279381830"
               "11949129833673362440656643086021394946"
               "39522473719070217986094370277053921717"
               "62931767523846748184676694051320005681"
               "27145263560827785771342757789609173637"
               "17872146844090122495343014654958537105"
               "07922796892589235420199561121290219608"
               "64034418159813629774771309960518707211"
               "34999999")
# Convertit pi en chaîne et prend n_decimales+2 caractères (3. inclus)

def derivate_plot(x, y):
    z = [0]
    t = []
    u = []
    for i in range(len(y)-1):
        z.append(y[i+1]-y[i])
    for i in range(len(x)//2):
        t.append(x[2*i])
        u.append(z[2*i])
    plt.figure(dpi = 200)
    plt.plot(t, u)
    plt.xlabel('numéro de la décimale')
    plt.ylabel('temps de réaction (s)')
    plt.title('temps de reflexion selon la décimale de pi')
    plt.show()

def derivate_plot_2(x, y):
    z = [0]
    for i in range(len(y)-1):
        z.append(y[i+1]-y[i])
    plt.figure(dpi = 200)
    plt.plot(x, z)
    plt.xlabel('numéro de la décimale')
    plt.ylabel('temps de réaction (s)')
    plt.title('temps de reflexion selon la décimale de pi')
    plt.show()
    
def trainer(beg = 0, end = 100, plotting = True):
    errors = 0
    x = [beg]
    temps = [0.0]
    if beg != 0 :
        print("qui a-t-il après {}{}{}{}".format(decimales_pi[beg-4], decimales_pi[beg-3], decimales_pi[beg-2], decimales_pi[beg-1]))
    t0 = time.time()
    tmp = t0
    # Demande et vérifie les décimales
    for i in range(end):    
        decimale_entree = ''
        while decimale_entree == '':
            decimale_entree = get_char()
        tf = time.time()

        if i == 0 :
            t0 = tf
            tmp = int(1000*(tf-t0))/1000
        print(decimale_entree, end = "")
        temps.append(tmp)
        x.append(i+beg)
        if decimale_entree != decimales_pi[i+beg]:
            print("\n\n Erreur à la décimale #{}: Tu as entré '{}', la bonne décimale est '{}'.".format(beg+i+1, decimale_entree, decimales_pi[i+beg]))
            
            print("\nVous avez récité {} décimales en {} secondes soit environ {} décimales par secondes !".format(i, tmp, int(10*i/tmp)/10))
            if plotting :
                derivate_plot(x, temps)
            errors +=1
        else :
            tmp = int(1000*(tf-t0))/1000
            
    else:
        print("\nBravo, vous avez fini ! ({} erreurs)".format(errors))
        if plotting :
            derivate_plot(x, temps)

def space_pi():
    for i in range(len(decimales_pi)//2):
        print(decimales_pi[2*i]+decimales_pi[2*i+1], end = " ")
        
# comment zone : 
    
def decimales_suivantes(beg = 0, end = 400, size = 4, parity = True):
    if parity :
        ft_value = 2*random.randint(beg, end//2)
    else :
        ft_value = random.randint(beg, end)
    error = False
    for i in range(size) : 
        print(decimales_pi[ft_value + i], end = "")
    suite = input(" : ")
    for number in range(len(suite)):
        good_number = decimales_pi[ft_value + size + number]
        if suite[number] != good_number:
            print("Et non à la place de {} c'était {}.".format(suite[number],good_number))
            error = True
            
    if not error :
        print("bravo c'était ça !")
        return True
    else :
        return False
    
        
#space_pi()
def dec_par(n = 500):
    while True:
        if not decimales_suivantes(end = n, parity = True):
            break

trainer(end = 500)
#dec_par(500)

#https://github.com/RobinMenestret/RobinMenestret.git