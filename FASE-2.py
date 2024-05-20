'''
Teia de Mistério - Fase 2
'''

import time
import sys

def digitar(texto):
    style_color = "\033[1;32m"
    reset_color = "\033[0m"
    for char in texto:
        sys.stdout.write(style_color + char + reset_color)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def fala(nome_personagem, fala, cor):
    estilo_fala = f"\033[{cor}m"
    reset_cor = "\033[0m"
    print(f"{estilo_fala}{nome_personagem}:{reset_cor}")

    for linha in fala:
        for char in linha:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        time.sleep(0.5)

def digitar_texto(texto):
    estilo_cor = "\033[1;32m"
    reset_cor = "\033[0m"

    for char in texto:
        sys.stdout.write(estilo_cor + char + reset_cor)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

f2_tp2 = [
    "FLORIANÓPOLIS, 3 DE JUNHO DE 2007",
    "RUA TEODORO DA FONSSECA, 208 - 17h48"
]

for linha in f2_tp2:
    digitar(linha)
    time.sleep(1)

f2_loc1 = [
'Você foi chamado para investigar um caso de assassinato em Florianópolis.'
]

for linha in f2_loc1:
    print(linha)
    time.sleep(1.5)
#FALA OFICIAL

p_polic = '[OFICIAL]'
fala1_ofic= ['Boa tarde detetive Isaac,espero que o senhor tenha feito uma boa viagem.',
'A vítima é o Juiz, Kauan Queiroz, foi assassinado em casa.', 
'Nada da casa foi roubado, a casa estava bem arrumada,' ,
'tirando a mancha de sangue no tapete do quarto da vítima e da esposa dele, Eloise.', 
'Os vizinhos não ouviram nada. Fique a vontade para procurar pistas e esta é a FICHA da vítima.'
]

fala(p_polic, fala1_ofic, 94)

#ficha do caso

escolha = input('COMANDO: ').upper()
while escolha != 'FICHA':
    print()
    print('dica: digite o que está em caixa alta.')
    escolha = input('COMANDO: ').upper()
if escolha == 'FICHA':
    ficha_kauan =  """
 ____________________________________________
|                                            |
|           FICHA DA VÍTIMA:                 |
|____________________________________________|
|                                            |
| Nome: Kauan Queiroz                        |
| Data de nascimento: 24/10/1968             |
| Estado Civil: Casado                       |
| Aparência: Homem de estatura média,        |
| cabelos castanhos levemente grisalhos e    |
| olhos azuis                                |               
| Nascido Carazinho, interior de Santa       |
| Catarina, se mudou para Florianópolis      |
|  em 1986.                                  |
|____________________________________________|
"""
print(ficha_kauan)
time.sleep(1)

#CÔMODOS:
f2_loc2= [
    'Você tem alguns cômodos para investigar:',
    'SALA e QUARTO da vítima.',
    'Ao terminar, você pode SAIR.']

for linha in f2_loc2:
    print(linha)
    time.sleep(1.5)

escolha = input('PRA ONDE VOCÊ QUER IR?:').upper()
print()
opcoes_validas = ['SALA','QUARTO']

while escolha.upper() not in opcoes_validas:
        print()
        print("Tente ir até os locais escritos em caixa alta.")
        escolha = input('PRA ONDE VOCÊ QUER IR?:').upper()

#certidão de casamento

certid_casa = """
+-----------------------------------------------------------------------+
|                        CERTIDÃO DE CASAMENTO                          |
|                                                                       |
| Data do casamento:       10 de fevereiro de 2002                      |
|                                                                       |
| Esposo:                  Kauan Queiroz                                |
| Esposa:                  Eloise Bittencourt                           |
|                                                                       |
| Testemunhas:                                                          |
|             Joanna Queiroz      Rozana Amadeuz                        |
|                                                                       |
|                                                                       |
| Assinatura do Esposo            Assinatura da Esposa                  |
|   Kauan Queiroz                Yara Eloise Bittencourt                |
+-----------------------------------------------------------------------+

        """

procura_sala = ['A PORTA do cômodo está aberta e você entra sem nenhum problema.',
    'Dentro do local, a primeira coisa que você nota é um DIPLOMA perfeitamente moldurado na parede, próximo de uma ESTANTE cheia de livros e objetos de decoração.',
    'Ao lado do sofá, observa-se um ARMÁRIO que pode conter algo relevante para o caso e um a JANELA com cortinas a cobrindo.',
    'Quando terminar, você pode SAÍDA do cômodo.'
    ]

fala2_ofic = [
    "A viúva ainda está muito abalada, não quis responder nenhuma das perguntas… mas aqui o número dela caso queira entrar em contato."
    ]

