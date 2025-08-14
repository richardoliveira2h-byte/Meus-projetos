# Meus-projetos


#Neste código é feito um cálculo de probabilidade de uma coleta imaginária de minerio de ferro
1 


import random


import time




golpes_por_pedra = 6


tempo_trabalho = 60 #minutos


golpes_por_minuto = 12 # quantos golpes o minerio dá por minuto


pedra_por_hora = (tempo_trabalho * golpes_por_minuto) // golpes_por_pedra






sem_minerio = 0.30 # 30% só pedra


chance_ferro = 0.40 # 40% do que não é só pedra vira ferro


pedra = 0


ferro_coletado = 0


minerio_inutil = 0




necessario = 50 # 30 taxa + 20 extras




print("Minerando.............")


for i in range(pedra_por_hora):


    time.sleep(0.2)


    if random.random() > sem_minerio:


        if random.random() < chance_ferro:


            ferro_coletado += 1


            print(i+1,"Minerou ferro ")


        else:


            minerio_inutil+=1


            print(i+1,"Minerou minério inútil ")


    else:


        pedra+=1


        print(i+1,"Minerou pedra ")


   




print (f"\nPedra: {pedra}")


print (f"Ferro: {ferro_coletado}")


print (f"Minério inútil: {minerio_inutil}")


if ferro_coletado >= necessario:


    print ("Coletou ferro suficiente :)")


else:


    print("Não conseguiu ferro suficiente")
