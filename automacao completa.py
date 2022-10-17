from cv2 import threshold
import pyautogui as eu
from time import sleep
import pytesseract
import cv2

arquivo_consulta = open('cnpjrazao.txt', 'r')
for linha in arquivo_consulta:
    cnpj = linha.split()[0]    
    razao = linha.split()[1]
    #entrar na página de pesquisa
    eu.click(520,741,duration=1)
    eu.click(1338,61,duration=0.5)
    eu.click(200,40,duration=1)
    eu.click(277,186,duration=1)
    eu.click(577,190,duration=1)
    #pesquisar o cnpj
    eu.click(1182,206,duration=1)
    eu.write(cnpj)
    eu.click(337,145,duration=1)
    sleep(15)
    #abrir o software de print
    eu.hotkey('win','shift','s')
    sleep(3)
    #tirar a print
    eu.moveTo(562,217,duration=0.5)
    eu.dragTo(640,236,0.5,button='right')
    #ir pra area de trabalho e clicar na notificação da print
    eu.click(1364,738,duration=1)
    eu.click(1217,664,duration=1)
    #salvar a print na pasta
    eu.click(738,120,duration=2)
    eu.click(430,446,duration=2)
    eu.hotkey('ctrl','a')
    eu.write(razao)
    #salvar a print
    eu.click(608,503,duration=0.5)
    #fechar a print
    eu.click(873,87,duration=0.5)
    #caminho tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Administrador\AppData\Local\Tesseract-OCR\Tesseract.exe'
    #ler a imagem
    img = cv2.imread(razao + '.png')
    #transformar a imagem em cinza
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #fazer o treshold pra binario
    _, bin = cv2.threshold(grayimg, 120, 255, cv2.THRESH_BINARY)
     #desfoque da imagem
    desfoque = cv2.GaussianBlur(bin,(5,5),0)
    #aumetando a imagem para otimizar a leitura do tesserect
    img_rsz = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    #printando a imagem
    saida = pytesseract.image_to_string(img_rsz, lang='eng')
    #pesquisar a linha no FEV
    eu.click(568,741, duration=0.5)
    numero = open(razao + ".png",'r')
    eu.click(425,259,duration=1)
    sleep(1)
    eu.write(saida)
    eu.click(352,298,duration=0.5)
    sleep(3)
    if eu.locateAllOnScreen('print de conferencia 1.png'):
        eu.click(250,393,duration=1)
        eu.moveTo(454,202,duration=2)
        eu.click(412,269,duration=0.7)
        eu.click(556,344,duration=2)
        sleep(3) 
    else:
        continue
    #abrir a fatura 
    if eu.locateOnScreen('print de conferencia 2.png'):
        eu.click('print de conferencia 2.png',duration=0.5)
        eu.click(549,490,duration=1)
        eu.click(649,391,duration=1)
        eu.click(157,97,duration=1.5)
        sleep(12)
        eu.click(748,659,duration=1)
        sleep(22)
        #salvar a fatura
        eu.click(1125,625,duration=1)
        eu.write(razao)
        eu.click(1189,687,duration=0.5)
        #fechar a fatura
        eu.click(1023,43,duration=1)
        eu.click(324,196,duration=0.5)
    else:
        eu.click(324,196,duration=0.5)
        continue
    