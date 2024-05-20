'''
TEIA DE MISTÉRIO - FASE 1
'''

import time
import sys

def digitar_texto(texto):
    estilo_cor = "\033[1;32m"
    reset_cor = "\033[0m"

    for char in texto:
        sys.stdout.write(estilo_cor + char + reset_cor)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

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


def digitar_texto(texto):
    estilo_cor = "\033[1;32m"
    reset_cor = "\033[0m"

    for char in texto:
        sys.stdout.write(estilo_cor + char + reset_cor)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

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
    'Ah, você é o detetive que está cuidado do caso do Marcos? Por favor entre!',
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

pergunta = int(input('QUAL PERGUNTA VOCÊ QUER FAZER?:'))

opcoes_validas = [1, 2, 3]
if pergunta.upper() not in opcoes_validas:
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

    if pergunta == 2:
        det_pergunta2 = [
            'Você acha que o ladrão, de algum jeito, saberia que você estariam fora?'
            ]

        exibir_fala(det_isaac, det_pergunta2, 33)

        yara_resposta2 = [
            'O jantar com o Marcos foi surpresa para mim. Estávamos comemorando nosso aniversário de casamento. Alguém pode ter visto em algum blog a data do nosso casamento e, provavelmente, imaginou que iríamos comemorar fora...'
            ]

        exibir_fala(yara, yara_resposta2, 35)

    if pergunta == 3:
        det_pergunta3 = [
            'Você consegue pensar em alguém que não gosta do Marcos, algum inimigo?'
            ]

        exibir_fala(det_isaac, det_pergunta3, 33)

        yara_resposta3 = [
            'Oh não! Todos adoram- adoravam o Marcos *lacrimeja*... Ele era tão gentil e tranquilo. Talvez algum outro modelo sem tanto sucesso quanto ele? Não sei...'
            ]

        exibir_fala(yara, yara_resposta3, 35)

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