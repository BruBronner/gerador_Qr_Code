# importação de bibliotecas
import qrcode
import PySimpleGUI as sg 
from PIL import Image
import io
sg.theme("topanga") #tema


layout = [ [sg.Push(), sg.Text('Cole o seu link aqui'), sg.Push()],
          [sg.InputText(key = '-LINK-')],
          [sg.Button('Gerar seu qr code', key= '-BOTAO-', pad= (20,10), Row=(1))],
          [sg.Button('Sair', key = '-SAIR-', pad=(10,5), font=('helvética'), Row=(1))],
          [sg.Image(key='-IMAGE-')]
          ]

janela1 = sg.Window('Gerador de Qr Code', layout)
 
 
 
while True:
    
    events, values = janela1.read()
    
    if events == sg.WINDOW_CLOSED or events =='-SAIR-': #verificar do porque o erro
        break
    elif events == '-BOTAO-':
        link = values['-LINK-']
        if link:
            qr = qrcode.make(link)
            byte_1 = io.BytesIO()
            qr.save( byte_1, format='PNG')
            byte_1.seek(0)
            
            janela1['-IMAGE-'].update(data= byte_1.getvalue())
            sg.popup('qr code gerado com sucesso!')
        else: 
            sg.popup_cancel('insira um valor válido')
             
        
        

janela1.close()
