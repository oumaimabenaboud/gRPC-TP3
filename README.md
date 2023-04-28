# gRPC-TP3
 
### I. Première Partie :
Reprendre les mêmes exemples de la démonstration vidéo pour implémenter les 4 modèles pour le cas d'une conversion de monnaie:
 ![image](https://user-images.githubusercontent.com/120368654/234797185-a00fc3f3-0223-494e-ad27-9a8c5304920c.png)
 
##### - Unary Model
![image](https://user-images.githubusercontent.com/120368654/234796864-78326ab8-9770-49ca-aa3f-db73ba6d3bc2.png)
       
###### - Unary Model Synchrone
![image](https://user-images.githubusercontent.com/120368654/234796965-6d089291-04f1-43a7-9a72-a684f7aabdea.png)
            
###### - Unary Model Asynchrone
![image](https://user-images.githubusercontent.com/120368654/234800321-91797d7e-bedc-4397-8a67-18275e7d9f44.png)
            
##### - Server Sreaming Model
![image](https://user-images.githubusercontent.com/120368654/234804090-0cebb14b-8e8d-4ec6-82ee-e38aaf4254e5.png)
![image](https://user-images.githubusercontent.com/120368654/234805251-4f16e4ff-4dea-4f83-a44a-a056ac02d75f.png)
     
##### - Client Streaming Model
![image](https://user-images.githubusercontent.com/120368654/234812151-6e01b3e4-c40e-4e59-bb2f-99a82023cc70.png)
![image](https://user-images.githubusercontent.com/120368654/234816670-9e641881-e902-4a5e-9dcd-388879406e64.png)
     
##### - BiDirectional Streaming Model
![image](https://user-images.githubusercontent.com/120368654/234818657-1594b729-9d0a-4385-adab-1e855f241fce.png)
![image](https://user-images.githubusercontent.com/120368654/234819747-dc6760ac-d5eb-43ed-9922-89fa497afb7f.png)


### II. Deuxième partie
 1. Créer un serveur Chat GRPC
![image](https://user-images.githubusercontent.com/120368654/234832200-59e87b1c-6e49-4b5d-aaa2-6c8985934296.png)
 
 2. Tester le serveur Chat avec un client GRPC comme BloomRPC
![image](https://user-images.githubusercontent.com/120368654/234832438-d44bd292-bdc1-43e6-b453-fa026704ecb3.png)

 3. Créer un client GRPC Java
![image](https://user-images.githubusercontent.com/120368654/234846225-22de939f-ddc5-4ce6-8c4e-c58a3c3424c6.png)

 4. Créer un client GRPC Python
 ![image](https://user-images.githubusercontent.com/120368654/235003358-a163f937-c1a6-4d3a-ba26-2ec10738d3d5.png)


III. Troisième partie

 Créer un serveur JEU GRPC : Au démarrage le serveur choisit un nombre aléatoire entre 1 et 1000.Ensuite les clients GRPC doivent deviner en compétition le nombre secret. Le serveur répond à chaque fois avec les éventualités suivantes :
        . Votre nombre est plus grand
        . Votre nombre est plus petit
        . BRAVO vous avez gagné et envoyer le gagnant aux clients
        . Jeu terminé, le gagnant est "Numéro du gagnant"
        
  1. Création du serveur JEU GRPC :
 ![image](https://user-images.githubusercontent.com/120368654/235018085-6459722e-8a6b-41b0-878b-98b8c1d2ee48.png)
  2. Test des différents méthodes du serveur à l'aide de BloomRPC:
      - Démarrage du serveur:
![image](https://user-images.githubusercontent.com/120368654/235018399-be46a741-9d9b-4437-a680-7b84ac81748b.png)
      - Deviner le nombre secret:
        . Votre nombre est plus petit
![image](https://user-images.githubusercontent.com/120368654/235018755-a931beab-a294-424a-a22e-0bb3f7746523.png)
        . Votre nombre est plus grand
![image](https://user-images.githubusercontent.com/120368654/235018824-c45382a0-3d4b-43d8-99a4-b55b432aed2f.png)
        . BRAVO vous avez gagné et envoyer le gagnant aux clients
![image](https://user-images.githubusercontent.com/120368654/235019528-18b7a934-5baf-4606-946e-b17909745354.png)
        . Jeu terminé, le gagnant est "Numéro du gagnant"
![image](https://user-images.githubusercontent.com/120368654/235019859-5ae6603e-9c17-43a2-93d1-f43ec184ac9e.png)
![image](https://user-images.githubusercontent.com/120368654/235019930-83b06c6f-3fb0-40c7-b1fd-910e31057c88.png)

  3. Création de Clients
