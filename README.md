# Sistema de Locadora de Veículos

Projeto desenvolvido em **Python** com o objetivo de aplicar os principais conceitos de **Programação Orientada a Objetos (POO)**.

O sistema simula uma locadora de veículos e permite cadastrar, listar, alugar e devolver veículos.

## Integrantes

- Izabelle
- Kayo
- João Victor

## Funcionalidades

O sistema possui as seguintes opções:

1. Cadastrar veículo
2. Listar veículos
3. Alugar veículo
4. Devolver veículo
0. Sair do sistema

O menu permanece em execução até que o usuário escolha a opção `0`.

## Tipos de veículos

O sistema trabalha com dois tipos de veículos:

### Carro

Possui:

- Modelo
- Placa
- Valor da diária
- Quantidade de portas
- Disponibilidade

O valor do aluguel é calculado da seguinte forma:

```text
valor da diária × quantidade de dias
```

### Moto

Possui:

- Modelo
- Placa
- Valor da diária
- Cilindradas
- Disponibilidade

Para motos, é aplicado um desconto de **10%** sobre o valor total do aluguel.

```text
(valor da diária × quantidade de dias) - 10%
```

## Conceitos de Programação Orientada a Objetos

O projeto utiliza os principais conceitos de POO.

### Classes

Foram criadas três classes principais:

```text
Veiculo
├── Carro
└── Moto
```

A classe `Veiculo` representa as características comuns dos veículos.

As classes `Carro` e `Moto` herdam características e comportamentos da classe `Veiculo`.

### Objetos e instâncias

Cada veículo cadastrado no sistema é criado como um novo objeto.

Exemplo:

```python
carro = Carro(modelo, placa, valor_diaria, quantidade_portas)
```

Os objetos criados são armazenados em uma lista.

```python
veiculos = []
```

### Atributos

Alguns dos atributos utilizados são:

- `modelo`
- `placa`
- `valor_diaria`
- `disponivel`
- `quantidade_portas`
- `cilindradas`

### Métodos

Entre os principais métodos do sistema estão:

```python
alugar()
devolver()
calcular_aluguel()
exibir_informacoes()
```

### Herança

As classes `Carro` e `Moto` herdam da classe `Veiculo`.

```python
class Carro(Veiculo):
```

```python
class Moto(Veiculo):
```

Dessa forma, características comuns não precisam ser implementadas novamente.

### Encapsulamento

A disponibilidade do veículo é controlada pela própria classe.

O atributo é definido como privado:

```python
self.__disponivel
```

A situação do veículo é modificada através dos métodos:

```python
alugar()
devolver()
```

Assim, o programa não altera diretamente a disponibilidade do veículo.

### Polimorfismo

O método:

```python
calcular_aluguel()
```

existe tanto em `Carro` quanto em `Moto`, porém possui comportamentos diferentes.

No carro, o cálculo é:

```text
diária × dias
```

Na moto, é aplicado um desconto de 10%.

## Estrutura do programa

O programa utiliza funções para organizar as operações do menu:

```python
cadastrar_veiculo()
listar_veiculos()
buscar_veiculo()
alugar_veiculo()
devolver_veiculo()
menu()
```

## Exemplo do menu

```text
===== LOCADORA DE VEÍCULOS =====
1 - Cadastrar veículo
2 - Listar veículos
3 - Alugar veículo
4 - Devolver veículo
0 - Sair
```

## Exemplo de cadastro

```text
===== CADASTRO DE VEÍCULO =====
1 - Carro
2 - Moto

Escolha o tipo de veículo: 1
Modelo: Corolla
Placa: ABC1234
Valor da diária: R$ 180
Quantidade de portas: 4

Carro cadastrado com sucesso.
```

## Exemplo de aluguel

```text
Placa do veículo: ABC1234
Quantidade de dias: 3

Veículo: Corolla
Quantidade de dias: 3
Valor do aluguel: R$ 540.00
Veículo alugado com sucesso.
```

## Tecnologias utilizadas

- Python 3
- Programação Orientada a Objetos

## Como executar

1. Tenha o Python instalado no computador.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

```bash
python main.py
```

## Objetivo acadêmico

O objetivo deste projeto é demonstrar, de forma prática, os conceitos de:

- Classes
- Objetos
- Instâncias
- Atributos
- Métodos
- Abstração
- Encapsulamento
- Herança
- Polimorfismo
- Estruturas condicionais
- Estruturas de repetição

## Conclusão

O projeto demonstra a aplicação dos principais conceitos de Programação Orientada a Objetos em Python através de um sistema simples de locadora de veículos.

A utilização de classes, herança, encapsulamento e polimorfismo permite organizar melhor o código e representar diferentes tipos de veículos de forma estruturada.