'''
TEIA DE MISTÉRIO - FASE 1
'''

import time
import sys


# FUNC PRA DIGITAR TEXTO DE UM JEITO BONITINHO
def digitar_texto(texto):
    estilo_cor = "\033[1;32m"
    reset_cor = "\033[0m"

    for char in texto:
        sys.stdout.write(estilo_cor + char + reset_cor)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# FUNC PRA EXIBIR A FALA DE UM JEITO BONITINHO
def exibir_fala(nome_personagem, fala, cor):
    estilo_fala = f"\033[1;{cor}m"
    reset_cor = "\033[0m"

    print(f"{estilo_fala}{nome_personagem}:{reset_cor}")

    for linha in fala:
        for char in linha:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        time.sleep(0.5)



# ------------------------------------------------------------------------------------------------------------------------------------- #

f1_tp1 = [
    'SÃO PAULO, 04 DE FEVEREIRO DE 2000',
    'RUA DOS MAGNATAS, 389 - 23h07'
]

for linha in f1_tp1:
    digitar_texto(linha)
    time.sleep(1)


f1_loc1 = [
'Você chega na cena do crime, uma casa de alto nível.',
'Há vários policiais no local coletando evidências, um deles se aproxima de você.'
]

# LOOP PRA PRINTAR A MENSAGEM DE UM JEITO BONITINHO
for linha in f1_loc1:
    print(linha)
    time.sleep(1.5)



p_laurentino = '[POLICIAL LAURENTINO]'
pl_fala1 = [
    'Boa noite detetive Isaac. A vítima é aquele modelo famoso, Marcos Matarazzo.',
    'Ele e a esposa estavam voltando de um jantar no centro da cidade, quando chegaram em casa foram abordados por um ladrão que disparou dois tiros:', 
    'Um na testa de Marcos e outro na bochecha da esposa, Yara, que já foi levada para o hospital.',
    'O pessoal já separou umas pistas. Essa é a FICHA da vítima:'
]

exibir_fala(p_laurentino, pl_fala1, 31)

escolha = input('COMANDO: ')
while escolha != 'FICHA':
    print('dica: digite o que está em caixa alta.')
    escolha = input('COMANDO: ')

if escolha == 'FICHA':
    ficha_marcos =  """
 ____________________________________________
|                                            |
|           FICHA DA VÍTIMA:                 |
|____________________________________________|
|                                            |
| Nome: Marcos Matarazzo                     |
| Data de nascimento: 08/08/1971             |
| Estado Civil: Casado                       |
| Aparência: Homem alto, cabelos pretos      |
|            e olhos castanhos               |
| Nascido na capital de São Paulo            |
|____________________________________________|
"""
print(ficha_marcos)
time.sleep(1)

# DENTRO DA CASA
f1_loc2 = [
    'Você tem alguns cômodos para investigar:',
    'SALA, JARDIM e QUARTO da vítima.'
]

for linha in f1_loc2:
    print(linha)
    time.sleep(1.5)

escolha = input('PRA ONDE VOCÊ QUER IR?:')
print()
opcoes_validas = ['SALA', 'JARDIM', 'QUARTO']
if escolha.upper() not in opcoes_validas:
    print("Tente ir até os locais escritos em caixa alta.")

# SALA DA CASA
if escolha == 'SALA':
    f1_locSala = [
        'Ao entrar na sala você vê o corpo de Marcos, ele está usando um PALETÓ de grife. Olhando no rosto dele, você vê uma espressão de choque.',
        'Você também vê algumas marcas de sangue no CHÃO, uma ESTANTE com algumas fotos do casal e um APARADOR com algumas decorações que parecem mais caras que sua casa.'
    ]

    for linha in f1_locSala:
        print(linha)
        time.sleep(1.5)

escolha = input('ONDE VOCÊ QUER OLHAR?:')

# SE O USER DIGITAR ALGO DIFERENTE, MOSTRA UMA MENSAGEM DE ERRO
if escolha.upper() not in map(str.upper, f1_locSala):
    print("Tente escolher um dos lugares que estão em caixa alta.")
    escolha = input('ONDE VOCÊ QUER OLHAR?:')

