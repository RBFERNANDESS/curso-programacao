print("bem vindo ao Consultorio, Dr. Anderson Rogeres")


n1=int(input("digite seu peso "))
n2=float(input("digite sua altura "))
resultado= (n1/(n2*2))
print("imc=", (resultado))
if (resultado >= 18 and resultado <= 30):
    print(" você está acima do peso")
    print(" fecha a boca gordinho")
    print(" vai correr gordinho")