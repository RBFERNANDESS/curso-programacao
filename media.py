numero=int(input("digite numero"))
if numero %2 == 0:
    print("esse numero é par")
else:
    print("esse numero é impar")

n1=int(input("nota1 "))
n2=int(input("nota2 "))
n3=int(input("nota3 "))
n4=int(input("nota4 "))
if ((n1+n2+n3+n4)/4)>=7:
    print("PARABENS MIZERAVI")
    print("media",(n1+n2+n3+n4)/4)
if ((n1+n2+n3+n4)/4)<7:
    print("reprovado")
    print("media",(n1+n2+n3+n4)/4)
    print("ligando para seu pai...")
