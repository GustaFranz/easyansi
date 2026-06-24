<p align="center">
  <a href="../README.md"><img src="https://img.shields.io/badge/lang-English-blue?style=for-the-badge" alt="English"></a>
  <a href="README.pt.md"><img src="https://img.shields.io/badge/lang-Português-green?style=for-the-badge" alt="Português"></a>
  <a href="README.es.md"><img src="https://img.shields.io/badge/lang-Español-orange?style=for-the-badge" alt="Español"></a>
  <a href="README.zh.md"><img src="https://img.shields.io/badge/lang-中文-red?style=for-the-badge" alt="中文"></a>
</p>

<h1 align="center">EasyAnsi</h1>

<p align="center">
  <strong>La forma fácil y práctica de colorear texto en terminal.</strong><br>
  Comandos simples. Sin configuración. Escribe color dentro de la cadena como una f-string.<br>
  Cero dependencias · A prueba de fallos · Pensado para principiantes y scripts diarios.
</p>

<p align="center">
  <a href="https://pypi.org/project/easyansi/"><img src="https://img.shields.io/pypi/v/easyansi?label=PyPI&color=blue" alt="Versión PyPI"></a>
  <a href="../LICENSE"><img src="https://img.shields.io/badge/licencia-MIT-green" alt="Licencia MIT"></a>
  <img src="https://img.shields.io/badge/python-%3E%3D3.8-blue" alt="Python >= 3.8">
  <img src="https://img.shields.io/badge/dependencias-cero-brightgreen" alt="Cero dependencias">
  <img src="https://img.shields.io/badge/typing-typed-informational" alt="Typed">
</p>

---

## Descripción general

**EasyAnsi** es una biblioteca Python ligera que convierte cadenas de texto en salida coloreada en terminal usando una sintaxis intuitiva inspirada en f-strings — no en la sintaxis de corchetes de Rich.

Escribe color directamente dentro de tus cadenas:

```python
from easyansi import eprint

cantidad = 12
eprint(f"//bold-blue/Hoy se vendieron {cantidad} dulces/bold-blue")
eprint(f"Quedan //red/{cantidad}/red unidades en stock")
```

Sin configuración. Sin objeto console pesado. Sin fallos si una etiqueta está mal escrita — los nombres desconocidos permanecen como texto plano.

---

## Detrás del proyecto

Estoy **aprendiendo Python**. Al estudiar, noté que colorear texto en terminal podía ser mucho más simple de lo que ofrecían otras bibliotecas — y esa complejidad dificultaba mi propio aprendizaje.

Soy **profesor de Educación Primaria desde hace 14 años**. En el aula aprendí a detectar lo que facilita o dificulta la práctica diaria: instrucciones claras, comandos fáciles de recordar y herramientas que no castigan el error. Con esa mirada diseñé EasyAnsi — no como experto en programación, sino como alguien que se preocupa por el **aprendizaje, la enseñanza y la practicidad del día a día**.

**Transparencia:** el código de esta biblioteca fue elaborado con apoyo de **inteligencia artificial**. Prefiero decirlo abiertamente antes que parecer que domino todo lo que hay aquí. Aún estoy construyendo mi capacidad técnica en Python — y esta biblioteca forma parte de ese camino.

Lo que aporto de verdad es la experiencia de quien enseña cada día: detectar barreras innecesarias, simplificar el camino y pensar en quienes están empezando. EasyAnsi nace de esa combinación — la curiosidad de quien estudia, la sensibilidad de quien enseña y la honestidad sobre cómo se construyó.

### Lo que 14 años en el aula me enseñaron sobre código

| En el aula | En EasyAnsi |
| --- | --- |
| El error no debe bloquear el aprendizaje | Las etiquetas desconocidas quedan como texto — nunca rompen el programa |
| Instrucciones cortas y claras | Sintaxis `//color/` fácil de recordar, como una f-string |
| Ver antes de memorizar | `preview()` muestra todos los colores en la terminal |
| Herramientas listas para el día a día | `success()`, `error()`, `setup_logging()` — un comando y listo |

