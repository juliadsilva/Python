from imageai.Detection import ObjectDetection

detector = ObjectDetection()

# Caminho da imagem de entrada, imagem de saída e modelo
model_path = "./models/yolo-tiny.h5"
input_path = "./input/test45.jpg"
output_path = "./output/newimage.jpg"

# Função para carregar modelo  pré-treinado
detector.setModelTypeAsTinyYOLOv3()

# Função aceita uma string que contém o caminho para o modelo pré-treinado:
detector.setModelPath(model_path)

# Função para carrega o modelo do caminho especificado
detector.loadModel()

# Detectar objetos na imagem
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

for eachItem in detection:
    print(eachItem["name"] , " : ", eachItem["percentage_probability"])