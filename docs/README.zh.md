<p align="center">
  <a href="../README.md"><img src="https://img.shields.io/badge/lang-English-blue?style=for-the-badge" alt="English"></a>
  <a href="README.pt.md"><img src="https://img.shields.io/badge/lang-Português-green?style=for-the-badge" alt="Português"></a>
  <a href="README.es.md"><img src="https://img.shields.io/badge/lang-Español-orange?style=for-the-badge" alt="Español"></a>
  <a href="README.zh.md"><img src="https://img.shields.io/badge/lang-中文-red?style=for-the-badge" alt="中文"></a>
</p>

<h1 align="center">EasyAnsi</h1>

<p align="center">
  <strong>在终端中为文本着色的简单实用方式。</strong><br>
  命令简单 · 无需配置 · 像 f-string 一样在字符串中直接写颜色。<br>
  零依赖 · 安全容错 · 适合初学者和日常脚本。
</p>

<p align="center">
  <a href="https://pypi.org/project/easyansi/"><img src="https://img.shields.io/pypi/v/easyansi?label=PyPI&color=blue" alt="PyPI 版本"></a>
  <a href="../LICENSE"><img src="https://img.shields.io/badge/许可证-MIT-green" alt="MIT 许可证"></a>
  <img src="https://img.shields.io/badge/python-%3E%3D3.8-blue" alt="Python >= 3.8">
  <img src="https://img.shields.io/badge/依赖-零-brightgreen" alt="零依赖">
  <img src="https://img.shields.io/badge/typing-typed-informational" alt="Typed">
</p>

---

## 概述

**EasyAnsi** 是一款轻量级 Python 库，使用直观的标记语法（灵感来自 f-string，而非 Rich 的方括号语法）将普通字符串转换为终端 ANSI 彩色输出。

直接在字符串中写入颜色：

```python
from easyansi import eprint

quantity = 12
eprint(f"//bold-blue/今天售出了 {quantity} 块饼干/bold-blue")
eprint(f"库存仅剩 //red/{quantity}/red 件")
```

无需配置。无需重量级 Console 对象。标签拼写错误也不会崩溃——未知名称保持为纯文本。

---

## 项目背景

我目前正在**学习 Python**。在学习过程中，我发现终端文本着色可以比现有库简单得多——而复杂的用法反而妨碍了我自己的学习。

我是一名拥有 **14 年小学教学经验** 的教师。在课堂中，我学会了识别什么会促进或阻碍日常实践：清晰的说明、容易记住的命令，以及不会因错误而“惩罚”用户的工具。正是带着这种视角，我构思了 EasyAnsi——不是以编程专家的身份，而是以一位关注**学习、教学与日常实用性**的人的身份。

**透明说明：** 本库的代码是在**人工智能**的协助下完成的。我选择公开说明这一点，而不是假装完全掌握其中的每一行代码。我仍在积累 Python 的技术能力——EasyAnsi 正是这段学习旅程的一部分。

我真正带来的，是每天教学的经验：发现不必要的障碍、简化路径、为初学者着想。EasyAnsi 源于这种结合——学习者的好奇心、教育者的敏感度，以及对构建方式的诚实。

### 14 年课堂经验教会我的编程道理

| 在课堂中 | 在 EasyAnsi 中 |
| --- | --- |
| 错误不应阻碍学习 | 未知标签变为纯文本——程序从不崩溃 |
| 指令简短清晰 | `//color/` 语法像 f-string 一样容易记住 |
| 先看见，再记忆 | `preview()` 在终端中展示所有颜色 |
| 日常即用的工具 | `success()`、`error()`、`setup_logging()` — 一行命令即可 |

使用 AI 并不意味着我在冒充专家：我是一位仍在学习的人，**发现了真实的需求**，并以诚实的方式去实现它——就像备课时为学生的日常生活着想一样。

---

## 目标：更简单、更实用

EasyAnsi 的存在只有一个原因：**让终端着色对所有人都触手可及**，而不仅仅是专家。

