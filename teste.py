import qrcode  
import PySimpleGUI as sg  
from PIL import Image  
import io  

sg.theme("topanga")  # tema  

layout = [  
    [sg.Text('Insira seu link aqui!')],  
    [sg.InputText(key='-LINK-')],  # adicionando uma chave para referência  
    [sg.Button('Gerar seu Qr Code')],  
    [sg.Button('Sair')],  
    [sg.Image(key='-IMAGE-')]  # local para mostrar a imagem do QR Code  
]  

window = sg.Window('Gerador de QR Code', layout)  

while True:  
    event, values = window.read()  
    
    if event == sg.WINDOW_CLOSED or event == 'Sair':  
        break  
    elif event == 'Gerar seu Qr Code':  
        link = values['-LINK-']  
        if link:  
            # Gerar o QR Code  
            qr = qrcode.make(link)  

            # Salvar o QR Code em um objeto de bytes  
            byte_array = io.BytesIO()  
            qr.save(byte_array, format='PNG')  
            byte_array.seek(0)  

            # Atualizar a imagem na interface  
            window['-IMAGE-'].update(data=byte_array.getvalue())  

            sg.popup('QR Code gerado com sucesso!')  
        else:  
            sg.popup('Por favor, insira um link válido.')  

window.close()  
