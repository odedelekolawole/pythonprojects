from random import randint

kolawole_words = [
    'Aiki', 'Buyu', 'Chinonjutsu', 'Cho sen', 'Dojo', 'Garuseli', 'Haibo', 'Jin', 'Kenshi',
    'Obake ken', 'Rakusha', 'Sanmaru', 'Tekkon', 'Yoko'
]

def kolarize(word):
    random_pos = randint(0, len(kolawole_words) -1)
    return f'{word} {kolawole_words[random_pos]}'

paragraphs = int(input('How many paragraphs of Kolawole ipsum: '))


with open('ipsum.txt') as ipsum_original:
    items = ipsum_original.read().split()


    for n in range(paragraphs):
        kolawole_text = list(map(kolarize, items))
        with open('kolawole_ipsum.txt', 'a') as ipsum_kolawole:
            ipsum_kolawole.write(' '.join(kolawole_text) + '\n\n')
