# importação de bibliotecas
import qrcode
import PySimpleGUI as sg 
from PIL import Image
import io
sg.theme("topanga") #tema



layout = [ [sg.Text('Insira seu link aqui! ')], #elementos da página
            [sg.InputText( key= '-LINK-')],
            [sg.Button('Gerar seu Qr Code',)],
            [sg.Button('sair')],
            [sg.Image(key = '-IMAGE-')]]

wind = sg.Window ("gerador de cpf",layout) #inicializador (talvez)


while True:
    events, values = wind.read()
    
    if events == sg.WINDOW_CLOSED or events == 'sair':
                break
            
    elif events == 'Gerar seu Qr Code':
        link = values['-LINK-']
        
        if link:
            qr = qrcode.make(link)
            sg.popup('qr code gerado com sucesso!')
            byt = io.BytesIO()
            qr.save(byt, format ='PNG')
            byt.seek(0)
            
            wind['-IMAGE-'].update(data=byt.getvalue())
        

