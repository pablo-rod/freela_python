from selenium import webdriver
from selenium.webdriver.common.by import By 
import openpyxl

driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

# extrair todos os textos
titulos = driver.find_elements(By.XPATH,"//a[@class='nome-produto']")

# extraindo os preços
precos = driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")

# criando a planilha
workbook = openpyxl.Workbook()
workbook.create_sheet('produtos')
# criando a página
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'

# inserindo os títulos preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, preco.text])
# exportando a planilha
workbook.save('produtos.xlsx')
