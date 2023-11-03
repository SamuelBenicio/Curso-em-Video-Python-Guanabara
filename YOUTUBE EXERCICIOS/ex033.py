A,B,C = map(int,input('Digite tres numeros: ').split(' '))
if(A>B and A>C):
    print(f'{A}(A) é o maior numero dos tres numeros que foram digitados')
    if(B>C):
        print(f'{C}(C) é o menor numero dos tres numeros que foram digitados')
    else:
        print(f'{B}(B) é o menor numero dos tres numeros que foram digitados')
if(B>A and B>C):
    print(f'{B}(B) é o maior numero dos tres numeros que foram digitados')
    if(A>C):
        print(f'{C}(C) é o menor numero dos tres numeros que foram digitados')
    else:
        print(f'{A}(A) é o menor numero dos tres numeros que foram digitados')
if(C>A and C>B):
    print(f'{C}(C) é o maior numero dos tres numeros que foram digitados')
    if(A>B):
        print(f'{B}(B) é o menor numero dos tres numeros que foram digitados')
    else:
        print(f'{A}(A) é o menor numero dos tres numeros que foram digitados')
