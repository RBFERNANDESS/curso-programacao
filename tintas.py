n1=int(input("quantos m² tem sua parede  "))
soma=int(n1/6)
print("voce precisa de ",(soma),("litros"))
if soma<18:
    soma=soma/3.6
    print("voce precisa de ",(soma),("latas de 3,6"))
if soma>=18:
    soma=soma/18
    print("voce precisa de ",(soma),("galao 18lts"))



