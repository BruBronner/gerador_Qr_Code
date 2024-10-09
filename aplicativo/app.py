# importação de bibliotecas
import qrcode
import PySimpleGUI as sg 
from PIL import Image
import io

sg.theme('DarkGrey10')  #tema


layout = [ [sg.Push(), sg.Text('Insira seu link aqui!', pad=(10,5), font=('mono space', 15,'bold')), sg.Push()],
          [sg.InputText(key = '-LINK-')],
          [sg.Button('Gerar seu qr code', key= '-BOTAO-', pad= (15,10), size=(20,1), font=('Helvetica', 11,'bold'), button_color=('white', 'green'))],
          [sg.Push(), sg.Button('Sair', key = '-SAIR-', pad=(10,5), font=('helvética', 11,'bold'), size=(15,1), button_color=('white', 'red')),sg.Push()],
          [sg.Image(key='-IMAGE-')]
          ]

janela1 = sg.Window('Gerador de Qr Code', layout, element_justification='center', realize)
 
 
 
while True:
    
    events, values = janela1.read()
    
    if events == sg.WINDOW_CLOSED or events =='-SAIR-': 
        break
    elif events == '-BOTAO-':
        link = values['-LINK-']
        if link:
            qr = qrcode.make(link)
            byte_1 = io.BytesIO()
            qr.save( byte_1, format='PNG')
            byte_1.seek(0)
            
            janela1['-IMAGE-'].update(data= byte_1.getvalue())
            
        else: 
           erro_centralizado =[ sg.popup('insira um valor válido', font=('helvetica', 12,'bold'),)]
             
   
        

janela1.close()
