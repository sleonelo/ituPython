"""Dadas 2 listas A y B de igual número de elementos, se desea generar e
imprimir una lista C conteniendo las sumas: A[i] + B[i] = C[i]. También 
indicar (solo imprimir por pantalla) aquellos elementos que están en A y no están en B."""

a = [1,3,5,7,9]
b = [1,4,6,8,10]
c = []
d=[]
for i in range(len(a)):
  c.append(a[i])


for i in range(len(b)):
  c[i] = c[i]+b[i]

for i in range(len(a)):
  if b[i] in a:
    d.append(b[i])
print(f"los elementos que se repiten son: {d}" )   
  
print(f"la suma es: {c}")