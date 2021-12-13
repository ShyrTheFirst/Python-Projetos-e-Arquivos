def dividir_linhas(frase):
    frase_split = frase.split()
    frase_junta = []
    palavra_junta = ''
    palavra_junta2 = ''
    for palavra in range(0,len(frase_split)):
        if palavra == 0:
            frase_junta.append(frase_split[palavra])
        if palavra == 1:
            frase_junta.append(frase_split[palavra])
        if palavra == 2:
            palavra_junta += frase_split[palavra]
        if palavra == 3:
            palavra_junta += ' ' + frase_split[palavra]
            frase_junta.append(palavra_junta)
        if palavra == 4:
            palavra_junta2 += frase_split[palavra]
        if palavra == 5:
            palavra_junta2 += ' ' + frase_split[palavra]
            frase_junta.append(palavra_junta2)

        if palavra == 3 and palavra < 4:
            frase_junta.append(frase_split[palavra])
        if palavra == 4 and palavra < 5:
            frase_junta.append(frase_split[palavra+1])

    frase_final = frase_junta
    return frase_final


frase = 'Espada entalhada do ceus celestial +10'
print("frase 01: ", dividir_linhas(frase))

frase02 = 'Espada +10'
frase03 = 'Espada entalhada +10'
frase04 = 'Espada entalhada do ceus +10'

print("frase 02: ", dividir_linhas(frase02))
print("frase 03: ", dividir_linhas(frase03))
print("frase 04: ", dividir_linhas(frase04))
