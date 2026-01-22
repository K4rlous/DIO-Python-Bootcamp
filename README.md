# Guia Python - DIO Bootcamp

## Tipos de Dados em Python

### Texto

-   **str** (String) - Textos e caracteres

```python
"Hello, World!"
'Python'
"""Texto multilinha"""
```

### Numéricos

-   **int** - Números inteiros: `42`, `-17`, `0`
-   **float** - Números decimais: `3.14`, `-0.001`, `2.0`
-   **complex** - Números complexos: `3+4j`, `2.5-1.5j`

### Sequências

-   **list** - Coleção ordenada e mutável: `[1, 2, 3]`, `["a", "b", "c"]`
-   **tuple** - Coleção ordenada e imutável: `(1, 2, 3)`, `("x", "y", "z")`
-   **range** - Sequência de números: `range(0, 10)`, `range(5)`

### Mapeamento

-   **dict** - Estrutura chave-valor: `{"nome": "João", "idade": 25}`

### Coleções

-   **set** - Elementos únicos (mutável): `{1, 2, 3}`, `{"a", "b", "c"}`
-   **frozenset** - Set imutável: `frozenset([1, 2, 3])`

### Booleano

-   **bool** - Valores lógicos: `True`, `False`

### Binários

-   **bytes** - Sequência imutável de bytes: `b"Hello"`, `bytes([65, 66, 67])`
-   **bytearray** - Sequência mutável de bytes: `bytearray(b"Hello")`
-   **memoryview** - Visualização de memória: `memoryview(bytes(5))`

---

## Comentários

```python
# Comentário de uma linha

'''
Comentário de
múltiplas linhas
'''

"""
Também funciona com
aspas duplas triplas
"""
```

---

## Interpretador Python no Terminal

Iniciar o interpretador:

```bash
$ python
>>> print("Olá, Mundo!")
Olá, Mundo!
```

Executar script e manter interpretador aberto:

```bash
$ python -i app.py
```

**Sair do interpretador:**

-   `exit()` ou `quit()`
-   `Ctrl+D` (Linux/Mac) ou `Ctrl+Z` + Enter (Windows)

### Funções Úteis

**dir()** - Lista atributos e métodos disponíveis

```python
dir()           # Nomes no escopo atual
dir(100)        # Métodos de inteiros
dir("texto")    # Métodos de strings
```

**help()** - Sistema de ajuda integrado

```python
help()          # Modo interativo
help(print)     # Ajuda sobre a função print
help(str)       # Ajuda sobre strings
```

---

## Variáveis e Constantes

### Variáveis

```python
idade = 24
nome = 'Carlos'
print(f'Meu nome é {nome} e eu tenho {idade} anos.')

# Declaração múltipla
idade2, nome2 = (30, 'Ana')
print(f'Meu nome é {nome2} e eu tenho {idade2} anos.')
```

Python define o tipo automaticamente. Não é possível criar variável sem valor inicial.

### Constantes

Por convenção, constantes são escritas em MAIÚSCULAS:

```python
PI = 3.14159
raio = 5
area = PI * (raio ** 2)
print(f'A área do círculo com raio {raio} é {area}.')
```

### Boas Práticas

-   Use **snake_case** para variáveis: `minha_variavel`
-   Use **SNAKE_CASE** para constantes: `MINHA_CONSTANTE`
-   Escolha nomes descritivos

### Atenção na Divisão

```python
print(5 / 2)   # 2.5 (divisão normal)
print(5 // 2)  # 2 (divisão inteira, ignora decimais)
```

---

## Conversão de Tipos

### Inteiro para Float

```python
preco = 10
print(preco)          # 10

preco = float(preco)
print(preco)          # 10.0

preco = 10 / 2
print(preco)          # 5.0
```

### Numérico para String

```python
preco = 19.90
print(str(preco))     # '19.9'

idade = 30
print(str(idade))     # '30'

texto = f"Idade: {idade} Preço: {preco}"
print(texto)          # 'Idade: 30 Preço: 19.9'
```

### String para Numérico

```python
preco = "19.90"
print(float(preco))   # 19.9

idade = "30"
print(int(idade))     # 30
```

---

## Entrada e Saída de Dados

### Lendo valores com input()

```python
nome = input("Por favor, insira seu nome: ")
print("Olá, " + nome + "!")

idade = input("Por favor, insira sua idade: ")
print("Você tem " + idade + " anos.")
```

**Importante:** `input()` sempre retorna string. Para usar como número, converta:

```python
idade = int(input("Digite sua idade: "))
preco = float(input("Digite o preço: "))
```

### Manipulação do print()

```python
nome = 'Carlos'
sobrenome = 'Rocha'

print(nome, sobrenome)                    # Carlos Rocha
print(nome, sobrenome, end="...\n")      # Carlos Rocha...
print(nome, sobrenome, sep="#")          # Carlos#Rocha
```

**Parâmetros:**

-   `sep` - Separador entre valores (padrão: espaço)
-   `end` - Final da linha (padrão: `\n`)

---

## Operadores

### Operadores Aritméticos

```python
soma = 5 + 3
subtracao = 10 - 4
multiplicacao = 6 * 7
divisao = 20 / 5
modulo = 10 % 3                # Resto da divisão
exponenciacao = 2 ** 3         # Potência
divisao_inteira = 15 // 4      # Divisão sem decimais
```

### Operadores de Comparação

```python
igual = (5 == 5)
diferente = (5 != 3)
maior_que = (10 > 5)
menor_que = (3 < 7)
maior_ou_igual = (8 >= 8)
menor_ou_igual = (4 <= 6)
```

### Operadores de Atribuição

```python
x = 10
x += 5  # x = x + 5
x -= 3  # x = x - 3
x *= 2  # x = x * 2
x /= 4  # x = x / 4
x %= 3  # x = x % 3
```

### Operadores Lógicos

```python
e = (True and False)
ou = (True or False)
nao = not True              # Negação
```

### Operadores de Identidade

```python
a = [1, 2, 3]
b = a
identico = (a is b)
nao_identico = (a is not [1, 2, 3])
```

### Operadores de Associação

```python
frutas = ['maçã', 'banana', 'laranja']
tem_maca = ('maçã' in frutas)
nao_tem_uva = ('uva' not in frutas)
```

### Precedência dos Operadores

1. Parênteses
2. Expoentes
3. Multiplicações e Divisões (esquerda para direita)
4. Somas e Subtrações (esquerda para direita)

---

## Estruturas Condicionais

### if / elif / else

```python
idade = 18

if idade >= 18:
    print("Maior de idade")
elif idade >= 16:
    print("Pode votar")
else:
    print("Menor de idade")
```

### if Ternário

```python
MAIOR_IDADE = 18
idade = 20

mensagem = "Maior de idade" if idade >= MAIOR_IDADE else "Menor de idade"
print(mensagem)
```

---

## Estruturas de Repetição

### for

```python
# Iterando sobre uma lista
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)

# Usando range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Range com início e fim
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# Range com passo
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### while

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# While com condição
senha = ""
while senha != "1234":
    senha = input("Digite a senha: ")
```

---

## Identação e Blocos

Python usa identação (espaços ou tabs) para definir blocos de código. Não usa chaves como outras linguagens.

```python
# Correto
if True:
    print("Identado corretamente")
    print("Mesmo bloco")

# Errado - vai dar erro
if True:
print("Sem identação")
```

**Importante:** Use 4 espaços por nível de identação (padrão PEP 8).

---

## Manipulação de Strings em Python

### Métodos de Transformação

#### Mudança de Caso

```python
curso = "pYtHon"

print(curso.upper())    # PYTHON
print(curso.lower())    # python
print(curso.title())    # Python
```

#### Eliminando Espaços em Branco

```python
curso = "  Python "

print(curso.strip())    # "Python" (remove dos dois lados)
print(curso.lstrip())   # "Python " (remove da esquerda)
print(curso.rstrip())   # "  Python" (remove da direita)
```

#### Junções e Centralização

```python
curso = "Python"

print(curso.center(10, "#"))    # ##Python##
print(".".join(curso))          # P.y.t.h.o.n
```

### Interpolação de Variáveis

Python oferece 3 formas de interpolar variáveis em strings. A primeira (com %) não é mais recomendada em Python 3.

#### Método Antigo (não recomendado)

```python
nome = "Carlos"
idade = 25
print("Me chamo %s e tenho %d anos de idade" % (nome, idade))
```

#### Método format

```python
nome = "Carlos"
idade = 25
print("Me chamo {} e tenho {} anos de idade".format(nome, idade))
```

#### Método f-strings (recomendado)

```python
nome = "Carlos"
idade = 25
print(f"Me chamo {nome} e tenho {idade} anos de idade")
```

### Formatação de Strings com f-string

```python
PI = 3.14159

# 2 casas decimais
print(f"Valor de PI: {PI:.2f}")         # Valor de PI: 3.14

# 10 caracteres de largura com 2 casas decimais
print(f"Valor de PI: {PI:10.2f}")       # Valor de PI:       3.14

# Formatando números
preco = 1500.50
print(f"Preço: R$ {preco:.2f}")         # Preço: R$ 1500.50
```

### Fatiamento de String (Slicing)

O fatiamento usa a sintaxe `[start:stop:step]` para retornar partes da string.

```python
texto = "Python Programming"

# Primeiros 6 caracteres
print(texto[0:6])       # Python
print(texto[:6])        # Python (mesmo resultado)

# Do índice 7 até o final
print(texto[7:])        # Programming

# Últimos 5 caracteres
print(texto[-5:])       # mming

# Pulando de 2 em 2
print(texto[::2])       # Pto rgamn

# Invertendo a string
print(texto[::-1])      # gnimmargorP nohtyP

# Do índice 7 até o 14
print(texto[7:14])      # Program
```

### Strings Multilinha

Preserva a estrutura e recuos da string:

