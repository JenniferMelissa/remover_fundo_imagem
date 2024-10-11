import flet as ft
from rembg import remove
from PIL import Image

def main(page: ft.Page):

    def remover_fundo(e):
        imagem_path = imagem_input.value  # Pegue o valor do campo de texto
        try:
            nova_img = f'nova_{imagem_path}.png'
            original = Image.open(imagem_path)
            img_sem_fundo = remove(original)
            img_sem_fundo.save(nova_img)
            resultado_text.value = f"Imagem processada e salva como {nova_img} com sucesso!"
        except Exception as e:
            resultado_text.value = f"Não foi possível remover o fundo da imagem. {e}"

        page.update()

    page.title = 'Remover Fundo de Imagens'  # título da janela
    page.scroll = 'adaptive'

    imagem_input = ft.TextField(label='Informe o nome da imagem com a extensão: ')
    resultado_text = ft.Text()

    page.add(
        ft.Column(
            [
                ft.Text('Remover Fundo da Imagem', size=40, weight='bold', text_align='center'),
                imagem_input,
                ft.ElevatedButton('Remover', on_click=remover_fundo),
                resultado_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.update()

ft.app(target=main)
