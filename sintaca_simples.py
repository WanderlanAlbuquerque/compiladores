'''
No código, NLTK significa Natural Language Toolkit. 
É uma biblioteca Python amplamente utilizada para 
processamento de linguagem natural (NLP). 
Ela fornece ferramentas e recursos para trabalhar
com texto e linguagem, como tokenização, 
análise gramatical, categorização, stemização, e até mesmo treinamento de modelos de aprendizado de máquina para NLP.
No contexto do código que forneci, o NLTK é usado para:
Definir gramáticas, como as Regras Gramaticais de Contexto Livre (CFG)
Construir parsers (analisadores) que permitem realizar análises sintáticas, criando estruturas hierárquicas do texto com base em regras gramaticais.
'''
import nltk
from nltk import CFG
# Define a gramática para expressões matemáticas
gramatica = CFG.fromstring("""
    S -> E
    E -> E '+' T | E '-' T | T
    T -> T '*' F | T '/' F | F
    F -> '(' E ')' | NUM
    NUM -> '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0'
""")
# Construção do parser baseado na gramática
'''
Um parser é uma ferramenta ou componente usado para 
analisar a estrutura de um texto ou código de acordo 
com regras gramaticais ou sintáticas predefinidas.
A principal função de um parser é interpretar e 
decompor um conjunto de dados (como uma linguagem natural, 
expressão matemática ou código de programação)
em uma estrutura compreensível e utilizável, 
como uma árvore sintática.
'''
parser = nltk.ChartParser(gramatica)
# Expressão para teste
#expressao = ['3', '+', '(', '5', '*', '2', ')']
#expressao=['3','+',"5"]
expressao=['7','*','(','4','+','2',')']
# Testa a análise sintática
print("Árvores Sintáticas Geradas:")
for arvore in parser.parse(expressao):
    #print(arvore)
    arvore.draw()  # Mostra a árvore sintática (é necessário ter tkinter instalado para visualizar)