```python
mensagem = """
Olá, bem-vindo ao curso de Python!
    Este é um exemplo de string multilinha.
    Ela preserva os recuos e quebras de linha.
"""
print(mensagem)

# Outra forma com aspas simples
texto = '''
Linha 1
    Linha 2 indentada
        Linha 3 mais indentada
'''
print(texto)
```

---

## Trabalhando com Listas em Python

### Introdução

Listas são estruturas de dados mutáveis e ordenadas que podem armazenar qualquer tipo de objeto em Python.

### Criação e Acesso aos Dados

```python
# Criando listas
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
mista = [1, "texto", 3.14, True]
vazia = []

# Acessando elementos (índice começa em 0)
print(frutas[0])        # maçã
print(frutas[1])        # banana
print(frutas[-1])       # laranja (último elemento)
print(frutas[-2])       # banana (penúltimo)

# Modificando elementos
frutas[0] = "morango"
print(frutas)           # ['morango', 'banana', 'laranja']
```

### Iterando sobre Listas

```python
frutas = ["maçã", "banana", "laranja"]

# Forma simples
for fruta in frutas:
    print(fruta)

# Com índice usando enumerate
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# Resultado:
# 0: maçã
# 1: banana
# 2: laranja
```

### Compreensão de Listas (List Comprehension)

Forma concisa de criar listas baseadas em sequências existentes:

```python
# Criar lista de quadrados
quadrados = [x**2 for x in range(10)]
print(quadrados)        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Com condição
pares = [x for x in range(20) if x % 2 == 0]
print(pares)            # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transformando strings
nomes = ["carlos", "ana", "joão"]
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos) # ['CARLOS', 'ANA', 'JOÃO']
```

### Métodos da Classe list

#### append() - Adiciona elemento no final

```python
frutas = ["maçã", "banana"]
frutas.append("laranja")
print(frutas)           # ['maçã', 'banana', 'laranja']
```

#### insert() - Adiciona elemento em posição específica

```python
frutas = ["maçã", "banana"]
frutas.insert(1, "morango")
print(frutas)           # ['maçã', 'morango', 'banana']
```

#### remove() - Remove primeira ocorrência do elemento

```python
frutas = ["maçã", "banana", "laranja"]
frutas.remove("banana")
print(frutas)           # ['maçã', 'laranja']
```

#### pop() - Remove e retorna elemento (último ou do índice especificado)

```python
frutas = ["maçã", "banana", "laranja"]
ultima = frutas.pop()
print(ultima)           # laranja
print(frutas)           # ['maçã', 'banana']

primeira = frutas.pop(0)
print(primeira)         # maçã
print(frutas)           # ['banana']
```

#### clear() - Remove todos os elementos

```python
frutas = ["maçã", "banana", "laranja"]
frutas.clear()
print(frutas)           # []
```

#### index() - Retorna índice da primeira ocorrência

```python
frutas = ["maçã", "banana", "laranja"]
indice = frutas.index("banana")
print(indice)           # 1
```

#### count() - Conta ocorrências de um elemento

```python
numeros = [1, 2, 3, 2, 4, 2, 5]
quantidade = numeros.count(2)
print(quantidade)       # 3
```

#### sort() - Ordena a lista (modifica original)

```python
numeros = [3, 1, 4, 1, 5, 9, 2]
numeros.sort()
print(numeros)          # [1, 1, 2, 3, 4, 5, 9]

# Ordem decrescente
numeros.sort(reverse=True)
print(numeros)          # [9, 5, 4, 3, 2, 1, 1]
```

#### sorted() - Retorna nova lista ordenada (não modifica original)

```python
numeros = [3, 1, 4, 1, 5, 9, 2]
ordenados = sorted(numeros)
print(ordenados)        # [1, 1, 2, 3, 4, 5, 9]
print(numeros)          # [3, 1, 4, 1, 5, 9, 2] (original inalterado)
```

#### reverse() - Inverte a ordem dos elementos

```python
frutas = ["maçã", "banana", "laranja"]
frutas.reverse()
print(frutas)           # ['laranja', 'banana', 'maçã']
```

#### copy() - Cria uma cópia superficial da lista

```python
original = [1, 2, 3]
copia = original.copy()
copia.append(4)
print(original)         # [1, 2, 3]
print(copia)            # [1, 2, 3, 4]
```

#### len() - Retorna o tamanho da lista

```python
frutas = ["maçã", "banana", "laranja"]
tamanho = len(frutas)
print(tamanho)          # 3
```

#### extend() - Adiciona elementos de outra lista

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)           # [1, 2, 3, 4, 5, 6]
```

### Fatiamento de Listas (Slicing)

Funciona igual ao fatiamento de strings:

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:5])     # [2, 3, 4]
print(numeros[:5])      # [0, 1, 2, 3, 4]
print(numeros[5:])      # [5, 6, 7, 8, 9]
print(numeros[::2])     # [0, 2, 4, 6, 8] (de 2 em 2)
print(numeros[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (invertido)
```

---

## Conhecendo Tuplas em Python

### Introdução

Tuplas são estruturas de dados **imutáveis** e ordenadas. Após criadas, não podem ser modificadas (não é possível adicionar, remover ou alterar elementos). São úteis para dados que não devem mudar durante a execução do programa.

### Criação de Tuplas

```python
# Tupla com vários elementos
frutas = ("maçã", "banana", "laranja")

# Tupla com um único elemento (vírgula obrigatória!)
tupla_um = (42,)        # Correto
nao_tupla = (42)        # Errado - isso é apenas um int em parênteses

# Sem parênteses também funciona
numeros = 1, 2, 3, 4, 5
print(type(numeros))    # <class 'tuple'>

# Tupla vazia
vazia = ()

# Tupla mista
mista = (1, "texto", 3.14, True)
```

**Importante:** A vírgula no final é necessária para tuplas de um único elemento, senão o Python interpreta apenas como um valor entre parênteses.

### Acessando Elementos

```python
frutas = ("maçã", "banana", "laranja", "uva")

print(frutas[0])        # maçã
print(frutas[-1])       # uva (último elemento)
print(frutas[1:3])      # ('banana', 'laranja') (fatiamento)
```

### Iteração

```python
frutas = ("maçã", "banana", "laranja")

for fruta in frutas:
    print(fruta)

# Com enumerate
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
```

### Métodos de Tuplas

#### count() - Conta ocorrências de um elemento

```python
numeros = (1, 2, 3, 2, 4, 2, 5)
quantidade = numeros.count(2)
print(quantidade)       # 3
```

#### index() - Retorna índice da primeira ocorrência

```python
frutas = ("maçã", "banana", "laranja")
indice = frutas.index("banana")
print(indice)           # 1
```

#### len() - Retorna tamanho da tupla

```python
frutas = ("maçã", "banana", "laranja")
tamanho = len(frutas)
print(tamanho)          # 3
```

### Desempacotamento de Tuplas

```python
# Desempacotamento simples
coordenadas = (10, 20)
x, y = coordenadas
print(x, y)             # 10 20

# Ignorando valores com _
dados = (1, 2, 3, 4, 5)
primeiro, _, _, _, ultimo = dados
print(primeiro, ultimo) # 1 5

# Usando * para capturar múltiplos valores
numeros = (1, 2, 3, 4, 5, 6)
primeiro, *meio, ultimo = numeros
print(primeiro)         # 1
print(meio)             # [2, 3, 4, 5]
print(ultimo)           # 6
```

---

## Explorando Conjuntos em Python

### Introdução

Sets (conjuntos) são estruturas de dados que armazenam coleções de elementos **únicos** e **não ordenados**. São úteis para eliminar duplicatas e realizar operações matemáticas de conjuntos (união, interseção, diferença).

**Características:**

-   Não permite elementos duplicados
-   Não mantém ordem de inserção
-   Não suporta indexação ou fatiamento
-   Elementos devem ser imutáveis (não pode ter listas ou dicionários dentro)

### Criação de Sets

```python
# Criando um set
numeros = {1, 2, 3, 4, 5}
frutas = {"maçã", "banana", "laranja"}

# Set vazio (usar set(), não {})
vazio = set()           # Correto
nao_vazio = {}          # Errado - isso cria um dicionário

# Criando set a partir de lista (remove duplicatas)
lista = [1, 2, 2, 3, 3, 3, 4, 5]
conjunto = set(lista)
print(conjunto)         # {1, 2, 3, 4, 5}
```

### Conversão de Set para Lista

Para acessar elementos por índice, converta para lista:

```python
frutas = {"maçã", "banana", "laranja"}

# Converter para lista
lista_frutas = list(frutas)
print(lista_frutas[0])  # Acessa primeiro elemento

# Ou usar sorted para ordenar e converter
ordenado = sorted(frutas)
print(ordenado)         # Lista ordenada alfabeticamente
```

### Iteração

```python
frutas = {"maçã", "banana", "laranja"}

for fruta in frutas:
    print(fruta)

# Usando enumerate
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
```

### Operações de Conjuntos

#### union() - União de conjuntos

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
uniao = set1.union(set2)
# Ou: uniao = set1 | set2
print(uniao)            # {1, 2, 3, 4, 5}
```

#### intersection() - Interseção (elementos em comum)

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersecao = set1.intersection(set2)
# Ou: intersecao = set1 & set2
print(intersecao)       # {3, 4}
```

#### difference() - Diferença (elementos só no primeiro)

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diferenca = set1.difference(set2)
# Ou: diferenca = set1 - set2
print(diferenca)        # {1, 2}
```

#### symmetric_difference() - Diferença simétrica

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
simetrica = set1.symmetric_difference(set2)
# Ou: simetrica = set1 ^ set2
print(simetrica)        # {1, 2, 5, 6} (elementos que estão em apenas um)
```

