import random
#for randint()

name = input('Enter Your Name: ')

question = input('"Yes" or "No" question you\'d like to ask the Magic 8-Ball: ')

answer = ''

random_number = random.randint(1, 9)

print(random_number)

end_it = 1
while(end_it!=0):
    if random_number == 1:
        answer = 'Yes - definitely'
    elif random_number == 2:
        answer = 'It is decidedly so'
    elif random_number == 3:
        answer = 'Without a doubt'
    elif random_number == 4:
        answer = 'Reply hazy, try again'
    elif random_number == 5:
        answer = 'Ask again later'
    elif random_number == 6:
        answer = 'Better not tell you now'
    elif random_number == 7:
        answer = 'My sources say no'
    elif random_number == 8:
        answer = 'outlook not so good'
    elif random_number == 9:
        answer = 'Very doubtful'
    else:
        answer = 'Error'

    if name == '':
        print('asks:', question)
        print('Magic 8 Ball\'s answer: Outlook not so good')
    elif question == '':
        print('You dont have any questions!')
    else:
        print(name, 'asks:', question)
        print('Magic 8-Ball\'s answer :', answer)

    end_it = int(input('Press 0 to end!'))