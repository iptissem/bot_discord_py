# bot_discord_py

## Fonctionnalitées bot 

### QUIZ 

Ce quiz contient 6 questions, je l'ai créer à partir d'un dictionnaire, avec 3 clées distinctes : la question, les options et la bonne réponse.

Les différentes commandes possible : 

- !quiz :   - si la commande n'a jamais été lancé
			* la variable quiz_started deviendra True.
			* la variable quiz_starter_id va enregistrer l'id de la personne qui à écrit.
			* la personne pourra poursuivre avec !ok pour la suite.
		- si la commande à déjà été lancé par la même personne : un message disant que le quiz est déjà en cours.

- !ok : on va tout d'abord boucler grace à un for sur mon dictionnaire question.
	 on affiche ensuite la valeur de la clé question, puis celle des options.

fonction check_answer :

vérifie si la réponse donnée par l'utilisateur est bonne, on comparant le numéro qu'il à choisi à l'index de la bonne réponse dans le dictionnaire.

Deux compteurs : correct et incorrect_answer sont crées pour enregistré les bonnes et mauvaises réponses.

Utilisateur de asyncio.TimeoutError, pour annuler le point au joueur qui met plus de 30 secondes à répondre à la question.

Affichage des résultats : 
Si la personne à plus de la moitié de bonnes réponses: elle gagne. Sinon c'est une défaite.

- !exit : le joueur à la possibilité de quiter le quiz à n'importe quel moment du jeu. après cela, un message s'affichera en indiquant son score de bonnes et de mauvaises réponses

## CALCULETTE

après !calcul : affichage d'un message de bienvenue.
fonction check : on récupère dans un premier temps le message du l'utilisateur.
		 utilisation de la méthode eval pour effectuer le calcul.
	vérification : syntaxe, temps de réponse ( un délai de 30 secondes ).

## USER INFO generateur 

Commandes possibles :
- `!info` : afficher message d'introduction 
- `!info plus` : ici l'argument plus va permettre de : 
	- supprimer le premier élément de user_info pour pouvoir passer à l'info suivante.
	- si le tableau est vide, renvoie un message de fin.
fonction **get_user_info** :
pour chaque info de la liste info_user récupérer l'information souhaiter grâce à l'API de discord .
