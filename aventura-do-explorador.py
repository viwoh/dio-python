#Entrada
quantidade_passos = int(input())

#Verifica se a quantidade de passos é positiva
if quantidade_passos > 0:
    #Utiliza um loop for para imprimir a mensagem do explorador indicando o número do passo
    for i in range(1, quantidade_passos + 1):
        print("Explorador:", i, "passo" if i == 1 else "passos")
else:
    print("Nenhum passo dado na floresta.")
