import QCManglais
i = 0
i = i + QCManglais.QCM("in what year was the first minecraft version released?", "1 : 2009", "2 : 2011", "3 : 2013", 1)
i = i + QCManglais.QCM("in what year was the first OFFICIAL minecraft version released?", "1 : 2009", "2 : 2011", "3 : 2013", 2)
i = i + QCManglais.QCM("how to a honeycomb? ", "1 : use an empty bottle on a bee nest", "2 : use shears on a bee nest", "3 : put a campfire below the bee nest then use an empty bottle", 2)
i = i + QCManglais.QCM("in what version were the elytras added?", "1 : 1.9", "2 : 1.11", "3 : 1.13", 1)
i = i + QCManglais.QCM("what is the only food that we can eat faster? ", "1 : dried kelp", "2 : notch apple", "3 : golden carrot", 1)
i = i + QCManglais.QCM("in what version was the parameter 'item' in the command '/execute if' added?""2 :1.21.3", "3 : 1.20.3", 3)
i = i + QCManglais.QCM("did you like this QCM? ", "1 : no", "2 : yes", "3 : a lot", 3)
print(i, end="/7 right answers! ")
print("thanks!")