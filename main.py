meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "Aterrador/siniestro",
            "PAPEO": "Humillar/ganarle a alguien",
            "ROFL": "Una respuesta a una broma"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print("\n" * 1)
    print(meme_dict[word])
    
    print("\n" * 1)
    print("¡Perfecto, aquí tienes su definición de que significa!")
else:
    print("\n" * 1)
    print("Lo lamento, pero esa palabra no esta en nuestra lista")
