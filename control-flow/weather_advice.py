# weather_advice.py

weather = input("Quel temps fait-il aujourd'hui ? (ensoleillé/pluvieux/froid) : ")

if weather == "ensoleillé":
    print("Portez un t-shirt et des lunettes de soleil.")
elif weather == "pluvieux":
    print("N'oubliez pas votre parapluie et un imperméable.")
elif weather == "froid":
    print("Assurez-vous de porter un manteau chaud et une écharpe.")
else:
    print("Désolé, je n'ai pas de recommandations pour cette météo.")
