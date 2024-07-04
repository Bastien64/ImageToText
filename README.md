#Étape 1 : Installation de Tesseract
Sur Windows
Téléchargez l'installateur de Tesseract depuis ce lien.
Installez Tesseract en suivant les instructions de l'installateur.

#Étape 2 : Ajouter Tesseract au PATH
Après l'installation, vous devez ajouter le chemin du dossier d'installation de Tesseract à votre variable d'environnement PATH.

Trouvez le chemin d'installation de Tesseract. Par défaut, il pourrait être quelque chose comme C:\Program Files\Tesseract-OCR.

##Ajoutez ce chemin au PATH :

Cliquez avec le bouton droit sur "Ce PC" ou "Ordinateur" sur le bureau ou dans l'Explorateur de fichiers, puis cliquez sur "Propriétés".
Cliquez sur "Paramètres système avancés".
Dans l'onglet "Avancé", cliquez sur "Variables d'environnement".
Dans la section "Variables système", trouvez et sélectionnez la variable PATH, puis cliquez sur "Modifier".
Cliquez sur "Nouveau" et ajoutez le chemin vers le dossier d'installation de Tesseract (C:\Program Files\Tesseract-OCR).
Étape 3 : Spécifier le chemin dans le script (Optionnel)
Si vous ne voulez pas modifier votre variable PATH ou si vous rencontrez toujours des problèmes, vous pouvez spécifier directement le chemin de l'exécutable Tesseract dans votre script Python.
