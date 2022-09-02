from itertools import product


letras=list("programacion")
for letters in letras:
    print (letters, end="///")
    
kiosco=["pan","fiambre", "cosa","otra"]

#kiosco[2:3]=[]
#print(kiosco[3])
for i, product in enumerate(kiosco):
    print("\n",i,product)