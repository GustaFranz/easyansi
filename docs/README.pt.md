<p align="center">
  <a href="../README.md"><img src="https://img.shields.io/badge/lang-English-blue?style=for-the-badge" alt="English"></a>
  <a href="README.pt.md"><img src="https://img.shields.io/badge/lang-Português-green?style=for-the-badge" alt="Português"></a>
  <a href="README.es.md"><img src="https://img.shields.io/badge/lang-Español-orange?style=for-the-badge" alt="Español"></a>
  <a href="README.zh.md"><img src="https://img.shields.io/badge/lang-中文-red?style=for-the-badge" alt="中文"></a>
</p>

<h1 align="center">EasyAnsi</h1>

<p align="center">
  <strong>A forma fácil e prática de colorir texto no terminal.</strong><br>
  Comandos simples. Zero configuração. Escreva cor dentro da string como numa f-string.<br>
  Zero dependências · Fail-safe · Feita para iniciantes e scripts do dia a dia.
</p>

<p align="center">
  <a href="https://pypi.org/project/easyansi/"><img src="https://img.shields.io/pypi/v/easyansi?label=PyPI&color=blue" alt="Versão PyPI"></a>
  <a href="../LICENSE"><img src="https://img.shields.io/badge/licença-MIT-green" alt="Licença MIT"></a>
  <img src="https://img.shields.io/badge/python-%3E%3D3.8-blue" alt="Python >= 3.8">
  <img src="https://img.shields.io/badge/dependências-zero-brightgreen" alt="Zero dependências">
  <img src="https://img.shields.io/badge/typing-typed-informational" alt="Typed">
</p>

---

## Visão geral

A **EasyAnsi** é uma biblioteca Python leve que transforma strings comuns em saída colorida no terminal usando uma sintaxe intuitiva inspirada em f-strings — não na sintaxe de colchetes do Rich.

Escreva cor diretamente dentro das suas strings:

```python
from easyansi import eprint

quantidade = 12
eprint(f"//bold-blue/Hoje todos os {quantidade} doces foram vendidos/bold-blue")
eprint(f"Sobrou //red/{quantidade}/red item no estoque")
```

Sem configuração. Sem objeto console pesado. Sem crash se uma tag estiver errada — nomes desconhecidos permanecem como texto puro.

---

## Por trás do projeto

Estou **aprendendo Python**. Ao estudar, percebi que colorir textos no terminal poderia ser muito mais simples do que encontrei nas bibliotecas existentes — e isso atrapalhava meu próprio aprendizado.

Sou **professor do Ensino Fundamental há 14 anos**. Na sala de aula, aprendi a enxergar o que facilita ou dificulta a prática do dia a dia: instruções claras, comandos fáceis de lembrar e ferramentas que não punem o erro. Foi com esse olhar que idealizei a EasyAnsi — não como especialista em programação, mas como alguém que se importa com **aprendizado, ensino e praticidade**.

**Transparência:** o código desta biblioteca foi elaborado com apoio de **inteligência artificial**. Prefiro dizer isso abertamente do que parecer que domino tudo o que está aqui. Ainda estou construindo minha capacidade técnica em Python — e esta biblioteca faz parte desse processo.

O que eu trago de fato é a experiência de quem ensina todos os dias: perceber barreiras desnecessárias, simplificar o caminho e pensar em quem está começando. A EasyAnsi nasce dessa combinação — a curiosidade de quem estuda, a sensibilidade de quem ensina e a honestidade sobre como foi construída.

### O que 14 anos de sala de aula me ensinaram sobre código

| Na sala de aula | Na EasyAnsi |
| --- | --- |
| Erro não pode paralisar o aprendizado | Tags desconhecidas viram texto normal — nunca quebram o programa |
| Instrução curta e objetiva | Sintaxe `//cor/` fácil de lembrar, como uma f-string |
| Ver antes de decorar | `preview()` mostra todas as cores no terminal |
| Ferramentas prontas para o dia a dia | `success()`, `error()`, `setup_logging()` — um comando e pronto |

Não sou impostor por usar IA: sou alguém em aprendizado que soube **identificar uma necessidade real** e buscar a forma honesta de torná-la real — com a mesma preocupação que tenho quando preparo uma aula para facilitar a vida dos meus alunos.

---

## Objetivo: ser mais fácil e prático

A EasyAnsi existe por um motivo: **tornar cores no terminal acessíveis para todos**, não só para especialistas.

