import pyautogui
import openpyxl
import pyperclip

# 2 - abrir a planilha
workbook = openpyxl.load_workbook(r'C:/Users/paulo/Desktop/automação de produtos/produtos.xlsx')
sheet_produtos = workbook['produtos']
for linha in sheet_produtos.iter_rows(min_row=2,max_row=501):
    produto = linha[0].value
    fornecedor = linha[1].value
    categoria = linha[2].value
    quantidade = linha[3].value
    valor_unitario = linha[4].value
    notificar_venda = linha[5].value
    # colar dados campo produto
    pyautogui.click(530,281,duration=1)
    pyautogui.write(produto)
    # colar dados campo fornecedor
    pyautogui.click(531,359,duration=1)
    pyautogui.write(fornecedor)
    # colar dados campo categoria
    pyautogui.click(529,436,duration=1)
    pyperclip.copy(categoria)
    pyautogui.hotkey('ctrl','v')
    # colar dados campo valor unitário
    pyautogui.click(529,522,duration=1)
    pyperclip.copy(valor_unitario)
    pyautogui.hotkey('ctrl','v')
    # Clicar na seta para selecionar SIM ou NÃO
    pyautogui.click(839,598,duration=1)
    # se notificar venda for igual a sim, marcar sim
    # se notificar venda for igual a não, marcar não
    if notificar_venda == "Sim":
        pyautogui.click(625,624, duration=1)
    elif notificar_venda == "Não":
        pyautogui.click(707,639, duration=1)
    # clicar em registrar produto
    pyautogui.click(609,655, duration=1)
    # clicar em ok, na mensagem de cadastro com sucesso
    pyautogui.click(685,448,duration=1)

# 3 -  após ter aberto a planilha eu devo copiar o dado que está dentro do campo produto e colar no seu campo respectivo dentro do sistema web
# 4 - Repetir o mesmo processo para as outras colunas
# 5 - Repetir até chegar ao último cadastro da planilha com os 500 cadastros