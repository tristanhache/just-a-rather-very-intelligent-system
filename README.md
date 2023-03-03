# Bonjour Tristan!  
## Voici comment utilser les nouvelles platformes pour ton développement web!  
  
### VScode:  
Tu peux télécharger l'application sur le site: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)  
Cette application te permettra d'écrire ton code dans le language de ton choix (python, nodejs etc).  
  
Dans VScode, pour débuter, tu devras installer les extensions suivantes:  
- python  
- git  
  
### Github / Git:  
Github est la plateforme pour y conserver les différents scripts que tu voudras créer. À partir de VScode, tu pourras ajouter ton code directement sur github, et Heroku.  



  
### Heroku:
Heroku est la platforme qui te permettra de déployer ton code en ligne et être accessible sous ton site web tristanapp.com!

https://devcenter.heroku.com/articles/heroku-cli


### Débuter!

1. ouvre ton terminal sur ton ordi
2. dirige-toi vers le dossier où tu veux entreposer ton code
3. clone le répertoire de git
	 `git clone https://github.com/tristanhache/tristanapp`	
4. ouvre le répertoire
	`dir tristanapp`
5. crée un environement virtuel python
	`python3 -m venv venv`
6. installe les packages python que tu auras besoin
	`python3 -m pip install -r requirements.txt`
7. exécute l'application localement, dans ton terminal:
	`python -m flask run`
8. Dans ton navigateur web (chrome), navige sur:
	 http://localhost:5000