| O que você precisa | EasyAnsi | Bibliotecas mais pesadas |
| --- | --- | --- |
| Começar em 30 segundos | `from easyansi import eprint` | Configurar Console, aprender regras de markup |
| Colorir uma palavra | `//red/{valor}/red` na f-string | Envolver objetos, montar segmentos Text |
| Dizer "sucesso" | `success("Pronto")` | Criar renderizáveis customizados |
| Ativar log colorido | `setup_logging()` — uma linha | Handlers, temas, plugins |
| Tag escrita errada | Vira texto normal (sem crash) | Pode gerar erro de markup |

**Filosofia:** menos conceitos, menos imports, comandos fáceis que você lembra e reutiliza todo dia.

---

## Comandos práticos (cola rápida)

Copie e use — sem configuração extra:

```python
from easyansi import eprint, einput, fmt, success, error, warning, info, red, green, bold, ansi, title, paint

# Imprimir com cor (o mais comum)
eprint("//green/Olá!/green")
eprint(f"Pontuação: //bold-blue/{pontos}/bold-blue")

# Texto inteiro de uma vez (sem tags inline)
print(ansi("Olá!").easyansi("bold-blue"))
print(paint("Olá!", "bold-blue"))

# Título decorativo
print(ansi("CADASTRO DE ALUNOS").title("="))

# Atalhos de uma palavra
print(red("erro"), green("ok"), bold("título"))
print(bold(red("crítico")))                       # encadeamento
print("//bg-yellow/aviso em amarelo/bg-yellow")   # com activate()

# Linhas de status (prontas)
success("Salvo")
error("Falhou")
warning("Conexão lenta")
info("Porta 8080")

# Input com prompt colorido
nome = einput("//cyan/Nome/cyan: ")

# Só a string (sem imprimir)
texto = fmt("//yellow/aviso/yellow")

# Ver todas as cores no terminal
import easyansi; easyansi.preview()
```

**Logging em uma linha:**

```python
from easyansi.logging import setup_logging
setup_logging()          # pronto — logging.info() já sai colorido
```

---

## Recursos

| Recurso | Descrição |
| --- | --- |
| **Sintaxe simples** | `//cor/texto/cor` — abre com `//nome/`, fecha com `/nome` ou `//` |
| **Colorir parcialmente** | Colore uma palavra dentro da f-string sem envolver a linha inteira |
| **Texto inteiro** | `ansi("texto").easyansi("bold-blue")` ou `paint("texto", "bold-blue")` |
| **Títulos decorativos** | `title("Título", "=")` ou `.title("=")` com cores de linha e texto |
| **Estilos + cores** | Combine com `-`: `bold-blue`, `italic-underline-red` |
| **Cores reais** | Suporte a hex: `//#ff8800/laranja/#ff8800` |
| **Fundos** | `bg-blue`, `bg-#222222` |
| **Nomes bilíngues** | Inglês + apelidos em português (`negrito`, `vermelho`, …) |
| **Atalhos diretos** | `red()`, `bold()`, `green()` — ótimo para autocomplete no editor |
| **Mensagens de status** | `success()`, `error()`, `warning()`, `info()` |
| **Logging colorido** | `ColorFormatter` plug-and-play para o módulo `logging` |
| **Parser fail-safe** | URLs como `https://` e tags desconhecidas nunca quebram a saída |
| **Saída inteligente** | Texto limpo automaticamente em pipe, redirecionamento ou `NO_COLOR` |
| **Windows pronto** | VT/ANSI habilitado automaticamente no import |
| **Zero deps** | Apenas stdlib — instala em qualquer lugar |

---

## Requisitos

- Python **3.8+**
- Terminal com suporte a códigos ANSI (habilitado automaticamente no Windows 10+)

---

## Instalação

```bash
pip install easyansi
```

A partir do código-fonte:

```bash
git clone https://github.com/seu-usuario/easyansi.git
cd easyansi
pip install -e ".[dev]"
```

---

## Comece em 1 minuto

**Recomendado — use `print` e `input` normais:**

```python
import easyansi

easyansi.activate()   # uma linha no inicio do script

print("//green/Tudo certo!/green")
print(f"Estoque: //red/{3}/red unidades restantes")
nome = input("Digite //cyan/seu nome/cyan: ")
```

Sem renomear funcoes. Use `easyansi.deactivate()` para restaurar os originais.

