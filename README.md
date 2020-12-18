## 1. Contenu du dataset

- La base de donnée consiste a des  valeurs multi spectrale de pixels dans une image satellite. La classe à prédire et le pixel central dans chaque groupe de voisins. La classe à prédire à été transformé et pour des raisons de facilité à des valeurs entre 1 et 7.
Nous avons 4435 valeurs dans le training set et 2000 dans le testing set.

- Chaque image prise par le satellite landsat consiste en 4 différentes images de la meme scène mais prise dans des valeurs spectrales différentes (2 dans le domaine du visible et 2 dans l'infrarouge). Chaque image à une résolution de 2340 x 3380 

- Dans notre dataset, on à une petite partie de l'image (82 x 100 pixels) 

Sur le schéma ci-dessous j'ai représenté 1 ligne du dataframe. La ligne répresente en fait 1 pixel (rouge) qu'on cherche à prédire, ainsi que ces voisins. Comme on peut le voir les pixels sont mis à la ligne les uns a la suite des autres, et chaque pixels est représenté par 4 valeurs entre 0 et 255.

![Getting Started](pixels.png)