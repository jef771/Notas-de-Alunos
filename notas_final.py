import sys
from sys import argv

script, filename = argv


def transformar_float(lista):
    float_lista = []

    if lista[0].isnumeric():
            sys.exit("ERRO: nome do aluno incorreto, cheque o template.")

    for i in lista:
        if i.isalpha() or ' ' in i:
            float_lista.append(i)
            float_lista = ''.join(float_lista)

        else:
            try:
                float_lista.append(float(i))
            except ValueError:
                sys.exit("ERRO: nota incorreta, cheque o template.")
            except AttributeError:
                sys.exit("ERRO: nota incorreta, cheque o template.")


    return float_lista


def detail(lista):
        print(f"Nome: {lista['nome']}")
        print(f"Deveres: {lista['deveres']}")
        print(f"Quizzes: {lista['quizzes']}")
        print(f"Testes: {lista['testes']}")



def media_aritmetica(lista):
    return sum(lista) / len(lista)


def get_average(lista, input):
    for i in range(len(lista)):
        if lista[i]['nome'] == input:
            media0 = media_aritmetica(lista[i]['deveres']) * 0.10
            media1 = media_aritmetica(lista[i]['quizzes']) * 0.30
            media2 = media_aritmetica(lista[i]['testes'])  * 0.60
            media_final = media0 + media1 + media2


    return media_final

def get_letter_grade(float):
    if float >= 9:
        return 'A'
    elif float >= 7:
        return 'B'
    elif float >= 5:
        return 'C'
    elif float >= 4.5:
        return 'D'
    else:
        return 'E'


def get_class_average(lista):
    media_classe = 0
    for i in range(len(lista)):
        detail(lista[i])
        print(f"Média simples: %.2f" %(get_average(lista, lista[i]['nome'])))
        print(f"Média conceito: {get_letter_grade(get_average(lista, lista[i]['nome']))}\n")
        media_classe = media_classe + get_average(lista, lista[i]['nome'])

    return print(f"Média classe: %.2f" %(media_classe / len(lista)))


# main function para transformar txt em lista com dicionários e dar print
def main():
    # abrindo o arquivo com a estrutura
    arquivo = open(filename, 'r')
    # definindo variáveis necessárias
    estudantes = []
    estudante = {}
    for linha in arquivo.readlines():
        # verifica o separador
        if linha == "#\n":
        # copiando o dicionário ou ele se sobrepoe
            estudante_copy = estudante.copy()
            estudantes.append(estudante_copy)

        else:
            (key, val) = linha.split(':')
            val = val.rstrip()
            val = val.rsplit(',')
            estudante[key] = transformar_float(val)

    get_class_average(estudantes)
    # fechando arquivo
    arquivo.close()


# print
if __name__ == '__main__':
  main()
