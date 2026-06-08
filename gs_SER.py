#importando bibliotecas:
import random
import time

print("Iniciando a geração de dados...")

try:
    while True:
        #Gerando dados:
        dado_temperatura = random.randint( -200,200)
        dado_comunicacao = random.randint( 0,100)
        dado_energia = random.randint( 0,100)
        opções = ("Módulos operacionais funcionando", "Erro em módulo operacional")
        dado_modulos = random.choices(opções, weights=[80,20])[0]

        #Interpretando os dados gerados:
        if dado_temperatura >= 150:
            temperatura = f"Crítica!!! Risco de superaquecimento({dado_temperatura}°C)"
        elif dado_temperatura <= -150:
            temperatura = f"Crítica!!! Risco de congelamento({dado_temperatura}°C)"
        else:
            temperatura =  f"OK ({dado_temperatura}°C)"
        if dado_comunicacao <= 20:
            comunicacao = f"instavel ({dado_comunicacao}%)"
        else:
            comunicacao = f"estável ({dado_comunicacao}%)"
        if dado_energia <= 25:
            energia = f"Pouca energia({dado_energia}%)."
        else:
            energia = f"Nível de energia OK ({dado_energia}%)"
        if dado_modulos == "Módulos operacionais funcionando":
            modulos= "Módulos funcionando perfeitamente"
        else:
            modulos = "Erro em módulos operacionais"
        print(f"Temperatura externa {temperatura} \nComunicação com a nave {comunicacao} \n{energia}\n{modulos} \n")

        time.sleep(3)

        #Soluções de problemas
        if dado_temperatura >= 150 and dado_energia > 15:
            solucao_temp = "Módulo de resfriamento da nave ativado."
            print(f"{solucao_temp}\n")
        elif dado_temperatura <= -150 and dado_energia > 15:
            solucao_temp = "Módulo de aquecimento da nave ativado."
            print(f"{solucao_temp}\n")
        elif dado_energia <= 15 and dado_temperatura >= 150:
            solucao_temp = "Sem energia para o controle de temperatura da nave, aguardando recarregamento."
            print(f"{solucao_temp}\n")
        elif dado_energia <= 15 and dado_temperatura <= -150:
            solucao_temp = "Sem energia para o controle de temperatura da nave, aguardando recarregamento."
            print(f"{solucao_temp}\n")
        else:
            pass

        if dado_energia <= 25:
            print(f"Modo economia de energia ativado. \n")
        else:
            pass

        if dado_comunicacao <= 20 and dado_modulos == "Módulos operacionais funcionando":
            print("Reestabelecendo posição da nave para ajustar sinal de comunicação.\n")
        elif dado_comunicacao <= 20 and dado_modulos == "Erro em módulo operacional":
            print("impossível reestabelecer comunicação com a nave, assistência em módulo operacional necessária.\n")
        else:
            pass

        time.sleep(30)

except KeyboardInterrupt:
    print("\nSimulação interrompida pelo usuário.")