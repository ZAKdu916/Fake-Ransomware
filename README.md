Simulation Fake Ransomware
Salut, bienvenue sur mon projet de simulation de ransomware en Python !

C’est quoi ce truc ?
En gros, c’est un script Python qui fait comme si ton ordinateur était infecté par un ransomware — ce programme malveillant qui chiffre tes fichiers et demande une rançon.
Mais rassure-toi, ce script ne fait rien de mal : aucun fichier n’est touché, rien n’est supprimé, c’est juste pour simuler l’effet visuel et pour comprendre comment ça peut se présenter.

Pourquoi j’ai fait ça ?
J’étais curieux de comprendre à quoi ça ressemblait, comment ça pouvait faire peur, et aussi pour vous montrer ce que ça donne, sans risquer de faire de dégâts.
C’est aussi une manière de sensibiliser à la sécurité informatique et l’importance des sauvegardes.

Comment ça marche ?
Quand tu lances le script, il :

Vide la console pour que tu n’aies plus rien d’autre à l’écran.

Affiche un message bien flippant style ransomware qui menace de supprimer tes fichiers.

Lance un compte à rebours (genre 10 secondes) avant la “suppression”.

Affiche un message final qui explique que c’est une simulation et qu’il faut pas paniquer.

Puis bloque l’écran avec un message, en attendant que tu fasses Ctrl+C pour quitter.

Installation
Tu dois avoir Python 3 d’installé sur ta machine.
Si ce n’est pas le cas, tu peux le télécharger ici : https://www.python.org/downloads/

Clone ou télécharge ce repo.

Ouvre un terminal dans le dossier du script.

Utilisation
Lance simplement le script :

bash
Copier
Modifier
python ransomware_simulation.py
Tu verras alors la simulation se dérouler.

Code rapide
Voici un extrait clé du script pour que tu voies comment ça fonctionne (attention, c’est un peu basique, c’est fait exprès) :

python
Copier
Modifier
def ransomware_simulation():
    clear_screen()
    print("!!! VOTRE ORDINATEUR EST INFECTÉ !!!")
    # compte à rebours, etc...
Sécurité
Pour être clair, ce script ne fait rien de dangereux, il ne modifie aucun fichier, il ne chiffre rien.
C’est uniquement pour simuler un écran de ransomware.

Remarques
Si tu veux utiliser ce script pour montrer à quelqu’un, préviens-le que c’est une simulation !

Toujours faire des sauvegardes régulières, c’est super important.

Merci
Merci d’avoir regardé ce projet, n’hésite pas à me dire ce que tu en penses ou à proposer des améliorations.
Si tu veux, je peux aussi t’aider à faire un vrai mini outil de sensibilisation plus poussé.

Contact
Moi-même, via GitHub.

