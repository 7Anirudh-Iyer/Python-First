#hangman
print('1. Sports')
print('2. Food')

a = int(input('Choose: '))

if a==1:
    print('Welcome to sports section')
    print('Guess the word')
    print('________')
    x = int(input('Enter a no. from 1 to five: '))
    if x==1:
        print('Most popular sport in the world')
        print('Known by different name only in Britain')
        print('Ball based sport')
        w = input('Enter the sport name: ')

        while w!='football':
            print('Wrong')
            print('Try again')
            w = input('Enter the sport name: ')
        
        if w=='football':
            print('You are correct!')
            print('Well done!')

    elif x==2:
        print('Most popular sport in China and South Korea')
        print('Used to be played by British officials often in India')
        print('Feathers are important')
        w = input('Enter the sport name: ')

        while w!='badminton':
            print('Wrong')
            print('Try again')
            w = input('Enter the sport name: ')
        
        if w=='badminton':
            print('You are correct!')
            print('Well done!')

    elif x==3:
        print('Most popular in United States of America')
        print('Uses implement to play')
        print('Nets are used by players')
        w = input('Enter the sport name: ')

        while w!='lacrosse':
            print('Wrong')
            print('Try again')
            w = input('Enter the sport name: ')
        
        if w=='lacrosse':
            print('You are correct!')
            print('Well done!')

    elif x==4:
        print('One of the oldest sports')
        print('Original Olympian Sport')
        print('Animals are present')
        w = input('Enter the sport name: ')

        while w!='horse racing':
            print('Wrong')
            print('Try again')
            w = input('Enter the sport name: ')
        
        if w=='horse racing':
            print('You are correct!')
            print('Well done!')

    elif x==5:
        print('Turns out this sport is among top 10 least played sports!')
        print('Started in India')
        print('Primitive in many senses')
        print('Can be violent too sometimes')
        w = input('Enter the sport name: ')

        while w!='kabaddi':
            print('Wrong')
            print('Try again')
            w = input('Enter the sport name: ')
        
        if w=='kabaddi':
            print('You are correct!')
            print('Well done!')
