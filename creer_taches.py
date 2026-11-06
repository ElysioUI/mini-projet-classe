import subprocess
import sys

PROJET = "Mini-projet classe"
ETIQUETTE = "enhancement"
# titre, description, estimation en heures, sprint
TACHES = [
    ("Créer le fichier index.html", "Fichier vide à la racine du dépôt.", 1, 1),
    ("Écrire la structure HTML", "En-tête, liste, image, pied de page.", 2, 1),
    ("Ajouter l'en-tête de la classe", "Titre h1 avec le nom de la classe.", 1, 1),
    ("Ajouter la liste des élèves", "Liste à puces de six prénoms fictifs.", 2, 1),
    ("Écrire le style des titres", "Fichier style.css, titres lisibles.", 2, 1),
    ("Ajouter l'emploi du temps", "Image edt.svg avec texte alternatif.", 2, 1),
    ("Rendre la page lisible sur téléphone", "Balise viewport et largeur.", 3, 1),
    ("Écrire le pied de page", "Mention de la date de mise à jour.", 1, 2),
    ("Vérifier les liens et les images", "Aucun lien mort, aucune image absente.", 1, 2),
    ("Contrôler les titres et les textes alternatifs", "Ordre h1 puis h2.", 2, 2),
    ("Tester sur deux navigateurs", "Edge et Firefox, ordinateur et téléphone.", 2, 2),
    ("Activer GitHub Pages", "Réglage Pages du dépôt, branche main.", 1, 2),
    ("Publier la page et relever l'adresse", "Adresse notée dans le README.", 1, 2),
    ("Faire valider la page", "Relecture par la personne qui valide.", 3, 2),
]

essai = len(sys.argv) > 1 and sys.argv[1] == "essai"
for titre, texte, heures, sprint in TACHES:
    corps = f"{texte}\n\nEstimation : {heures} h. Sprint {sprint}."
    commande = ["gh", "issue", "create", "--title", titre, "--body", corps,
                "--label", ETIQUETTE, "--project", PROJET]
    if essai:
        print(commande)
    else:
        subprocess.run(commande, check=True)