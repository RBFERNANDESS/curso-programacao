produto= ["arroz", "feijao", "açucar", "café", "leite"]
estoque =[10, 3, 1, 20, 5]
preco=[10.00, 5.00, 7.00, 3.00, 8.00]

for b in range (len(produto)):
    produtos = produto [b]
    estoques = estoque [b]
    precos = preco [b]
    totals = estoque [b]*preco[b]
    print(f"produto: {produtos}, estoque: {estoques}, preços {precos}, Total {totals}")
