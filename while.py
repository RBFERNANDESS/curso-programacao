n1=int(input("digite numero inicial "))
n2=int(input("digite numero para parar "))
contador = n1
while contador <= n2:
    contador +=1
    if contador %2== 0:
        print(contador,("esse numero é par"))
    else:
        print(contador,("esse numero é impar"))

n1=int(input("digite numero inicial "))
n2=int(input("digite numero para parar "))
contador = n1
for b in range (n1,n2,1):
   
    if b %2 ==0: 
        print(b,"esse nuemro é par",)
    else:
        print(b,"esse numero é impar")