#### issubset() - Verifica se é subconjunto

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
resultado = set1.issubset(set2)
print(resultado)        # True (todos elementos de set1 estão em set2)
```

#### issuperset() - Verifica se é superconjunto

```python
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
resultado = set1.issuperset(set2)
print(resultado)        # True (set1 contém todos elementos de set2)
```

#### isdisjoint() - Verifica se são disjuntos

```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
resultado = set1.isdisjoint(set2)
print(resultado)        # True (não têm elementos em comum)
```

### Métodos de Modificação

#### add() - Adiciona um elemento

```python
frutas = {"maçã", "banana"}
frutas.add("laranja")
print(frutas)           # {'maçã', 'banana', 'laranja'}
```

#### discard() - Remove elemento (não dá erro se não existir)

```python
frutas = {"maçã", "banana", "laranja"}
frutas.discard("banana")
print(frutas)           # {'maçã', 'laranja'}

frutas.discard("uva")   # Não dá erro
```

#### remove() - Remove elemento (dá erro se não existir)

```python
frutas = {"maçã", "banana", "laranja"}
frutas.remove("banana")
print(frutas)           # {'maçã', 'laranja'}

# frutas.remove("uva")  # Daria KeyError
```

#### pop() - Remove e retorna elemento aleatório

```python
frutas = {"maçã", "banana", "laranja"}
elemento = frutas.pop()
print(elemento)         # Elemento removido (aleatório)
print(frutas)           # Set sem o elemento removido
```

#### clear() - Remove todos os elementos

```python
frutas = {"maçã", "banana", "laranja"}
frutas.clear()
print(frutas)           # set()
```

### Funções Úteis

#### len() - Retorna tamanho do set

```python
frutas = {"maçã", "banana", "laranja"}
tamanho = len(frutas)
print(tamanho)          # 3
```

#### in - Verifica se elemento existe

```python
frutas = {"maçã", "banana", "laranja"}
print("maçã" in frutas)     # True
print("uva" in frutas)      # False
```

---

## Utilizando Dicionários em Python

### Introdução

Dicionários são estruturas de dados que armazenam pares **chave-valor**. São mutáveis, não ordenados (antes do Python 3.7) e mantêm ordem de inserção (a partir do Python 3.7+).

**Importante:** As chaves devem ser imutáveis (strings, números, tuplas), mas os valores podem ser de qualquer tipo, inclusive mutáveis.

### Criação de Dicionários

```python
# Dicionário simples
pessoa = {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}

# Dicionário vazio
vazio = {}
# Ou
vazio = dict()

# Usando dict() construtor
pessoa2 = dict(nome="Ana", idade=30, cidade="Rio")

# Valores podem ser de qualquer tipo
dados = {
    "nome": "João",
    "idade": 35,
    "casado": True,
    "filhos": ["Maria", "Pedro"],
    "endereco": {"rua": "Rua A", "numero": 123}
}
```

### Modos de Acessar os Dados

```python
pessoa = {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}

# Acesso direto (dá erro se chave não existir)
print(pessoa["nome"])       # Carlos

# Usando get() (retorna None se chave não existir)
print(pessoa.get("nome"))   # Carlos
print(pessoa.get("telefone"))   # None

# get() com valor padrão
print(pessoa.get("telefone", "Não informado"))  # Não informado

# Modificando valores
pessoa["idade"] = 26
print(pessoa)               # {'nome': 'Carlos', 'idade': 26, 'cidade': 'São Paulo'}

# Adicionando novos pares chave-valor
pessoa["profissao"] = "Programador"
```

### Aninhamento de Dicionários

Dicionários podem conter outros dicionários, permitindo estruturas complexas:

```python
# Dicionário aninhado
empresa = {
    "funcionario1": {
        "nome": "Carlos",
        "idade": 25,
        "cargo": "Desenvolvedor"
    },
    "funcionario2": {
        "nome": "Ana",
        "idade": 30,
        "cargo": "Designer"
    }
}

# Acessando dados aninhados
print(empresa["funcionario1"]["nome"])          # Carlos
print(empresa["funcionario2"]["cargo"])         # Designer

# Modificando dados aninhados
empresa["funcionario1"]["idade"] = 26

# Múltiplos níveis de aninhamento
dados = {
    "pessoa": {
        "nome": "João",
        "contatos": {
            "email": "joao@email.com",
            "telefones": {
                "residencial": "1111-1111",
                "celular": "99999-9999"
            }
        }
    }
}

# Acessando
print(dados["pessoa"]["contatos"]["telefones"]["celular"])  # 99999-9999
```

### Iteração de Dicionários

```python
pessoa = {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}

# Iterando sobre as chaves
for chave in pessoa:
    print(chave)
# nome
# idade
# cidade

# Iterando sobre as chaves (explícito)
for chave in pessoa.keys():
    print(chave)

# Iterando sobre os valores
for valor in pessoa.values():
    print(valor)
# Carlos
# 25
# São Paulo

# Iterando sobre chave e valor
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
# nome: Carlos
# idade: 25
# cidade: São Paulo
```

### Métodos de Dicionários

#### copy() - Cria cópia superficial

```python
original = {"a": 1, "b": 2}
copia = original.copy()
copia["c"] = 3
print(original)         # {'a': 1, 'b': 2}
print(copia)            # {'a': 1, 'b': 2, 'c': 3}
```

#### fromkeys() - Cria dicionário com chaves e valor padrão

```python
chaves = ["nome", "idade", "cidade"]
dicionario = dict.fromkeys(chaves)
print(dicionario)       # {'nome': None, 'idade': None, 'cidade': None}

# Com valor padrão
dicionario2 = dict.fromkeys(chaves, "Não informado")
print(dicionario2)      # {'nome': 'Não informado', 'idade': 'Não informado', 'cidade': 'Não informado'}
```

#### get() - Retorna valor da chave (ou padrão se não existir)

```python
pessoa = {"nome": "Carlos", "idade": 25}
print(pessoa.get("nome"))           # Carlos
print(pessoa.get("cidade"))         # None
print(pessoa.get("cidade", "SP"))   # SP
```

#### pop() - Remove e retorna valor da chave

```python
pessoa = {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}
idade = pessoa.pop("idade")
print(idade)            # 25
print(pessoa)           # {'nome': 'Carlos', 'cidade': 'São Paulo'}

# Com valor padrão se chave não existir
valor = pessoa.pop("telefone", "Não encontrado")
print(valor)            # Não encontrado
```

#### popitem() - Remove e retorna último par inserido

```python
pessoa = {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}
item = pessoa.popitem()
print(item)             # ('cidade', 'São Paulo')
print(pessoa)           # {'nome': 'Carlos', 'idade': 25}
```

#### clear() - Remove todos os itens

```python
pessoa = {"nome": "Carlos", "idade": 25}
pessoa.clear()
print(pessoa)           # {}
```

#### items() - Retorna pares chave-valor

```python
pessoa = {"nome": "Carlos", "idade": 25}
itens = pessoa.items()
print(itens)            # dict_items([('nome', 'Carlos'), ('idade', 25)])

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

#### keys() - Retorna todas as chaves

```python
pessoa = {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}
chaves = pessoa.keys()
print(chaves)           # dict_keys(['nome', 'idade', 'cidade'])
print(list(chaves))     # ['nome', 'idade', 'cidade']
```

#### values() - Retorna todos os valores

```python
pessoa = {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}
valores = pessoa.values()
print(valores)          # dict_values(['Carlos', 25, 'São Paulo'])
print(list(valores))    # ['Carlos', 25, 'São Paulo']
```

#### setdefault() - Retorna valor ou define se não existir

```python
pessoa = {"nome": "Carlos"}
idade = pessoa.setdefault("idade", 25)
print(idade)            # 25
print(pessoa)           # {'nome': 'Carlos', 'idade': 25}

# Se já existir, apenas retorna
nome = pessoa.setdefault("nome", "João")
print(nome)             # Carlos (mantém o valor original)
```

#### update() - Atualiza dicionário com outro

```python
pessoa = {"nome": "Carlos", "idade": 25}
novos_dados = {"idade": 26, "cidade": "São Paulo"}
pessoa.update(novos_dados)
print(pessoa)           # {'nome': 'Carlos', 'idade': 26, 'cidade': 'São Paulo'}

# Também aceita argumentos nomeados
pessoa.update(profissao="Programador", estado="SP")
print(pessoa)
```

### Operadores e Funções Úteis

#### in - Verifica se chave existe

```python
pessoa = {"nome": "Carlos", "idade": 25}
print("nome" in pessoa)         # True
print("cidade" in pessoa)       # False
```

#### del - Remove chave

```python
pessoa = {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}
del pessoa["idade"]
print(pessoa)           # {'nome': 'Carlos', 'cidade': 'São Paulo'}
```

#### len() - Retorna número de pares chave-valor

```python
pessoa = {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"}
tamanho = len(pessoa)
print(tamanho)          # 3
```

---

## Dominando Funções em Python

### Criação de Função e Retorno

#### Sintaxe Básica

```python
def nome_da_funcao():
    print("Olá, mundo!")

# Chamando a função
nome_da_funcao()        # Olá, mundo!
```

#### Funções com Parâmetros

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Carlos")      # Olá, Carlos!
```

#### Retorno de Valores

```python
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)        # 8

# Função sem return explícito retorna None
def sem_retorno():
    x = 10

valor = sem_retorno()
print(valor)            # None
```

#### Retornando Múltiplos Valores

```python
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    return soma, subtracao, multiplicacao

s, sub, mult = operacoes(10, 5)
print(s, sub, mult)     # 15 5 50

# Ou receber como tupla
resultado = operacoes(10, 5)
print(resultado)        # (15, 5, 50)
```

#### Return Antecipado

```python
def verificar_idade(idade):
    if idade < 18:
        return "Menor de idade"
    return "Maior de idade"

print(verificar_idade(15))  # Menor de idade
print(verificar_idade(20))  # Maior de idade
```

---

### Argumentos Nomeados

#### Argumentos Posicionais vs Nomeados

```python
def criar_usuario(nome, idade, cidade):
    print(f"{nome} tem {idade} anos e mora em {cidade}")

