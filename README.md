# gRPC-TP3
 
I. Première Partie :
Reprendre les mêmes exemples de la démonstration vidéo pour implémenter les 4 modèles pour le cas d'une conversion de monnaie:
- Unary Model
- Server Sreaming Model
- Client Streaming Model
- BiDirectional Streaming Model


II. Deuxième partie
 1. Créer un serveur Chat GRPC
 ![image](https://user-images.githubusercontent.com/120368654/234797185-a00fc3f3-0223-494e-ad27-9a8c5304920c.png)
 2. Tester le serveur Chat avec un client GRPC comme BloomRPC
      - Unary Model
     ![image](https://user-images.githubusercontent.com/120368654/234796864-78326ab8-9770-49ca-aa3f-db73ba6d3bc2.png)

     - Server Sreaming Model
     - Client Streaming Model
     - BiDirectional Streaming Model
 3. Créer un client GRPC Java
 ![image](https://user-images.githubusercontent.com/120368654/234796965-6d089291-04f1-43a7-9a72-a684f7aabdea.png)

 4. Créer un client GRPC Python

III. Troisième partie
 1. Créer un serveur JEU GRPC :
     - Au démarrage le serveur choisit un nombre aléatoire entre 1 et 1000. 
     - Ensuite les clients GRPC doivent deviner en compétition le nombre secret.
     - Le serveur répond à chaque fois avec les éventualités suivantes :
        . Votre nombre est plus grand
        . Votre nombre est plus petit
        . BRAVO vous avez gagné et envoyer le gagnant aux clients
        . Jeu terminé, le gagnant est ""Numéro du gagnant"
