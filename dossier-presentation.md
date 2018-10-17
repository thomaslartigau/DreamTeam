# DREAM TEAM : PRESENTATION DU PROJET


1.	PRESENTATION DU CONCEPT

## LA NBA

La NBA, pour National Basketball Association, est la ligue majeure de basket du monde. C’est dans cette ligue fermée de 20 équipes que les meilleurs joueurs de basket du monde s’affrontent au cours d’une saison en deux phases qui s’écoule de mi-octobre à début juin. 
Si vous ne connaissez pas la NBA, la page Wikipédia (lien) donne toute les informations nécessaires pour comprendre le projet.
La première phase de la saison, appelé saison régulière, chaque équipe joue un total de 82 matchs ce qui fait de cette partie de la saison la partie la plus longue, que ce soit pour les joueurs mais également pour les fans qui peuvent se lasser rapidement de l’enchainement des matchs.
Les jeux de type fantasy ou de pronostique proposent au fan de vivre plus intensément la compétition qu’il suit (pronostics entre amis de match de la coupe du monde de football par exemple).

## QU’EST-CE QU’UNE FANTASY ?

La fantasy ou ligue fantasy (en anglais : fantasy sport), également connue en anglais sous le nom de rotisserie, roto, fantasy league1 ou owner simulation, est un jeu où les participants endossent le rôle de propriétaires d'équipes sportives, et défient d'autres joueurs sur la base des résultats des vrais joueurs et équipes. En fonction de la pertinence des choix stratégiques effectués, le joueur de fantasy reçoit un certain nombre de points. Comme un véritable propriétaire d'équipe, le joueur peut vendre, acheter ou rompre le contrat d'un membre de son équipe. [Source : Wikipédia].
En France, la fantasy de Trashtalk domine le marché. Le principe de leur fantasy est simple : chaque jour l’utilisateur doit sélectionner un joueur NBA qui joue le soir même, en sachant qu’il ne pourra plus le sélectionner les 30 jours suivants. Il gagne des points en fonction de la performance réel du joueur NBA choisit.

## LE JEU

#### Quel est le principe général ?

L’utilisateur se glisse dans la peau d’un Général Manager (GM) d’une équipe NBA : il essaie de construire la meilleure équipe possible en respectant les règles de la NBA en termes de nombre de joueurs dans son équipe et de masse salariale. Dans le cadre du jeu, nous ne sommes pas obligés de fixer les même seuils que la NBA, à savoir 15 joueurs maximum par équipe et une masse salariale de 100 M$ environ. Le but de l’utilisateur est donc d’optimiser son effectif en terme de cout, de point glaner par joueur NBA et dispersion d’équipe NBA. 

#### Comment créer l’attachement au jeu ?

Il faut que l’utilisateur ait envie de revenir tous les jours sur le site pour voir les points qu’il a gagné grâce au match de la nuit et les améliorations qu’il peut apporter à son effectif. Etre présent sur plusieurs supports (site web, application, communication sur les réseaux sociaux) est important. 

#### Comment monnayer le jeu ?

En proposant à l’utilisateur d’acheter de la monnaie virtuelle du jeu, des bonus, skins.
La pub sur le site est également envisageable à terme, tout comme un partenariat avec un site d’actualité NBA.
Les règles en détails

Règles : 
- Les joueurs sont représentés par des cartes
- Nombre maximum de carte dans l’effectif
- Nombre maximum de contrat rookie dans l’effectif
- Masse salarial maximum pour l’effectif
- Une équipe de 5 joueurs par poste par semaine
- Une carte a une poste défini
- Le poste d’une carte peut être changé selon le joueur de la carte (ex : Anthony Davis = AF ou C) via un bonus
- Chaque carte a un contrat, i.e un nombre de match qu’elle peut jouer
- Le contrat d’une carte diminue de 1 à chaque match joué
- L’utilisateur gagne 0.5 contrat par match joué (favorise de mettre une équipe avec beaucoup de match)
- L’utilisateur gagne de la monnaie virtuelle avec les points fantasy glané par ses cartes

Bonus :
- Bonus joueur de plus dans l’effectif *
- Bonus masse salariale de plus *
- Bonus changement de poste (une carte générique ou une carte par changement ?)
- Bonus point multiplié par XX % toute la semaine pour la carte sélectionné
- Changement de carte en cours de semaine
- Accès au joueur chaud / froid pendant une certaine durée
* Une limite maximale devra tout de même est fixée

Trading :
- Un marché de trading existe : possibilité de vendre tout type de carte aux enchères / vente direct contre de la monnaie virtuelle
- Possibilité de négocier des trades de packs de carte (+ monnaie virtuelle) entre utilisateur

Autres :
- Ajouter des utilisateurs en amis pour favoriser les contacts
- Possibilité de créer des groupes d’utilisateur pour échanger plus facilement, se vaner, classement du groupe etc…

Défis : 
- Possibilité de défier un autre utilisateur sur une période donnée (1 soir, 2, 3, … 1 semaine) avec une mise (carte / monnaie) en jeux
- Imaginer des défis qui permette de remporter de la monnaie virtuelle (ex : faire une équipe de la semaine qu’avec des joueurs de la conférence Est)

2.	DECOUPAGE DU PROJET

Le but de ce projet est donc développer un site internet mais aussi des applications iOS et Android pour jouer au jeu détailler en première partie.

## EQUIPES TECHNIQUES

Pour mener à bien ce projet, trois équipes techniques sont identifiés.

#### Equipe Data Collection & Processing

Cette équipe a pour but de fournir la matière première de la fantasy, à savoir les données générales sur la NBA. Elle devra aussi réaliser les différent programme de processing sur ces données afin d’obtenir les données nécessaire au fonctionnement du jeu.

Rôle : 
- Collecter la matière première, à savoir les données de la NBA
- API, Scrapping, Database (Mongo DB ?)
- Calculs de données lié au jeu (proba de tirer une carte par exemple)
- AWS Gateway ; AWS Lambda ; Python ?

#### Equipe API

Cette équipe a pour but de développé l’API qui sera utilisé par les diverses applications. C’est elle qui fait le lien entre la partie interface graphique et le stockage de la base de données. 

Rôle :
- Exposer les données stockés, de façon le plus simple possible
- node JS, express
- Stocker les données générées par les actions d’utilisateur
- Vérification des règles dites « métiers » (i.e du jeu)

#### Equipe Applications

Cette équipe aura pour objectif de développer les différents supports qui permettront de jouer à la fantasy. En plus du traditionnel site internet, des applications mobiles iOS et Android seront construites.  

Rôle :
- Maquettage du site internet et des applications pour qu’ils soient user friendly 
- Créer et maintenance du site internet et des applications
- Angular 5, ionic

#### MARKETING ET COMMUNICATION
