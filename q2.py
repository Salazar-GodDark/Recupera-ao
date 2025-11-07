notas = [8.5, 4.0, 10.0, 7.5, 6.0, 9.0]

soma_notas = 0
quantidade_aprovadas = 0

for nota in notas:
  soma_notas += nota
  if nota >= 7.0:
    quantidade_aprovadas += 1

media = soma_notas / len(notas)

print(f"A média das notas é: {media:.2f}")
print(f"Quantidade de notas iguais ou superiores a 7.0 são: {quantidade_aprovadas}")