while escolha != 'SAIR':

    # PALETÓ DO MARCOS MATARAZZO 
    if escolha == 'PALETÓ':
        print('Checando os bolsos do paletó do corpo frio de Marcos, você encontra um recibo de estacionamento:')
        time.sleep(1.5)
        recibo_marcos = """"
+-----------------------------------------------------------------------+
|                        RECIBO DE ESTACIONAMENTO                       |
|                                                                       |
|                          Estacionamento Seguro                        |
|-----------------------------------------------------------------------|
| Data de entrada:      04/02/2000       Horário de entrada:   20:10    |
| Data de saída:        04/02/2000       Horário de saída:     21:47    |
|-----------------------------------------------------------------------|
| Tempo estacionado:                   1 hora e 37 minutos              |
|                                                                       |
| Valor cobrado:                       R$ 32,00                         |
|                                                                       |
+-----------------------------------------------------------------------+
"""
        print(recibo_marcos)

    # CHÃO DA SALA
    if escolha == 'CHÃO':
        print('Em meio às marcas de sangue próximas do corpo e vários policiais analisando provas, você encontra uma cápsula de bala calibre 9mm')
        time.sleep(1)
        
    # ESTANTE DA SALA
    if escolha == 'ESTANTE':
        print('Você encontra várias revistas de moda, livros de publicidade e arte moderna. Nada que vai te ajudar agora')
        time.sleep(1)

    # APARADOR DA SALA
    if escolha == 'APARADOR':
        f1_aparador = [
            'Você abre as gavetas do aparador.',
            'Em meio à alguns panfletos e alguns documentos muito bem organizados, você encontra a certidão de casamento de Marcos e Yara'

        ]
    
        for linha in f1_aparador:
            print(linha)
            time.sleep(1.5)

        certidao_casamento1 = """
+-----------------------------------------------------------------------+
|                        CERTIDÃO DE CASAMENTO                          |
|                                                                       |
| Data do casamento:       04 de fevereiro de 1995                      |
|                                                                       |
| Esposo:                  Marcos Matarazzo                             |
| Esposa:                  Yara ██████████                              |
|                                                                       |
| Testemunhas:                                                          |
|                 Victor Matarazzo      Isabela Vieira                  |
|                                                                       |
|                                                                       |
| Assinatura do Esposo            Assinatura da Esposa                  |
|   Marcos Matarazzo                 Yara ██████████                    |
+-----------------------------------------------------------------------+
"""
        print(certidao_casamento1)
        print('A certidão parece um pouco desgastada com o tempo.')
    
    print()
    print('Você pode checar PALETÓ, CHÃO, ESTANTE e o APARADOR, ou você pode SAIR.')
    escolha = input('ONDE VOCÊ VAI OLHAR?:')

for linha in f1_loc2:
    print(linha)
    time.sleep(1.5)

escolha = input('PRA ONDE VOCÊ QUER IR?:')
print()

opcoes_validas = ['SALA', 'JARDIM', 'QUARTO']
if escolha.upper() not in opcoes_validas:
    print("Tente ir até os locais escritos em caixa alta.")

# JARDIM DA CASA
if escolha == 'JARDIM':
    f1_locJardim = [
        'Ao sair pelo jardim, você vê um espaço muito agradável para lazer.',
        'Você vê algumas flores, um balanço e um gazebo.',
        'Olhando para a casa, você percebe que uma das janelas está quebrada,',
        'os cacos estão para o lado de dentro.'
    ]

    for linha in f1_locJardim:
        print(linha)
        time.sleep(1.5)

for linha in f1_loc2:
    print(linha)
    time.sleep(1.5)

escolha = input('PRA ONDE VOCÊ QUER IR?:')
print()

opcoes_validas = ['SALA', 'JARDIM', 'QUARTO']
if escolha.upper() not in opcoes_validas:
    print("Tente ir até os locais escritos em caixa alta.")

