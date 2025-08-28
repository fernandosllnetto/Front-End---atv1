alturas = []
alturas_m = []
contador_f = 0

for i in range(15):
    altura = float(input(f"Altura da pessoa {i+1} (em metros): "))
    genero = input("Gênero (M/F): ")

    alturas.append(altura)

    if genero == 'M':
        alturas_m.append(altura)
    elif genero == 'F':
        contador_f += 1

print(f"Maior altura: {max(alturas):.2f} m")
print(f"Menor altura: {min(alturas):.2f} m")

if alturas_m:
    media_m = sum(alturas_m) / len(alturas_m)
    print(f"Média de altura dos homens: {media_m:.2f} m")
else:
    print("Nenhum homem no grupo.")

print(f"Número de mulheres: {contador_f}")
