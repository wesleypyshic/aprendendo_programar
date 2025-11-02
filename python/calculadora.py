def calculadora(n1,n2):

    while True:

        n1 = float(input('n1 = '))
        n2 = float(input('n2 = '))

        operacao = input('Operação (Ou digite "Sair"):')

        if operacao == '+':
            resul = n1 + n2
            print('Resultado:', resul)
        elif operacao == '-':
            resul = n1 - n2
            print('Resultado:', resul)
        elif operacao == '*' :
            resul = n1 * n2 
            print('Resultado:', resul)
        elif operacao == '/' :
            if n2 == 0 :
                print("Erro.")
            else:
                resul = n1 / n2
                print('Resultado:', resul)
        elif operacao.lower() == 'sair':
            print('Adeus.')
            break
        else:
            print('Erro.')
        return resul
    
    print(resul)