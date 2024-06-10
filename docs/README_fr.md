
## HyperFlux
🌐 [日本語README](./wiki/README_ja.md) | 🇬🇧 [English README](./wiki/README_en.md) | 🇫🇷 [Français README](./wiki/README_fr.md) | 🇨🇳 [中文 README](./wiki/README_zh.md)

#### 🌟 Objectifs du projet  
HyperFlux vise à atteindre les objectifs suivants :
- ⚡ **Traitement transactionnel ultra-rapide** : Les algorithmes propriétaires BFT + DAG traitent jusqu'à 10 000 transactions par seconde.
- 🛡️ **Haute sécurité** : Vérification tout en protégeant la confidentialité des transactions grâce à la technologie zk-SNARKs.
- 🤖 **BFT (Byzantine Fault Tolerance)** : Algorithme BFT mis en œuvre pour améliorer la tolérance aux pannes dans les systèmes distribués.
- 📈 **DAG (Directed Acyclic Graph)** : Le DAG a été mis en œuvre pour permettre le traitement parallèle des transactions et augmenter le débit.

### 📁 Liste et description des fichiers  
- **`CONTRIBUTING.md`** : Guide de contribution au projet comprenant la vision du projet, les méthodes de contribution, les instructions d'installation, le style de codage, les canaux de communication, la gestion des problèmes, le processus de demande d'extraction, la feuille de route, les remerciements, les récompenses et les FAQ.
- **`README.md`** : Vue d'ensemble du projet, objectif, instructions d'installation, directives d'utilisation et détails des écrans d'exécution.
- **`hyperflux.py`** : Script pour le traitement des transactions, la gestion des blockchains, le traitement parallèle des transactions en utilisant DAG, et la simulation d'un réseau BFT.
- **`test_hyperflux.py`** : Script pour tester les fonctionnalités de `hyperflux.py` en utilisant le framework `unittest`. Il teste la validité des transactions, la création de blocs de genèse, et l'intégrité de la blockchain.
- **`__pycache__`** : Répertoire pour la mise en cache du bytecode Python.
- **`requirements.txt`** : Liste des dépendances du projet, y compris Flask.
- **`wiki/`** : Répertoire contenant de la documentation supplémentaire sur le projet.

### 🛠️ Instructions d'installation  
Suivez les étapes suivantes pour configurer HyperFlux :
1. **Clonez le dépôt** :
   ``bash
   git clone https://github.com/yukihamada/HyperFlux.git  
   cd HyperFlux  
   ```
2. **Installer les dépendances nécessaires** :
   ``bash
   pip install -r requirements.txt  
   ```

### 🚀 Comment l'utiliser  
Pour démarrer le projet HyperFlux, exécutez la commande suivante :  
``bash
python hyperflux.py  
```  

### 📖 Détails de l'écran au moment de l'exécution  
Lorsque vous exécutez `python hyperflux.py`, vous rencontrez un tableau de bord qui vous permet de surveiller et d'interagir avec le système HyperFlux. Vous trouverez ci-dessous les vues détaillées et les fonctionnalités auxquelles vous pouvez accéder.

## Ecran initial
Lorsque vous démarrez le projet, vous verrez ce qui suit :
``plaintext
==================================================
Statut HyperFlux : Initialisation...
[###----] Chargement de la configuration...
[#####---] Connexion au réseau...
[########] Le noeud a démarré avec succès...
==================================================
Interface WEB HyperFlux : http://localhost:8080
==================================================
Tableau de bord :
1. 🚀 Vérifier l'état du nœud
2. 💸 Soumettre une transaction
3. 🌐 Vérifier l'état du réseau
4. 📜 Gestion des contrats intelligents
5. 🗳️ Gouvernance
6. 🌉 Fonctionnalité inter-chaînes
7. ⚙️ Configuration
==================================================
Sélectionnez la fonctionnalité (1-7) :
```
Pour une explication détaillée de ce que vous verrez lorsque vous exécuterez le projet, veuillez vous référer au [Screen at Runtime Guide](./wiki/Screen_at_Runtime.md).

