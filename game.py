import random
from rich.console import Console

f = open("file.txt")
text = f.read().replace("\n",",")
sample=text.split(',')   # list of all 5 letter words
f.close()

console = Console()
console.print("WELCOME TO WORDLE\n",style="bold underline purple")
console.print("INSTRUCTIONS for playing the game:\n",style='bold green')
console.print("1. You have to guess the Wordle in six goes.\n2. Every word you enter must be in the word list.\n3. A correct letter turns green.\n4. A correct letter in the wrong place turns yellow.\n5. An incorrect letter turns gray.\n6. Letters can be used more than once",style= "blue") 


def check(original,word):  #storing word with color
    l=[]
    if len(word)==5:
        for i in range(5):
            if original[i]==word[i]:
                l+=f'[black on green]{word[i]}[/]'
            elif word[i] in original:
                l+=f'[black on yellow]{word[i]}[/]'
            else:
                l+=f'[black on grey]{word[i]}[/]'
        return ''.join(l)
        #y=''.join(l)
        #console.print(y)
         
    else:
        console.print("The length of the word must be equal to 5",style='red')
console.print('\nLets start the game',style='bold yellow')
x=1
word=''
played=0
won=0
while(x):
    num=random.randint(0,len(sample)-1)   # generating a random number to select a 5 letter word from 
    original=sample[num]
    
    guessedwords=[]
    output=[]
    while(len(guessedwords)!=6 ):
       
            console.print('\nEnter your guess word:',end='')
            word=input()
            if word in sample:
                if word in guessedwords:
                    console.print('You have already entered this word as a guess',style='bold red')
                else:

                    guessedwords.append(word)
                    guessed=check(original,word)
             
                    output.append(guessed)
                    console.print('\nYour guesses uptil now: \n')
                    for i in output:
                        console.print(i,end='\n')
                    if word==original:
                        break
            else:
                console.print('You have not entered a correct word',style='bold red')
    played=played+1            
    if word==original:
        console.print('You have successfully guessed the word',style='bold green')
        won=won+1
    else:
        console.print('\nThe original word was',end=' ')
        console.print(original,style='bold blue')
        #console.print(guessed)
        #print(guessed)

    console.print("\n\n Game statistics")
    console.print(" No of games played: ",end='')
    console.print(played,style='purple')
    console.print(" No of games won: ",end='')
    console.print(won,style='purple')
    console.print("\n\n Game statistics")
    console.print("\nTo continue the game press 1 ",end='',style='bold yellow')
    console.print("\nTo exit the game press 0 ",end='',style='bold yellow')
    x=int(input())


