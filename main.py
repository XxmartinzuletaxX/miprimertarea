print("hola,desconoces alguna palabra de las nuevas generaciones?")
for i in range(5):
    meme_dict = {
                "CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso",
                "CREEPY": "aterrador, siniestro",
                "GG": "victoria inminente",
                "RANDOM": "evento aleatorio"       
                }
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
       print(meme_dict[word])
    else:
        print("no encuentro esa palabra")
