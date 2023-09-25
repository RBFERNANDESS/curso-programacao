
prod=["arroz","feijao","açucar","cafe","sal"]
custos=[15,5,3,4,2]
estoque=[10,8,7,6,5]
imp1=0.12
imp2=0.06
imp3=0.03
frete=50
for b in range(len(prod)):
    produto=prod[b]
    custo=custos[b]
    estoq=estoque[b]
    lucro=0.60
    custoimp1=(custo*imp1)
    custoimp2=(custo*imp2)
    custoimp3=(custo*imp3)
    frete=((50/estoq))
    precocusto=(custo+custoimp1+custoimp2+custoimp3)
    margemdelucro=(precocusto*lucro)
    precovenda=(precocusto+margemdelucro)
    precovendacomfrete=(precovenda+frete)
    print(f"produto: , {produto}, custo s/ imposto:, {custo:.2f}, custo c/ imposto: , {precocusto:.2f}, preço de venda: , {precovenda:.2f}, preço de venda com frete: , {precovendacomfrete:.2f}" )