| 你的需求 | EasyAnsi | 较重的库 |
| --- | --- | --- |
| 30 秒上手 | `from easyansi import eprint` | 配置 Console、学习 markup 规则 |
| 给单个词着色 | f-string 中的 `//red/{value}/red` | 包装对象、构建 Text 片段 |
| 显示"成功" | `success("完成")` | 自定义 renderable |
| 启用彩色日志 | `setup_logging()` — 一行 | Handler、主题、插件 |
| 标签写错 | 保持纯文本（不崩溃） | 可能抛出 markup 错误 |

**理念：** 更少的概念、更少的 import、每天都能记住并复用的实用命令。

---

## 实用命令（速查表）

复制即用——无需额外配置：

```python
from easyansi import eprint, einput, fmt, success, error, warning, info, red, green, bold

# 彩色打印（最常用）
eprint("//green/你好!/green")
eprint(f"得分: //bold-blue/{score}/bold-blue")

# 单词快捷方式
print(red("错误"), green("成功"), bold("标题"))
print(bold(red("严重")))                          # 链式调用
print("//bg-yellow/黄色背景警告/bg-yellow")       # 配合 activate()

# 状态行（开箱即用）
success("已保存")
error("失败")
warning("连接缓慢")
info("端口 8080")

# 彩色输入提示
name = einput("//cyan/姓名/cyan: ")

# 仅获取字符串（不打印）
text = fmt("//yellow/警告/yellow")

# 在终端中查看所有颜色
import easyansi; easyansi.preview()
```

**一行启用日志着色：**

```python
from easyansi.logging import setup_logging
setup_logging()          # 完成 — logging.info() 现已彩色输出
```

---

## 功能特性

| 功能 | 说明 |
| --- | --- |
| **简单语法** | `//color/text/color` — 用 `//name/` 打开，用 `/name` 或 `//` 关闭 |
| **局部着色** | 在 f-string 中给单个词着色，无需包裹整行 |
| **样式 + 颜色** | 用 `-` 组合：`bold-blue`、`italic-underline-red` |
| **真彩色** | 支持 hex：`//#ff8800/橙色/#ff8800` |
| **背景色** | `bg-blue`、`bg-#222222` |
| **双语名称** | 英语 + 葡萄牙语别名（`negrito`、`vermelho` 等） |
| **直接快捷函数** | `red()`、`bold()`、`green()` — IDE 自动补全友好 |
| **状态消息** | `success()`、`error()`、`warning()`、`info()` |
| **彩色日志** | 即插即用的 `ColorFormatter` |
| **安全解析器** | `https://` 等 URL 和未知标签不会破坏输出 |
| **智能输出** | 管道/重定向/`NO_COLOR` 时自动输出纯文本 |
| **Windows 就绪** | 导入时自动启用 VT/ANSI |
| **零依赖** | 仅标准库 |

---

## 环境要求

- Python **3.8+**
- 支持 ANSI 转义码的终端（Windows 10+ 自动启用）

---

## 安装

```bash
pip install easyansi
```

从源码安装：

```bash
git clone https://github.com/seu-usuario/easyansi.git
cd easyansi
pip install -e ".[dev]"
```

---

## 快速开始

**推荐 — 使用普通的 `print` 和 `input`：**

```python
import easyansi

easyansi.activate()   # 在脚本开头加一行

print("//green/一切正常!/green")
print(f"库存: //red/{3}/red 件剩余")
name = input("请输入 //cyan/你的名字/cyan: ")
```

无需重命名函数。调用 `easyansi.deactivate()` 可恢复原始函数。

**备选 — 显式使用 `eprint` / `einput`：**

```python
from easyansi import eprint, einput, fmt

eprint("//green/一切正常!/green")
eprint("库存: //red/3/red 件剩余")
name = einput("请输入 //cyan/你的名字/cyan: ")
message = fmt("//yellow/警告/yellow")
```

---

## 语法指南

### 打开与关闭

| 模式 | 含义 | 示例 |
| --- | --- | --- |
| `//name/` | 打开标签 | `//red/` |
| `/name` | 关闭标签（显式） | `/red` |
| `//` | 关闭最后一个打开的标签 | `//green/文本//` |

### 组合样式与颜色

（以下示例假设已调用 `easyansi.activate()`）

