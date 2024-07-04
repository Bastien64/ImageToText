# Étape 1 : Installation de Tesseract Sur Windows

Téléchargez l'installateur de Tesseract depuis ce [lien](https://github.com/UB-Mannheim/tesseract/wiki).

Installez Tesseract en suivant les instructions de l'installateur.

# Étape 2 : Ajouter Tesseract au PATH

Après l'installation, vous devez ajouter le chemin du dossier d'installation de Tesseract à votre variable d'environnement PATH.

Trouvez le chemin d'installation de Tesseract. Par défaut, il pourrait être quelque chose comme `C:\Program Files\Tesseract-OCR`.

## Ajoutez ce chemin au PATH :

1. Cliquez avec le bouton droit sur "Ce PC" ou "Ordinateur" sur le bureau ou dans l'Explorateur de fichiers, puis cliquez sur "Propriétés".
2. Cliquez sur "Paramètres système avancés".
3. Dans l'onglet "Avancé", cliquez sur "Variables d'environnement".
4. Dans la section "Variables système", trouvez et sélectionnez la variable PATH, puis cliquez sur "Modifier".
5. Cliquez sur "Nouveau" et ajoutez le chemin vers le dossier d'installation de Tesseract (`C:\Program Files\Tesseract-OCR`).

# Étape 3 : Spécifier le chemin dans le script (Optionnel)

Si vous ne voulez pas modifier votre variable PATH ou si vous rencontrez toujours des problèmes, vous pouvez spécifier directement le chemin de l'exécutable Tesseract dans votre script Python.

```python
import pytesseract

# Spécifiez le chemin de l'exécutable Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