proc_quarto =[
            'Ao entrar, você dá de cara com a cena do crime, o CORPO da vitima repousado o tapete do local.', 
            'Sobre a mesa da ESCRIVANINHA parece ter algo, será que tem alguma pista?',
            'O ARMÁRIO ao lado da cama parece limpo, mas é sempre bom verificar para o caso ter algo.',
            "Quando terminar, você pode sair pela ENTRADA do quarto." 
    ]

coisas_s = [
      "DIPLOMA","JANELA","ESTANTE",'ARMÁRIO','SAÍDA'
]
coisas_q = [
      'CORPO','ESCRIVANINHA','ARMÁRIO','ENTRADA'
]

while escolha != "SAIR":
#ESCOLHA DOS CÔMODOS
        
        #SALA

        if escolha == "SALA": 
                
            for linha in procura_sala:
                print(linha)
                time.sleep(1.5)
            print()
            escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()
            #em caso escrever o nome de um lugar errado
            
            while escolha.upper() not in coisas_s:
                    print()
                    print("Tente escolher um dos lugares 1658 que estão em caixa alta.")
                    escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()
                
            while escolha != 'SAÍDA':
                if escolha == "DIPLOMA":
                            diplom = ["Você vê os diplomas de direito de Kauan.",
                            "Ele estava ativo como juiz desde 1999"
                            ]
                            for linha in diplom:
                                print(linha)
                                time.sleep(1.5)
                            print()
                            escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()

                elif escolha == "PORTA":
                            porta = ['Você não encontra nenhum sinal de arrombamento.']
                            for linha in porta:
                                print(linha)
                                time.sleep(1)
                            print()
                            escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()

                elif escolha == "ARMÁRIO":
                            arm = [
                            'Você procura algum tipo de rastro deixado pelo assassino, mas só encontra papéis cotidianos como contas e folhetos.'
                            ]
                            for linha in arm:
                                print(linha)
                                time.sleep(1)
                            print()
                            escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()
                        
                elif escolha == "ESTANTE":
                            estan1 = [
                            "No meio de todos os livros de leis e revistas de casos, você encontra a certidão de casamento da vítima."]
                            for linha in estan1:
                                print(linha)
                                time.sleep(1)
                            print(certid_casa)

                            estan2 = ["Ele se casou com Eloise Bittencourt no dia 10/02/2002."]
                            for linha in estan2:
                                print(linha)
                                time.sleep(1.5)
                            print()
                            escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()

                elif escolha == "JANELA":
                        jan = ["Você tenta ver se existe algum rastro que mostre que alguém tenha entrado por alguma janela, mas não encontra nada."]
                        for linha in jan:
                                print(linha)
                                time.sleep(1)
                        print()
                        escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()

                        # SE O USER DIGITAR ALGO DIFERENTE, MOSTRA UMA MENSAGEM DE ERROs
                elif escolha.upper() not in coisas_s:
                        print()
                        print("Tente escolher um dos lugares que estão em caixa alta.")
                        escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()
        #DEPOIS QUE SAI DA SALA

        elif escolha == "SAÍDA":
            for linha in f2_loc2:
                print(linha)
                time.sleep(1.5)
            escolha = input('PRA ONDE VOCÊ QUER IR?:').upper()            

        #QUARTO

        elif escolha == "QUARTO":
            
            for linha in proc_quarto:
                print(linha)
                time.sleep(1.5)

            escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()
            
            #caso escreva o nome de um lugar do cômodo errado:

            while escolha.upper() not in coisas_q:
                    print()
                    print("Tente escolher um dos lugares que estão em caixa alta.")
                    escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()

            while escolha != 'SAIR DO CÔMODO':
                if escolha == "CORPO":
                        corp = ["Você entra no quarto e vê o corpo da vítima sentado em sua escrivaninha, com um buraco de tiro na parte de trás de sua cabeça.",
                        "Ele não sabia que iria ser morto…"]
                        for linha in corp:
                                print(linha)
                                time.sleep(1)
                        print()
                        escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()
                    
                elif escolha == "ESCRIVANINHA":
                        esc = ["Os documentos que Kauan lia antes de ser assassinado estão todos manchados de sangue o pouco que você vê te faz concluir que é sobre um caso de roubo que ele estava trabalhando."]
                        for linha in esc:
                            print(linha)
                            time.sleep(1)
                        print()
                        escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()
                        
                elif escolha == "ARMÁRIO":
                        arm = ["Você encontra várias roupas sociais masculinas pretas com contraste da parte feminina que é sofisticada e com vários tons de cores."]
                        for linha in arm:
                            print(linha)
                            time.sleep(1)
                        print()
                        escolha = input('ONDE VOCÊ QUER OLHAR?:').upper()
                        
                elif escolha == "ENTRADA":
                        ent = ["Após não conseguir muito investigando as pistas, você se encontra com o oficial de novo."]
                        for linha in ent:
                            print(linha)
                            time.sleep(1)
                        print()
                        #fala(p_polic, fala2_ofic, 94)
                        escolha = 'SAIR DO CÔMODO'
        
                elif escolha.upper() not in coisas_q:
                        print("Tente escolher um dos lugares que estão em caixa alta.")
                        escolha = input('ONDE VOCÊ QUER OLHAR?:')
        #depois que saiu do quarto

        elif escolha == "SAIR DO CÔMODO":
            for linha in f2_loc2:
                print(linha)
                time.sleep(1.5)
            escolha = input('PRA ONDE VOCÊ QUER IR?:').upper()
        
        #caso escrva o nome do cômodo errado
        elif escolha.upper() not in opcoes_validas:
            print()
            print("Tente ir até os locais escritos em caixa alta.")
            escolha = input('PRA ONDE VOCÊ QUER IR?:').upper()

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()

