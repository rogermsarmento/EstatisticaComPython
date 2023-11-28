# Média ou mediana? 
## Entendendo Cada Uma

Estava fazendo uma análise das notas dos alunos. Queremos ver como a abordagem de ensino está influenciando as notas dos alunos. Portanto, vamos analisar as notas de antes e depois da mudança.

Para fazer essa análise, vamos analisar as notas de uma turma com 21 alunos.
```Python
6.0, 7.1, 5.5, 3.0, 10.0, 100.0, 6.5, 8.2, 2.9, 3.5, 9.9, 
9.1, 8.2, 7.6, 9.9, 10.0, 6.7, 4.9, 10.0, 6.8, 6.0
```

O quão bem foi a turma? Isto é, qual a média de notas da turma?

Podemos tirar uma média aritmética simples. Ou seja, somar todas as notas e dividir pelo número de alunos. Logo teremos:
```Python
(6.0 + 7.1 + 5.5 + … + 6.0) / 21
```
O resultado desse cálculo é **11.51**, aproximadamente. As notas são de 0 a 10, então, por que nossa média é **11**?

## Entendendo a Média
A média é influenciada por todos os valores da amostra. Ou seja, se tivermos valores muito discrepantes, o valor da média é alterado.

Por exemplo, na nossa amostra de notas, temos uma nota com o valor 100.0. Por isso a média está com um valor não tão usual. Esses valores muito discrepantes, tanto maiores quanto menores, são conhecidos como outliers.

Existem muitas maneiras de tratar outliers. Uma delas é remover o outlier. Em amostras com um grande número de dados isso não tem tantos problemas, já em uma amostra com pouco dados, como a nossa, retirar um outlier pode causar muito impacto. Então como podemos resolver esse problema?

Uma forma é checar se aquele dado da amostra está correto. Outra forma é substituir esse valor pelo valor que mais se repete na amostra, ou então pelo valor da mediana. Mas o que é a mediana?

## Conhecendo a Mediana
A mediana é o valor que está no meio da amostra. Ou seja, ela divide a amostra em duas partes, onde metade está acima e metade abaixo. De que forma podemos calcular a mediana?

Uma forma de calcular a mediana é ordenando todos os nossos dados:
```Python
2.9, 3.0, 3.5, 4.9, 5.5, 6.0, 6.0, 6.5, 6.7, 6.8,
7.1, 7.6, 8.2, 8.2, 9.1, 9.9, 9.9, 10.0, 10.0, 10.0, 100.0
```

Agora que ordenamos os dados, precisamos saber qual o dado que está no meio da nossa amostra. Isto é, no nossa caso temos 21 elementos na amostra. Como é um número ímpar, basta somar 1 a este valor e dividir por 2.

Logo, temos a fórmula `(numero_de_elementos + 1) / 2`. Fazendo a conta, veremos que o valor do resultado é 11. Portanto, o nosso elemento mediano está na posição número 11.

```Python
---------------------
|Posição | Elemento |
|-------------------|
|1       | 2.9      | 
|-------------------|
|2       | 3.0      |
|-------------------|
|.       | .        |
|.       | .        |
|.       | .        |
|-------------------|
|11      | 7.1      |
---------------------
```
A nossa nota mediana é 7.1. Isso significa que metade dos nossos dados estão abaixo de 7.1 e metade dos dados estão acima.

Agora que temos a mediana, podemos substituir o outlier com o seu valor. Quando substituirmos e calcularmos a nova média, veremos que seu valor mudou para 7.09. E, calculando a mediana novamente, ela se mantém em 7.1, **mas isso não é uma regra**.

A mediana é o elemento do meio. Ela divide nossos dados em duas partes. No nosso caso, nossa amostra contém um conjunto de dados com um valor ímpar. Mas e se tivéssemos um valor par? **Como é calculada a mediana nesse caso?**

## Amostra com valores pares
Para uma amostra com um número par de valores, temos que realizar um passo parecido, porém, ao invés de pegar o valor central, pegamos os dois valores que estão no centro. Então nossa amostra terá duas medianas?

Com esses dois valores nós podemos calcular sua média. Essa média dos valores centrais é a mediana da amostra.

Por exemplo, vamos imaginar que temos a seguinte amostra; `1, 2, 5, 7, 9, 11`. Precisamos dos dois valores centrais. Para isso, podemos utilizar a fórmula `numero_de_elementos / 2` e `(numero_de_elementos / 2) + 1`.

Ou seja, temos seis elementos. Logo, as fórmulas ficam `6 / 2` e `(6 / 2) + 1`. Com isso temos como resultado 3 e 4. Portanto, os nossos elementos centrais são o terceiro (5) e quarto (7) elemento.

Realizando o cálculo de média entre eles, obteremos o valor de 6. Ou seja, nessa amostra nossa mediana vale 6.

## Para Saber Mais
Além da média `aritmética` que realizamos, existem outras médias. Como, por exemplo, as médias `geométrica` e `harmônica`.

Basicamente, a média geométrica vai medir a proporção média de um elemento em relação ao outro. Já a média harmônica mede a razão entre os elementos.

Pelo fato da média ser muito influenciada por outliers, geralmente é comum utilizar a mediana para fazer comparações entre amostras.

Além da média e da mediana, temos também a moda. A moda é o valor que mais se repete na amostra. Podemos ter distribuições com um valor modal (unimodal), dois valores (bimodal) e com muitos valores (multimodal). Há também a média ponderada. **Média**, **Mediana** e **Moda** são medidas estatísticas muito utilizadas quando estamos fazendo análise de dados. A

