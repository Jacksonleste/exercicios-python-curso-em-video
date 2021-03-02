print('{} LOJÃO LESTER {}'.format(8 * '=-', 8 * '=-'))
preço = float(input('preço das compras: R$'))
pag = int(input('''FORMAS DE PAGAMENTO
[1] Á VISTA NO DINHEIRO/CHEQUE (10% de desconto.)
[2] Á VISTA NO CARTÃO (5% de desconto.)
[3] 2X NO CARTÃO (preço normal.)
[4] 3X OU MAIS NO CARTÃO (20% de juros.)
-insira o número da opção desejada: '''))
text = 'sua compra de R${:.2f} vai custar'.format(preço)
if pag == 1 or pag == 2 or pag == 3 or pag == 3 or pag == 4:
    if pag == 1:
        print('{} R${:.2f} com desconto'.format(text, preço - (preço * 10) / 100))
    elif pag == 2:
        print('{} R${:.2f} com desconto'.format(text, preço - (preço * 5) / 100))
    elif pag == 3:
        print('sua compra será parcelada em 2x de {:.2f} '.format(preço / 2))
        print('Você vai pagar {:.2f}'.format(preço))
    elif pag == 4:
        parcel = int(input('em quantas parcelas?'))
        if parcel == 1:
            print('para isso selecione a opção [2]')
        elif parcel == 2:
            print('para isso selecione a opção [3]')
        else:
            final = preço + (preço * 20) / 100
            print('sua compra será párcelada em {}x de {:.2f}'.format(parcel, final / parcel))
            print('{} R${:.2f}'.format(text, final))
else:
    print('\033[31;1mOPÇÃO INVÁLIDA, TENTE NOVAMENTE.')
