from PIL import Image  # Usado apenas para abrir e salvar

def converter_para_cinza_jpeg(entrada, saida):
    imagem = Image.open(entrada)
    imagem = imagem.convert("RGB")

    largura, altura = imagem.size
    imagem_cinza = Image.new("L", (largura, altura))

    for x in range(largura):
        for y in range(altura):
            r, g, b = imagem.getpixel((x, y))
            nivel_cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
            imagem_cinza.putpixel((x, y), nivel_cinza)

    imagem_cinza.save(saida, "JPEG")
    print(f"✅ Imagem convertida para tons de cinza salva como: {saida}")

# Exemplo de uso
converter_para_cinza_jpeg("entrada.jpg", "saida_cinza.jpg")
