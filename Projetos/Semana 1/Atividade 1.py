#Projeto semana 1


#Neste código é feito um calculo de escolha e probabilidade de coleta de materiais.


import random


vida = 10
arvores = 0


for hora in range(3): # 3 horas
    print(f"\nHora {hora+1}: O lenhador cortou uma árvore.")
    print("O goblin apareceu!")
    acao = input("Você escolheu que o lenhador iria correr ou lutar? ").lower()


    if acao == "correr":
        if random.random() < 0.5:
            print("O lenhador correu, mas não conseguiu levar a árvore!")
        else:
            arvores += 1
            print("O lenhador correu e conseguiu levar a arvore.")
    elif acao == "lutar":
        vida -= 2
        arvores += 1
        print("O lenhador lutou e levou 2 de dano. Vida restante:", vida)
    else:
        vida = 0
        print("Ação inválida! ele fica parado e o goblin o ataca, tirando toda a vida dele, resultando em morte imediata!!")
        print("O Lenhador morreu!")
        break


    if vida <= 0:
        print("O Lenhador morreu!")
        break


# Calculo das estacas
estacas = 0
for i in range(arvores):
    estacas += random.randint(5, 7)


print(f"\nFim do dia. Árvores coletadas: {arvores}, Vida restante: {vida}")
print(f"Você conseguiu {estacas} estacas no total.")




# Neste segundo código é retratado o de uma resistência e chance de chegada de inimigos e quantas rondas.


import random
import time
# Configurações iniciais
#Temos as variáveis para a contagem da vida e recursos que temos.
estacas_disponiveis = 2
lenhador = 4
minerador = 10
ferreiro = 10
planta = 7


print("=== A VILA ESTA SENDO ATACADA ===")
print("As barreiras estão sendo armadas. Prepare-se para os ataques!")
time.sleep(1)
RONDA = random.randint(2, 3)


for i in range(RONDA):
    print(f"\n|---- RONDA {i+1} ----|")


    goblins = random.randint(2, 5)
    print(f"{goblins} goblins estão atacando!")
    time.sleep(0.5)
    for j in range(goblins):
        print(f"\nGoblin #{j+1} está tentando atravessar!")
        time.sleep(0.5)
        if estacas_disponiveis > 0:
            chance = random.randint(1, 100)
            if chance >= 30:
                print(f"Estaca bloqueou o goblin! (porcentagem = {chance})")
            else:
                estacas_disponiveis -= 1
                print(f"A estaca destruída! Goblin conseguiu passar! (porcentagem = {chance})")
                time.sleep(1)
                escolha = input("Você quer enfrentar o goblin? (s/n): ").strip().lower()
                if escolha == "s":
                    print("Você enfrentou o goblin!")
                else:
                    time.sleep(1)
                    print("Goblin atacou os moradores!")
                    time.sleep(1)
                    queima = random.randint(1, 100)
                    if queima <= 5:
                        print("VOCÊ PERDEU UMA PLANTAÇÃO!!!!")
                        plantacoes -= 1
                    else:
                        print("1 de dano causado aos moradores da vila.")
                        lenhador -= 1
                        minerador -= 1
                        ferreiro -= 1
        else:
            print(f"Sem estacas! O goblin passou direto! (porcentagem = {chance})")
            escolha = input("Você quer enfrentar o goblin? (s/n): ").strip().lower()
            if escolha == "s":
                print("Você enfrentou o goblin!")
            else:
                time.sleep(1)
                print("Goblin atacou os moradores!")
                queima = random.randint(1, 100)
                if queima <= 5:
                    print("VOCÊ PERDEU UMA PLANTAÇÃO!")
                    plantacoes -= 1
                else:
                    lenhador - 1
                    minerador - 1
                    ferreiro - 1
                    print("1 dano causado aos moradores.")


# Fim do combate
print(f"\n=== RESULTADO FINAL ===")
time.sleep(1)
print(f"Estacas restantes: {estacas_disponiveis}")
time.sleep(1)
print(f"Vida do lenhador: {lenhador}")
time.sleep(1)
print(f"vida do minerador: {minerador}")
time.sleep(1)
print(f"vida do ferreiro: {ferreiro}")
time.sleep(1)
print(f"Plantações restantes: {planta}")
time.sleep(1)
print("========================")
