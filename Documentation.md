# Projeto Python: Gerenciador de Finanças Pessoais no Terminal

26/09/2026

## Visão geral

Você vai construir, em 8 ciclos de 2 dias (16 dias), um gerenciador de finanças pessoais que roda no terminal: registra receitas e despesas, salva em arquivo, gera relatórios e exporta dados. É um problema real, pequeno o bastante para caber em 16 dias e grande o bastante para exigir organização de código.

O projeto cobre os fundamentos do roadmap.sh/python na prática: sintaxe básica, tipos, condicionais, laços, funções, estruturas de dados (listas e dicionários), exceções, arquivos, módulos, classes simples e testes.

**Regras do projeto**

- Só Python e a biblioteca padrão. Nada de `pip install`.
- Sem LLMs: nada de ChatGPT, Claude, Copilot, nem o resumo de IA do Google (veja como desligar na seção de fontes).
- Cada ciclo termina com o programa funcionando e a funcionalidade nova entregue, mesmo que simples.
- Copiar código de fórum é permitido só se você conseguir explicar cada linha. Se não conseguir, reescreva do seu jeito.

**O modelo de dados** (o formato é decisão sua, mas este é um bom ponto de partida): cada transação é um dicionário com `id`, `tipo` ("receita" ou "despesa"), `valor`, `categoria`, `descricao` e `data`.

## Como funciona cada ciclo

Dia 1 é para estudar os conceitos do ciclo e fazer a parte principal da funcionalidade. Dia 2 é para terminar, testar à mão, corrigir bugs e documentar. O desafio extra só entra se sobrar tempo; ele não bloqueia o próximo ciclo.

**Rotina no GitHub**

- Crie o repositório `financas-terminal` com um `README.md` e um `.gitignore` para Python (o GitHub oferece um pronto na criação).
- Faça commits pequenos, um por pedaço que funciona (ex.: `adiciona validação de valor`), não um commitão no fim do dia.
- No fim de cada ciclo, marque a entrega com uma tag: `git tag ciclo-01` e `git push --tags`. Assim dá para comparar o código entre ciclos.
- Mantenha no README um diário de ciclos com três linhas por ciclo: o que foi entregue, onde travou, o que aprendeu. Esse registro é o que me permite acompanhar e dar feedback útil.

Se um ciclo estourar o prazo, não pule: termine o critério de pronto e só então avance. Atraso é informação, anote no diário.

## Os 8 ciclos

Cada ciclo lista a entrega, os conceitos que ela exige, o critério de pronto (marque os itens conforme concluir) e um desafio extra opcional.

### Ciclo 1 (dias 1–2): menu e cadastro em memória

**Entrega:** um menu em loop com as opções adicionar transação, listar transações e sair. Os dados vivem numa lista enquanto o programa roda.

**Conceitos:** variáveis, tipos (`int`, `float`, `str`, `bool`), `input()` e conversão de tipos, `if/elif/else`, `while`, listas, dicionários, `print()` com f-strings.

- [ ] O menu volta a aparecer após cada ação até o usuário escolher sair
- [ ] Uma transação tem tipo, valor, categoria e descrição
- [ ] Listar mostra todas as transações cadastradas, uma por linha
- [ ] Opção inválida no menu mostra uma mensagem, sem encerrar o programa

**Desafio extra:** mostrar uma mensagem diferente quando a lista estiver vazia.

### Ciclo 2 (dias 3–4): funções e validação de entrada

**Entrega:** o código reorganizado em funções, com entradas validadas. Digitar `abc` no valor ou uma data inválida não derruba mais o programa.

**Conceitos:** `def`, parâmetros, `return`, escopo de variáveis, `try/except` (`ValueError`), módulo `datetime` para ler e validar datas, formatação de números (`f"{valor:.2f}"`).

- [ ] Existe uma função por ação do menu (ex.: `adicionar_transacao`, `listar_transacoes`)
- [ ] Valor precisa ser número positivo; o programa pergunta de novo até receber um válido
- [ ] Data no formato DD/MM/AAAA, validada com `datetime.strptime`; vazio assume a data de hoje
- [ ] Tipo aceita só receita ou despesa
- [ ] A listagem sai alinhada em colunas, com valores em R$ e duas casas decimais

**Desafio extra:** uma função genérica `perguntar_numero(mensagem)` reutilizada em todo lugar que pede número.

### Ciclo 3 (dias 5–6): persistência em arquivo JSON

**Entrega:** as transações são salvas num arquivo `transacoes.json` e carregadas ao abrir o programa. Fechar e reabrir não perde nada.

**Conceitos:** `open()` e o gerenciador de contexto `with`, módulo `json` (`dump`, `load`), `pathlib.Path`, tratamento de `FileNotFoundError` e `json.JSONDecodeError`, por que datas precisam virar texto para ir ao JSON.

