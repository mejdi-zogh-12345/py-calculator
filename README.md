# py-calculator

My first Python project.

Features:
- Addition
- Subtraction
- Multiplication
- Division

Built while learning Python fundamentals.

## Pression artérielle moyenne (PAM)

`pression_arterielle_moyenne.py` calcule la PAM à partir de la pression
systolique (PAS) et diastolique (PAD) :

    PAM = (PAS + 2 × PAD) / 3

Lancement :

    python3 pression_arterielle_moyenne.py

Exemple : PAS = 120, PAD = 80 → PAM = 93.3 mmHg (normale).

### Version web

`web/index.html` est une application web autonome (HTML/CSS/JS, sans serveur) :
ouvrez simplement le fichier dans un navigateur. Le calcul se met à jour en
direct, avec l'affichage type moniteur `PAS/PAD (PAM)`, la pression pulsée et
une échelle d'interprétation.
