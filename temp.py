# Lista com os nomes dos meses
nomes_meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

# Lista para armazenar as temperaturas máximas
temperaturas_maximas = [None] * 12  # Inicializa com None para garantir que todos os meses sejam preenchidos

print("📥 Informe os dados meteorológicos de 2021 (temperatura máxima por mês):")

# Coleta e validação dos dados
meses_preenchidos = set()
while len(meses_preenchidos) < 12:
    try:
        mes = int(input("Digite o número do mês (1 a 12): "))
        if mes < 1 or mes > 12:
            print("Mês inválido. Digite um número entre 1 e 12.")
            continue
        if mes in meses_preenchidos:
            print("Este mês já foi preenchido. Escolha outro.")
            continue

        temp = float(input(f"Digite a temperatura máxima de {nomes_meses[mes - 1]} (entre -60°C e 50°C): "))
        if temp < -60 or temp > 50:
            print("Temperatura fora do intervalo permitido. Tente novamente.")
            continue

        temperaturas_maximas[mes - 1] = temp
        meses_preenchidos.add(mes)

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")

# Cálculo da média anual
media_anual = sum(temperaturas_maximas) / 12

# Contagem de meses escaldantes (> 33°C)
meses_escaldantes = sum(1 for temp in temperaturas_maximas if temp > 33)

# Identificação do mês mais escaldante e menos quente
indice_max = temperaturas_maximas.index(max(temperaturas_maximas))
indice_min = temperaturas_maximas.index(min(temperaturas_maximas))

# Exibição dos resultados
print("\nRESULTADOS:")
print(f"• Temperatura média máxima anual: {media_anual:.2f}°C")
print(f"• Quantidade de meses escaldantes (>33°C): {meses_escaldantes}")
print(f"• Mês mais escaldante do ano: {nomes_meses[indice_max].capitalize()} ({temperaturas_maximas[indice_max]}°C)")
print(f"• Mês menos quente do ano: {nomes_meses[indice_min].capitalize()} ({temperaturas_maximas[indice_min]}°C)")