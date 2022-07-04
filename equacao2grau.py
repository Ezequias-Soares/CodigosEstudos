while True:
    eq2gr = input('Escreva uma equação do segundo grau do tipo (1), (2) ou (3)\n'
                  '(1)  aX²+bX+c=0\n'
                  '(2)  aX²+bX=0\n'
                  '(3)  aX²+c=0\n\n')
    eq2gr = eq2gr.replace('x²', 'aa')
    eq2gr = eq2gr.replace('x', 'bb')
    if 'aa+' in eq2gr:
        sinal_b = float(1)
        if 'bb+' in eq2gr:
            sinal_c = float(1)
        else:
            sinal_c = float(1 * (-1))
    else:
        sinal_b = float(1 * (-1))
        if 'bb+' in eq2gr:
            sinal_c = float(1)
        else:
            sinal_c = float(1 * (-1))
    eq2gr = eq2gr.replace('-', '+')

# EQUAÇÃO DO TIPO X²+X+1=0
    if 'aa' in eq2gr\
            and 'bb' in eq2gr\
            and '=0' in eq2gr\
            and eq2gr[-3].isnumeric():

        # ELEMENTO A
        elem_a = eq2gr.split('aa+')[0]
        if elem_a == '':
            elem_a = '1'

        # ELEMENTO B
        elem_b = eq2gr.split('aa+')[1]
        elem_b = elem_b.split('bb+')[0]
        if elem_b == '':
            elem_b = '1'

        # ELEMENTO C
        elem_c = eq2gr.split('bb+')[1]
        elem_c = elem_c.split('=')[0]


# EQUAÇÃO DO TIPO X²+X=0
    elif 'aa' in eq2gr\
            and 'bb' in eq2gr\
            and '=0' in eq2gr:

        # ELEMENTO A
        elem_a = eq2gr.split('aa+')[0]
        if elem_a == '':
            elem_a = '1'

        # ELEMENTO B
        elem_b = eq2gr.split('aa+')[1]
        elem_b = elem_b.split('bb=')[0]
        if elem_b == '':
            elem_b = '1'

        # ELEMENTO C
        elem_c = eq2gr.split('bb')[1]
        elem_c = elem_c.split('=')[0]
        if elem_c == '':
            elem_c = '0'

# EQUAÇÃO DO TIPO X²+1=0
    elif 'aa' in eq2gr \
            and '=0' in eq2gr\
            and eq2gr[-3].isnumeric():

        # ELEMENTO A
        elem_a = eq2gr.split('aa+')[0]
        if elem_a == '':
            elem_a = '1'

        # ELEMENTO B
        elem_b = eq2gr.split('aa')[1]
        elem_b = elem_b.split('+')[0]
        if elem_b == '':
            elem_b = '0'

        # ELEMENTO C
        elem_c = eq2gr.split('aa+')[1]
        elem_c = elem_c.split('=')[0]
    else:
        print('Equação inválida...')
        continue

    if elem_a.isalnum() and elem_b.isalnum() and elem_c.isalnum():

        # RESOLUÇÃO BHASKARA
        elem_a = float(elem_a)
        elem_b = float(elem_b)
        elem_c = float(elem_c)
        if elem_b != 0:
            elem_b = elem_b * sinal_b
        if elem_c != 0:
            elem_c = elem_c * sinal_c

        delta = (elem_b ** 2) - (4 * elem_a * elem_c)
        if delta < 0:
            print(f'A equação não possui raízes reais.')
            break

        raiz = delta ** 0.5

        x_1 = ((elem_b * (-1)) - raiz) / (2 * elem_a)
        x_2 = ((elem_b * (-1)) + raiz) / (2 * elem_a)

        print(f'Nesta equação os elementos a, b e c contém os seguintes valores:\n'
              f'a = {elem_a}    b = {elem_b}    c = {elem_c}\n'
              f'Δ = {round(delta, 2)}\n'
              f'X1 = {round(x_1, 2)}\nX2 = {round(x_2, 2)}')
        break
    else:
        print('Equação inválida...')


