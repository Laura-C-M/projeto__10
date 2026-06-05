import cv2

# Carrega a imagem do disco em escala de cinza (o segundo argumento 0 faz isso)
# Certifique-se de que 'imagem.png' está no mesmo diretório ou forneça o caminho completo
img = cv2.imread("imagem2.png", 0)

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho do ficheiro.")
else:
    # Aplica o algoritmo Canny para deteção de bordas
    # Argumentos: imagem em escala de cinza, limiar mínimo, limiar máximo
    edges = cv2.Canny(img, 100, 200)

    # Exibe a imagem com as bordas detetadas
    cv2.imshow("Edges", edges)

    # Espera indefinidamente por uma tecla ser pressionada
    cv2.waitKey(0)

    # Destrói todas as janelas criadas pelo OpenCV
    cv2.destroyAllWindows()