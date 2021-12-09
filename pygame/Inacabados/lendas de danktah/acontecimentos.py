import random

def locais():
    lista_locais = ["Cidade grande","Vilarejo","Floresta","Pântano","Deserto","Ártico","Praia","Rio","Lago","Ruínas","Casa abandonada"]
    local_escolhido = random.choice(lista_locais)
    return local_escolhido

def acontecimento():
    lista_acontecimentos = ["Mudança climática","Uma ameaça surge","Você encontra uma coisa","Você descobre um boato","Algo surge para te prejudicar","Algo inesperado acontece"]
    acontecimento_escolhido = random.choice(lista_acontecimentos)
    return acontecimento_escolhido

def personagensnacena():
    lista_personagens = ["Animal","Pessoa comum","Pessoa estranha","Pessoa famosa","Máquina","Criatura sobrenatural"]
    personagem_escolhido = random.choice(lista_personagens)
    return personagem_escolhido

def Criar_Aventura():
    oqueaconteceu = ["uma invasão começa","um artefato foi roubado","pessoas desapareceram","alguém precisa de ajuda","uma doença está se espalhando","você foi ameaçado"]
    oqueaconteceu_escolhido = random.choice(oqueaconteceu)
    oquefazer = ["construir algo","encontrar algo","destruir algo","conversar com alguém","proteger um local","impedir alguém"]
    oquefazer_escolhido = random.choice(oquefazer)
    senao = ["vários sofrerão","você será o culpado","uma aliança será desfeita","um desastre ocorrerá","um inimigo ficará mais poderoso","algo será destruído"]
    senao_escolhido = random.choice(senao)
    aventura = "As coisas pareciam calmas, até que " + oqueaconteceu_escolhido + " para resolver isso, você deve " + oquefazer_escolhido + " ou então " + senao_escolhido
    
    if oqueaconteceu_escolhido == "uma invasão começa":
        responder = "invasão do que?"
    if oqueaconteceu_escolhido == "um artefato foi roubado":
        responder = "qual artefato e de onde?"
    if oqueaconteceu_escolhido == "pessoas desapareceram":
        responder = "quem desapareceu e em qual lugar no mundo?"
    if oqueaconteceu_escolhido == "alguém precisa de ajuda":
        responder = "que tipo de ajuda?"
    if oqueaconteceu_escolhido == "uma doença está se espalhando":
        responder = "que doença é essa?"
    if oqueaconteceu_escolhido == "você foi ameaçado":
        responder = "por quem? Com o que?"
    return aventura + "\n\n" + responder


print("Vamos começar nossa história. O que será que está acontecendo com você?\n")
print(Criar_Aventura())
resposta1 = input()



