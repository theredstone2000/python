import QCManglais
i = 0
i = i + QCManglais.QCM("what tense is that : I was happy.", "1 : past simple", "2 : past continuous", "3 : present perfect", 1)
i = i + QCManglais.QCM("what tense is that : I have been here for 3 years.", "1 : past simple", "2 : past continuous", "3 : present perfect", 3)
i = i + QCManglais.QCM("what tense is that : I was walking in the street", "1 : past simple", "2 : past continuous", "3 : present perfect", 2)
i = i + QCManglais.QCM("what tense is that : I did it !", "1 : past simple", "2 : past continuous", "3 : present perfect", 1)
i = i + QCManglais.QCM("what tense is that : you were eating.", "1 : past simple", "2 : past continuous", "3 : present perfect", 2)
i = i + QCManglais.QCM("what tense is that : I ate a burger yesterday.", "1 : past simple", "2 : past continuous", "3 : present perfect", 1)
i = i + QCManglais.QCM("what tense is that : I haven't had a bite in 3 days.", "1 : past simple", "2 : past continuous", "3 : present perfect", 3)
i = i + QCManglais.QCM("did you like this python program ?", "1 : no", "2 : yes", "3 : a lot", 3)
print(i, end="/8 good job !")
print("")
print("thanks for using this program !")