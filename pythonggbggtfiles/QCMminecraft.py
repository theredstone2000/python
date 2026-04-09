import QCM
i = 0
i = i + QCM.QCM("en quelle année la première version de minecraft est sorti ?", "1 : 2009", "2 : 2011", "3 : 2013", 1)
i = i + QCM.QCM("en quelle année la prémière version OFFICIELLE de minecraft est-elle sortie ?", "1 : 2009", "2 : 2011", "3 : 2013", 2)
i = i + QCM.QCM("comment obtient-on un rayon de miel ? ", "1 : utiliser une bouteille vide sur une ruche", "2 : utiliser une cisaille sur une ruche", "3 : utiliser un feu de camp sous la ruche puis une bouteille vide", 2)
i = i + QCM.QCM("dans quelle version ont été ajouter les élytras ?", "1 : 1.9", "2 : 1.11", "3 : 1.13", 1)
i = i + QCM.QCM("quelle est la seule nouriture du jeu qui se mange plus rapidement que les autres ? ", "1 : le kelp séché", "2 : la pomme de notch", "3 : la carotte dorée", 1)
i = i + QCM.QCM("dans quelle version le paramètre 'item' dans la commande /execute if a-t-il été ajouté ?", "1 : 1.19.4", "2 : 1.21.3", "3 : 1.20.3", 3)
i = i + QCM.QCM("avez-vous aimer ce QCM ? ", "1 : non", "2 : oui", "3 : énormément", 3)
print(i, end="/7 bonnes réponses ! ")
print("merci d'avoir participé !")