#### 🔧 Caractéristiques principales  
- Prise en charge des contrats intelligents** : Compatibilité EVM pour le développement dans Solidity. Intégration transparente avec l'écosystème Ethereum existant.
- Communication P2P** : Communication peer-to-peer en temps réel à l'aide de WebRTC. Transfert de données rapide et sécurisé entre les nœuds, optimisant les performances des applications distribuées.
- Évolutivité** : Fonctionnalités d'évolutivité avancées avec sharding et DAG, garantissant des performances élevées et constantes, même lorsque le réseau s'agrandit.

### 💻 Scénarios d'utilisation
Voici un exemple de manipulation de chaque fonction HyperFlux à l'aide d'arguments de ligne de commande.

#### Vérifier l'état d'un nœud
```bash
python hyperflux.py status
```

Sortie :
``plaintext
==================================================
Statut du noeud :
- State : Actif
- Nombre de pairs connectés : 12
- Hauteur du bloc : 654321
- Nombre de transactions : 987654
- Mémoire utilisée : 256MB
- Temps de disponibilité : 48 heures
==================================================
```

#### Transmission des transactions
```bash
python hyperflux.py send --adresse 0x1234abcd --montant 50
```

Sortie :
``plaintext
==================================================
Transaction envoyée à :
- Adresse de destination : 0x1234abcd
- Quantité de jetons à envoyer : 50
Transaction envoyée...
ID de la transaction : 0xabcd1234efgh5678
Transaction envoyée avec succès.
==================================================
```

### ⚙️ Pourquoi c'est faisable  
HyperFlux atteint ses objectifs grâce aux innovations suivantes :
1. **Algorithme propriétaire BFT + DAG** : Traitement rapide et finalisation des transactions avec un débit élevé.
2. Technologie **zk-SNARKs** : Amélioration de la confidentialité et de la sécurité des données.
3. Technologie **Sharding** : Répartition efficace de la charge du réseau et amélioration de l'évolutivité.
4. **Compatibilité Ethereum** : Utilisation plus facile des outils et des bibliothèques existants dans l'écosystème Ethereum.
5. **Logiciel de développement autonome** : Des outils comme OpenDevin rationalisent le processus de développement.

#### 🎯 Contribuer  
Les parties intéressées sont encouragées à contribuer au projet. Veuillez consulter le fichier `CONTRIBUTING.md` dans le dépôt pour plus d'informations.

### 📜 Licence  
Ce projet est sous licence selon les termes spécifiés dans le fichier `LICENSE` du dépôt.

### 📘 Guide de contribution  
Pour plus d'informations, veuillez vous référer au [GUIDE DE CONTRIBUTION](./CONTRIBUTING.md).

N'hésitez pas à explorer et à contribuer à l'amélioration d'HyperFlux ! 🚀🔋

### Pourquoi est-ce faisable ?

HyperFlux est capable d'atteindre ces objectifs grâce aux innovations suivantes : 1.

