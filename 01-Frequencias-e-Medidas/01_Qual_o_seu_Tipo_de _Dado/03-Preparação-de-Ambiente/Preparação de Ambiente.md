# Transcrição

Antes de começarmos o conteúdo do curso de fato, falaremos sobre a ferramenta que usaremos neste treinamento.

Usaremos o Google Colab acessível neste link. Logo no começo, teremos uma introdução explicativa e algumas dicas interessantes.

É bastante parecido com o **Anaconda** ou **Jupyter Notebook**, mas com esta ferramenta não precisaremos nos preocupar muito com instalações, a não ser que usemos uma versão específica como a que veremos adiante.

Já será possível criarmos um "New Python 3 notebook" clicando em "File" na barra de opções, onde poderemos digitar comandos ou operações, e executá-los com as teclas "Shift + Enter" da mesma maneira feita no Jupyter.

Pode ser que a execução seja um pouco mais lenta, visto que é um recurso online.

No passo anterior, disponibilizamos um link para download de nosso projeto inicial, o qual pode ser acessado na pasta 02.

Quando já estiver baixado e salvo, acessaremos "File > Upload notebook...", e abriremos o notebook `Verifica_versão.ipynb` caso seja necessário para compararmos a versão desta aula com a que será feita o exercício.

Neste arquivo, importaremos as bibliotecas pandas, `numpy, seaborn e scipy`, pois as usaremos neste treinamento. Em seguida, imprimiremos as versões que estão sendo utilizadas.

```python
    print('Versão do pandas -> %s' % pandas.__version__)
    print('Versão do numpy -> %s' % numpy.__version__)
    print('Versão do seaborn -> %s' % seaborn.__version__)
    print('Versão do scipy -> %s' % scipy.__version__)
```

A execução das importações pode demorar um pouco. Depois das execuções, veremos que a versão do `pandas, numpy, seaborn` e `scipy` são respectivamente `0.22.0`, `1.14.6`, `0.7.1` e `1.1.0` até esta aula.

Caso o exercício seja feito em uma versão diferente, pode ser que funcione sem problemas. Mas se apresentar alguma questão, é possível voltar para estas versões citadas e tentar rodar novamente.

Para voltarmos com o Pandas por exemplo, bastará digitarmos `!pip install pandas` seguido de `==` com a versão desejada entre aspas simples na célula seguinte.
```python
    !pip install pandas=='0.22.0'
```

O sistema rodará o comando e pedirá para reiniciarmos a execução por meio do botão "Restart Runtime" que aparecerá ao final do resultado, então clicaremos neste e em "Yes" na mensagem de confirmação.

Na mesma barra de ferramentas de edição, veremos o escrito "initializing" para indicar o reinício do Runtime. Terminado o processo, rodaremos as células anteriores novamente para vermos se a versão foi alterada na impressão.

Caso usemos sempre um notebook e precisemos retornar para versões anteriores, é interessante executarmos estes comandos logo na primeira célula antes de qualquer outro código. Após o restart, poderemos até apagar o que estava antes da mudança, para então seguirmos adiante com a versão setada para o trabalho.

Em algumas situações, a reinicialização poderá ser necessária de novo. Para este efeito, acessaremos "Runtime > Reset all runtimes..." ou "Runtime > Restart runtime..." que pode ser acionado com teclas "Ctrl + M".

Se tivermos feito o upload de algum arquivo, o comando "Reset all runtimes..." apagará todos os arquivos da memória, então teremos que fazer o upload deles novamente.

Estes macetes serão vistos ao longo do curso, e com o tempo estaremos familiarizados com seu funcionamento.

A seguir, começaremos com a prática e iniciaremos o treinamento de fato.

Até lá!