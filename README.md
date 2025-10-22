\# 🧠 Redução de Imagens e Conversão para Escala de Cinza e Binária



Este projeto foi desenvolvido com o objetivo de demonstrar o processo de \*\*conversão de imagens coloridas para tons de cinza\*\* e, em seguida, para \*\*imagens binárias (preto e branco)\*\* — sem utilizar bibliotecas externas para a conversão em si, apenas para leitura e gravação da imagem.



---



\## 🎯 Objetivo



O trabalho visa aplicar conceitos de \*\*processamento digital de imagens\*\*, especificamente:

\- Conversão de imagem colorida (RGB) para \*\*escala de cinza (0 a 255)\*\*;

\- Conversão de imagem em tons de cinza para \*\*imagem binária (preto e branco)\*\*;

\- Uso de \*\*Python\*\* para demonstrar a lógica dos algoritmos de forma didática.



---



\## 🧩 Estrutura do Projeto



📁 \*\*Arquivos principais:\*\*

| Arquivo | Função |

|----------|--------|

| `converter\_cinza\_jpeg.py` | Converte uma imagem colorida (`entrada.jpg`) para tons de cinza (`saida\_cinza.jpg`). |

| `converter\_preto\_branco\_jpg.py` | Converte a imagem em tons de cinza (`saida\_cinza.jpg`) para imagem binária (`saida\_pb.jpg`). |



---



\## ⚙️ Requisitos



Antes de executar os scripts, você precisa ter instalado:



\- \[Python 3.10+](https://www.python.org/downloads/)

\- Gerenciador de pacotes \*\*pip\*\*

\- Biblioteca \*\*Pillow\*\* (para abrir e salvar imagens JPEG)



Para instalar o Pillow:

```bash

pip install pillow

🚀 Execução Passo a Passo

1️⃣ Converter imagem colorida para cinza

Coloque uma imagem chamada entrada.jpg na mesma pasta dos scripts.



Execute:



bash

Copy code

python converter\_cinza\_jpeg.py

Resultado:

Uma nova imagem será gerada com o nome saida\_cinza.jpg, contendo a versão em tons de cinza.



2️⃣ Converter imagem cinza para binária

Execute:



bash

Copy code

python converter\_preto\_branco\_jpg.py

Resultado:

Uma nova imagem chamada saida\_pb.jpg será criada, contendo apenas pixels preto (0) e branco (255).



🧮 Lógica Utilizada

Conversão RGB → Cinza

A conversão é feita com a média ponderada:



ini

Copy code

Cinza = 0.299 \* R + 0.587 \* G + 0.114 \* B

Conversão Cinza → Binário

Cada pixel é comparado com um limiar (threshold):



scss

Copy code

Se valor < 128 → Preto (0)

Senão → Branco (255)

🧑‍💻 Autor

Carlos Mello

💼 Especialista em IA, Automação e Desenvolvimento

🌐 AutomationsAI



🧾 Licença

Este projeto é de uso educacional e livre para estudos e melhorias.