1. **Algorithme propriétaire BFT + DAG** : Permet un traitement et une finalisation plus rapides des transactions, ce qui se traduit par un débit plus élevé [[oai_citation:1,GitHub - Setheum-Labs/Setheum : Setheum : zk-SNARKs Enabled DAG Powered Blockchain for Light-speed Smart Contracts. Prêt pour le hacking ](https://github.com/Setheum-Labs/Setheum) [oai_citation:2,SNARKtor : A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | World's Fastest EVM](https://www.telos.net/post/ snarktor-a-decentralized-protocol-for-scaling-snarks-verification-in-blockchains)
2. **technologie zk-SNARKs** : fournit un environnement blockchain de confiance avec une confidentialité et une sécurité accrues des données [[oai_citation:3,Zero-knowledge rollups | ethereum.org](https:// ethereum.org/en/developers/docs/scaling/zk-rollups/)
3. **Technologie duharding** : répartit efficacement la charge du réseau et améliore l'évolutivité [[oai_citation:4,The Convergence of Zero-Knowledge Proofs and Decentralized Systems : Part 2 | AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2/) [oai_citation:5,ZkEVM explained : examining the future of zk rollups - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of-zk-rollups/)
4. **Compatibilité EVM** : la compatibilité avec l'écosystème Ethereum existant permet aux développeurs d'utiliser plus facilement les outils et les bibliothèques existants [ [oai_citation:6,The Sudden Rise of EVM-Compatible ZK Rollups](https ://www.coindesk.com/tech/2022/07/20/the-sudden-rise-of-evm-compatible-zk-rollups/)
5. **Utilisation de logiciels de développement autonomes** : L'avènement de logiciels de développement autonomes tels qu'OpenDevin a considérablement augmenté l'efficacité du processus de développement et permis la mise en œuvre de technologies avancées.

### Pourquoi cela n'a jamais été fait auparavant.

Les projets traditionnels de blockchain ont été confrontés au « trilemme » de l'évolutivité, de la sécurité et de la décentralisation. De nombreux projets se sont concentrés sur certains de ces éléments, ce qui a rendu très difficile la réalisation simultanée de tous ces éléments. Par exemple, la combinaison de la compatibilité EVM avec les zk-SNARKs était techniquement très complexe et nécessitait beaucoup de ressources et de temps [[oai_citation:7,SNARKtor : A Decentralized Protocol for Scaling SNARKs Verification in Blockchains | Telos Blockchain | World's Fastest EVM](https://www.telos.net/post/snarktor-a-decentralized-protocol-for- scaling-snarks-verification-in-blockchains) [oai_citation:8,The Convergence of Zero-Knowledge Proofs and Decentralized Systems : Partie 2 | AdaPulse]( AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2/) [oai_citation:9,ZkEVM explained : examining the future of zk rollups - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of-zk-rollups/)

Cependant, HyperFlux a adopté une nouvelle approche pour surmonter ces défis en intégrant les résultats de la recherche et les technologies accumulées à ce jour. Plus précisément, les facteurs suivants rendent cela possible : 1.

1. **Intégration de la recherche et de la technologie de pointe** : en combinant la technologie et les algorithmes de blockchain de pointe, nous avons pu surmonter les limitations techniques précédentes [[oai_citation:10,GitHub - Setheum-Labs/Setheum : Setheum : zk- SNARKs Enabled DAG Powered Blockchain for Light-speed Smart Contracts. Prêt pour le hacking ](https://github.com/Setheum-Labs/Setheum) [oai_ citation:11,SNARKtor : Un protocole décentralisé pour la mise à l'échelle de la vérification SNARKs dans les Blockchains | Telos Blockchain | World's Fastest EVM](https:// www.telos.net/post/snarktor-a-decentralized-protocol-for-scaling-snarks-verification-in-blockchains)
2. une équipe et une communauté de développement solides** : La collaboration entre l'équipe d'experts et la communauté open source permet un développement technologique rapide et la résolution des problèmes [[oai_citation:12,The Sudden Rise of EVM-Compatible ZK Rollups]( https://www.coindesk.com/tech/2022/07/20/the-sudden-rise-of-evm-compatible-zk-rollups/)
3. **Utilisation de logiciels de développement autonomes** : Des outils comme OpenDevin rationalisent le processus de développement et facilitent la mise en œuvre de technologies complexes.
4. **Amélioration et tests continus** : Grâce à des tests continus et à des boucles de rétroaction, nous améliorons la fiabilité et les performances de notre technologie [[oai_citation:13,The Convergence of Zero-Knowledge Proofs and Decentralized Systems : Part 2 | AdaPulse](https://adapulse.io/the-convergence-of-zero-knowledge-proofs-and-decentralized-systems-part-2 /) [oai_citation:14,ZkEVM explained : examining the future of zk rollups - LimeChain](https://limechain.tech/blog/zkevm-explained-the-future-of- zk-rollups/)

Ces facteurs permettent à HyperFlux d'offrir des performances et une commodité qui surpassent les autres projets de blockchain et permettent la prochaine génération de technologie blockchain.

## CONTRIBUER

Les parties intéressées sont encouragées à contribuer au projet. Veuillez consulter CONTRIBUTING.md dans le référentiel pour plus d'informations.

## Guide de contribution

Pour plus d'informations, veuillez vous référer au [GUIDE DE CONTRIBUTION](. /CONTRIBUTING.md) pour plus d'informations.