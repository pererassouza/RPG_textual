import cohere
import random

# Chave de API do Cohere
API_KEY = "HgoyG78y95WA5yyIpWSSG5gB8DlsfVUAZlXISlQ8"


def config_choice(vida_inimigo, dano_fisico_inimigo, dano_magico_inimigo,
                  vida_jogador, dano_fisico_jogador, dano_magico_jogador,
                  resistencia_inimigo, resistencia_jogador):
    co = cohere.Client(API_KEY)

    # Lógica para variar a escolha com base nos atributos
    escolhas_possiveis = ["basic_attck", "intimidar", "power_up"]

    if vida_inimigo < vida_jogador * 0.5:  # Se a vida do inimigo está baixa
        escolha = random.choices(escolhas_possiveis, weights=[
                                 0.5, 0.3, 0.2], k=1)[0]
    elif resistencia_jogador > dano_fisico_inimigo + dano_magico_inimigo:  # Se a resistência do jogador é alta
        escolha = random.choices(escolhas_possiveis, weights=[
                                 0.3, 0.5, 0.2], k=1)[0]
    else:  # Caso contrário, escolha aleatória
        escolha = random.choice(escolhas_possiveis)

    return escolha


def s(re, vida_inimigo, dano_fisico_inimigo, dano_magico_inimigo,
      vida_jogador, dano_fisico_jogador, dano_magico_jogador,
      resistencia_inimigo, resistencia_jogador):
    escolha_inimigo = config_choice(vida_inimigo, dano_fisico_inimigo, dano_magico_inimigo,
                                    vida_jogador, dano_fisico_jogador, dano_magico_jogador,
                                    resistencia_inimigo, resistencia_jogador)
    return re, escolha_inimigo


def atacar(rees, vida_inimigo, dano_fisico_inimigo, dano_magico_inimigo,
           vida_jogador, dano_fisico_jogador, dano_magico_jogador,
           resistencia_inimigo, resistencia_jogador):
    return s(rees, vida_inimigo, dano_fisico_inimigo, dano_magico_inimigo,
             vida_jogador, dano_fisico_jogador, dano_magico_jogador,
             resistencia_inimigo, resistencia_jogador)
