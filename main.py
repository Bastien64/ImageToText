import os
from PIL import Image, ImageEnhance
import pytesseract

# Spécifier le chemin vers l'exécutable Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Spécifier le chemin vers le dossier tessdata
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

# Chemin vers l'image
image_path = 'test2.jpg'

# Charger l'image avec PIL
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print(f"Le fichier spécifié est introuvable : {image_path}")
    exit(1)

# Améliorer le contraste de l'image
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2.0)  # Augmente le contraste de l'image (ajustez la valeur selon votre besoin)

# Charger l'image avec PIL
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print(f"Le fichier spécifié est introuvable : {image_path}")
    exit(1)

# Convertir l'image en noir et blanc (binarisation)
image = image.convert('L')

# Améliorer le contraste de l'image
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2.0)  # Augmente le contraste de l'image (ajustez la valeur selon votre besoin)

# Utiliser Tesseract pour extraire le texte
try:
    text = pytesseract.image_to_string(image, lang='fra', config='--psm 6')  # 'lang='fra'' est utilisé pour le français
except pytesseract.TesseractError as e:
    print(f"Erreur lors de l'exécution de Tesseract : {e}")
    exit(1)

# Chemin vers le fichier de sortie
output_text_path = '5.txt'

# Enregistrer le texte dans un fichier .txt
with open(output_text_path, 'w', encoding='utf-8') as file:
    file.write(text)

print(f"Texte extrait et enregistré dans {output_text_path}")
