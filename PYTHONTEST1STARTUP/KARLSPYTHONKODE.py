def matematik():
    print('Hej nu skal vi lave noget matematik')
    answer2 = int(input('Vælg et tal.'))
    answer3 = int(input('Hvilket tal hvil du gange dit første tal med?'))
    print(answer2 * answer3)


#Optjen oplysninger om kundens kolonariske præferencer
def fishBuyingAnswer():
    print('Nå men... Vil du så købe noget fisk?')
    answer1 = input()
    if answer1 == 'JA!':
        print('Sådan skal det lyde', customerName + '!','Så har jeg helt sikkert noget der kan friste ^-^')
        matematik()
    elif answer1 == 'Ja!':
        print('Sådan skal det lyde', customerName + '!','Så har jeg helt sikkert noget der kan friste ^-^')
        matematik()
    elif answer1 == 'Ja':
        print('Hvor er entutiasmen', customerName, 'Prøv dog lige igen', customerName, '´_´')
        fishBuyingAnswer()
    elif answer1 == 'ja!':
        print('Har du ikke lært at bruge stort begyndelsesbogstav', customerName + '?', 'Jesus')
        fishBuyingAnswer()
    elif answer1 == 'ja':
        print('Jeg mangler at høre idt entutiasme... Også, det er lidt cringe at du ikke har lært at bruge stort begyndelsesbogstav tbh. Bruh.')
        fishBuyingAnswer()
    elif answer1 == 'NEJ!':
        print('Nå! Men så gå dog!')
        exit()
    elif answer1 == 'Nej!':
        print('Nå! Men så gå dog!')
        exit()
    elif answer1 == 'Nej':
        print('Nå! Men så gå dog!')
        exit()
    elif answer1 == 'nej!':
        print('Nå! Men så gå dog!')
        exit()
    elif answer1 == 'nej':
        print('Nå! Men så gå dog!')
        exit()
    else:
        print('Hvad er det overhovedet for et svar? Prøv dog lige igen', customerName, '´_´')
        fishBuyingAnswer()

# Optjen oplysninger om kundens navn
customerName = input('Velkommen to Jerrys Fiskebutik! Jeg er Jerry, og her kan du købe fisk. Hvad hedder du?')

# Giv kunden en falsk forståelse af tryghed ved at give et kompliment
print('Nå, ok så,', customerName,'--> Det er et fint nok navn... I guess *_*')

fishBuyingAnswer()