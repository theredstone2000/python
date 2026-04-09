import my_modules.QCM as QCM
i = 0
i = i + QCM.QCM("qui présente la théorie de la dérive des continents à partir d'un continent unique ?", "1 : fred wegener", "2 : alfred wegener", "3 : alfred wegner", 2)
i = i + QCM.QCM("comment s'appelle ce continent ?", "1 : pangée", "2 : pangé", "3 : pengé", 1)
i = i + QCM.QCM("lorsque les plaques se rapprochent, que se passe-t-il ?", "1 : une subduction", "2 : une subuduction", "3 : une subdction", 1)
i = i + QCM.QCM("ou aussi : ", "1 : une collision des pays", "2 : une collision des montagnes", "3 : une collision des continents", 3)
i = i + QCM.QCM("ce qui provoque une formation de...", "1 : chaîne de montagne", "2 : dorsale océanique", "3 : volcan", 1)
i = i + QCM.QCM("de quoi la lithosphère océanique est-elle constituée ? ", "1 : d'andésite", "2 : de basalte", "3 : de terre", 2)
i = i + QCM.QCM("quelle est le nom de la couche située en-dessous de la lithosphère ? ", "1 : l'asthénosphère", "2 : le noyau externe", "3 : le noyau interne", 1)
i = i + QCM.QCM("est-ce que vous avez aimez ce QCM ?", "1 : non", "2 : oui", "3 : énormément", 3)
print("nombre de bonne réponse : ")
print(i, end=(" / 8 !"))
print("")
print("merci d'avoir participé !")