Usar IA no me convierte en impostor: soy alguien en aprendizaje que supo **identificar una necesidad real** y buscar una forma honesta de resolverla — con la misma preocupación con la que preparo una clase para facilitar la vida de mis alumnos.

---

## Objetivo: ser más fácil y práctico

EasyAnsi existe por una razón: **hacer que el color en terminal sea accesible para todos**, no solo para expertos.

| Lo que necesitas | EasyAnsi | Bibliotecas más pesadas |
| --- | --- | --- |
| Empezar en 30 segundos | `from easyansi import eprint` | Configurar Console, aprender reglas de markup |
| Colorear una palabra | `//red/{valor}/red` en f-string | Envolver objetos, crear segmentos Text |
| Decir "éxito" | `success("Listo")` | Crear renderizables personalizados |
| Activar log colorido | `setup_logging()` — una línea | Handlers, temas, plugins |
| Etiqueta mal escrita | Queda como texto (sin crash) | Puede lanzar error de markup |

**Filosofía:** menos conceptos, menos imports, comandos fáciles que recuerdas y reutilizas cada día.

---

## Comandos prácticos (chuleta)

Copia y usa — sin configuración extra:

```python
from easyansi import eprint, einput, fmt, success, error, warning, info, red, green, bold

# Imprimir con color (lo más común)
eprint("//green/Hola!/green")
eprint(f"Puntuación: //bold-blue/{puntos}/bold-blue")

# Atajos de una palabra
print(red("error"), green("ok"), bold("título"))

# Líneas de estado (listas)
success("Guardado")
error("Falló")
warning("Conexión lenta")
info("Puerto 8080")

# Input con prompt colorido
nombre = einput("//cyan/Nombre/cyan: ")

# Solo la cadena (sin imprimir)
texto = fmt("//yellow/advertencia/yellow")

# Ver todos los colores en terminal
import easyansi; easyansi.preview()
```

**Logging en una línea:**

```python
from easyansi.logging import setup_logging
setup_logging()          # listo — logging.info() ya sale colorido
```

---

## Características

| Característica | Descripción |
| --- | --- |
| **Sintaxis simple** | `//color/texto/color` — abre con `//nombre/`, cierra con `/nombre` o `//` |
| **Color parcial** | Colorea una palabra dentro de la f-string sin envolver toda la línea |
| **Estilos + colores** | Combina con `-`: `bold-blue`, `italic-underline-red` |
| **Colores reales** | Soporte hex: `//#ff8800/naranja/#ff8800` |
| **Fondos** | `bg-blue`, `bg-#222222` |
| **Nombres bilingües** | Inglés + alias en portugués (`negrito`, `vermelho`, …) |
| **Atajos directos** | `red()`, `bold()`, `green()` — ideal para autocompletado en el IDE |
| **Mensajes de estado** | `success()`, `error()`, `warning()`, `info()` |
| **Logging colorido** | `ColorFormatter` listo para el módulo `logging` |
| **Parser seguro** | URLs como `https://` y etiquetas desconocidas nunca rompen la salida |
| **Salida inteligente** | Texto limpio automático en pipe, redirección o con `NO_COLOR` |
| **Windows listo** | VT/ANSI habilitado automáticamente al importar |
| **Cero deps** | Solo stdlib — se instala en cualquier entorno |

---

## Requisitos

- Python **3.8+**
- Terminal con soporte para códigos ANSI (habilitado automáticamente en Windows 10+)

---

## Instalación

```bash
pip install easyansi
```

Desde el código fuente:

```bash
git clone https://github.com/seu-usuario/easyansi.git
cd easyansi
pip install -e ".[dev]"
```

---

## Inicio rápido

**Recomendado — use `print` e `input` normales:**

```python
import easyansi

easyansi.activate()   # una linea al inicio del script

print("//green/Todo correcto!/green")
print(f"Stock: //red/{3}/red unidades restantes")
nombre = input("Escribe //cyan/tu nombre/cyan: ")
```

