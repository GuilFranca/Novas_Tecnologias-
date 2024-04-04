def desenhar_caixa(largura, altura):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            print('*' * largura)
        else:
            print('*' + ' ' * (largura - 2) + '*')

def desenhar_oval(largura, altura):
    centro_horizontal = largura // 2
    centro_vertical = altura // 2

    for y in range(altura):
        linha = ''
        for x in range(largura):
            if ((x - centro_horizontal) ** 2) / (centro_horizontal ** 2) + ((y - centro_vertical) ** 2) / (centro_vertical ** 2) <= 1:
                linha += '*'
            else:
                linha += ' '
        print(linha)

def desenhar_seta(tamanho):
    for i in range(tamanho):
        print(' ' * (tamanho - i - 1) + '*' * (i + 1))
    for i in range(tamanho - 2, -1, -1):
        print(' ' * (tamanho - i - 1) + '*' * (i + 1))

def desenhar_losango(largura):
    meio = largura // 2
    for i in range(meio):
        print(' ' * (meio - i) + '*' * (2 * i + 1))
    for i in range(meio, -1, -1):
        print(' ' * (meio - i) + '*' * (2 * i + 1))


print("Caixa:")
desenhar_caixa(10, 5)
print("\nOval:")
desenhar_oval(10, 5)
print("\nSeta:")
desenhar_seta(5)
print("\nLosango:")
desenhar_losango(5)
