# Projet JCDecaux Vélo

Ce projet est une implémentation Python pour interagir avec l'API de partage de vélos JCDecaux. Il permet de récupérer diverses informations sur les stations de vélos et les contrats disponibles.

## Fonctionnalités

- Liste des contrats disponibles
- Liste des stations pour un contrat donné
- Pourcentage de vélos mécaniques et électriques par ville pour un contrat donné
- Classement des villes avec le plus grand nombre de vélos pour un contrat donné
- Liste des stations avec des installations bancaires pour un contrat donné
- Liste des stations avec des points bonus pour un contrat donné

## Installation

1. Clonez ce dépôt

```bash

git clone https://github.com/RiadSa59/Riad-API-Python

python3 -m venv venv ## Optionnel 1 

source venv/bin/activate ## Optionnel 2 

pip install -r requirements.txt

```


### Lancement 

<p>

Pour lancer le programme, suivez les étapes d'installation décrites dans le fichier README.md. Une fois les dépendances installées, exécutez le fichier main.py en utilisant la commande suivante : `python main.py`

</p>

<p>

L'interaction entre l'utilisateur et le programme se fait via un système de menus en mode console. Le programme présente d'abord un menu principal avec la liste des contrats disponibles et une option pour quitter le programme. L'utilisateur doit entrer un nombre pour choisir un contrat ou pour quitter.

Si un contrat est sélectionné, un sous-menu s'affiche avec différentes options pour afficher des informations spécifiques sur ce contrat, telles que la liste des stations, le classement des villes par nombre de vélos, le pourcentage de vélos mécaniques et électriques par ville, etc. L'utilisateur doit entrer un nombre pour choisir une option parmi celles proposées.

Après avoir sélectionné une option, le programme affiche les informations correspondantes à l'écran. L'utilisateur peut alors choisir de revenir au menu précédent pour sélectionner d'autres options ou de quitter le programme.

Voici un exemple de l'interaction entre l'utilisateur et le programme :

- L'utilisateur lance le programme avec python main.py.
- Le menu principal s'affiche avec la liste des contrats disponibles et une option pour quitter.
- L'utilisateur choisit un contrat en entrant le numéro correspondant.
- Le sous-menu pour le contrat sélectionné s'affiche avec différentes options.
- L'utilisateur choisit une option en entrant le numéro correspondant.
- Le programme affiche les informations correspondantes à l'option choisie.
- L'utilisateur peut choisir de revenir au menu précédent, de choisir une autre option ou de quitter le programme.
- L'interaction se poursuit jusqu'à ce que l'utilisateur décide de quitter le programme.

</p>