# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:25:54 2021

@author: julia
"""
# Biblioteca utilizada para webscraping
from selenium import webdriver

# Configura o navegador para não abrir o arquivo e fazer o download diretamente
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"plugins.always_open_pdf_externally": True # Não vai mostrar o pdf diretamente no chrome
})

# Abre o navegador com as configurações anteriores
navegador = webdriver.Chrome(options=options)

# Abre o site desejado
navegador.get("http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar")

# Fecha a janela de pop-up
navegador.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div/div/div[1]/button/span").click()

# Clica no link para o padrão TISS mais recente
navegador.find_element_by_xpath("/html/body/div[9]/div/div[2]/div[2]/div[2]/a").click()

# Fecha a janela de pop-up novamente
navegador.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div/div/div[1]/button/span").click()

# Clica no link para download do arquivo desejado
navegador.find_element_by_xpath("/html/body/div[9]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a").click()