Sin renombrar funciones. Use `easyansi.deactivate()` para restaurar los originales.

**Alternativa — `eprint` / `einput` explicitos:**

```python
from easyansi import eprint, einput, fmt

eprint("//green/Todo correcto!/green")
eprint("Stock: //red/3/red unidades restantes")
nombre = einput("Escribe //cyan/tu nombre/cyan: ")
mensaje = fmt("//yellow/advertencia/yellow")
```

---

## Guía de sintaxis

### Apertura y cierre

| Patrón | Significado | Ejemplo |
| --- | --- | --- |
| `//nombre/` | Abre etiqueta | `//red/` |
| `/nombre` | Cierra etiqueta (explícito) | `/red` |
| `//` | Cierra la última etiqueta abierta | `//green/texto//` |

### Combinar estilos y colores

Usa `-` para apilar atributos:

```python
eprint("//bold-blue/encabezado/bold-blue")
eprint("//italic-underline-magenta/destacado/italic-underline-magenta")
eprint("//bg-yellow/texto negro sobre amarillo/bg-yellow")
eprint("//#ff8800/naranja exacto/#ff8800")
```

### Funciona dentro de f-strings

```python
valor = 42
eprint(f"Resultado: //green/{valor}/green puntos")
```

### Escapar barras literales

```python
eprint(r"ruta: \/usr\/local/bin")
```

### Seguro por diseño

Solo se interpretan nombres **conocidos** de estilo/color. Todo lo demás queda literal:

```python
eprint("Visita https://ejemplo.com/pagina")   # URL intacta
eprint("//typo/texto/typo")                    # tratado como texto plano
```

---

## Referencia de la API

### Funciones principales

| Función | Descripción |
| --- | --- |
| `activate()` | Hace que `print` e `input` globales interpreten el marcado EasyAnsi |
| `deactivate()` | Restaura `print` e `input` originales |
| `is_active()` | Indica si `activate()` está activo |
| `fmt(texto, *, color=None)` | Devuelve cadena formateada (ANSI o limpia) |
| `eprint(*values, sep=" ", end="\n", file=None, color=None, flush=False)` | `print` colorido |
| `einput(prompt="", *, color=None)` | `input` colorido |
| `preview(file=None)` | Imprime todos los estilos y colores disponibles |

**Parámetro `color`:** `None` = detecta terminal · `True` = fuerza ANSI · `False` = texto limpio

### Atajos de color

`black` · `red` · `green` · `yellow` · `blue` · `magenta` · `cyan` · `white`

### Atajos de estilo

`bold` · `dim` · `italic` · `underline` · `strike` · `style(nombre, texto)`

Todos aceptan `color=None|True|False` y pueden encadenarse:

```python
from easyansi import bold, red
print(bold(red("crítico")))
```

### Mensajes de estado

```python
from easyansi import success, error, warning, info

success("Despliegue completado")
error("Error de conexión")
warning("Caché desactualizada")
info("Escuchando en puerto 8000")
```

Los símbolos usan fallback ASCII (`[OK]`, `[ERRO]`) cuando el terminal no soporta Unicode.

---

## Logging colorido

Integración con el módulo `logging` estándar de Python. Los niveles se colorean en terminal; la salida permanece limpia en archivos y con `NO_COLOR`.

```python
import logging
from easyansi.logging import ColorFormatter, setup_logging

# Opción 1 — conectar al setup existente
handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter())
logging.root.addHandler(handler)
logging.info("Servidor iniciado")

# Opción 2 — configuración en una línea
setup_logging(level=logging.INFO)
logging.warning("Caché desactualizada")
logging.error("Error de conexión")
```

**Colores predeterminados por nivel:**

| Nivel | Estilo |
| --- | --- |
| DEBUG | `dim` |
| INFO | `cyan` |
| WARNING | `yellow` |
| ERROR | `red` |
| CRITICAL | `bold-red` |

**Marcado EasyAnsi en mensajes de log:**

