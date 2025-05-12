import pyautogui as p

# Captura a screenshot
ss = p.screenshot()

# Define o caminho para salvar (lembre-se de colocar um nome de arquivo)
ss.save(r"C:\Users\DEVT-B\Desktop\python\screenshot.png")

# Exibe a screenshot
ss.show()