print('@@@@@@@  @    @  @@@@@@    @@@@@@  @@@@@@  @     @  @@@@@@\n'
      '   @     @    @  @         @       @    @  @ @ @ @  @    \n' 
      '   @     @@@@@@  @@@@@     @  @@@  @@@@@@  @  @  @  @@@@@\n'
      '   @     @    @  @         @    @  @    @  @     @  @    \n'
      '   @     @    @  @@@@@@    @@@@@@  @    @  @     @  @@@@@@')
print('AI version.Guess the number!')
input('press enter to continue...')
def gaming():
    import random
    abscis = 0
    ord = 10000
    for n in range(4000):
        pcg = random.randint(abscis, ord)
        print(f'Is the number {pcg}?')
        user = input()
        if user == 'yes':
            print(f'Yay!I knew!It was {pcg}')
            break
        if user == 'lower':
            ord = pcg - 1
        if user == 'higher':
            abscis = pcg + 1
def instruction():
    print('Game instruction:\n'
          'In this game you need to think at a number and keep it in ur mind.\n'
          'Then the pc will tell you a number.\n'
          'If the number is lower than ur number type "higher",otherwise type "lower"\n'
          'If the number is egal as yours ,type "yes".')
    mainmenu = input('Press enter to proceed to the main menu: ')
while True:
    hilp = input('For instruction type "help".To start the game type "start".To exit type "quit": ')
    if hilp == 'help':
        instruction()
    if hilp == 'start':
        gaming()
    if hilp == 'quit':
        quit()
