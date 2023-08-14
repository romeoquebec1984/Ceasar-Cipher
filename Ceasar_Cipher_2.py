alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
play=1
def ceasar(answer):
    index=0
    osomething=(input('Enter message: '))
    something=osomething.lower()
    somethings=[]
    for i in range(0,len(something)):
        somethings.append(something[i])
    index=int(input('enter index for cipher'))
    if index>=len(alphabet):
        index= index%len(alphabet)
    if answer==2:
        index= index * -1


    for i in range(0,len(somethings)):
        if somethings[i] in alphabet:
             for j in range(0,len(alphabet)):
                if alphabet[j]==somethings[i] and j+index<=len(alphabet)-1:
                    somethings[i]=alphabet[j+index]
                    break
                elif alphabet[j]==somethings[i] and j+index >= len(alphabet)-1:
                    somethings[i]= alphabet[j+index-26]
                    break

    print(f'\nOriginal message: {osomething}')
    print(f'\nProcessed message: {"".join(somethings)}')
while play==1:
    branch1=int(input('Would you like to Ciper(1) or Dicipher(2)'))
    ceasar(branch1)
    play=int(input('\nRun Program again? Y=1 N=2 : '))
    