from PIL import Image

def binarizacao_automatica(entrada, saida):
    """
    Converte uma imagem em tons de cinza para preto e branco (binária)
    de forma automática, escolhendo o limiar ideal.
    """
    # Abre a imagem em tons de cinza
    imagem = Image.open(entrada)
    imagem = imagem.convert("L")

    largura, altura = imagem.size

    # Calcula o limiar automático como a média de todos os pixels
    total_pixels = largura * altura
    soma = 0
    for x in range(largura):
        for y in range(altura):
            soma += imagem.getpixel((x, y))
    limiar = soma // total_pixels
    print(f"🔹 Limiar automático calculado: {limiar}")

    # Cria imagem binária
    imagem_binaria = Image.new("1", (largura, altura))

    for x in range(largura):
        for y in range(altura):
            pixel = imagem.getpixel((x, y))
            if pixel > limiar:
                imagem_binaria.putpixel((x, y), 1)  # branco
            else:
                imagem_binaria.putpixel((x, y), 0)  # preto

    # Salva a imagem binária
    imagem_binaria.save(saida, "JPEG")
    print(f"✅ Imagem binária salva como: {saida}")

# Exemplo de uso
binarizacao_automatica("saida_cinza.jpg", "saida_binaria_auto.jpg")