#DIAS DEPOIS - CENA DA CAFETERIA

f2_tp3 = [
    '2 DIAS DEPOIS...'
]

f2_tp4 = [
    "CAFETERIA, 5 DE JUNHO DE 2007",
    "RUA TEODORO DA FONSSECA, 208 - 17h48"
]

print()

for linha in f2_tp3:
    digitar(linha)
    time.sleep(1)
print()

for linha in f2_tp4:
    digitar(linha)
    time.sleep(1)

print()


f2_loc3 = [
'Após não conseguir muitas informações investigando a cena do crime,você decide se encontrar com a única pessoa que poderia lhe ajudar,',
'a esposa de Kauan, Eloise Queiroz.',
'Você se senta e vê uma mulher jovem e bonita, com uma cicatriz na bochecha.'
]

for linha in f2_loc3:
    print(linha)
    time.sleep(1.5)
print()

eloise = '[ELOISE]'
f2_elo = [
    ' Detetive Isaac? Sou a viúva do Kauan Queiroz, é você o responsável do caso, certo? Estou pronta para responder qualquer pergunta que tiver.'
]

fala(eloise, f2_elo,95)

#PERGUNTAS

f2_loc4 = [
    'Você pode fazer algumas perguntas para Yara.',
    '1 - Onde você estava quando tudo aconteceu?',
    '2 - Você reparou algo estranho na sua casa?',
    '3 - Seu marido tinha algum inimigo, ou teve alguma briga recentemente?',
    '4 - Desculpe a indelicadeza, mas como conseguiu essa cicatriz?',
    'Quando terminar, você pode fazer a pergunta 0',
]

for linha in f2_loc4:
    print(linha)
    time.sleep(1.5)

f2_loc5 = [
     1,2,3,4,0
]

pergunta = int(input('QUAL PERGUNTA VOCÊ QUER FAZER?'))

#CONVERSA

while pergunta != 0:
    if pergunta == 1:
        print()
        print(" Naquela noite, eu tinha saído para ir ao mercado.", 
        "Quando cheguei em casa encontrei o Kauan no chão do nosso quarto, mas já era tarde demais….")
        pergunta = int(input('QUAL PERGUNTA VOCÊ QUER FAZER?'))

    elif pergunta == 2:
        print()
        print("Não, não. Tudo parecia normal até eu entrar no quarto.")
        pergunta = int(input('QUAL PERGUNTA VOCÊ QUER FAZER?'))

    elif pergunta == 3:
        print()
        print("Não consigo nem imaginar quem poderia fazer uma coisa dessas com meu marido.")
        pergunta = int(input('QUAL PERGUNTA VOCÊ QUER FAZER?'))
    
    elif pergunta == 4:
        print()
        print("Ah… Tive um ex namorado muito abusivo no passado, ele me deu um soco no rosto.",
        "Quando eu o denunciei, ele foi preso. Foi nesse julgamento que eu conheci o Kauan…")
        pergunta = int(input('QUAL PERGUNTA VOCÊ QUER FAZER?'))

    elif pergunta not in f2_loc5:
         print()
         print("Digite o que estiver na caixa acima")
         pergunta = int(input('QUAL PERGUNTA VOCÊ QUER FAZER?'))

#FIM DA SEGUNDA FASE

f2_tp4 = [
    "Após a conversa, Eloise se levanta e se despede com um beijo no rosto.", 
    "Você finaliza o interrogatório sem muitas respostas e com o sentimento de que aquela cicatriz te lembrava um caso antigo não resolvido."
]

for linha in f2_tp4:
    print(linha)
    time.sleep(1)