- [ ] Primeira execução, sem arquivo, funciona normalmente
- [ ] Cada transação nova é salva no arquivo
- [ ] Arquivo corrompido gera um aviso claro, não um traceback
- [ ] Cada transação ganha um `id` único e crescente

**Desafio extra:** antes de sobrescrever, criar uma cópia `transacoes.json.bak`.

### Ciclo 4 (dias 7–8): saldo e resumo por categoria

**Entrega:** uma opção de resumo que mostra total de receitas, total de despesas, saldo e gasto por categoria, do maior para o menor.

**Conceitos:** acumuladores, `sum()` com expressões geradoras, list comprehensions, agrupamento com dicionário (`dict.get` ou `collections.defaultdict`), `sorted()` com `key` e `lambda`. Também o problema do `float` com dinheiro: rode `0.1 + 0.2` e entenda o resultado.

- [ ] Saldo = receitas − despesas, correto conferido à mão com 5 transações
- [ ] Gastos por categoria aparecem ordenados do maior para o menor
- [ ] Cada categoria mostra o percentual do total de despesas

**Desafio extra:** trocar `float` por `decimal.Decimal` em todo o projeto e ver o que muda na leitura e gravação do JSON.

### Ciclo 5 (dias 9–10): buscar, filtrar, editar e excluir

**Entrega:** filtrar transações por mês, por categoria ou por palavra na descrição; editar ou excluir uma transação pelo `id`.

**Conceitos:** métodos de string (`lower`, `strip`, `in`, `split`), comparação de datas, busca em lista, remover itens de uma lista com segurança (por que não remover enquanto se percorre com `for`), confirmação antes de ações destrutivas.

- [ ] Busca ignora maiúsculas e minúsculas
- [ ] Filtro por mês aceita MM/AAAA
- [ ] Editar permite manter um campo apertando Enter
- [ ] Excluir pede confirmação; `id` inexistente gera mensagem clara
- [ ] Toda alteração é salva no arquivo

**Desafio extra:** combinar filtros (ex.: categoria Mercado em 09/2026).

### Ciclo 6 (dias 11–12): módulos e uma classe

**Entrega:** o mesmo programa, agora dividido em arquivos, com a transação representada por uma classe. Nada muda para o usuário; muda a organização.

**Conceitos:** módulos e `import`, `if __name__ == "__main__":`, classes (`__init__`, atributos, métodos, `__str__`), `dataclasses.dataclass`, type hints básicos, separação de responsabilidades.

Estrutura sugerida: `main.py` (menu), `modelos.py` (classe `Transacao`), `armazenamento.py` (JSON), `relatorios.py` (cálculos).

- [ ] `main.py` só cuida do menu e chama funções dos outros módulos
- [ ] Os cálculos de `relatorios.py` não usam `input()` nem `print()`: recebem dados e devolvem resultados
- [ ] Transacao tem métodos `para_dict()` e `de_dict()` para converter de e para JSON
- [ ] Todas as funcionalidades dos ciclos anteriores continuam funcionando

**Desafio extra:** adicionar type hints em todas as funções e rodar `python -m py_compile *.py` para checar a sintaxe.

### Ciclo 7 (dias 13–14): relatório mensal, orçamento e CSV

**Entrega:** um relatório mensal com gráfico de barras em texto, limite de orçamento por categoria com alerta, e exportação/importação em CSV (abre no Excel ou LibreOffice).

**Conceitos:** módulo `csv` (`DictWriter`, `DictReader`), multiplicação de strings para desenhar barras (`"#" * n`), escala proporcional, encoding (`utf-8`) e separador `;` para o Excel brasileiro.

- [ ] Relatório do mês mostra uma barra por categoria, proporcional ao gasto
- [ ] Usuário define limite por categoria; ao adicionar despesa que estoura o limite, aparece um alerta
- [ ] Exportar gera um CSV que abre certo numa planilha, com acentos corretos
- [ ] Importar lê um CSV e ignora linhas inválidas, informando quantas foram ignoradas

**Desafio extra:** comparar o mês atual com o anterior, mostrando a variação por categoria.

### Ciclo 8 (dias 15–16): testes e linha de comando

**Entrega:** testes automatizados para as funções de cálculo e validação, e comandos rápidos pelo terminal sem abrir o menu, como `python main.py saldo` ou `python main.py add despesa 45.90 Mercado`.

**Conceitos:** `unittest` (casos de teste, `assertEqual`, `assertRaises`), por que funções puras são fáceis de testar, `argparse` (subcomandos, argumentos, `--help`), `sys.exit` com código de saída.