if escolha == 'QUARTO':
    pl_fala2 = [
        'A empregada deu falta de um colar, o dinheiro que estava no cofre e uma arma 9mm que Marcos tinha por segurança.'
    ]
    
    exibir_fala(p_laurentino, pl_fala2, 31)
    f1_locQuarto = [
        'Ao entrar no quarto, você vê um ARMÁRIO bem bagunçado e uma das portas está quebrada.',
        'Você também vê uma penteadeira cheia de maquiagens e perfumes.',
        'Olhando na cabeceira da cama você vê uma foto de aparentemente Marcos e Yara sorrindo.'
    ]

    for linha in f1_locQuarto:
        print(linha)
        time.sleep(1.5)

    print('Você pode checar ARMÁRIO ou você pode SAIR.')
    escolha = input('ONDE VOCÊ QUER OLHAR?:')
    while escolha != 'SAIR':
        if escolha == 'ARMÁRIO':
            f1_armario = [
                'Você vê muitas roupas de marcas que você nem sabe pronunciar.',
                'No meio da bagunça do armário, você encontra um cofre.',
            ]
            for linha in f1_armario:
                print(linha)
                time.sleep(1.5)
            f1_cofre = [
                'Você afasta algumas roupas para alcançar o cofre.',
                'Ao olhar a fechadura, você percebe que já foi arrombada.',
                'Olhando dentro do cofre, você vê que o ladrão ainda deixou algumas jóias e certa quantidade de dinheiro.'
            ]
            for linha in f1_cofre:
                print(linha)
                time.sleep(2)

        print('Você pode checar ARMÁRIO denovo, ou você pode SAIR.')
        escolha = input('ONDE VOCÊ QUER OLHAR?:')

    opcoes_validas = ['ARMÁRIO', 'SAIR']
    if escolha.upper() not in opcoes_validas:
        print("Tente ir até os locais escritos em caixa alta.")

f1_loc3 = [
    'Você sente que já viu tudo o que podia.'
    'Você volta para a entrada da casa, o Oficial Laurentino se aproxima.'
]
for linha in f1_loc3:
    print(linha)
    time.sleep(1.5)

pl_fala3 = [
    'A viúva do senhor Marcos está internada no Hospital Esperança, aqui perto. Poderíamos fazer uma visita amanhã, ver se ela pode nos ajudar...'
]
exibir_fala(p_laurentino, pl_fala3, 31)


f1_tp2 = [
    'SÃO PAULO, 05 DE FEVEREIRO DE 2000',
    'HOSPITAL ESPERANÇA, 9h47'
]

for linha in f1_tp2:
    digitar_texto(linha)
    time.sleep(1)

f1_hospital = [
    'Você chega ao hospital com o objetivo de fazer algumas perguntas para a viúva de Marcos, Yara.', 
    'Você chega a recepção e a recepcionista logo pede para alguma enfermeira te levar até Yara.'
]

for linha in f1_hospital:
    print(linha)
    time.sleep(1.5)

enfermeira = '[ENFERMEIRA]'
enf_fala1 = [
    'A senhora Yara passou por uma cirurgia muito complicada, ela acordou faz algumas horas. Ninguém veio fazer visita. Detetive Isaac, peço para que o senhor seja delicado. O trauma dela ainda é recente.'
]

exibir_fala(enfermeira, enf_fala1, 34)

f1_hloc1 = [
    'Ao entrar no quarto de Yara, ela se ajeita na maca.',
    'Ela sorri.',
    'Ou pelo menos tenta...'
]

for linha in f1_hloc1:
    print(linha)
    time.sleep(2.5)

yara = '[YARA]'
yara_fala1 = [
    'Ah, você é o detetive que está cuidando do caso do Marcos? Por favor entre!',
    'Pode perguntar qualquer coisa, vou tentar lembra de tudo *ri*',
    'Pelo meu Marcos, eu ajudo o máximo que puder.'
]

exibir_fala(yara, yara_fala1, 35)

f1_loc4 = [
    'Você pode fazer algumas perguntas para Yara.',
    '1 - Você se lembra de como o ladrão era?',
    '2 - Você acha que o ladrão sabia que vocês estavam fora?',
    '3 - Seu marido tinha alguém que não gostasse dele?',
    'Quando terminar, você pode SAIR'
]

for linha in f1_loc4:
    print(linha)
    time.sleep(1)

