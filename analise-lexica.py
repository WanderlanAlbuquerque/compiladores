import re
#O código usa apenas a biblioteca re 
#(para expressões regulares), que é uma biblioteca padrão do Python 
#e não requer instalação adicional.
# Definição dos tokens e expressões regulares
tokens = [
    ('NUMBER0', r'\d+(\.\d+)?'),  # Números inteiros ou decimais
    ('MAIS', r'\+'),              # Soma
    ('MENUS', r'\-'),             # Subtração
    ('MULTIPLICACAO', r'\*'),     # Multiplicação
    ('DIVISAO', r'\/'),            # Divisão
    ('LPAREN', r'\('),            # Parêntese esquerdo
    ('RPAREN', r'\)'),            # Parêntese direito
]

# Função para tokenizar a entrada
##tokenizar a entrada é o processo de dividir uma sequência de
#caracteres em partes menores chamadas "tokens", de acordo com 
#regras específicas. Em um contexto de linguagens de programação 
#ou análise de texto, os tokens são unidades básicas de significado,
#como palavras individuais, operadores, símbolos especiais, números, 
#etc.

def tokenize(input_string):
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)
    for match in re.finditer(token_regex, input_string):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'SPACE':
            yield token_type, token_value

# Exemplo de uso
if __name__ == '__main__':
    #input_string = "3 + 4 * (10 - 2)"
    #input_string = "7 - 4 * (10 - 2)"
    #input_string = "7 - 4 * {10 - 2}"
    #input_string = "7 - 4.75 * (10.0 - 2)"
    input_string = "5 + 10"
    for token in tokenize(input_string):
        print(token)