```python
print("//bold-blue/标题/bold-blue")
print("//italic-underline-magenta/高亮/italic-underline-magenta")
print("//bg-yellow/黄底黑字/bg-yellow")
print("//#ff8800/精确橙色/#ff8800")
```

### 在 f-string 中使用

```python
value = 42
print(f"结果: //green/{value}/green 分")
```

### 转义字面斜杠

```python
print(r"路径: \/usr\/local/bin")
```

### 安全容错设计

仅**已知**的样式/颜色名称会被解析：

```python
print("访问 https://example.com/page")   # URL 不受影响
print("//typo/文本/typo")                 # 视为纯文本
```

---

## 个性化示例

日常用法，复制即可（配合 `activate()`）：

```python
import easyansi
easyansi.activate()

# 整行着色
print("//green/保存成功/green")

# 仅一个词
score = 10
print(f"得分: //bold-blue/{score}/bold-blue 分")

# 样式 + 颜色组合
print("//italic-underline-magenta/重要提示/italic-underline-magenta")

# 背景色与 hex
print("//bg-yellow/黑字黄底/bg-yellow")
print("//#ff8800/自定义橙色/#ff8800")

# 葡萄牙语别名同样可用
print("//negrito-vermelho/错误/negrito-vermelho")
```

---

## API 参考

### 核心函数

| 函数 | 说明 |
| --- | --- |
| `activate()` | 使全局 `print` 和 `input` 解析 EasyAnsi 标记 |
| `deactivate()` | 恢复原始的 `print` 和 `input` |
| `is_active()` | 返回 `activate()` 是否已生效 |
| `fmt(text, *, color=None)` | 返回格式化字符串（ANSI 或纯文本） |
| `eprint(*values, ...)` | 彩色 `print` |
| `einput(prompt="", *, color=None)` | 彩色 `input` |
| `preview(file=None)` | 打印所有可用样式和颜色 |

**`color` 参数：** `None` = 自动检测 · `True` = 强制 ANSI · `False` = 纯文本

### 颜色快捷函数

`black` · `red` · `green` · `yellow` · `blue` · `magenta` · `cyan` · `white`

```python
from easyansi import red, green, yellow, blue, magenta, cyan, white, black

print(red("错误"), green("成功"), yellow("警告"))
print(blue("信息"), magenta("高亮"), cyan("提示"), white("文本"))
print(black("深色文字"))
```

### 样式快捷函数

`bold` · `dim` · `italic` · `underline` · `strike` · `style(name, text)`

```python
from easyansi import bold, dim, italic, underline, strike, style, red

print(bold("标题"), dim("次要"), italic("备注"))
print(underline("链接"), strike("已删除"))
print(bold(red("严重")))                    # 链式调用
print(style("bold-blue", "自定义组合"))    # 通过 style() 使用任意名称
```

所有快捷函数均支持 `color=None|True|False`。

### 状态消息

```python
from easyansi import success, error, warning, info

success("部署完成")
error("连接失败")
warning("缓存过期")
info("监听端口 8000")
```

终端不支持 Unicode 时，符号自动回退为 ASCII（`[OK]`、`[ERRO]`）。

---

## 彩色日志

与 Python 标准 `logging` 模块集成。终端中日志级别自动着色；文件输出和 `NO_COLOR` 环境下保持纯文本。

```python
import logging
from easyansi.logging import ColorFormatter, setup_logging

# 方式 1 — 接入现有配置
handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter())
logging.root.addHandler(handler)
logging.info("服务器已启动")

# 方式 2 — 一行配置
setup_logging(level=logging.INFO)
logging.warning("缓存过期")
logging.error("连接失败")
```

**默认级别颜色：**

| 级别 | 样式 |
| --- | --- |
| DEBUG | `dim` |
| INFO | `cyan` |
| WARNING | `yellow` |
| ERROR | `red` |
| CRITICAL | `bold-red` |

**日志消息中的 EasyAnsi 标记：**

```python
setup_logging(markup=True, force=True)
logging.info("//green/部署完成/green")
```

**自定义级别颜色（可选）：**

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

---

