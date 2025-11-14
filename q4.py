estoque = [
{"nome": "Teclado", "preco": 150.00, "quantidade": 5},
{"nome": "Mouse", "preco": 80.00, "quantidade": 12},
{"nome": "Monitor", "preco": 700.00, "quantidade": 3},
{"nome": "Headset", "preco": 250.00, "quantidade": 8}
]
for estoque in estoque :
    if estoque ["quantidade"] < 10:
        print ( estoque ["nome"])