- [ ] Pelo menos 10 testes, cobrindo saldo, agrupamento por categoria, filtros e validação
- [ ] `python -m unittest` roda tudo e passa
- [ ] Sem argumentos, o programa abre o menu; com argumentos, executa o comando e sai
- [ ] `python main.py --help` explica os comandos
- [ ] README final explica como instalar, rodar e testar

**Desafio extra:** escrever um teste que falha de propósito antes de corrigir um bug (o ciclo básico do TDD).

## Onde buscar informação

Comece sempre pelo próprio Python e pela documentação oficial; fórum e artigo vêm depois. Isso treina a habilidade que mais importa: ler documentação.

| Fonte | Quando usar |
| --- | --- |
| `help()` e `dir()` no terminal interativo | Primeiro passo para qualquer dúvida sobre uma função ou objeto: `help(str.split)`, `dir(list)` |
| [Tutorial oficial em português](https://docs.python.org/pt-br/3/tutorial/) | Conceitos da linguagem: funções, estruturas de dados, exceções, classes, módulos |
| [Referência da biblioteca padrão](https://docs.python.org/3/library/) | Detalhes de `json`, `csv`, `datetime`, `pathlib`, `argparse`, `unittest`; cada página tem exemplos no fim |
| [Python Tutor](https://pythontutor.com/) | Visualizar o código rodando linha a linha, ótimo para entender laços e listas |
| [Stack Overflow em português](https://pt.stackoverflow.com/) e [em inglês](https://stackoverflow.com/) | Erros específicos: cole a última linha do traceback na busca |
| [Real Python](https://realpython.com/) | Artigos aprofundados, em inglês, sobre um tema (ex.: "python json", "python dataclasses") |
| [Automate the Boring Stuff](https://automatetheboringstuff.com/) | Livro gratuito online, bom para arquivos, CSV e manipulação de texto |
| [PEP 8](https://peps.python.org/pep-0008/) | Estilo: nomes de variáveis, espaçamento, organização de imports |
| Os links de cada tópico no roadmap.sh | Quando o ciclo toca um item do roadmap |

**Evitando IA sem querer:** o Google mostra resumos gerados por IA no topo. Use a aba "Web" nos resultados, ou adicione `&udm=14` ao fim da URL da busca, para ver só links. No DuckDuckGo, dá para desligar as respostas de IA nas configurações. Desative também o autocompletar de IA do seu editor (Copilot, extensões similares).

## Quando travar

Travar faz parte do treino. Siga esta ordem antes de buscar a resposta pronta:

1. **Leia o traceback de baixo para cima.** A última linha diz o tipo do erro (`KeyError`, `TypeError`); as linhas acima dizem em que arquivo e linha ele aconteceu.
2. **Descreva o problema em português antes do código.** Escreva em comentário os passos que o programa precisa fazer. Se você não consegue descrever, o problema é de lógica, não de Python.
3. **Reduza.** Isole o trecho num arquivo separado ou no terminal interativo, com dados fixos, até o erro aparecer em poucas linhas.
4. **Inspecione.** Use `print()` com os valores e tipos (`print(type(x), x)`) ou coloque `breakpoint()` na linha e execute passo a passo (comandos `n`, `s`, `p variavel`, `c`).
5. **Explique em voz alta** o que cada linha faz. Muitas vezes o erro aparece no meio da explicação.
6. **Só então pesquise**, com a mensagem de erro exata e o nome do módulo.

Regra de tempo: 30 minutos tentando sozinho antes de pesquisar. Depois de 1 hora sem avanço, anote a dúvida no diário e siga para outra parte do ciclo; voltar descansado resolve mais do que insistir.

## Ponto de chegada

Ao fim dos 16 dias, você terá um programa completo no GitHub e deve conseguir fazer cada item abaixo sem consultar o próprio código. Item que você não consegue explicar é a lacuna a revisar.

- [ ] Explicar a diferença entre `list`, `dict`, `tuple` e `set`, e quando usar cada um
- [ ] Escrever funções com parâmetros e retorno, e explicar por que uma função pura é mais fácil de testar
- [ ] Tratar erros de entrada com `try/except` sem esconder erros de verdade
- [ ] Ler e gravar JSON e CSV, e explicar para que serve o `with`
- [ ] Agrupar, filtrar e ordenar dados usando dicionários, comprehensions e `sorted`
- [ ] Explicar por que `float` é ruim para dinheiro
- [ ] Dividir um programa em módulos e explicar o que faz `if __name__ == "__main__"`
- [ ] Criar uma classe simples e converter objetos de e para dicionário
- [ ] Escrever e rodar testes com `unittest`
- [ ] Ler um traceback e chegar à linha do problema
- [ ] Encontrar a resposta de uma dúvida na documentação oficial

Fica de fora de propósito, para projetos seguintes: bancos de dados, bibliotecas externas, ambientes virtuais e interfaces gráficas.