**Alternativa — `eprint` / `einput` explicitos:**

```python
from easyansi import eprint, einput, fmt

eprint("//green/Tudo certo!/green")
eprint("Estoque: //red/3/red unidades restantes")
nome = einput("Digite //cyan/seu nome/cyan: ")
mensagem = fmt("//yellow/aviso/yellow")
```

---

## Guia de sintaxe

### Abertura e fechamento

| Padrão | Significado | Exemplo |
| --- | --- | --- |
| `//nome/` | Abre tag | `//red/` |
| `/nome` | Fecha tag (explícito) | `/red` |
| `//` | Fecha a última tag aberta | `//green/texto//` |

### Combinar estilos e cores

Use `-` para empilhar atributos (exemplos assumem que `easyansi.activate()` foi chamado):

```python
print("//bold-blue/cabeçalho/bold-blue")
print("//italic-underline-magenta/destaque/italic-underline-magenta")
print("//bg-yellow/texto preto em fundo amarelo/bg-yellow")
print("//#ff8800/laranja exato/#ff8800")
```

### Funciona dentro de f-strings

```python
valor = 42
print(f"Resultado: //green/{valor}/green pontos")
```

### Escapar barras literais

```python
print(r"caminho: \/usr\/local/bin")
```

### Fail-safe por design

Somente nomes **conhecidos** de estilo/cor são interpretados. Todo o resto fica literal:

```python
print("Acesse https://exemplo.com/pagina")   # URL intacta
print("//erro/texto/erro")                    # tratado como texto puro
```

---

## Exemplos de personalização

Padrões do dia a dia para copiar e adaptar (com `activate()`):

```python
import easyansi
easyansi.activate()

# linha inteira
print("//green/Salvo com sucesso/green")

# só uma palavra
pontos = 10
print(f"Pontuação: //bold-blue/{pontos}/bold-blue pontos")

# estilo + cor combinados
print("//italic-underline-magenta/Nota importante/italic-underline-magenta")

# fundo e hex
print("//bg-yellow/preto em amarelo/bg-yellow")
print("//#ff8800/laranja exato/#ff8800")

# apelidos em português
print("//negrito-vermelho/Erro/negrito-vermelho")
```

---

## Texto inteiro e títulos decorativos

Colora uma string inteira sem tags inline ou monta títulos com linhas repetidas.

```python
from easyansi import ansi, title, paint, ask, activate

activate()

# Texto inteiro para print
print(ansi("Olá, mundo!").easyansi("bold-blue"))
print(paint("Olá", "bold-blue"))

# Escopos no input: pergunta, resposta ou ambos
nome = ansi("Qual é o seu nome?").easyansi("bold-blue", scope="prompt").read()
nome = ansi("Qual é o seu nome?").easyansi("green", scope="answer").read()
nome = ansi("Qual é o seu nome?").easyansi("bold-blue", scope="both").read()
nome = ask("Qual é o seu nome?", prompt_style="bold-blue", answer_style="green")

# Títulos decorativos
print(ansi("CADASTRO DE ALUNOS").title("="))
print(title("CADASTRO DE ALUNOS", "-", line_style="blue", text_style="bold"))
print(ansi("MENU").title("~", style="bold-blue"))
```

**Escopo (`scope`):** `text` (padrão) · `prompt` · `answer` · `both`

**Nota:** o terminal não colore em tempo real o que o usuário digita. Colorir a resposta aplica ANSI ao **valor retornado**, que aparece colorido ao imprimir depois.

---

## Referência da API

### Funções principais

| Função | Descrição |
| --- | --- |
| `activate()` | Faz `print` e `input` globais interpretarem a marcação EasyAnsi |
| `deactivate()` | Restaura `print` e `input` originais |
| `is_active()` | Indica se `activate()` está ativo |
| `fmt(texto, *, color=None)` | Retorna string formatada (ANSI ou limpa) |
| `eprint(*values, sep=" ", end="\n", file=None, color=None, flush=False)` | `print` colorido |
| `einput(prompt="", *, color=None)` | `input` colorido (aceita `str` ou `AnsiText`) |
| `preview(file=None)` | Imprime todos os estilos e cores disponíveis |
| `ansi(texto)` | Wrapper fluente para texto inteiro e títulos |
| `title(texto, char="=", ...)` | Título decorativo com linhas repetidas |
| `paint(texto, estilo, *, color=None)` | Aplica estilo ao texto inteiro (texto primeiro) |
| `ask(texto, *, prompt_style=None, answer_style=None)` | `input` colorido com escopos |

