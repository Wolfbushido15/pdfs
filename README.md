# Conversor de PDF com Tradução

Este projeto é um conversor de arquivos PDF que permite aos usuários carregar um PDF em inglês e obter uma versão traduzida para o idioma desejado (por padrão, português). O site utiliza Flask como back-end para processar os arquivos PDF e a Google Translate API para tradução. O front-end é simples e interativo, permitindo aos usuários fazer upload de seus PDFs.

## Tecnologias Usadas

- **Flask** - Framework de back-end para Python
- **PyMuPDF (fitz)** - Para extrair o texto dos arquivos PDF
- **Google Translate API** - Para realizar a tradução do texto extraído
- **ReportLab** - Para gerar arquivos PDF traduzidos
- **HTML/CSS/JavaScript** - Para o desenvolvimento do front-end
- **Vercel** - Para hospedagem do site

## Instalação

### Requisitos

- Python 3.x
- Node.js e npm (para o front-end)
- Conta no [Vercel](https://vercel.com/)

### Passos para rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/conversor-pdf.git
cd conversor-pdf

pip install -r requirements.txt

npm install

python app.py


