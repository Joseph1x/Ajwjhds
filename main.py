from PIL import Image, ImageDraw, ImageFont

# Abra a imagem
imagem = Image.open("01.jpg")

# Crie um objeto de desenho
draw = ImageDraw.Draw(imagem)

# Defina a fonte e o tamanho do texto (fonte padrão do Pillow, tamanho 36)
fonte = ImageFont.load_default().font_variant(size=15)

# Defina a posição e o texto a ser adicionado
posicao = (257, 43)
texto = "Texto a ser adicionado"

# Adicione o texto à imagem
draw.text(posicao, texto, fill="white", font=fonte)

# Salve a imagem modificada
imagem.save("imagem_modificada.jpg")
