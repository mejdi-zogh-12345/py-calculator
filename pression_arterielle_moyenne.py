# -*- coding: utf-8 -*-
"""Calcul de la pression artérielle moyenne (PAM).

Formule : PAM = (PAS + 2 x PAD) / 3
  - PAS : pression artérielle systolique (mmHg)
  - PAD : pression artérielle diastolique (mmHg)
"""


def calculer_pam(pas, pad):
    """Retourne la PAM (mmHg) à partir de la PAS et de la PAD."""
    if pas <= 0 or pad <= 0:
        raise ValueError("La PAS et la PAD doivent être strictement positives.")
    if pad >= pas:
        raise ValueError("La PAS doit être supérieure à la PAD.")
    return (pas + 2 * pad) / 3


def interpreter_pam(pam):
    """Donne une interprétation indicative de la PAM."""
    if pam < 65:
        return "Basse (< 65 mmHg) : risque d'hypoperfusion des organes"
    if pam <= 100:
        return "Normale (65 - 100 mmHg)"
    return "Élevée (> 100 mmHg)"


def lire_nombre(message):
    """Demande une valeur numérique jusqu'à ce que la saisie soit valide."""
    while True:
        saisie = input(message).strip().replace(",", ".")
        try:
            return float(saisie)
        except ValueError:
            print("Valeur invalide, veuillez entrer un nombre.")


def main():
    print("=== Calcul de la pression artérielle moyenne (PAM) ===")
    while True:
        pas = lire_nombre("PAS - pression systolique (mmHg) : ")
        pad = lire_nombre("PAD - pression diastolique (mmHg) : ")
        try:
            pam = calculer_pam(pas, pad)
        except ValueError as erreur:
            print(f"Erreur : {erreur}")
        else:
            print(f"PAM = {pam:.1f} mmHg -> {interpreter_pam(pam)}")

        if input("Nouveau calcul ? (o/n) : ").strip().lower() != "o":
            print("Au revoir !")
            break


if __name__ == "__main__":
    main()
