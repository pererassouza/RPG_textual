import cohere


def config_scene():
    print("Making Scene...\n")
    co = cohere.Client("HgoyG78y95WA5yyIpWSSG5gB8DlsfVUAZlXISlQ8")
    historia = (
        "No mundo de Dungeons and Dragons, \
    os aventureiros se encontram em um deserto "
        "onde o clima está ensolarado. Eles \
    encontram uma facção de bandidos que os informa sobre "
        "uma missão urgente: resgatar um prisioneiro. Durante a missão, eles são \
    auxiliados por um personagem "
        "chamado Aragorn, que é bravo e tem o papel de líder."
    )
    response = co.chat(
        message="Você é um mestre de jogos de Dungeons and Dragons. \
    Ajude a melhorar a história."
    )

    re = co.chat(
        message=historia,
        chat_history=response.chat_history
    )

    r = co.chat(
        message="Agora preciso que crie descrevendo APENAS um cenario, \
    sem colcar entidades, porém quero que gere \
    apenas a apresentação da história, e toda vez que eu falar 'mais uma' quero \
    que voce me manda mais uma apresentação",
        chat_history=re.chat_history
    )


    more_one = co.chat(
        message='mais',
        chat_history=r.chat_history
    )
    historia = more_one.text
    return historia
