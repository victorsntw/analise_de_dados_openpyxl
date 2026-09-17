# 📊 Analisador e Separador de Alunos por arquivos

Script em Python para leitura, análise e manipulação de dados acadêmicos em Excel, utilizando a biblioteca `openpyxl`. O script classifica os alunos por aprovação e gera novos relatórios.

## ✨ Funcionalidades

* **Leitura de Dados:** Extrai informações de uma planilha Excel (`alunos.xlsx`).
* **Análise Estatística:** Calcula a média geral e identifica o aluno com a maior nota.
* **Classificação:** Separa automaticamente alunos em aprovados (nota ≥ 7) e reprovados.
* **Geração de Relatórios:** Cria duas novas planilhas (`Aprovados.xlsx` e `Reprovados.xlsx`) com cabeçalhos formatados.
* **Resumo no Console:** Exibe métricas rápidas ao final da execução.

## 🚀 Como Usar
Certifique-se de que alunos.xlsx está no mesmo diretório.
A aba deve se chamar Alunos com as colunas: Nome, Curso, Idade, Nota Final, Data Matricula (dados a partir da linha 2).
Execute:

## Execute

`main.py`

## ⚙️ Requisitos

* Python 3.x
* Biblioteca `openpyxl`

```bash
pip install openpyxl