**Parâmetro `color`:** `None` = detecta terminal · `True` = força ANSI · `False` = texto limpo

### Atalhos de cor

`black` · `red` · `green` · `yellow` · `blue` · `magenta` · `cyan` · `white`

```python
from easyansi import red, green, yellow, blue, magenta, cyan, white, black

print(red("erro"), green("sucesso"), yellow("aviso"))
print(blue("info"), magenta("destaque"), cyan("prompt"), white("texto"))
print(black("texto escuro"))
```

### Atalhos de estilo

`bold` · `dim` · `italic` · `underline` · `strike` · `style(nome, texto)`

```python
from easyansi import bold, dim, italic, underline, strike, style, red

print(bold("título"), dim("secundário"), italic("nota"))
print(underline("link"), strike("removido"))
print(bold(red("crítico")))                      # encadeamento
print(style("bold-blue", "combo personalizado")) # qualquer nome via style()
```

Todos aceitam `color=None|True|False`.

### Mensagens de status

```python
from easyansi import success, error, warning, info

success("Deploy concluído")
error("Falha ao conectar")
warning("Cache desatualizado")
info("Rodando na porta 8000")
```

Os símbolos usam fallback ASCII (`[OK]`, `[ERRO]`) quando o terminal não suporta Unicode.

---

## Logging colorido

Integração com o módulo `logging` padrão do Python. Níveis são coloridos no terminal; a saída permanece limpa em arquivos e com `NO_COLOR`.

```python
import logging
from easyansi.logging import ColorFormatter, setup_logging

# Opção 1 — plugar no setup existente
handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter())
logging.root.addHandler(handler)
logging.info("Servidor iniciado")

# Opção 2 — configuração em uma linha
setup_logging(level=logging.INFO)
logging.warning("Cache desatualizado")
logging.error("Falha ao conectar")
```

**Cores padrão por nível:**

| Nível | Estilo |
| --- | --- |
| DEBUG | `dim` |
| INFO | `cyan` |
| WARNING | `yellow` |
| ERROR | `red` |
| CRITICAL | `bold-red` |

**Marcacao EasyAnsi nas mensagens de log:**

```python
setup_logging(markup=True, force=True)
logging.info("//green/Deploy concluído/green")
```

**Cores de nivel personalizadas (opcional):**

```python
import logging
from easyansi.logging import ColorFormatter, setup_logging

handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter(level_colors={
    logging.DEBUG: "dim",
    logging.INFO: "green",
    logging.WARNING: "yellow",
    logging.ERROR: "bold-red",
    logging.CRITICAL: "bold-red",
}))
logging.root.addHandler(handler)
```

**Parâmetros do `ColorFormatter`:** `fmt`, `datefmt`, `color`, `markup`, `level_colors`, `stream`

---

## Referência de estilos e cores

### Estilos de texto

