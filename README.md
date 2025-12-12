# DIO-Python-Bootcamp 🐍

---

## 📌 Conhecendo a Linguagem

### 📋 Tipos de Dados em Python

Python oferece uma rica variedade de tipos de dados nativos para diferentes necessidades de programação.

#### 📝 Texto
- **`str`** (String) - Representa textos e caracteres
  ```python
  "Hello, World!"
  'Python'
  """Texto multilinha"""
  ```

#### 🔢 Numéricos
- **`int`** (Integer) - Números inteiros
  ```python
  42
  -17
  0
  ```
- **`float`** (Float) - Números decimais
  ```python
  3.14
  -0.001
  2.0
  ```
- **`complex`** (Complex) - Números complexos
  ```python
  3+4j
  2.5-1.5j
  ```

#### 📚 Sequências
- **`list`** (Lista) - Coleção ordenada e mutável
  ```python
  [1, 2, 3]
  ["a", "b", "c"]
  ```
- **`tuple`** (Tupla) - Coleção ordenada e imutável
  ```python
  (1, 2, 3)
  ("x", "y", "z")
  ```
- **`range`** (Range) - Sequência de números
  ```python
  range(0, 10)
  range(5)
  ```

#### 🗺️ Mapeamento
- **`dict`** (Dictionary) - Estrutura de chave-valor
  ```python
  {"nome": "João", "idade": 25}
  ```

#### 🎯 Coleções
- **`set`** (Set) - Coleção não ordenada de elementos únicos (mutável)
  ```python
  {1, 2, 3}
  {"a", "b", "c"}
  ```
- **`frozenset`** (Frozenset) - Set imutável
  ```python
  frozenset([1, 2, 3])
  ```

#### ✅ Booleano
- **`bool`** (Boolean) - Valores lógicos
  ```python
  True
  False
  ```

#### 💾 Binários
- **`bytes`** (Bytes) - Sequência imutável de bytes
  ```python
  b"Hello"
  bytes([65, 66, 67])
  ```
- **`bytearray`** (Bytearray) - Sequência mutável de bytes
  ```python
  bytearray(b"Hello")
  ```
- **`memoryview`** (Memoryview) - Visualização de memória de objetos binários
  ```python
  memoryview(bytes(5))
  ```

---

### 💬 Comentários em Python

Comentários são usados para explicar o código e são ignorados pelo interpretador.

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

Os comentários facilitam a leitura, manutenção e documentação do código.

---

### 🖥️ Interpretador Python no Terminal

Ao digitar `python` no terminal, você inicia o interpretador interativo do Python.

```bash
$ python
>>> print("Olá, Mundo!")
Olá, Mundo!
```

Você pode executar um script e manter o interpretador aberto com a flag `-i`:
```bash
$ python -i app.py
```

**Para sair do interpretador:**
- `exit()` ou `quit()`
- `Ctrl+D` (Linux/Mac)
- `Ctrl+Z` + Enter (Windows)

#### Função `dir()`
Retorna uma lista de atributos e métodos disponíveis.

```python
dir()           # Lista nomes no escopo atual
dir(100)        # Lista métodos disponíveis para inteiros
dir("texto")    # Lista métodos disponíveis para strings
```

#### Função `help()`
Invoca o sistema de ajuda integrado do Python.

```python
help()          # Modo interativo
help(print)     # Ajuda sobre a função print
help(str)       # Ajuda sobre strings
```

---

### 📦 Variáveis e Constantes

#### Variáveis (Mutáveis)

```python
idade = 24
nome = 'Carlos'
print(f'Meu nome é {nome} e eu tenho {idade} anos.')

# Declaração múltipla
idade2, nome2 = (30, 'Ana')
print(f'Meu nome é {nome2} e eu tenho {idade2} anos.')
```

O Python define automaticamente o tipo de dados! Não é possível criar uma variável sem atribuir um valor inicial.

#### Constantes (Imutáveis)

Em Python, constantes são escritas em MAIÚSCULAS por convenção.

```python
PI = 3.14159
raio = 5
area = PI * (raio ** 2)
print(f'A área do círculo com raio {raio} é {area}.')
```

#### 📌 Boas Práticas

- Use **snake_case** para nomes de variáveis: `minha_variavel`
- Use **SNAKE_CASE** para constantes: `MINHA_CONSTANTE`
- Escolha nomes descritivos e claros

#### ⚠️ Atenção

```python
print(5 / 2)   # 2.5 (divisão normal)
print(5 // 2)  # 2 (divisão inteira, ignora decimais)
```

---

### 🔄 Conversão de Tipos

#### Inteiro para Float
```python
preco = 10
print(preco)          # 10

preco = float(preco)
print(preco)          # 10.0

preco = 10 / 2
print(preco)          # 5.0
```

#### Numérico para String
```python
preco = 19.90
print(str(preco))     # '19.9'

idade = 30
print(str(idade))     # '30'

texto = f"Idade: {idade} Preço: {preco}"
print(texto)          # 'Idade: 30 Preço: 19.9'
```

#### String para Numérico
```python
preco = "19.90"
print(float(preco))   # 19.9

idade = "30"
print(int(idade))     # 30
```

---

### ⌨️ Funções de Entrada e Saída

#### Lendo valores com `input()`

```python
# Solicitando nome
nome = input("Por favor, insira seu nome: ")
print("Olá, " + nome + "!")

# Solicitando idade
idade = input("Por favor, insira sua idade: ")
print("Você tem " + idade + " anos.")
```

**Importante:** `input()` sempre retorna uma string! Para usar como número, faça a conversão:

```python
idade = int(input("Digite sua idade: "))
preco = float(input("Digite o preço: "))
```

#### Manipulação do `print()`

```python
nome = 'Carlos'
sobrenome = 'Rocha'

print(nome, sobrenome)                    # Carlos Rocha
print(nome, sobrenome, end="...\n")      # Carlos Rocha...
print(nome, sobrenome, sep="#")          # Carlos#Rocha
```

**Parâmetros úteis:**
- `sep` - Define o separador entre os valores (padrão: espaço)
- `end` - Define o que vem no final (padrão: `\n` quebra de linha)

---

## 📖 Recursos Adicionais

- [Documentação Oficial do Python](https://docs.python.org/pt-br/3/)
- [DIO - Digital Innovation One](https://www.dio.me/)

---