# Argumentos posicionais (ordem importa)
criar_usuario("Carlos", 25, "São Paulo")

# Argumentos nomeados (ordem não importa)
criar_usuario(idade=25, cidade="São Paulo", nome="Carlos")

# Misturando (posicionais devem vir antes)
criar_usuario("Carlos", cidade="São Paulo", idade=25)
```

#### Valores Padrão

```python
def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

saudacao("Carlos")                      # Olá, Carlos!
saudacao("Ana", "Bom dia")             # Bom dia, Ana!
saudacao("João", mensagem="E aí")      # E aí, João!
```

**Importante:** Parâmetros com valor padrão devem vir depois dos sem padrão.

```python
# Correto
def funcao(a, b, c=10):
    pass

# Errado - vai dar erro
# def funcao(a, c=10, b):
#     pass
```

---

### \*args e \*\*kwargs

#### \*args - Argumentos Posicionais Variáveis

Permite passar quantidade variável de argumentos posicionais. Os argumentos são recebidos como uma **tupla**.

```python
def soma(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(soma(1, 2, 3))            # 6
print(soma(1, 2, 3, 4, 5))      # 15
print(soma(10, 20))             # 30
```

#### \*\*kwargs - Argumentos Nomeados Variáveis

Permite passar quantidade variável de argumentos nomeados. Os argumentos são recebidos como um **dicionário**.

```python
def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_info(nome="Carlos", idade=25, cidade="São Paulo")
# nome: Carlos
# idade: 25
# cidade: São Paulo
```

#### Combinando \*args e \*\*kwargs

```python
def funcao_completa(obrigatorio, *args, **kwargs):
    print(f"Obrigatório: {obrigatorio}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

funcao_completa(
    "valor1",
    "extra1", "extra2",
    nome="Carlos", idade=25
)
# Obrigatório: valor1
# Args: ('extra1', 'extra2')
# Kwargs: {'nome': 'Carlos', 'idade': 25}
```

#### Ordem dos Parâmetros

A ordem correta é: `posicionais`, `*args`, `padrão`, `**kwargs`

```python
def funcao(pos1, pos2, *args, padrao=10, **kwargs):
    print(pos1, pos2, args, padrao, kwargs)

funcao(1, 2, 3, 4, padrao=20, x=100, y=200)
# 1 2 (3, 4) 20 {'x': 100, 'y': 200}
```

---

### Parâmetros Somente por Posição

Use `/` para indicar que parâmetros **antes** dele só podem ser passados por posição.

```python
def funcao(a, b, /, c):
    print(a, b, c)

# Correto
funcao(1, 2, 3)
funcao(1, 2, c=3)

# Errado - vai dar erro
# funcao(a=1, b=2, c=3)  # a e b não podem ser nomeados
# funcao(1, b=2, c=3)    # b não pode ser nomeado
```

#### Exemplo Prático

```python
def dividir(dividendo, divisor, /):
    return dividendo / divisor

print(dividir(10, 2))       # 5.0

# Errado - vai dar erro
# print(dividir(dividendo=10, divisor=2))
```

---

### Parâmetros Somente por Nome

Use `*` para indicar que parâmetros **depois** dele só podem ser passados por nome.

```python
def funcao(a, b, *, c, d):
    print(a, b, c, d)

# Correto
funcao(1, 2, c=3, d=4)
funcao(1, 2, d=4, c=3)

# Errado - vai dar erro
# funcao(1, 2, 3, 4)  # c e d devem ser nomeados
```

#### Exemplo Prático

```python
def criar_conexao(host, porta, *, timeout, ssl):
    print(f"Conectando em {host}:{porta}")
    print(f"Timeout: {timeout}, SSL: {ssl}")

criar_conexao("localhost", 8080, timeout=30, ssl=True)

# Errado - vai dar erro
# criar_conexao("localhost", 8080, 30, True)
```

#### Combinando / e \*

```python
def funcao(pos_only, /, normal, *, keyword_only):
    print(pos_only, normal, keyword_only)

# Correto
funcao(1, 2, keyword_only=3)
funcao(1, normal=2, keyword_only=3)

# Errado
# funcao(pos_only=1, normal=2, keyword_only=3)  # pos_only deve ser posicional
# funcao(1, 2, 3)  # keyword_only deve ser nomeado
```

---

### Objetos de Primeira Classe

Em Python, funções são **objetos de primeira classe**, ou seja, podem ser:

-   Atribuídas a variáveis
-   Passadas como argumentos
-   Retornadas de outras funções
-   Armazenadas em estruturas de dados

#### Atribuindo Função a Variável

```python
def saudacao(nome):
    return f"Olá, {nome}!"

# Atribuindo função a variável
cumprimento = saudacao
print(cumprimento("Carlos"))    # Olá, Carlos!
```

#### Função como Argumento

```python
def aplicar_operacao(func, x, y):
    return func(x, y)

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

print(aplicar_operacao(soma, 5, 3))            # 8
print(aplicar_operacao(multiplicacao, 5, 3))   # 15
```

#### Retornando Função

```python
def criar_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

vezes_2 = criar_multiplicador(2)
vezes_5 = criar_multiplicador(5)

print(vezes_2(10))      # 20
print(vezes_5(10))      # 50
```

#### Armazenando em Estruturas

```python
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

operacoes = {
    "soma": soma,
    "subtracao": subtracao
}

print(operacoes["soma"](10, 5))         # 15
print(operacoes["subtracao"](10, 5))    # 5
```

---

### Escopo Local e Global

#### Escopo Local

Variáveis criadas dentro de uma função existem apenas nela.

```python
def funcao():
    x = 10  # Variável local
    print(x)

funcao()        # 10
# print(x)      # Erro - x não existe fora da função
```

#### Escopo Global

Variáveis criadas fora de funções são globais.

```python
x = 100  # Variável global

def funcao():
    print(x)  # Acessa variável global

funcao()        # 100
print(x)        # 100
```

#### Problema: Variável Local vs Global

```python
x = 100

def funcao():
    x = 10  # Cria nova variável local, não modifica a global
    print(x)

funcao()        # 10
print(x)        # 100 (global não foi alterada)
```

#### Usando global para Modificar

Para modificar uma variável global dentro de uma função, use `global`.

```python
contador = 0

def incrementar():
    global contador  # Declara que vai usar a global
    contador += 1

incrementar()
print(contador)     # 1

incrementar()
print(contador)     # 2
```

**Por que usar global?**

Sem `global`, Python tenta criar uma variável local, mas se você tentar fazer `contador += 1`, ele precisa **ler** contador antes de incrementar, gerando erro porque ela não existe localmente.

```python
contador = 0

def incrementar():
    contador += 1  # Erro! UnboundLocalError

# incrementar()  # Vai dar erro
```

#### Exemplo Prático com global

```python
saldo = 1000

def depositar(valor):
    global saldo
    saldo += valor
    print(f"Depositado: R$ {valor}. Saldo: R$ {saldo}")

def sacar(valor):
    global saldo
    if valor <= saldo:
        saldo -= valor
        print(f"Sacado: R$ {valor}. Saldo: R$ {saldo}")
    else:
        print("Saldo insuficiente!")

depositar(500)      # Depositado: R$ 500. Saldo: R$ 1500
sacar(200)          # Sacado: R$ 200. Saldo: R$ 1300
print(f"Saldo final: R$ {saldo}")  # Saldo final: R$ 1300
```

#### Escopo LEGB

Python procura variáveis nesta ordem:

1. **L**ocal - dentro da função
2. **E**nclosing - funções externas (em caso de funções aninhadas)
3. **G**lobal - escopo do módulo
4. **B**uilt-in - funções nativas do Python

```python
x = "global"

def externa():
    x = "enclosing"

    def interna():
        x = "local"
        print(x)

    interna()       # local
    print(x)        # enclosing

externa()
print(x)            # global
```

---

### Boas Práticas com Funções

#### Use Docstrings

```python
def calcular_area(base, altura):
    """
    Calcula a área de um retângulo.

    Args:
        base (float): Base do retângulo
        altura (float): Altura do retângulo

    Returns:
        float: Área do retângulo
    """
    return base * altura
```

#### Evite Usar global

Prefira passar valores como parâmetros e retornar resultados:

```python
# Ruim
contador = 0

def incrementar():
    global contador
    contador += 1

# Melhor
def incrementar(valor):
    return valor + 1

contador = 0
contador = incrementar(contador)
```

#### Funções Devem Fazer Uma Coisa

```python
# Ruim - faz muita coisa
def processar_usuario(nome, email):
    validar_email(email)
    salvar_banco(nome, email)
    enviar_email(email)

# Melhor - separar responsabilidades
def validar_email(email):
    # validação
    pass

def salvar_usuario(nome, email):
    # salvar
    pass

def enviar_confirmacao(email):
    # enviar
    pass
```
---

# Introdução à Bancos de Dados NoSQL

## O que é NoSQL?

**NoSQL** significa "**Not Only SQL**" (Não Apenas SQL), não "No SQL". São bancos de dados projetados para lidar com:

- **Alto volume de dados** e escalabilidade horizontal
- **Alta flexibilidade** na estrutura dos dados
- **Consistência eventual** (em vez de imediata)
- **Dados não estruturados ou semi-estruturados**

### Quando usar NoSQL?

Ideal para cenários onde:
- A consistência imediata dos dados não é crítica
- Precisa escalar horizontalmente (adicionar mais servidores)
- Estrutura dos dados muda frequentemente
- Grande volume de leitura/escrita
- Dados não relacionais ou hierárquicos

---

## SQL vs NoSQL

### SQL (Relacional)

**Características:**
- Estrutura rígida (esquema fixo)
- Tabelas com linhas e colunas
- Relacionamentos definidos (chaves estrangeiras)
- ACID (Atomicidade, Consistência, Isolamento, Durabilidade)
- Consultas complexas com JOINs

**Exemplos:** MySQL, PostgreSQL, Oracle, SQL Server

**Quando usar:**
- Dados estruturados e relacionados
- Transações financeiras
- Consistência crítica
- Consultas complexas frequentes

### NoSQL (Não Relacional)

**Características:**
- Estrutura flexível (schema-less ou dinâmico)
- Não usa tabelas tradicionais
- Sem relacionamentos rígidos
- BASE (Basically Available, Soft state, Eventually consistent)
- Escalabilidade horizontal

**Exemplos:** MongoDB, Redis, Cassandra, Neo4j

**Quando usar:**
- Grande volume de dados
- Dados não estruturados
- Necessidade de alta disponibilidade
- Mudanças frequentes na estrutura

---

## Vantagens e Desvantagens do NoSQL

### Vantagens

✅ **Tolerância a falhas** - Replicação automática e distribuída
✅ **Flexibilidade na modelagem** - Esquema dinâmico
✅ **Alta escalabilidade** - Escala horizontalmente com facilidade
✅ **Melhor desempenho** - Em cenários de consulta intensiva
✅ **Custo reduzido** - Usa hardware commodity

### Desvantagens

❌ **Menor consistência imediata** - Consistência eventual
❌ **Consultas complexas limitadas** - Depende do tipo de NoSQL
❌ **Maturidade** - Menos ferramentas e padrões estabelecidos
❌ **Curva de aprendizado** - Paradigma diferente do SQL tradicional

---

## Tipos de Bancos NoSQL

### 1. Key-Value (Chave-Valor)

**Estrutura:** Armazena pares chave-valor simples

**Bancos:** Redis, Riak, Amazon DynamoDB

**Exemplo de uso:**
```
Chave: "sessao_usuario_123"
Valor: {"nome": "Carlos", "ultima_visita": "2025-01-15"}
```

**Caso prático:** Site usa Redis para armazenar informações de sessão do usuário

**Vantagens:**
- Extremamente rápido
- Simples de usar
- Ótimo para cache

**Quando usar:**
- Cache de dados
- Sessões de usuário
- Filas de mensagens

---

### 2. Documento

**Estrutura:** Armazena documentos (JSON, BSON, XML)

**Bancos:** MongoDB, CouchDB, Couchbase

**Exemplo de uso:**
```json
{
  "_id": "prod123",
  "nome": "Notebook",
  "preco": 3500.00,
  "categorias": ["Eletrônicos", "Informática"],
  "especificacoes": {
    "ram": "16GB",
    "processador": "Intel i7"
  }
}
```

**Caso prático:** Catálogo de e-commerce usando MongoDB para armazenar produtos com descrição, preço, categorias e especificações

**Vantagens:**
- Flexível
- Suporta estruturas complexas
- Consultas ricas

**Quando usar:**
- Catálogos de produtos
- Gerenciamento de conteúdo
- Perfis de usuário

---

### 3. Coluna (Wide-Column)

**Estrutura:** Armazena dados em colunas em vez de linhas

**Bancos:** Apache Cassandra, ScyllaDB, HBase

**Exemplo de uso:**
```
Row Key: "log_2025-01-15"
Coluna: timestamp | level | message | user
Valor:  10:30:00  | ERROR | "Falha"  | "user123"
```

**Caso prático:** Sistema de registro de logs usando Apache Cassandra para armazenar milhões de registros distribuídos

**Vantagens:**
- Alta performance para escrita
- Compressão eficiente
- Ótimo para análise de dados

**Quando usar:**
- Logs de sistema
- Séries temporais
- Análise de big data

---

### 4. Grafo

**Estrutura:** Armazena nós (entidades) e arestas (relacionamentos)

**Bancos:** Neo4j, Amazon Neptune, JanusGraph

**Exemplo de uso:**
```
Nó: (Usuario:Carlos)
Nó: (Usuario:Ana)
Aresta: (Carlos)-[AMIGO_DE]->(Ana)
```

**Caso prático:** Rede social usando Neo4j para armazenar perfis e conexões, permitindo consultas eficientes para encontrar amigos em comum

**Vantagens:**
- Relacionamentos complexos
- Consultas de grafos rápidas
- Visualização de conexões

**Quando usar:**
- Redes sociais
- Sistemas de recomendação
- Detecção de fraudes
- Análise de conexões

---

## MongoDB - Banco de Documentos

### O que é MongoDB?

MongoDB é um banco de dados NoSQL orientado a documentos que armazena dados em formato **BSON** (Binary JSON). É o banco NoSQL mais popular do mundo.

### Características Principais

**✅ Flexibilidade:** Esquema dinâmico, não precisa definir estrutura antes
**✅ Escalabilidade:** Sharding automático para distribuição de dados
**✅ Performance:** Índices poderosos e consultas rápidas
**✅ Alta disponibilidade:** Réplicas automáticas
**✅ Consultas ricas:** Suporte a agregações complexas

### Vantagens do MongoDB

✅ **Desenvolvimento ágil** - Esquema flexível acelera iterações
✅ **Documentos intuitivos** - Estrutura similar a objetos (JSON)
✅ **Escalabilidade horizontal** - Adiciona servidores facilmente
✅ **Performance** - Consultas indexadas muito rápidas
✅ **Ecossistema rico** - Drivers para todas as linguagens
✅ **Atlas (Cloud)** - Serviço gerenciado gratuito

### Desvantagens do MongoDB

❌ **Consumo de memória** - Pode usar muita RAM
❌ **Transações complexas** - Não é ideal para operações ACID complexas
❌ **Tamanho dos documentos** - Limite de 16MB por documento
❌ **JOINs limitados** - Não é ideal para dados altamente relacionados
❌ **Duplicação de dados** - Pode haver redundância

### Quando usar MongoDB?

**✅ Use quando:**
- Dados não estruturados ou semi-estruturados
- Estrutura de dados muda frequentemente
- Precisa escalar rapidamente
- Desenvolvimento ágil
- Catálogos, CMS, aplicações real-time

**❌ Evite quando:**
- Transações financeiras críticas
- Dados altamente relacionados (muitos JOINs)
- Requisitos ACID rígidos
- Orçamento de memória limitado

---

## MongoDB - Modelagem de Dados

### Estrutura Básica

**Database (Banco de Dados):**
- Container de coleções
- Exemplo: `loja`, `blog`, `usuarios`

**Collection (Coleção):**
- Equivalente a uma "tabela" no SQL
- Agrupa documentos relacionados
- Exemplo: `produtos`, `pedidos`, `clientes`

**Document (Documento):**
- Equivalente a uma "linha/registro" no SQL
- Formato BSON (Binary JSON)
- Cada documento pode ter estrutura diferente

```
Database: loja
  └── Collection: produtos
       ├── Document: {"nome": "Notebook", "preco": 3500}
       └── Document: {"nome": "Mouse", "preco": 50, "wireless": true}
```

### Tipos de Dados Simples

```json
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "nome": "Carlos",
  "idade": 25,
  "salario": 5000.50,
  "ativo": true,
  "cargo": null,
  "data_cadastro": ISODate("2025-01-15T10:30:00Z")
}
```

**Tipos básicos:**
- **String** - Texto: `"Carlos"`
- **Number** - Inteiro ou decimal: `25`, `5000.50`
- **Boolean** - Verdadeiro/falso: `true`, `false`
- **Null** - Valor nulo: `null`
- **ObjectId** - ID único do MongoDB: `ObjectId("...")`
- **Date** - Data/hora: `ISODate("2025-01-15")`

### Tipos de Dados Complexos

#### Array (Lista)

```json
{
  "nome": "Carlos",
  "hobbies": ["programação", "games", "música"],
  "notas": [8.5, 9.0, 7.5]
}
```

#### Documentos Embutidos (Embedded Documents)

```json
{
  "nome": "Carlos",
  "endereco": {
    "rua": "Av. Paulista",
    "numero": 1000,
    "cidade": "São Paulo",
    "cep": "01310-100"
  },
  "contatos": {
    "email": "carlos@email.com",
    "telefone": "11999999999"
  }
}
```

#### Referências (References)

```json
// Documento de Usuario
{
  "_id": ObjectId("user123"),
  "nome": "Carlos"
}

// Documento de Post (referencia usuario)
{
  "_id": ObjectId("post456"),
  "titulo": "Meu Post",
  "autor_id": ObjectId("user123")
}
```

#### GeoJSON (Dados Geográficos)

```json
{
  "nome": "Restaurante",
  "localizacao": {
    "type": "Point",
    "coordinates": [-23.5505, -46.6333]
  }
}
```

### Ferramenta: JSON Formatter

**Site:** [jsonformatter.curiousconcept.com](https://jsonformatter.curiousconcept.com)

Use para:
- Validar JSON
- Formatar/identar JSON
- Criar estruturas JSON
- Debug de documentos MongoDB

---

## Estratégias de Modelagem

### 1. Embedded Documents (Documentos Embutidos)

**Use quando:** Dados sempre acessados juntos

```json
{
  "pedido_id": "123",
  "cliente": "Carlos",
  "itens": [
    {"produto": "Notebook", "qtd": 1, "preco": 3500},
    {"produto": "Mouse", "qtd": 2, "preco": 50}
  ],
  "total": 3600
}
```

**Vantagens:**
- Uma única consulta
- Melhor performance
- Atomicidade garantida

**Desvantagens:**
- Duplicação de dados
- Limite de 16MB por documento

### 2. References (Referências)

**Use quando:** Dados grandes ou compartilhados

```json
// Collection: usuarios
{
  "_id": ObjectId("user123"),
  "nome": "Carlos"
}

// Collection: posts
{
  "_id": ObjectId("post456"),
  "titulo": "Meu Post",
  "autor_id": ObjectId("user123")
}
```

**Vantagens:**
- Sem duplicação
- Flexibilidade
- Documentos menores

**Desvantagens:**
- Múltiplas consultas (ou $lookup)
- Complexidade maior

### 3. Híbrido (Melhor prática)

Combine estratégias conforme necessidade:

```json
{
  "pedido_id": "123",
  "cliente": {
    "_id": ObjectId("user123"),
    "nome": "Carlos",
    "email": "carlos@email.com"
  },
  "itens": [
    {"produto": "Notebook", "qtd": 1, "preco": 3500}
  ]
}
```

---

## Instalação e Configuração

### MongoDB Atlas (Cloud - Recomendado)

1. Acesse [mongodb.com/atlas](https://www.mongodb.com/atlas)
2. Crie conta gratuita
3. Crie cluster grátis (M0)
4. Configure acesso (IP e usuário)
5. Obtenha connection string
6. Conecte via Compass ou código

**Vantagens:**
- Grátis até 512MB
- Sem configuração de servidor
- Backups automáticos
- Interface web

---

## Operações no MongoDB

### MongoDB Compass (Interface Gráfica)

**Download:** [mongodb.com/products/compass](https://www.mongodb.com/products/compass)

**Recursos:**
- Interface visual
- Criação de databases/collections
- Inserção e edição de documentos
- Consultas visuais
- Análise de performance

### Criando Database e Collection

```javascript
// No Compass: New Database
// Database: loja
// Collection: produtos

// Via código (MongoDB Shell)
use loja
db.createCollection("produtos")
```

### Inserção de Documentos

#### insertOne() - Inserir um documento

```javascript
db.produtos.insertOne({
  nome: "Notebook",
  preco: 3500,
  estoque: 10,
  categorias: ["Eletrônicos", "Informática"]
})
```

#### insertMany() - Inserir múltiplos documentos

```javascript
db.produtos.insertMany([
  {
    nome: "Mouse",
    preco: 50,
    estoque: 100
  },
  {
    nome: "Teclado",
    preco: 150,
    estoque: 50
  }
])
```

### Consultas (Query)

#### find() - Buscar todos

```javascript
// Todos os documentos
db.produtos.find()

// Com filtro
db.produtos.find({ preco: { $lt: 100 } })

// Com projeção (selecionar campos)
db.produtos.find({}, { nome: 1, preco: 1, _id: 0 })
```

#### findOne() - Buscar um

```javascript
db.produtos.findOne({ nome: "Notebook" })
```

### Atualização

#### updateOne() - Atualizar um

```javascript
db.produtos.updateOne(
  { nome: "Notebook" },
  { $set: { preco: 3200 } }
)
```

#### updateMany() - Atualizar múltiplos

```javascript
db.produtos.updateMany(
  { estoque: { $lt: 10 } },
  { $set: { em_falta: true } }
)
```

#### findOneAndUpdate() - Buscar e atualizar

```javascript
db.produtos.findOneAndUpdate(
  { nome: "Mouse" },
  { $inc: { estoque: -1 } },
  { returnNewDocument: true }
)
```

### Deleção

#### deleteOne() - Deletar um

```javascript
db.produtos.deleteOne({ nome: "Mouse" })
```

#### deleteMany() - Deletar múltiplos

```javascript
db.produtos.deleteMany({ estoque: 0 })
```

#### findOneAndDelete() - Buscar e deletar

```javascript
db.produtos.findOneAndDelete({ nome: "Teclado" })
```

### Operadores Lógicos

```javascript
// $and
db.produtos.find({
  $and: [
    { preco: { $gte: 100 } },
    { estoque: { $gt: 0 } }
  ]
})

// $or
db.produtos.find({
  $or: [
    { preco: { $lt: 50 } },
    { estoque: { $gt: 100 } }
  ]
})

// $not
db.produtos.find({
  preco: { $not: { $gte: 1000 } }
})

// $nor (nenhum verdadeiro)
db.produtos.find({
  $nor: [
    { preco: { $lt: 50 } },
    { estoque: 0 }
  ]
})
```

### Operadores de Comparação

```javascript
// $eq (igual)
db.produtos.find({ preco: { $eq: 100 } })

// $ne (diferente)
db.produtos.find({ preco: { $ne: 100 } })

// $gt (maior que)
db.produtos.find({ preco: { $gt: 100 } })

// $gte (maior ou igual)
db.produtos.find({ preco: { $gte: 100 } })

// $lt (menor que)
db.produtos.find({ preco: { $lt: 100 } })

// $lte (menor ou igual)
db.produtos.find({ preco: { $lte: 100 } })

// $in (está na lista)
db.produtos.find({ nome: { $in: ["Mouse", "Teclado"] } })

// $nin (não está na lista)
db.produtos.find({ nome: { $nin: ["Mouse", "Teclado"] } })
```

### Ordenação

```javascript
// Crescente (1)
db.produtos.find().sort({ preco: 1 })

// Decrescente (-1)
db.produtos.find().sort({ preco: -1 })

// Múltiplos campos
db.produtos.find().sort({ categoria: 1, preco: -1 })
```

### Limitação

```javascript
// Limitar resultados
db.produtos.find().limit(5)

// Pular resultados
db.produtos.find().skip(10)

// Combinar
db.produtos.find().skip(10).limit(5)
```

### Paginação

```javascript
// Página 1 (10 itens por página)
db.produtos.find().limit(10).skip(0)

// Página 2
db.produtos.find().limit(10).skip(10)

// Página 3
db.produtos.find().limit(10).skip(20)

// Fórmula: skip = (pagina - 1) * limite
```

---

## Redis - Banco Key-Value

### O que é Redis?

**Redis** (Remote Dictionary Server) é um banco de dados **em memória** do tipo chave-valor, extremamente rápido e versátil.

### Características Principais

**✅ Armazenamento em memória** - Dados na RAM para performance máxima
**✅ Estruturas de dados versáteis** - Strings, listas, sets, hashes, etc
**✅ Operações atômicas** - Garantia de consistência
**✅ Persistência opcional** - Pode salvar em disco
**✅ Pub/Sub** - Sistema de mensagens em tempo real
**✅ Expiration** - TTL automático para dados temporários

### Casos de Uso

**1. Cache de Dados**
```
Armazenar resultados de consultas pesadas
Reduzir carga no banco principal
```

**2. Filas de Mensagens**
```
Processar tarefas assíncronas
Sistema de jobs
```

**3. Contadores e Estatísticas**
```
Contagem de acessos em tempo real
Ranking de usuários/produtos
```

**4. Gerenciamento de Sessões**
```
Sessões de usuário em aplicações web
Tokens de autenticação
```

**5. Cache de Resultados de Consultas**
```
Guardar resultados de SQL queries
Reduzir tempo de resposta
```

### Principais Comandos

#### SET - Definir valor

```redis
SET usuario:123:nome "Carlos"
SET produto:456:preco 3500
SET sessao:abc123 "dados_da_sessao" EX 3600  # Expira em 1h
```

#### GET - Obter valor

```redis
GET usuario:123:nome
# Retorna: "Carlos"
```

#### DEL - Deletar chave

```redis
DEL usuario:123:nome
```

#### EXISTS - Verificar se existe

```redis
EXISTS usuario:123:nome
# Retorna: 1 (existe) ou 0 (não existe)
```

#### KEYS - Listar chaves

```redis
KEYS usuario:*
# Retorna: todas chaves que começam com "usuario:"
```

#### INCR / DECR - Incrementar/Decrementar

```redis
SET visitas:pagina 0
INCR visitas:pagina  # Incrementa para 1
INCR visitas:pagina  # Incrementa para 2
DECR visitas:pagina  # Decrementa para 1
```

#### EXPIRE - Definir tempo de expiração

```redis
SET token:abc "valor"
EXPIRE token:abc 3600  # Expira em 3600 segundos (1h)
```

#### TTL - Ver tempo restante

```redis
TTL token:abc
# Retorna: segundos restantes ou -1 (sem expiração)
```

### Estruturas de Dados

#### Listas

```redis
LPUSH fila:jobs "job1"
LPUSH fila:jobs "job2"
RPOP fila:jobs  # Remove do final
```

#### Sets

```redis
SADD tags:post1 "python" "mongodb" "redis"
SMEMBERS tags:post1  # Lista todos
```

#### Hashes

```redis
HSET usuario:123 nome "Carlos" idade 25
HGET usuario:123 nome  # Retorna: "Carlos"
HGETALL usuario:123    # Retorna todos campos
```

### Testar Redis Online

**Site:** [try.redis.io](https://try.redis.io)

Execute comandos Redis diretamente no navegador para praticar!

---

## Recursos Adicionais

- [MongoDB University](https://university.mongodb.com) - Cursos gratuitos oficiais
- [MongoDB Documentation](https://docs.mongodb.com)
- [Redis Documentation](https://redis.io/docs)
- [Redis Commands](https://redis.io/commands) - Lista completa de comandos

---

# Fundamentos de ETL com Python

## O que é ETL?

**ETL** é um processo de integração de dados em três etapas:

- **E**xtract (Extrair) - Importar dados de diversas fontes
- **T**ransform (Transformar) - Converter e limpar dados
- **L**oad (Carregar) - Armazenar no destino final

### Definição Completa

ETL envolve ferramentas de software voltadas para **extração de dados de diversos sistemas**, **transformação desses dados conforme regras de negócio** bem definidas, para por fim serem **carregados em um Data Mart e/ou Data Warehouse**.

É um tipo de integração de dados usado para combinar dados de diversas fontes e construir um Data Warehouse.

---

## As Três Etapas do ETL

### 1. Extract (Extração)

**O que é:** Processo de comunicação com outros sistemas ou bancos de dados para capturar os dados que serão inseridos no destino (staging area ou outro sistema).

**Fontes de dados suportadas:**
- Planilhas Excel
- Diversos bancos de dados (SQL Server, Oracle, MySQL, etc)
- CSV
- TXT
- JSON
- XML
- APIs
- Web scraping

**Mapeamento:**
Na extração, a origem deve conter a especificação da entidade e seus atributos detalhados. Tudo é armazenado numa **zona temporária (staging area)**, onde serão efetuadas análises e filtragens. A nova versão poderá ser comparada com a cópia da versão prévia.

### 2. Transform (Transformação)

**O que é:** Processo composto por várias etapas de preparação dos dados.

**Operações de transformação:**

**Padronização:**
- Dados vindos de sistemas diferentes têm padrões diferentes
- Nomenclaturas variadas
- Tipos de dados diferentes (VARCHAR2 do Oracle vs VARCHAR do SQL Server)

**Limpeza:**
- Remove erros
- Padroniza informações
- Corrige inconsistências
- Remove duplicatas

**Complementação:**
- Acréscimo de dados
- Enriquecimento de informações
- Cálculos e agregações

**Operações comuns:**
- Modificar colunas e linhas
- Alterar tipos de dados
- Mesclar tabelas
- Acrescentar dados
- Criar listas e tabelas derivadas

**Garantia de qualidade:**
- Validação de dados
- Verificação de integridade
- Conformidade com regras de negócio

### 3. Load (Carregamento)

**O que é:** Etapa final onde os dados são lidos da área de staging e carregados no Data Warehouse ou Data Mart final.

**Destinos comuns:**
- Data Warehouse
- Data Mart
- Data Lake
- Bancos de dados analíticos
- Sistemas de nuvem

---

## ETL vs ELT

### ETL (Extract, Transform, Load)
Transformação ocorre **antes** do carregamento.

**Vantagens:**
- Dados já chegam limpos no destino
- Menor carga no banco de dados final
- Melhor para destinos com recursos limitados

### ELT (Extract, Load, Transform)
Transformação ocorre **depois** do carregamento.

**Vantagens:**
- Aproveita processamento do banco de dados
- Melhor performance em bancos modernos
- Flexibilidade para transformações futuras
- Ideal para Big Data e Cloud

---

## Vantagens das Ferramentas ETL

### 1. Garantia de Qualidade dos Dados
Através de sequências de operações e instruções, as ferramentas têm condições de solucionar problemas de maior complexidade.

### 2. Funcionalidade de Execução
A ferramenta já possui suas funções específicas, sendo necessária apenas a atenção no fluxo de dados.

### 3. Desenvolvimento das Cargas
Mesmo usuários não técnicos podem desenvolver rotinas de carga devido à facilidade e rapidez para codificação.

### 4. Manutenção das Cargas
As tarefas de manutenção são mais simples comparadas à manutenção de código manual.

### 5. Metainformação
Os metadados (informações úteis para identificar, localizar, entender e gerenciar os dados) são gerados e mantidos automaticamente, evitando problemas de informações incorretas.

### 6. Performance
Os métodos mais usados para grandes volumes conseguem extrair, transformar e carregar dados com maior velocidade e menos recursos, como:
- Gravações em bloco
- Operações não logadas

### 7. Transferência
Ferramentas de ETL podem ser deslocadas de um servidor mais facilmente ou distribuídas entre vários servidores.

### 8. Conectividade
A conexão com múltiplas fontes de dados é transparente. Para adicionar mais fontes (SAP, VSAM, Mainframe), basta adquirir o conector sem necessidade de codificar.

### 9. Reinicialização
Ferramentas possuem capacidade de reiniciar a carga de onde pararam sem necessidade de codificação.

### 10. Segurança e Estabilidade
É possível articular melhor a segurança tornando-a modular, dividindo as finalidades:
- Criação de cargas
- Execução de cargas
- Agendamento

---

## Principais Ferramentas ETL

### Ferramentas Tradicionais

#### IBM Information Server (DataStage)
Solução enterprise robusta e escalável da IBM.

**Site:** [cetax.com.br/datastage-ibm-ferramenta-de-etl](https://www.cetax.com.br/datastage-ibm-ferramenta-de-etl/)

#### Informatica PowerCenter
Uma das ferramentas mais populares do mercado.

**Site:** [cetax.com.br/power-center-informatica-ferramenta-de-etl](https://www.cetax.com.br/power-center-informatica-ferramenta-de-etl/)

#### Microsoft SSIS (SQL Server Integration Services)
Ferramenta nativa do SQL Server para integração de dados.

**Site:** [cetax.com.br/ssis-sql-server-integration](https://www.cetax.com.br/ssis-sql-server-integration)

#### Oracle Data Integrator (ODI)
Solução da Oracle para integração de dados.

#### Pentaho Data Integration
Ferramenta open source completa.

#### Talend ETL
Plataforma open source popular e poderosa.

**Site:** [cetax.com.br/criando-job-simples-no-talend](https://www.cetax.com.br/criando-job-simples-no-talend/)

---

## ETL para Big Data

### Por que é diferente?

Com o crescimento dos projetos de Big Data, aumenta-se mais ainda a necessidade de fazer ETL entre plataformas heterogêneas. Projetos como o **Hadoop** possuem ferramentas próprias para carga de dados.

### O que é Hadoop?

**Hadoop** é uma plataforma de software em Java de computação distribuída voltada para:
- Clusters de servidores
- Processamento de grandes volumes de dados
- Atenção à tolerância a falhas

### Ferramentas do Ecossistema Hadoop

#### SQOOP
Ferramenta para movimentar dados entre bancos de dados relacionais e o ambiente Hadoop.

**Uso:**
```bash
# Importar dados do MySQL para Hadoop
sqoop import --connect jdbc:mysql://localhost/db --table users
```

#### HIVE
Ambiente de SQL sobre um cluster Hadoop.

**Características:**
- Query language similar ao SQL (HiveQL)
- Processa grandes volumes de dados
- Trabalha sobre HDFS

#### PIG
Ferramenta de Script para transformação e processamento de dados.

**Características:**
- Linguagem de alto nível (Pig Latin)
- Transforma automaticamente em MapReduce
- Ótimo para ETL complexo

#### SPARK
Framework de processamento em memória.

**Características:**
- Processamento até 100x mais rápido
- API em Python, Scala, Java, R
- Suporte a streaming e ML

### Ingestão de Dados (Big Data ETL)

Em Big Data, o processo de carga também é conhecido como **Ingestão de Dados**, que geralmente é a primeira parte da carga (Extract).

**Destino:** Data Lake ou ambiente de dados utilizado

**Características:**
- Parte mais simples do processo
- Consiste em extrair dados dos sistemas de origem
- Trazer para dentro do Data Lake

---

## Pandas - Biblioteca Python para ETL

### O que é Pandas?

Pandas é a principal biblioteca Python para manipulação e análise de dados. É essencial para processos ETL.

### Tipos de Dados Suportados

✅ **Dados tabulares** - Como planilhas Excel ou tabelas SQL
✅ **Séries temporais** - Dados ordenados por tempo
✅ **Matrizes** - Dados multidimensionais
✅ **Dados não rotulados** - Qualquer conjunto de dados

### Bibliotecas Complementares

- **OpenCV** - Processamento de imagens
- **Scikit-Image** - Manipulação de imagens
- **Pillow** - Edição de imagens
- **Matplotlib** - Visualização de dados

---

## Estruturas de Dados do Pandas

### Series

**O que é:** Matriz unidimensional que contém uma sequência de valores com indexação.

**Características:**
- Similar a uma coluna do Excel
- Pode ter índices numéricos ou rótulos
- Permite operações vetorizadas

```python
import pandas as pd

# Criando uma Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)
# a    10
# b    20
# c    30
# d    40
```

### DataFrame

**O que é:** Estrutura de dados tabular bidimensional, semelhante a uma planilha Excel.

**Características:**
- Linhas e colunas com rótulos
- Cada coluna pode ter tipo diferente
- Similar a uma tabela SQL

```python
import pandas as pd

# Criando um DataFrame
df = pd.DataFrame({
    'nome': ['Carlos', 'Ana', 'João'],
    'idade': [25, 30, 22],
    'cidade': ['SP', 'RJ', 'MG']
})
print(df)
#     nome  idade cidade
# 0  Carlos     25     SP
# 1     Ana     30     RJ
# 2    João     22     MG
```

---

## Principais Funções do Pandas

### Leitura de Dados

```python
import pandas as pd

# Ler CSV
df = pd.read_csv('arquivo.csv')

# Ler Excel
df = pd.read_excel('arquivo.xlsx')

# Ler JSON
df = pd.read_json('arquivo.json')

# Ler SQL
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM tabela', conn)
```

### Exploração de Dados

#### shape - Dimensões do DataFrame
```python
df.shape
# Retorna: (linhas, colunas)
# Exemplo: (100, 5) = 100 linhas, 5 colunas
```

#### head() - Primeiras linhas
```python
df.head()        # Primeiras 5 linhas (padrão)
df.head(10)      # Primeiras 10 linhas
```

#### tail() - Últimas linhas
```python
df.tail()        # Últimas 5 linhas
df.tail(10)      # Últimas 10 linhas
```

#### info() - Informações do DataFrame
```python
df.info()
# Mostra:
# - Número de linhas
# - Tipos de dados de cada coluna
# - Memória usada
# - Valores não-nulos
```

#### describe() - Estatísticas descritivas
```python
df.describe()
# Retorna para colunas numéricas:
# - count (quantidade)
# - mean (média)
# - std (desvio padrão)
# - min (mínimo)
# - 25%, 50%, 75% (quartis)
# - max (máximo)
```

### Manipulação de Colunas

#### Renomear colunas
```python
# Alterar nomes de colunas
df.columns = ['nova_col1', 'nova_col2', 'nova_col3']

# Renomear colunas específicas
df.rename(columns={'nome_antigo': 'nome_novo'}, inplace=True)
```

### Verificação de Dados

#### isnull() - Verificar valores nulos
```python
# Verificar nulos em todo DataFrame
df.isnull()

# Contar nulos por coluna
df.isnull().sum()

# Verificar se há algum nulo
df.isnull().any()
```

#### unique() - Valores únicos
```python
# Valores únicos de uma coluna
df['cidade'].unique()
# Retorna: array(['SP', 'RJ', 'MG'])

# Quantidade de valores únicos
df['cidade'].nunique()
# Retorna: 3
```

#### value_counts() - Contagem de valores
```python
df['cidade'].value_counts()
# Retorna:
# SP    50
# RJ    30
# MG    20
```

### Visualização com Matplotlib

```python
import matplotlib.pyplot as plt

# Gráfico de linha
df.plot()

# Gráfico de barras
df.plot(kind='bar')

# Histograma
df['idade'].plot(kind='hist')

# Gráfico de pizza
df['cidade'].value_counts().plot(kind='pie')

# Mostrar gráfico
plt.show()
```

### Exemplos Práticos

```python
import pandas as pd

# Ler dados
df = pd.read_csv('vendas.csv')

# Explorar dados
print(df.shape)          # (1000, 6)
print(df.head())         # Primeiras 5 linhas
print(df.info())         # Informações gerais
print(df.describe())     # Estatísticas

# Verificar nulos
print(df.isnull().sum())

# Análise de categorias
print(df['produto'].unique())
print(df['produto'].value_counts())

# Visualização
df['valor'].plot(kind='hist')
plt.show()
```

---

## Scikit-learn - Machine Learning para ETL

### O que é Scikit-learn?

Biblioteca Python que dispõe de ferramentas simples e eficientes para análise preditiva de dados.

### Características

✅ **Simples e eficiente** - Análise preditiva acessível
✅ **Reutilizável** - Funciona em diferentes situações
✅ **Código aberto** - Acessível a todos
✅ **Integrado** - Construído sobre NumPy, SciPy e Matplotlib

### Funcionalidades Principais

**Classificação:**
- Identificar a qual categoria um objeto pertence
- Exemplos: spam detection, reconhecimento de imagens

**Regressão:**
- Prever um atributo de valor contínuo
- Exemplos: previsão de preços, demanda

**Clustering:**
- Agrupamento automático de objetos similares
- Exemplos: segmentação de clientes

**Redução de dimensionalidade:**
- Reduzir número de variáveis
- Visualização de dados de alta dimensão

**Pré-processamento:**
- Preparação de dados para ML
- Normalização, encoding, etc.

### Exemplo de Uso em ETL

```python
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Normalizar dados numéricos
scaler = StandardScaler()
df['valor_normalizado'] = scaler.fit_transform(df[['valor']])

# Codificar categorias
encoder = LabelEncoder()
df['categoria_encoded'] = encoder.fit_transform(df['categoria'])
```

---

## Manipulando Dados com Pandas

### Exemplo Prático - Leitura de CSV

```python
import pandas as pd

# Ler arquivo CSV
df = pd.read_csv('dados.csv')

# Ver primeiras linhas
print(df.head())

# Informações do dataset
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Verificar valores nulos
print(df.isnull().sum())

# Preencher valores nulos
df.fillna(0, inplace=True)

# Filtrar dados
df_filtrado = df[df['idade'] > 18]

# Agrupar dados
agrupamento = df.groupby('cidade')['valor'].sum()

# Salvar resultado
df_filtrado.to_csv('dados_processados.csv', index=False)
```

### Exemplo Completo de ETL

```python
import pandas as pd

# EXTRACT
# Ler dados de múltiplas fontes
df_vendas = pd.read_csv('vendas.csv')
df_produtos = pd.read_excel('produtos.xlsx')
df_clientes = pd.read_json('clientes.json')

# TRANSFORM
# Limpar dados
df_vendas.dropna(inplace=True)
df_vendas['data'] = pd.to_datetime(df_vendas['data'])

# Mesclar dados
df_merged = df_vendas.merge(df_produtos, on='produto_id')
df_merged = df_merged.merge(df_clientes, on='cliente_id')

# Criar novas colunas
df_merged['total'] = df_merged['quantidade'] * df_merged['preco']
df_merged['mes'] = df_merged['data'].dt.month

# Agregações
df_resumo = df_merged.groupby('mes').agg({
    'total': 'sum',
    'quantidade': 'sum',
    'cliente_id': 'count'
})

# LOAD
# Salvar em diferentes formatos
df_merged.to_csv('vendas_processadas.csv', index=False)
df_resumo.to_excel('resumo_mensal.xlsx')

# Ou carregar em banco de dados
import sqlite3
conn = sqlite3.connect('database.db')
df_merged.to_sql('vendas', conn, if_exists='replace', index=False)
```

---

## Framework Luigi para ETL

### O que é Luigi?

**Luigi** é um framework de execução criado pelo **Spotify** que cria pipelines de dados em Python.

### Características

✅ **Gerenciamento de dependências** - Controla ordem de execução
✅ **Workflow management** - Gerencia fluxo de trabalho
✅ **Visualização** - Interface gráfica para monitorar
✅ **Tratamento de falhas** - Recuperação automática
✅ **Integração CLI** - Linha de comando integrada
✅ **Compatibilidade** - Python 2.7, 3.6, 3.7+

### Conceitos Principais

#### Target (Destino)

**O que é:** Contém a saída de uma tarefa.

**Tipos:**
- Arquivo local
- Bucket S3
- Tabela MySQL
- Qualquer destino customizado

```python
import luigi

class MeuTarget(luigi.Target):
    def __init__(self, path):
        self.path = path
    
    def exists(self):
        import os
        return os.path.exists(self.path)
```

#### Task (Tarefa)

**O que é:** Onde o trabalho real ocorre. Pode ser independente ou dependente.

**Estrutura de uma Task:**

```python
import luigi

class MinhaTask(luigi.Task):
    
    def requires(self):
        # Tarefas que devem executar antes
        return []
    
    def output(self):
        # Onde a saída será armazenada
        return luigi.LocalTarget('saida.txt')
    
    def run(self):
        # Lógica real da tarefa
        with self.output().open('w') as f:
            f.write('Tarefa concluída!')
```

### Métodos Principais

#### requires()
Contém todas as instâncias de tarefas que devem ser executadas antes da tarefa atual.

```python
def requires(self):
    return [TarefaAnterior1(), TarefaAnterior2()]
```

#### output()
Contém o destino onde a saída da tarefa será armazenada. Pode conter um ou mais objetos de destino.

```python
def output(self):
    return luigi.LocalTarget('resultado.csv')
```

#### run()
Contém a lógica real para executar uma tarefa.

```python
def run(self):
    # Seu código ETL aqui
    import pandas as pd
    df = pd.read_csv('entrada.csv')
    df_processado = processar(df)
    df_processado.to_csv(self.output().path, index=False)
```

### Instalação

```bash
pip install luigi
```

### Exemplo Completo de Pipeline ETL

```python
import luigi
import pandas as pd

class ExtrairDados(luigi.Task):
    """Extrai dados de uma fonte"""
    
    def output(self):
        return luigi.LocalTarget('dados_brutos.csv')
    
    def run(self):
        # Simular extração de dados
        df = pd.DataFrame({
            'nome': ['Carlos', 'Ana', 'João'],
            'idade': [25, 30, 22],
            'cidade': ['SP', 'RJ', 'MG']
        })
        df.to_csv(self.output().path, index=False)

class TransformarDados(luigi.Task):
    """Transforma dados extraídos"""
    
    def requires(self):
        return ExtrairDados()
    
    def output(self):
        return luigi.LocalTarget('dados_transformados.csv')
    
    def run(self):
        # Ler dados brutos
        df = pd.read_csv(self.input().path)
        
        # Transformações
        df['nome'] = df['nome'].str.upper()
        df['faixa_etaria'] = df['idade'].apply(
            lambda x: 'Jovem' if x < 30 else 'Adulto'
        )
        
        # Salvar dados transformados
        df.to_csv(self.output().path, index=False)

class CarregarDados(luigi.Task):
    """Carrega dados no destino final"""
    
    def requires(self):
        return TransformarDados()
    
    def output(self):
        return luigi.LocalTarget('pipeline_completo.flag')
    
    def run(self):
        # Ler dados transformados
        df = pd.read_csv(self.input().path)
        
        # Carregar em banco de dados (exemplo)
        import sqlite3
        conn = sqlite3.connect('database.db')
        df.to_sql('usuarios', conn, if_exists='replace', index=False)
        conn.close()
        
        # Marcar como completo
        with self.output().open('w') as f:
            f.write('Pipeline executado com sucesso!')

# Executar pipeline
if __name__ == '__main__':
    luigi.run(['CarregarDados', '--local-scheduler'])
```

### Interface Gráfica do Luigi

Luigi possui uma interface web para visualizar e monitorar pipelines.

**Iniciar servidor:**
```bash
luigid
```

**Acessar:** http://localhost:8082

**Recursos da interface:**
- Visualizar dependências entre tasks
- Monitorar execução em tempo real
- Ver histórico de execuções
- Identificar falhas
- Acompanhar progresso

### Documentação

**Site oficial:** [luigi.readthedocs.io](https://luigi.readthedocs.io)

---

## Resumo - Boas Práticas ETL

### 1. Planejamento
- Defina bem as fontes de dados
- Mapeie transformações necessárias
- Escolha destino apropriado

### 2. Qualidade dos Dados
- Sempre valide dados na extração
- Implemente regras de limpeza
- Documente transformações

### 3. Performance
- Use processamento em lotes
- Aproveite índices nos bancos
- Considere processamento paralelo

### 4. Monitoramento
- Implemente logs detalhados
- Configure alertas de falha
- Monitore tempo de execução

### 5. Manutenibilidade
- Código modular e reutilizável
- Documentação clara
- Controle de versão (Git)

### 6. Segurança
- Não exponha credenciais no código
- Use variáveis de ambiente
- Implemente controle de acesso

---

## Recursos Adicionais

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Luigi Documentation](https://luigi.readthedocs.io)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Apache Hadoop](https://hadoop.apache.org/)
- [Apache Spark](https://spark.apache.org/)
---

## Recursos Adicionais

-   [Documentação Oficial do Python](https://docs.python.org/pt-br/3/)
-   [DIO - Digital Innovation One](https://www.dio.me/)
