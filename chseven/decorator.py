def cough_dec(func):


    def dec_wrapper():

        print('*Cough*')

        func()

        print('*Cough*')
    return dec_wrapper



@cough_dec
def question():
    print('Can you give me a discount on that')

question()


@cough_dec
def answer():
    print('Hmm! dey play')

answer()