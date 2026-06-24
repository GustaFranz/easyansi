# Proposta de Vídeo Explicativo — EasyAnsi

> **Versão do roteiro:** alinhado à EasyAnsi **v0.5.0**  
> **Repositório:** https://github.com/GustaFranz/easyansi  
> **Uso sugerido:** copie **cada PARTE** abaixo no NotebookLM para gerar slides; depois monte o vídeo a partir dos slides.

---

## Índice das partes

| Parte | Título | Duração sugerida |
| --- | --- | --- |
| [PARTE 1](#parte-1-abertura-e-gancho) | Abertura e gancho | 30–45 s |
| [PARTE 2](#parte-2-o-problema) | O problema | 45–60 s |
| [PARTE 3](#parte-3-quem-criou-e-por-quê) | Quem criou e por quê | 60–90 s |
| [PARTE 4](#parte-4-o-que-é-a-easyansi) | O que é a EasyAnsi | 45–60 s |
| [PARTE 5](#parte-5-instalação-e-primeiro-contato) | Instalação e primeiro contato | 60–90 s |
| [PARTE 6](#parte-6-sintaxe-básica-cor) | Sintaxe básica `//cor/` | 90–120 s |
| [PARTE 7](#parte-7-colorir-uma-palavra-vs-linha-inteira) | Uma palavra vs linha inteira | 60–90 s |
| [PARTE 8](#parte-8-activate-print-e-input-nativos) | `activate()` — print e input nativos | 60 s |
| [PARTE 9](#parte-9-atalhos-e-mensagens-prontas) | Atalhos e mensagens prontas | 60–90 s |
| [PARTE 10](#parte-10-input-colorido-e-scopes-v040) | Input colorido e scopes (v0.4) | 90 s |
| [PARTE 11](#parte-11-títulos-decorativos-v040) | Títulos decorativos (v0.4) | 60–90 s |
| [PARTE 12](#parte-12-recursos-extras) | Recursos extras | 60–90 s |
| [PARTE 13](#parte-13-segurança-e-boas-práticas) | Segurança e boas práticas | 45–60 s |
| [PARTE 14](#parte-14-encerramento-e-chamada-para-ação) | Encerramento e CTA | 30–45 s |

**Duração total estimada:** 12 a 16 minutos (ajuste conforme seu ritmo).

---

## Guia rápido de produção

### Como usar este documento no NotebookLM

1. Abra o NotebookLM e crie um notebook novo (ex.: *EasyAnsi — Vídeo explicativo*).
2. Faça upload deste arquivo **ou** cole **uma PARTE por vez** como fonte.
3. Peça ao NotebookLM algo como:  
   *“Gere slides em português a partir da PARTE X: título, 3–5 bullets, nota visual e código se houver.”*
4. Revise os slides: mantenha **pouco texto por slide** e **fonte grande** (acessibilidade).
5. Exporte/imprima os slides e grave a tela do terminal + sua narração.

### O que mostrar em cada tipo de cena

| Cena | O que aparece na tela | Dica |
| --- | --- | --- |
| **Talking head** | Você falando para a câmera | Use nas partes 1, 3 e 14 |
| **Terminal** | VS Code + terminal com fundo escuro | Demonstre todo código ao vivo |
| **Slide** | Bullet points + logo EasyAnsi | Resumo entre demos |
| **Split** | Slide à esquerda, terminal à direita | Ideal nas partes 6–11 |

### Checklist antes de gravar

- [ ] Terminal com fonte grande (18–22 pt)
- [ ] Tema escuro com bom contraste
- [ ] `pip install easyansi` ou `pip install -e .` já testado
- [ ] Windows: terminal Windows Terminal ou VS Code integrado
- [ ] Arquivo `demo_video.py` com os exemplos prontos (copie da seção [Apêndice A](#apêndice-a-arquivo-demo_videopy-completo))
- [ ] Link do GitHub visível no slide final

---

## PARTE 1 — Abertura e gancho

### Objetivo desta parte

Prender atenção em 30 segundos e dizer **o que** o espectador vai aprender.

### Slides sugeridos (NotebookLM)

**Slide 1 — Título**
- EasyAnsi
- Cor no terminal Python, do jeito simples

**Slide 2 — Promessa**
- Sem configuração complicada
- Sintaxe fácil de lembrar
- Zero dependências

**Slide 3 — O que você vai ver**
- Instalar e usar em segundos
- Colorir texto no `print` e no `input`
- Títulos bonitos no terminal

### Roteiro falado (narração)

> “Olá! Neste vídeo eu vou te mostrar a **EasyAnsi** — uma biblioteca Python que colore texto no terminal de um jeito **simples e prático**.”
>
> “Se você já cansou de bibliotecas pesadas, de configurar console, de decorador complicado… aqui a ideia é outra: **escrever a cor dentro da string**, quase como uma f-string.”
>
> “No final, você vai saber instalar, usar no dia a dia, colorir perguntas no `input`, e até montar **títulos com linhas** no terminal. Vamos lá.”

### O que acrescentar na edição

- Música de abertura **suave** (volume baixo).
- Logo ou nome **EasyAnsi** centralizado.
- Corte rápido para o terminal (1–2 s de transição).

### Transição

> “Mas antes de código, deixa eu te mostrar **por que** isso existe.”

---

## PARTE 2 — O problema

### Objetivo desta parte

Mostrar a dor comum: terminal sem cor, ou libs complexas demais para quem está aprendendo.

### Slides sugeridos

**Slide 1 — Terminal sem cor**
- `print("Erro: arquivo não encontrado")`
- Tudo igual, difícil de escanear

**Slide 2 — Alternativas existentes**
- Funcionam bem para projetos grandes
- Muitos conceitos para um script simples

**Slide 3 — O que precisamos**
- Poucos imports
- Comandos curtos
- Erro de digitação **não quebra** o programa

### Roteiro falado

> “Quando a gente programa scripts, logs ou ferramentas de linha de comando, **cor ajuda muito**: erro em vermelho, sucesso em verde, aviso em amarelo.”
>
> “Só que muitas soluções pedem que você aprenda **objetos**, **renderables**, **temas**… e para um exercício, uma aula ou um script do dia a dia, isso vira barreira.”
>
> “A EasyAnsi nasceu com outra pergunta: **e se colorir no terminal fosse tão fácil quanto escrever texto?**”

### Demo na tela (opcional, 10 s)

Mostre um terminal **sem cor** com três linhas iguais em preto/branco; depois corte para a versão colorida (preview da PARTE 5).

### O que acrescentar

- Setas ou destaque nos slides comparando “antes / depois”.
- Não critique outras bibliotecas pelo nome — fale em “soluções mais completas”.

### Transição

> “Quem pensou nisso fui eu — e vou te contar rapidinho **de onde veio** essa ideia.”

---

## PARTE 3 — Quem criou e por quê

### Objetivo desta parte

Humanizar o projeto: professor, aprendiz de Python, transparência sobre IA.

### Slides sugeridos

**Slide 1 — Quem sou**
- Professor de Educação Física há 14 anos
- Aprendendo Python

**Slide 2 — O que a sala de aula ensinou**
- Instrução curta
- Erro não pode travar o aluno
- Ver antes de decorar

**Slide 3 — Transparência**
- Projeto feito com apoio de IA
- Código aberto no GitHub

### Roteiro falado

> “Eu sou professor de Educação Física há **14 anos**. Hoje estou **aprendendo Python** — não vou fingir que domino tudo aqui.”
>
> “Na escola eu aprendi que ferramenta boa é a que **não pune erro**: se o aluno erra a instrução, a aula continua. Por isso a EasyAnsi é **fail-safe**: tag desconhecida vira texto normal, o programa **não quebra**.”
>
> “Também quero ser transparente: usei **inteligência artificial** para ajudar a construir partes desta biblioteca. O que eu trago de verdade é olhar de quem **ensina todo dia** — simplificar, organizar, pensar em quem está começando.”

### O que acrescentar

- Foto sua ou ícone de professor (opcional).
- Tom calmo, sem autopromoção exagerada.

### Transição

> “Então, afinal, **o que é** a EasyAnsi na prática?”

---

## PARTE 4 — O que é a EasyAnsi

### Objetivo desta parte

Definir a biblioteca em uma frase e listar diferenciais objetivos.

### Slides sugeridos

**Slide 1 — Definição**
- Biblioteca Python para ANSI no terminal
- Marcação dentro da string: `//cor/texto/cor`

**Slide 2 — Diferenciais**
- Zero dependências (só stdlib)
- Python 3.8+
- Windows: ANSI habilitado ao importar

**Slide 3 — Para quem é**
- Iniciantes
- Professores e tutoriais
- Scripts CLI do dia a dia

### Roteiro falado

> “A **EasyAnsi** formata strings para o terminal usando códigos **ANSI** — aqueles códigos invisíveis que o terminal transforma em cor e estilo.”
>
> “Em vez de montar objetos complexos, você escreve tags **dentro do texto**, no padrão `//nome/` para abrir e `/nome` para fechar.”
>
> “Ela não tem dependências externas, funciona a partir do Python 3.8, e no Windows já tenta **ativar o modo ANSI** quando você importa o pacote.”

### O que acrescentar

- Diagrama simples: `string com tags` → `EasyAnsi` → `terminal colorido`.
- Badge “zero dependencies” se tiver arte.

### Transição

> “Vamos instalar e ver a **primeira linha colorida**.”

---

## PARTE 5 — Instalação e primeiro contato

### Objetivo desta parte

Instalar, importar, imprimir a primeira mensagem colorida.

### Slides sugeridos

**Slide 1 — Instalação**
```bash
pip install easyansi
```

**Slide 2 — Primeiro script**
```python
from easyansi import eprint

eprint("//green/Olá, EasyAnsi!/green")
```

**Slide 3 — Ver todas as cores**
```python
import easyansi
easyansi.preview()
```

### Roteiro falado

> “Instalação: `pip install easyansi`. Se estiver clonando do GitHub, use `pip install -e .` na pasta do projeto.”
>
> “O caminho mais direto é importar `eprint` — um `print` que entende a marcação EasyAnsi.”
>
> “Roda isso no terminal… pronto: **verde**, sem configuração extra.”
>
> “Quer ver a paleta inteira? `easyansi.preview()` — isso é ótimo para **aula**: o aluno vê antes de decorar nome de cor.”

### Demo ao vivo — digite e execute

```python
from easyansi import eprint

eprint("//green/Olá, EasyAnsi!/green")
```

Depois:

```python
import easyansi
easyansi.preview()
```

### Comentários extras (se sobrar tempo)

> “Repare que no `preview()` aparecem nomes em inglês **e** apelidos em português, como `negrito` e `vermelho`.”

### O que acrescentar

- Zoom no terminal quando a cor aparecer.
- Legenda na tela: `pip install easyansi`

### Transição

> “Agora vamos entender a **sintaxe** — o coração da biblioteca.”

---

## PARTE 6 — Sintaxe básica `//cor/`

### Objetivo desta parte

Ensinar abrir, fechar, combinar estilos e usar em f-string.

### Slides sugeridos

**Slide 1 — Abrir e fechar**
| Padrão | Significado |
| --- | --- |
| `//red/` | Abre vermelho |
| `/red` | Fecha vermelho |
| `//` | Fecha a última tag aberta |

**Slide 2 — Exemplo simples**
```python
eprint("//red/Erro!/red")
eprint("//green/OK!/green")
```

**Slide 3 — Combinar com hífen**
```python
eprint("//bold-blue/Título/bold-blue")
eprint("//italic-underline-magenta/Destaque/italic-underline-magenta")
```

**Slide 4 — Dentro de f-string**
```python
quantidade = 12
eprint(f"//bold-blue/Vendidos {quantidade} itens/bold-blue")
eprint(f"Sobrou //red/{quantidade}/red na prateleira")
```

### Roteiro falado

> “A regra é simples: **duas barras + nome + barra** abre o estilo. Para fechar, **barra + nome** — por exemplo `/red`.”
>
> “Se você abriu uma tag e quer fechar rápido, use `//` — fecha a **última** aberta.”
>
> “Estilo e cor combinam com **hífen**: `bold-blue` é negrito **e** azul. `italic-underline-magenta` junta três coisas.”
>
> “O melhor para o dia a dia: colocar isso **dentro de f-string**. Colorir **só o número** ou **só uma palavra**, sem pintar a linha inteira.”

### Demo ao vivo

```python
from easyansi import eprint

quantidade = 3
eprint(f"Estoque: //red/{quantidade}/red unidades")
eprint("//bold-blue/Relatório do dia/bold-blue")
```

### O que acrescentar

- Highlight animado na string: `//` … `/`
- Slide separado com apelidos PT: `//negrito-vermelho/Erro/negrito-vermelho`

### Transição

> “Quando você **não** quer tags inline, a versão 0.4 trouxe outra forma…”

---

## PARTE 7 — Uma palavra vs linha inteira

### Objetivo desta parte

Contrastar marcação inline com `ansi()`, `paint()` e `style()`.

### Slides sugeridos

**Slide 1 — Inline (parcial)**
```python
eprint(f"Nota: //green/{nota}/green")
```

**Slide 2 — Linha inteira (v0.4)**
```python
from easyansi import ansi, paint

eprint(ansi("Processo concluído").easyansi("green"))
eprint(paint("Processo concluído", "green"))
```

**Slide 3 — Quando usar cada um**
- Inline → destacar pedaço do texto
- `ansi()` / `paint()` → mensagem toda com um estilo

### Roteiro falado

> “Duas necessidades diferentes.”
>
> “**Inline** — quando só um pedaço importa: a nota, o status, o número.”
>
> “**Linha inteira** — quando a mensagem toda é ‘sucesso’, ‘erro’ ou ‘título’. Na 0.4 você usa `ansi('texto').easyansi('bold-blue')` ou a função `paint('texto', 'bold-blue')`.”
>
> “`paint` recebe **texto primeiro**, estilo depois — pensado para quem prefere função em vez de encadeamento.”

### Demo ao vivo

```python
from easyansi import eprint, ansi, paint

nota = 9
eprint(f"Aluno: //green/{nota}/green")

eprint(ansi("Cadastro salvo com sucesso!").easyansi("bold-green"))
eprint(paint("Cadastro salvo com sucesso!", "bold-green"))
```

### Transição

> “Se você não quiser trocar `print` por `eprint`, tem o `activate()`.”

---

## PARTE 8 — `activate()` — print e input nativos

### Objetivo desta parte

Mostrar monkey-patch opt-in de `print` e `input`.

### Slides sugeridos

**Slide 1 — Uma linha no topo**
```python
import easyansi
easyansi.activate()
```

**Slide 2 — Use print normal**
```python
print("//green/Tudo certo!/green")
nome = input("//cyan/Seu nome/cyan: ")
```

**Slide 3 — Desativar**
```python
easyansi.deactivate()
```

### Roteiro falado

> “Algumas pessoas preferem continuar com `print` e `input` **normais**. Sem problema.”
>
> “No início do script: `import easyansi` e `easyansi.activate()`. A partir daí, o `print` global passa a entender as tags.”
>
> “Isso é **opt-in** — a biblioteca não muda seu Python sozinha. Terminou? `deactivate()` restaura tudo.”

### Demo ao vivo

```python
import easyansi

easyansi.activate()

print("//yellow/Aviso: conexão lenta/yellow")
print(f"Porta //cyan/{8080}/cyan aberta")
```

### O que acrescentar

- Caixa de alerta no slide: “Chame `activate()` **uma vez** no início.”

### Transição

> “Além da sintaxe, existem **atalhos** prontos — ainda mais rápidos.”

---

## PARTE 9 — Atalhos e mensagens prontas

### Objetivo desta parte

Apresentar `red()`, `bold()`, `success()`, `error()`, etc.

### Slides sugeridos

**Slide 1 — Atalhos de cor**
```python
from easyansi import red, green, bold

print(red("falhou"), green("ok"), bold("título"))
```

**Slide 2 — Encadeamento**
```python
print(bold(red("crítico")))
```

**Slide 3 — Status prontos**
```python
from easyansi import success, error, warning, info

success("Salvo")
error("Falhou")
warning("Conexão lenta")
info("Porta 8080")
```

### Roteiro falado

> “Para quem gosta de autocomplete no editor, existem funções diretas: `red()`, `green()`, `bold()`…”
>
> “Dá para **encadear**: `bold(red('texto'))`.”
>
> “E tem mensagens de status prontas — `success`, `error`, `warning`, `info` — com símbolo e cor. Perfeito para script que roda no terminal todo dia.”

### Demo ao vivo

```python
import easyansi
easyansi.activate()

from easyansi import success, error, warning, info, bold, red

success("Arquivo exportado")
error("Permissão negada")
warning("Memória baixa")
info("Versão 0.4.0")

print(bold(red("Encerrando em 3 segundos...")))
```

### Transição

> “E no `input`? Dá para colorir a **pergunta**, a **resposta**, ou **os dois**.”

---

## PARTE 10 — Input colorido e scopes (v0.4)

### Objetivo desta parte

Explicar `einput`, `ansi().read()`, `ask()` e scopes `prompt`, `answer`, `both`.

### Slides sugeridos

**Slide 1 — Prompt colorido (clássico)**
```python
from easyansi import einput

nome = einput("//cyan/Nome/cyan: ")
```

**Slide 2 — Wrapper com scopes**
| Escopo | Efeito |
| --- | --- |
| `prompt` | Só a pergunta colorida |
| `answer` | Valor retornado com ANSI |
| `both` | Pergunta e answer |

**Slide 3 — Exemplos v0.4**
```python
from easyansi import ansi, ask

nome = ansi("Qual é o seu nome?").easyansi("bold-blue", scope="prompt").read()
nome = ansi("Qual é o seu nome?").easyansi("green", scope="answer").read()
nome = ansi("Qual é o seu nome?").easyansi("bold-blue", scope="both").read()

nome = ask("Qual é o seu nome?", prompt_style="bold-blue", answer_style="green")
```

### Roteiro falado

> “No `einput`, as tags coloridem o **prompt** — a pergunta antes do usuário digitar.”
>
> “Na versão 0.4, o wrapper `ansi()` deixa você escolher **scope**.”
>
> “`scope='prompt'` — só a pergunta aparece colorida.”
>
> “`scope='answer'` — o que o usuário digitou volta com ANSI; quando você der `print(nome)` depois, aparece colorido.”
>
> “**Importante dizer no vídeo:** o terminal **não** colore tecla por tecla enquanto a pessoa digita — isso é limitação do `input()` padrão. A cor na answer é no **valor retornado**.”
>
> “`scope='both'` aplica o mesmo estilo nos dois. Ou use `ask()` com `prompt_style=` e `answer_style=` separados.”

### Demo ao vivo

```python
from easyansi import ansi, ask

# Grave a tela enquanto digita "Gustavo"
nome = ansi("Qual é o seu nome? ").easyansi("bold-cyan", scope="prompt").read()
print(f"Olá, {nome}!")

nome2 = ansi("Sua cidade? ").easyansi("green", scope="answer").read()
print(nome2)  # cidade aparece verde

nome3 = ask("Idade? ", prompt_style="bold", answer_style="yellow")
print(nome3)
```

### O que acrescentar

- Texto na tela (legenda): *“Cor na answer = ao imprimir depois”*
- Evite demo longa de digitação — corte se necessário

### Transição

> “Outra novidade da 0.4: **títulos** com linhas no terminal.”

---

## PARTE 11 — Títulos decorativos (v0.4)

### Objetivo desta parte

Mostrar `title()` e `ansi().title()` com `=`, `-`, `~` e cores separadas.

### Slides sugeridos

**Slide 1 — Resultado esperado**
```
=================================================
              CADASTRO DE ALUNOS
=================================================
```

**Slide 2 — Função standalone**
```python
from easyansi import title

print(title("CADASTRO DE ALUNOS", "="))
print(title("CADASTRO DE ALUNOS", "-", line_style="blue", text_style="bold"))
```

**Slide 3 — Wrapper fluente**
```python
from easyansi import ansi

print(ansi("CADASTRO DE ALUNOS").title("="))
print(ansi("MENU").title("~", style="bold-blue"))
```

### Roteiro falado

> “Para menu de CLI, cabeçalho de relatório ou aula, a função `title()` cria **três linhas**: decoração, texto, decoração.”
>
> “O caractere pode ser `=`, `-`, `~` ou outro. A largura segue o **terminal** — ou você passa `width=` fixo.”
>
> “Quer linha azul e texto em negrito? `line_style='blue'` e `text_style='bold'`. Ou `style='bold-blue'` para aplicar nos dois.”
>
> “Com `ansi('Título').title('=')` você encadeia no mesmo estilo fluente da parte 7.”

### Demo ao vivo

```python
from easyansi import title, ansi

print(title("CADASTRO DE ALUNOS", "="))
print(title("LISTAGEM", "-", line_style="blue", text_style="bold-yellow"))
print(ansi("EasyAnsi v0.4").title("~", style="bold-cyan"))
```

### O que acrescentar

- Fullscreen no terminal para o bloco de título ficar impactante
- Mencionar alinhamento: padrão `centro`; `align="left"` também existe

### Transição

> “Antes de fechar, alguns **recursos extras** que valem conhecer.”

---

## PARTE 12 — Recursos extras

### Objetivo desta parte

Hex, fundo, logging, fmt, URLs seguras — visão rápida.

### Slides sugeridos

**Slide 1 — Fundo e hex**
```python
print("//bg-yellow/preto no amarelo/bg-yellow")
print("//#ff8800/laranja exato/#ff8800")
```

**Slide 2 — fmt sem imprimir**
```python
from easyansi import fmt
msg = fmt("//yellow/aviso/yellow")
```

**Slide 3 — Logging colorido**
```python
from easyansi.logging import setup_logging
setup_logging()
import logging
logging.info("Servidor iniciado")
```

**Slide 4 — Fail-safe com URL**
```python
print("Visite https://github.com/GustaFranz/easyansi")
```

### Roteiro falado

> “Cor de fundo: `bg-blue`, `bg-amarelo`. Cor exata com **hex**: `#ff8800`.”
>
> “`fmt()` devolve a string formatada **sem** imprimir — útil para montar mensagem antes.”
>
> “Para logs: `setup_logging()` e seu `logging.info()` já sai colorido.”
>
> “E reforçando: URL com `https://` **não quebra** — o parser só interpreta nomes **conhecidos**.”

### Demo rápida (30 s cada, se couber)

```python
import easyansi
easyansi.activate()

print("//bg-#222222/branco no painel escuro/bg-#222222")
print("//#ff8800/hex laranja/#ff8800")
print("Link: https://github.com/GustaFranz/easyansi")
```

### Transição

> “Dois minutos sobre **segurança** e quando a cor some.”

---

## PARTE 13 — Segurança e boas práticas

### Objetivo desta parte

NO_COLOR, pipe, tag errada, Windows.

### Slides sugeridos

**Slide 1 — Fail-safe**
- Tag desconhecida → texto literal
- Programa continua

**Slide 2 — NO_COLOR e redirecionamento**
- Variável `NO_COLOR` desliga ANSI
- Pipe/arquivo → texto limpo automaticamente

**Slide 3 — Windows**
- ANSI habilitado ao importar
- Use Windows Terminal ou VS Code

### Roteiro falado

> “Errou o nome da tag? Não explode — vira texto normal. Isso é de propósito.”
>
> “Se o usuário define `NO_COLOR`, ou se você redireciona saída para arquivo, a EasyAnsi **não** injeta códigos — respeita acessibilidade e arquivos limpos.”
>
> “No Windows 10+, o pacote tenta ativar VT ao importar. Terminal moderno recomendado.”

### Demo opcional

```python
import os
os.environ["NO_COLOR"] = "1"
from easyansi import eprint
eprint("//red/sem cor/red")  # sai sem ANSI
```

### Transição

> “Vamos encerrar com **onde encontrar** o projeto e o que fazer agora.”

---

## PARTE 14 — Encerramento e chamada para ação

### Objetivo desta parte

CTA claro: GitHub, instalar, contribuir, star.

### Slides sugeridos

**Slide 1 — Resumo em 4 pontos**
- Sintaxe `//cor/texto/cor`
- `activate()` ou `eprint`
- `ansi()` / `title()` na v0.4
- Zero dependências, fail-safe

**Slide 2 — Links**
- GitHub: https://github.com/GustaFranz/easyansi
- `pip install easyansi`
- README em PT, EN, ES, ZH

**Slide 3 — CTA**
- ⭐ Star no GitHub
- Teste nos seus scripts
- Feedback e issues bem-vindos

### Roteiro falado

> “Recapitulando: EasyAnsi colore o terminal com sintaxe **simples**, funciona com `print` nativo via `activate()`, tem atalhos prontos, input com scopes e títulos decorativos na **0.4**.”
>
> “O código está no GitHub — link na descrição. Instale com `pip install easyansi`, leia o README, rode `preview()` no seu terminal.”
>
> “Se isso te ajudou a aprender ou a ensinar, deixa uma **estrela** no repositório e me conta o que você construiu com a biblioteca.”
>
> “Obrigado — e bons scripts coloridos!”

### O que acrescentar na edição

- Tela final com QR code ou URL do repo (opcional)
- Música de encerramento suave
- Cards do YouTube/GitHub na descrição do vídeo

---

## Apêndice A — Arquivo `demo_video.py` completo

Copie este arquivo para gravar todas as demos em sequência:

```python
"""Demo para gravação do vídeo explicativo EasyAnsi v0.4.0.
Execute: python demo_video.py
Pause entre seções conforme o roteiro.
"""

import easyansi
from easyansi import (
    ansi,
    eprint,
    einput,
    fmt,
    paint,
    ask,
    title,
    success,
    error,
    warning,
    info,
    bold,
    red,
    green,
)

easyansi.activate()


def pausa(msg: str = "") -> None:
    if msg:
        print(f"\n--- {msg} ---\n")
    input("[Enter para continuar]")


# PARTE 5 — Primeiro contato
pausa("PARTE 5: primeiro contato")
eprint("//green/Olá, EasyAnsi!/green")

# PARTE 6 — Sintaxe básica
pausa("PARTE 6: sintaxe básica")
quantidade = 3
eprint(f"Estoque: //red/{quantidade}/red unidades")
eprint("//bold-blue/Relatório do dia/bold-blue")
eprint("//negrito-vermelho/Erro em PT-BR/negrito-vermelho")

# PARTE 7 — Linha inteira
pausa("PARTE 7: linha inteira")
eprint(ansi("Processo concluído!").easyansi("bold-green"))
eprint(paint("Processo concluído!", "bold-green"))

# PARTE 9 — Status
pausa("PARTE 9: mensagens prontas")
success("Salvo")
error("Falhou")
warning("Conexão lenta")
info("Porta 8080")
print(bold(red("Encerrando...")))

# PARTE 10 — Input (descomente para gravar com interação)
pausa("PARTE 10: input com scope")
nome = ansi("Qual é o seu nome? ").easyansi("bold-cyan", scope="prompt").read()
print(f"Olá, {nome}!")
# nome2 = ask("Sua idade? ", prompt_style="bold", answer_style="yellow")
# print(nome2)

# PARTE 11 — Títulos
pausa("PARTE 11: títulos")
print(title("CADASTRO DE ALUNOS", "="))
print(title("LISTAGEM", "-", line_style="blue", text_style="bold"))
print(ansi("EasyAnsi v0.4").title("~", style="bold-cyan"))

# PARTE 12 — Extras
pausa("PARTE 12: extras")
print("//bg-yellow/preto no amarelo/bg-yellow")
print("//#ff8800/hex laranja/#ff8800")
print("Link seguro: https://github.com/GustaFranz/easyansi")
msg = fmt("//yellow/aviso em variável/yellow")
print(msg)

pausa("FIM — preview()")
easyansi.preview()
```

---

## Apêndice B — Prompts prontos para o NotebookLM

Use um prompt por parte:

```
Com base na PARTE [N] do roteiro EasyAnsi, gere:
1) Título do slide deck (máx. 8 palavras)
2) 4 a 6 slides com: título curto, 3 bullets, nota visual
3) Slide opcional só com código (fonte monospace)
4) Sugestão de duração por slide
Tom: didático, acessível, português do Brasil.
Público: iniciantes em Python e professores.
```

```
Transforme a PARTE [N] em roteiro de narração corrida (150–200 palavras),
tom conversacional, sem jargão desnecessário.
```

```
Liste 3 ideias de B-roll ou animação simples para a PARTE [N] (terminal, setas, antes/depois).
```

---

## Apêndice C — Descrição sugerida do vídeo (YouTube / GitHub)

**Título sugerido:**  
*EasyAnsi — cor no terminal Python do jeito simples (tutorial completo)*

**Descrição curta:**

```
Aprenda a usar a biblioteca EasyAnsi (v0.4.0) para colorir print e input no terminal Python.

📦 pip install easyansi
🔗 https://github.com/GustaFranz/easyansi

Neste vídeo:
• Sintaxe //cor/texto/cor
• activate(), eprint, atalhos e status (success/error)
• Input colorido com scopes (prompt, answer, both)
• Títulos decorativos com title() e ansi().title()
• Fail-safe, NO_COLOR e zero dependências

Código demo: docs/ROTEIRO_VIDEO_EXPLICATIVO.md (Apêndice A)
```

**Tags sugeridas:** python, terminal, ansi, cli, biblioteca python, tutorial, easyansi, colorir terminal

---

## Apêndice D — Checklist pós-gravação

- [ ] Áudio sem ruído; narração pausada
- [ ] Terminal legível em 1080p
- [ ] Link do GitHub na descrição e no README (`docs/` ou seção Video)
- [ ] Thumbnail: nome EasyAnsi + exemplo colorido no terminal
- [ ] Legendas (PT) geradas e revisadas
- [ ] Card capítulo por PARTE no YouTube (14 capítulos)

---

*Documento gerado para apoiar a produção do vídeo explicativo oficial da EasyAnsi. Atualize se a versão da biblioteca mudar.*
