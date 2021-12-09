def calculo_media(lista_para_calcular):
    soma = 0
    for elem in lista_para_calcular:
        print("essa é a lista: ", lista_para_calcular)
        print("essa é a soma antes: ", soma)
        soma = soma + elem
        print("esse é o elemento: ", elem)
        print("essa é a soma depois: ", soma)
        print("essa é a len da lista: ", len(lista_para_calcular))

    media = soma/len(lista_para_calcular)
    resultado = 'essa é a media: %i' %(media)
    return resultado


print(calculo_media((8,7,9)))