```python
setup_logging(markup=True, force=True)
logging.info("//green/Despliegue completado/green")
```

**Parámetros de `ColorFormatter`:** `fmt`, `datefmt`, `color`, `markup`, `level_colors`, `stream`

---

## Referencia de estilos y colores

### Estilos de texto

| Inglés | Portugués | Etiqueta |
| --- | --- | --- |
| Bold | Negrito | `bold` / `negrito` |
| Dim | Fraco | `dim` / `fraco` |
| Italic | Itálico | `italic` / `italico` |
| Underline | Sublinhado | `underline` / `sublinhado` |
| Strikethrough | Tachado | `strike` / `tachado` |

### Colores nombrados

| Inglés | Portugués | Etiqueta |
| --- | --- | --- |
| Black | Preto | `black` / `preto` |
| Red | Vermelho | `red` / `vermelho` |
| Green | Verde | `green` / `verde` |
| Yellow | Amarelo | `yellow` / `amarelo` |
| Blue | Azul | `blue` / `azul` |
| Magenta | Rosa | `magenta` / `rosa` |
| Cyan | Ciano | `cyan` / `ciano` |
| White | Branco | `white` / `branco` |

### Variantes

- **Brillante:** `bright-red`, `claro-vermelho`
- **Fondo:** `bg-blue`, `fundo-azul`
- **Color real:** `#ff8800`, `bg-#222222`

### Descubre todo en tu terminal

```python
import easyansi
easyansi.preview()
```

---

## Comportamiento inteligente de la salida

EasyAnsi sigue las convenciones de la comunidad y se comporta correctamente en cualquier entorno:

| Condición | Comportamiento |
| --- | --- |
| Terminal interactivo (TTY) | Colores ANSI aplicados |
| Salida en pipe / redirigida | Texto limpio (sin códigos de escape) |
| Variable `NO_COLOR` definida | Texto limpio ([no-color.org](https://no-color.org/)) |
| Variable `FORCE_COLOR` definida | Colores forzados |
| `TERM=dumb` | Texto limpio |
| Windows 10+ | Modo VT habilitado al importar |

Control manual:

```python
fmt("//red/error/red", color=True)   # siempre colorido
fmt("//red/error/red", color=False)  # siempre limpio
```

---

## Arquitectura

Diseño modular con bajo acoplamiento — cada módulo tiene una responsabilidad única:

```
cadena → parser.parse → tokens → renderer.render → salida
                  ↑                      ↑
              codes.py            terminal.py (TTY / NO_COLOR)
```

| Módulo | Rol |
| --- | --- |
| `codes.py` | Tablas ANSI y resolución de nombres |
| `parser.py` | Tokenización del marcado (pila, anidamiento, escape) |
| `renderer.py` | Token → cadena ANSI (o texto limpio) |
| `terminal.py` | Detección de entorno, VT en Windows |
| `api.py` | `fmt`, `eprint`, `einput` |
| `shortcuts.py` | Atajos de color/estilo y mensajes de estado |
| `logging.py` | `ColorFormatter`, `setup_logging` |
| `preview.py` | Descubrimiento visual de la paleta |

---

## Desarrollo

```bash
pip install -e ".[dev]"
pytest
```

Ejecutar tests con layout src:

```bash
PYTHONPATH=src pytest
```

---

## Contribuir

Las contribuciones son bienvenidas:

1. Haz fork del repositorio
2. Crea una rama de feature
3. Añade tests para el nuevo comportamiento
4. Asegúrate de que `pytest` pase
5. Abre un pull request

---

## Roadmap

- [ ] Temas de accesibilidad (paletas de alto contraste)
- [ ] Backends de exportación HTML / PDF
- [ ] Tracebacks coloridos en logging

---

## Licencia

MIT — consulta [LICENSE](../LICENSE).

---

<p align="center">
  Hecho con cuidado para desarrolladores que quieren color en terminal de forma práctica — comandos fáciles, cero sobrecarga.
</p>