## 样式与颜色参考

### 文本样式

| 英语 | 葡萄牙语 | 标签 |
| --- | --- | --- |
| Bold | Negrito | `bold` / `negrito` |
| Dim | Fraco | `dim` / `fraco` |
| Italic | Itálico | `italic` / `italico` |
| Underline | Sublinhado | `underline` / `sublinhado` |
| Strikethrough | Tachado | `strike` / `tachado` |

```python
print("//bold/粗体/bold  //dim/暗淡/dim  //italic/斜体/italic")
print("//underline/下划线/underline  //strike/删除线/strike")
```

### 命名颜色

| 英语 | 葡萄牙语 | 标签 |
| --- | --- | --- |
| Black | Preto | `black` / `preto` |
| Red | Vermelho | `red` / `vermelho` |
| Green | Verde | `green` / `verde` |
| Yellow | Amarelo | `yellow` / `amarelo` |
| Blue | Azul | `blue` / `azul` |
| Magenta | Rosa | `magenta` / `rosa` |
| Cyan | Ciano | `cyan` / `ciano` |
| White | Branco | `white` / `branco` |

```python
print("//red/红  //green/绿  //yellow/黄  //blue/蓝")
print("//magenta/品红  //cyan/青  //white/白  //black/黑")
```

### 变体

- **亮色：** `bright-red`、`claro-vermelho`
- **背景：** `bg-blue`、`fundo-azul`
- **真彩色：** `#ff8800`、`bg-#222222`

```python
print("//bright-red/亮色/bright-red")
print("//bg-blue/蓝色背景/bg-blue")
print("//bg-#222222/深色面板/bg-#222222")
print("//#ff8800/精确 hex 颜色/#ff8800")
```

### 葡萄牙语别名

英语标签与葡萄牙语别名可互换使用：

```python
print("//negrito-vermelho/错误/negrito-vermelho")
print("//fundo-amarelo/黄色背景警告/fundo-amarelo")
```

### 在终端中发现全部颜色

```python
import easyansi
easyansi.preview()
```

---

## 智能输出行为

| 条件 | 行为 |
| --- | --- |
| 交互式终端 (TTY) | 应用 ANSI 颜色 |
| 管道 / 重定向输出 | 纯文本 |
| 设置 `NO_COLOR` | 纯文本 ([no-color.org](https://no-color.org/)) |
| 设置 `FORCE_COLOR` | 强制着色 |
| `TERM=dumb` | 纯文本 |
| Windows 10+ | 导入时启用 VT 模式 |

手动控制：

```python
from easyansi import fmt

fmt("//red/错误/red", color=True)   # 始终着色
fmt("//red/错误/red", color=False)  # 始终纯文本 — 适合文件/导出
```

---

## 架构

模块化设计，低耦合：

```
string → parser.parse → tokens → renderer.render → output
                  ↑                      ↑
              codes.py            terminal.py (TTY / NO_COLOR)
```

| 模块 | 职责 |
| --- | --- |
| `codes.py` | ANSI 码表与名称解析 |
| `parser.py` | 标记分词（栈、嵌套、转义） |
| `renderer.py` | Token → ANSI 字符串 |
| `terminal.py` | 环境检测、Windows VT |
| `api.py` | `fmt`、`eprint`、`einput` |
| `shortcuts.py` | 颜色/样式快捷函数与状态消息 |
| `logging.py` | `ColorFormatter`、`setup_logging` |
| `preview.py` | 可视化调色板 |

---

## 开发

```bash
pip install -e ".[dev]"
pytest
```

```bash
PYTHONPATH=src pytest
```

---

## 贡献

欢迎贡献：

1. Fork 仓库
2. 创建功能分支
3. 为新行为添加测试
4. 确保 `pytest` 通过
5. 提交 Pull Request

---

## 路线图

- [ ] 无障碍主题（高对比度调色板）
- [ ] HTML / PDF 导出后端
- [ ] 日志中的彩色 traceback

---

## 许可证

MIT — 见 [LICENSE](../LICENSE)。

---

<p align="center">
  为想要终端着色、又不想承担复杂性的开发者而精心打造。
</p>
