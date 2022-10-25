import argparse
from modules.colors import Colors

print("\n" * 130)
print('''
        
        .---.
        |[X]|
 _.==._.""""".___n__
d __ ___.-''-. _____b
|[__]  /."""".\ _   |
|     // /""\ \\\_)  |
|     \\\ \__/ //    |
|luci  \`.__.'/     |
\=======`-..-'======/
 `-----------------'   
''')
print('Hi, What you wanna learn today?')

def answerOne():
    print('''
        %s[1]%s Planos
        %s[2]%s Montagem
        %s[00]%s Sair
        %s
        ''' % (Colors.blue,
            Colors.gray,
            Colors.blue,
            Colors.gray,
            Colors.red,
            Colors.gray,
            Colors.reset))   
        
def answerTwoPlanos():
    print('''
    %s[1]%s Plano Aberto Extermo / Extreme Long Shot (ELS ou EWS)
    %s[2]%s Plano Aberto / Long Shot (LS ou WS)
    %s[3]%s Plano Comprido / Full Shot (FS)
    %s[4]%s Plano Médio / Medium Shot (MS)
    %s[5]%s Plano Americano / American Shot (AS)
    %s[6]%s Close-up Médio / Medium Close-up (MCU)
    %s[7]%s Plano Close / Close-up (CU)
    %s[8]%s Choker (CK)
    %s[9]%s Close-up Extremo / Extreme Close-UP (ECU)
    %s[0]%s Voltar
    %s[00]%s Sair
    %s
    ''' % (Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.red,
           Colors.gray,
           Colors.red,
           Colors.gray,
           Colors.reset))

def answerTwoPlanosAngulacao():
    print('''
    %s[1]%s Nivel dos olhos / Eye-Level (EL)
    %s[2]%s Angulo Alto / Hight Angle / Plongê (HA)
    %s[3]%s Angulo Baixo / Low Angle / Contre-Plongle (LA)
    %s[4]%s Plano Médio / Medium Shot (LA)
    %s[5]%s Por tras dos ombros / Over the Shouders (OTS)
    %s[6]%s Angulo Holandes / Duthc Angle (DA)
    %s[7]%s Pino / Top Shot (TS - BE)
    %s[8]%s Ponto de Vista / Subjetivo / Point of View(POV)
    %s[0]%s Voltar
    %s[00]%s Sair
    %s
    ''' % (Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.red,
           Colors.gray,
           Colors.red,
           Colors.gray,
           Colors.reset))

answerOne()
whatLearn = input('''%s[0] Put the relative number here:  %s''' % (Colors.white, Colors.reset)) 

# planos
if (whatLearn == '1'):
    print('''
    %s[1]%s Planos
    %s[2]%s Planos X Angulação
    %s[0]%s Voltar
    %s[00]%s Sair
    %s
    ''' % (Colors.blue,
           Colors.gray,
           Colors.blue,
           Colors.gray,
           Colors.red,
           Colors.gray,
           Colors.red,
           Colors.gray,
           Colors.reset))
    
    whatLearnPlanos = input('''%s[1] Put the relative number here:  %s''' % (Colors.white, Colors.reset)) 
# montagem 
if (whatLearn == '2'):
    print('montagem')
    exit()
# sair
if (whatLearn == '00'):
    exit() 
               
                        
              
if (whatLearnPlanos == '1'):
    answerTwoPlanos()              
if (whatLearnPlanos == '2'):
    answerTwoPlanosAngulacao()              
if (whatLearnPlanos == '0'):
    answerOne()
    whatLearn = input('''%s[0] Put the relative number here:  %s''' % (Colors.white, Colors.reset))
    # planos
    if (whatLearn == '1'):
        print('''
        %s[1]%s Planos
        %s[2]%s Planos X Angulação
        %s[0]%s Voltar
        %s[00]%s Sair
        %s
        ''' % (Colors.blue,
            Colors.gray,
            Colors.blue,
            Colors.gray,
            Colors.red,
            Colors.gray,
            Colors.red,
            Colors.gray,
            Colors.reset))
        
        whatLearnPlanos = input('''%s[1] Put the relative number here:  %s''' % (Colors.white, Colors.reset)) 
    # montagem 
    if (whatLearn == '2'):
        print('montagem')
        exit()
    # sair
    if (whatLearn == '00'):
        exit() 
    
                        
# def answerTwoPlanosAngulacao(): 


# parser = argparse.ArgumentParser()


# parser.add_argument('-p',
#                     '--planos',
#                     const=True,
#                     nargs='?')

# parser.add_argument('-m',
#                     '--montagem',
#                     const=True,
#                     nargs='?')


# args = parser.parse_args()

# if(args.planos):
#     planos()
# if(args.montagem):
#     montagem()


# I MUST USE WHILE