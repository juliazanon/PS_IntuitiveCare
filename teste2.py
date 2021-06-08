# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:24:16 2021

@author: julia
"""

import camelot
import pandas as pd
import shutil

# Arquivo para leitura
arquivo = "Padrao_TISS_Componente_Organizacional_202103.pdf"

# Leitura das tabelas desejadas
tabelas = camelot.read_pdf(arquivo,  pages = "79-85")

# Tabela 30 (Tabela de Tipo do Demandante)
demandante = tabelas[0].df

# Tabela 31 (Tabela de categoria do Padrão TISS)
tabelas_TISS = []
# Concatenação das tabelas lidas pelo camelot
for i in range (1, len(tabelas)-1):
    tabelas_TISS.append(tabelas[i].df)
TISS = pd.concat(tabelas_TISS)

# Tabela 32 (Tabela de Tipo de Solicitação)
tabela_solicitacao = tabelas[len(tabelas)-1].df

# Observação: esta tabela não foi lida corretamente pelo camelot,
# resultando na junção das colunas de código e descrição em uma só
# Assim, no código abaixo é consertado o dataframe
solicitacao = [[tabela_solicitacao[0][0], ""]]  # Primeira linha, título da tabela
serie = tabela_solicitacao[0][1].split("  ")  # Segunda linha, nomes das colunas
solicitacao.append(serie)
for i in range(2, len(tabela_solicitacao)):  # Demais linhas, valores
    serie = tabela_solicitacao[0][i].split("\n")
    solicitacao.append(serie)
    
# Transformação da matriz em dataframe
solicitacao = pd.DataFrame(solicitacao)    
    
# Exportações para csv
demandante.to_csv("Teste_Intuitive_Care_Julia_Harnisch/demandante.csv")
TISS.to_csv("Teste_Intuitive_Care_Julia_Harnisch/TISS.csv")
solicitacao.to_csv("Teste_Intuitive_Care_Julia_Harnisch/solicitacao.csv")

# Exportação para .zip
shutil.make_archive('Teste_Intuitive_Care_Julia_Harnisch', 'zip',
                    "D:/Users/julia/OneDrive/Área de Trabalho/Área de trabalho/IntuitiveCare/Teste_Intuitive_Care_Julia_Harnisch")
