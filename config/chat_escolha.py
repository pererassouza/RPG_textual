import cohere


def config_choice(elife, epp, epm, clife, cpp, cpm, roe, roc):
    co = cohere.Client("HgoyG78y95WA5yyIpWSSG5gB8DlsfVUAZlXISlQ8")
    response = co.chat(
        message="voce esta em um jogo de RPG, preciso que decida entre usar\
alguns ataques, vou falar a sua situação, \n\
ex: your_life: 40hp, power_of_your_physical_atack: 10atck, \
power_of_your_magical_atack: 20atck,  life_of_enemy: 80hp, \
power_of_enemy_physical_atack: 25atck, power_of_enemy_magical_atack: 15atck\
toda vez que eu te passar a situação atual quero que decida em realizar as\
seguntes ações tomando a melhor decisão: \n\
basic_attck: esta ação faz voce deferir um ataque ao inimigo com o dano atual \
intimidar: faz a resistencia a ataques do inimigo cair \
power_up: faz o poder dos seus atributos, como ataque magico e fisico aumentar\
Quero que guarde essas informações e espere eu passar os proximos status,\
quando eu passar quero que me responda apenas falando o que vai utilizar\
 ex: power_up"
    )
    r = co.chat(
        message='ótimo, vou mandar mais um aqui, lembre sempre de fazer a \
melhor escolha de acordo a sua situação atual',
        chat_history=response.chat_history
    )

    re = co.chat(
        message=f'Atributos iniciais: \n\
your_life: {elife}hp, power_of_your_physical_atack:\
{epp}atck \
power_of_your_magical_atack: {epm}atck, life_of_enemy: {clife}hp, \
power_of_enemy_physical_atack: {cpp}atck, power_of_enemy_magical_atack: \
{cpm}atck, your_resistence: {roe}, enemy_resistence: {roc}.',
        chat_history=r.chat_history)
    return re


def s(re, elife, epp, epm, clife, cpp, cpm, roe, roc):
    co = cohere.Client("HgoyG78y95WA5yyIpWSSG5gB8DlsfVUAZlXISlQ8")
    rees = co.chat(
        message=f'Atributos Atuais, o que voce vai fazer? ex: power_up\
intimidar ou basic_attack:\
your_life: {elife}hp, power_of_your_physical_atack:\
{epp}atck power_of_your_magical_atack: {epm}atck, \
life_of_enemy: {clife}hp, power_of_enemy_physical_atack: \
{cpp}atck, power_of_enemy_magical_atack: {cpm}atck, \
your_resistence: {roe}, enemy_resistence: {roc}\
Mande apenas a ação escolhida com a primeira letra minúscula, \
sem textos a mais, lembre de não usar apenas um ataque',
        chat_history=re.chat_history
    )
    return rees, rees.text


def atacar(rees, elife, epp, epm, clife, cpp, cpm, roe, roc):
    co = cohere.Client("HgoyG78y95WA5yyIpWSSG5gB8DlsfVUAZlXISlQ8")
    ree = co.chat(
        message=f'Atributos Atuais, o que voce vai fazer? ex: power_up\
intimidar ou basic_attack:\
your_life: {elife}hp, power_of_your_physical_atack:\
{epp}atck power_of_your_magical_atack: {epm}atck, \
life_of_enemy: {clife}hp, power_of_enemy_physical_atack: \
{cpp}atck, power_of_enemy_magical_atack: {cpm}atck, \
your_resistence: {roe}, enemy_resistence: {roc}\
Mande apenas a ação escolhida com a primeira letra minúscula, \
sem textos a mais, lembre de não usar apenas um ataque',
        chat_history=rees.chat_history
    )
    print(f'\nESCOLHA DO CHAT: {ree.text}\n')
    return ree.text
