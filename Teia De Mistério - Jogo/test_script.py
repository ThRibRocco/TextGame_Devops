import sys
import time
import os

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

#FUNCAO PARA EXIBIR AS NARRAÇÕES
def narra(texto):
    for linha in texto:
        print(linha)
        time.sleep(1)
    print()

#FUNCAO PARA OS CREDITOS
def fim():
    creditos = [
        'TEIA DE MISTÉRIO',
        'Por - Saturn Games',
        'Obrigado por jogar!'
    ]

    largura_tela = os.get_terminal_size().columns

    for linha in creditos:
        espacos = (largura_tela - len(linha)) // 2
        linha_formatada = ' ' * espacos + linha

        print(linha_formatada)
        time.sleep(2)


# TESTES
def test_digitar_texto():
    print("Testing digitar_texto function...")
    texto = "Testando a função digitar_texto."
    digitar_texto(texto)

def test_exibir_fala():
    print("Testing exibir_fala function...")
    nome_personagem = "Personagem"
    fala = ["Primeira linha de fala.", "Segunda linha de fala."]
    cor = "31"  # Cor vermelha
    exibir_fala(nome_personagem, fala, cor)

def test_narra():
    print("Testing narra function...")
    texto = ["Primeira linha de narrativa.", "Segunda linha de narrativa."]
    narra(texto)

def test_fim():
    print("Testing fim function...")
    fim()

if __name__ == "__main__":
    test_digitar_texto()
    test_exibir_fala()
    test_narra()
    test_fim()
