import sys
import time
import os
from TeiaDeMistério_Completo.py import digitar_texto, exibir_fala, narra, fim

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