pergunta = input('QUAL PERGUNTA VOCÊ QUER FAZER?:')

opcoes_validas = [1, 2, 3]
if pergunta not in opcoes_validas:
    print("Tente colocar somente o número da pergunta. Ou você pode SAIR")

while pergunta != 'SAIR':
    if pergunta == 1:
        det_isaac = '[VOCÊ]'
        det_pergunta1 = [
            'Você se lembra de alguma característica do ladrão? Cor da pele, dos olhos ou algo assim?'
            ]

        exibir_fala(det_isaac, det_pergunta1, 33)

        yara_resposta2 = [
            'Não... Foi tudo muito rápido. Ele também estava usando uma daquelas bandanas no rosto, não consigo me lembrar... Desculpe.'
            ]

        exibir_fala(yara, yara_resposta2, 35)
        pergunta = input('QUAL PERGUNTA VOCÊ QUER FAZER?:')
        opcoes_validas = [1, 2, 3]
        if pergunta not in opcoes_validas:
            print("Tente colocar somente o número da pergunta. Ou você pode SAIR")
        

    elif pergunta == 2:
        det_pergunta2 = [
            'Você acha que o ladrão, de algum jeito, saberia que você estariam fora?'
            ]

        exibir_fala(det_isaac, det_pergunta2, 33)

        yara_resposta2 = [
            'O jantar com o Marcos foi surpresa para mim. Estávamos comemorando nosso aniversário de casamento. Alguém pode ter visto em algum blog a data do nosso casamento e, provavelmente, imaginou que iríamos comemorar fora...'
            ]

        exibir_fala(yara, yara_resposta2, 35)
        pergunta = input('QUAL PERGUNTA VOCÊ QUER FAZER?:')
        opcoes_validas = [1, 2, 3]
        if pergunta not in opcoes_validas:
            print("Tente colocar somente o número da pergunta. Ou você pode SAIR")

    elif pergunta == 3:
        det_pergunta3 = [
            'Você consegue pensar em alguém que não gosta do Marcos, algum inimigo?'
            ]

        exibir_fala(det_isaac, det_pergunta3, 33)

        yara_resposta3 = [
            'Oh não! Todos adoram- adoravam o Marcos *lacrimeja*... Ele era tão gentil e tranquilo. Talvez algum outro modelo sem tanto sucesso quanto ele? Não sei...'
            ]

        exibir_fala(yara, yara_resposta3, 35)
        pergunta = input('QUAL PERGUNTA VOCÊ QUER FAZER?:')
        opcoes_validas = [1, 2, 3]
        if pergunta not in opcoes_validas:
            print("Tente colocar somente o número da pergunta. Ou você pode SAIR")                   

f1_loc5 = [
    'Depois da conversa com Yara, você ainda não tem muitas resposta.'
    'Ela tentou, mas não foi muito útil...'
]

for linha in f1_loc5:
    print(linha)
    time.sleep(1)

f1_tp3 = [
    '6 MESES DEPOIS...'
]

for linha in f1_tp3:
    digitar_texto(linha)
    time.sleep(1)

f1_loc6 = [
    'Seu superior arquiva o caso',
    'Você não tem o suficiente para achar o suspeito do assassinato de Marcos Matarazzo.'
]

for linha in f1_loc6:
    print(linha)
    time.sleep(2.5)

'''
FASE 2
'''

'''
Teia de Mistério - Fase 2
'''


f2_tp2 = [
    "FLORIANÓPOLIS, 3 DE JUNHO DE 2007",
    "RUA TEODORO DA FONSSECA, 208 - 17h48"
]

for linha in f2_tp2:
    digitar_texto(linha)
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

exibir_fala(p_polic, fala1_ofic, 94)

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
      "DIPLOMA","JANELA","ESTANTE",'ARMÁRIO','SAÍDA',"PORTA"
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
                    print("Tente escolher um dos lugares que estão em caixa alta.")
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
    digitar_texto(linha)
    time.sleep(1)
print()

for linha in f2_tp4:
    digitar_texto(linha)
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

exibir_fala(eloise, f2_elo,95)

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