| Inglês | Português | Tag | Amostra |
| --- | --- | --- | --- |
| Bold | Negrito | `bold` / `negrito` | <b>exemplo</b> |
| Dim | Fraco | `dim` / `fraco` | ![dim](https://placehold.co/15x15/888888/888888.png) exemplo |
| Italic | Itálico | `italic` / `italico` | <i>exemplo</i> |
| Underline | Sublinhado | `underline` / `sublinhado` | <u>exemplo</u> |
| Strikethrough | Tachado | `strike` / `tachado` | <s>exemplo</s> |

```python
print("//bold/Negrito/bold  //dim/Fraco/dim  //italic/Itálico/italic")
print("//underline/Sublinhado/underline  //strike/Tachado/strike")
```

### Cores nomeadas

| Inglês | Português | Tag | Amostra |
| --- | --- | --- | --- |
| Black | Preto | `black` / `preto` | ![preto](https://placehold.co/15x15/1e1e1e/1e1e1e.png) preto |
| Red | Vermelho | `red` / `vermelho` | ![vermelho](https://placehold.co/15x15/cd3131/cd3131.png) vermelho |
| Green | Verde | `green` / `verde` | ![verde](https://placehold.co/15x15/13a10e/13a10e.png) verde |
| Yellow | Amarelo | `yellow` / `amarelo` | ![amarelo](https://placehold.co/15x15/c19c00/c19c00.png) amarelo |
| Blue | Azul | `blue` / `azul` | ![azul](https://placehold.co/15x15/0451a5/0451a5.png) azul |
| Magenta | Rosa | `magenta` / `rosa` | ![rosa](https://placehold.co/15x15/bc3fbc/bc3fbc.png) rosa |
| Cyan | Ciano | `cyan` / `ciano` | ![ciano](https://placehold.co/15x15/059fc0/059fc0.png) ciano |
| White | Branco | `white` / `branco` | ![branco](https://placehold.co/15x15/e8e8e8/e8e8e8.png) branco |

```python
print("//red/vermelho  //green/verde  //yellow/amarelo  //blue/azul")
print("//magenta/rosa  //cyan/ciano  //white/branco  //black/preto")
```

### Variações

| Variação | Tag | Amostra |
| --- | --- | --- |
| Brilhante | `bright-red`, `claro-vermelho` | ![brilhante](https://placehold.co/15x15/ff5555/ff5555.png) brilhante |
| Fundo | `bg-blue`, `fundo-azul` | ![fundo](https://placehold.co/15x15/0451a5/0451a5.png) fundo azul |
| Cor real (hex) | `#ff8800`, `bg-#222222` | ![hex](https://placehold.co/15x15/ff8800/ff8800.png) `#ff8800` ![fundo](https://placehold.co/15x15/222222/222222.png) `bg-#222222` |

```python
print("//bright-red/brilhante/bright-red")
print("//bg-blue/fundo azul/bg-blue")
print("//bg-#222222/painel escuro/bg-#222222")
print("//#ff8800/laranja exato/#ff8800")
```

### Apelidos em português

Tags em inglês e apelidos em português funcionam da mesma forma:

```python
print("//negrito-vermelho/erro/negrito-vermelho")
print("//fundo-amarelo/aviso em amarelo/fundo-amarelo")
```

### Descubra tudo no terminal

```python
import easyansi
easyansi.preview()
```

---

## Comportamento inteligente da saída

A EasyAnsi segue convenções da comunidade e se comporta corretamente em qualquer ambiente:

| Condição | Comportamento |
| --- | --- |
| Terminal interativo (TTY) | Cores ANSI aplicadas |
| Saída em pipe / redirecionada | Texto limpo (sem escape codes) |
| Variável `NO_COLOR` definida | Texto limpo ([no-color.org](https://no-color.org/)) |
| Variável `FORCE_COLOR` definida | Cores forçadas |
| `TERM=dumb` | Texto limpo |
| Windows 10+ | Modo VT habilitado no import |

Controle manual:

```python
from easyansi import fmt

fmt("//red/erro/red", color=True)   # sempre colorido
fmt("//red/erro/red", color=False)  # sempre limpo — bom para arquivo/export
```

---

## Arquitetura

Design modular com baixo acoplamento — cada módulo tem uma responsabilidade única:

```
string → parser.parse → tokens → renderer.render → saída
                  ↑                      ↑
              codes.py            terminal.py (TTY / NO_COLOR)
```

| Módulo | Papel |
| --- | --- |
| `codes.py` | Tabelas ANSI e resolução de nomes |
| `parser.py` | Tokenização da marcacao (pilha, aninhamento, escape) |
| `renderer.py` | Token → string ANSI (ou texto limpo) |
| `terminal.py` | Detecção de ambiente, VT no Windows |
| `api.py` | `fmt`, `eprint`, `einput` |
| `shortcuts.py` | Atalhos de cor/estilo e mensagens de status |
| `logging.py` | `ColorFormatter`, `setup_logging` |
| `preview.py` | Descoberta visual da paleta |

---

## Desenvolvimento

```bash
pip install -e ".[dev]"
pytest
```

Executar testes com layout src:

```bash
PYTHONPATH=src pytest
```

---

## Contribuindo

Contribuições são bem-vindas:

1. Faça fork do repositório
2. Crie uma branch de feature
3. Adicione testes para o novo comportamento
4. Garanta que `pytest` passe
5. Abra um pull request

---

## Roadmap

- [ ] Temas de acessibilidade (paletas de alto contraste)
- [ ] Backends de exportação HTML / PDF
- [ ] Tracebacks coloridos no logging

---

## Licença

MIT — veja [LICENSE](../LICENSE).

---

<p align="center">
  Feita com cuidado para devs que querem cor no terminal de forma prática — comandos fáceis, zero overhead.
</p>
