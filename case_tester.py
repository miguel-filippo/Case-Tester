import os
from argparse import ArgumentParser

"""
Feito por: Miguel Filippo Rocha Calhabeu - nº USP: 15480331
Data: 02/10/2024

Programa feito para facilitar a realização de testes de casos de teste na disciplina Introdução à Ciência da Computação II (SCC0503).
O código a seguir realiza o teste dos casos presentes na pasta './cases' de um projeto.

OBSERVAÇÕES:
1. O código a seguir deve ser colocado no diretório pai da pasta 'cases', ou seja, fora da pasta 'cases'.

2. Os casos de teste devem possuir a extensão '.in' e '.out' para os casos de entrada e saída, respectivamente.
Além disso, os arquivos de entrada e saída devem possuir o mesmo nome.

3. O código a seguir deve ser executado no terminal, com o comando 'python case_tester.py {File2Test}.c'.
"""

class CaseTester:
    def __init__(self) -> None:
        try:
            self.cases = [case for case in os.listdir('cases') if case.endswith('.in')]
        except FileNotFoundError:
            print('Não foi possível encontrar a pasta "cases" no diretório atual.')
            exit

    def comparar_arquivos(self, arq1, arq2):
        with open(arq1, 'r') as f1, open(arq2, 'r') as f2:
            return f1.read() == f2.read()
        
def main():
    # Pegando o nome do arquivo a ser testado
    parser = ArgumentParser()
    parser.add_argument('file', type=str, help='Nome do arquivo a ser testado.')
    args = parser.parse_args()
    file = args.file

    # Compilando o arquivo
    os.system(f'gcc {file} -o {file[:-2]}')

    # Instanciando a classe CaseTester
    tester = CaseTester()

    # Testando os casos
    for case in tester.cases:
        os.system(f'{file[:-2]} < cases/{case} > cases/{case[:-3]}.txt')

        if tester.comparar_arquivos(f'cases/{case[:-3]}.out', f'cases/{case[:-3]}.txt'):
            print(f'Caso {case[:-3]}: ✅')

        else:
            print(f'Caso {case[:-3]}: ❌')
            print('======== Detalhes ========')
            print(f'Entrada: {case}')
            with open(f'cases/{case}', 'r') as entrada:
                print(entrada.read())
                print()

            print(f'Saída esperada:')
            with open(f'cases/{case[:-3]}.out', 'r') as saida_esperada:
                print(saida_esperada.read())

            print(f'Saída obtida:')
            with open(f'cases/{case[:-3]}.txt', 'r') as saida_obtida:
                print(saida_obtida.read()[:-2])
            print('==========================')

        os.remove(f'cases/{case[:-3]}.txt')
        

if __name__ == '__main__':
    main()
