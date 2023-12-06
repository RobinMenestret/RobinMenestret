from math import sqrt


def decompose (n): 
    liste=[1]
    #print("%d ="%(n), end=' ') 
    i=2 
    while n>1: 
        while n%i==0: 
            liste.append(i) 
            n=n/i 
        i=i+1  
    return liste
 
 
# =============================================================================
# def main(): 
#     decompose(120) 
#  
# if __name__ == '__main__': 
#     main() 
# =============================================================================
 
# This function returns a list containing all the factors of a ginven parameters n
def getFactors(n):
    # Create an empty list for factors
    factors=[];

    # Loop over all factors
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    # Return the list of factors
    return factors

compteur=0

# =============================================================================
# for i in range(2000):
#     liste = decompose(i+2)
#     if liste[-1]+liste[-2] == 2 * len(getFactors(i+2)):
#         compteur+=1
#         print(str(compteur) + " : " + str(i+2) + " a " +str(len(getFactors(i+2))) + " facteurs premiers et sa decomposition est " + str(decompose(i+2)))       
# =============================================================================
for i in range(20000):
    liste = decompose(i+2)
    if liste[-1]-1 == len(getFactors(i+2)) and liste[-2]+1 == len(getFactors(i+2)):
        compteur+=1
        print(str(compteur) + " : " + str(i+2) + " a " +str(len(getFactors(i+2))) + " facteurs premiers et sa decomposition est " + str(decompose(i+2)))