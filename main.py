import json
from operator import itemgetter
import re
from p1 import top_tweets
from p2 import top_usuarios
from p3 import top_dias
from p4 import top_hashtags

# Creamos una funcion inicio
def funcion_inicio(data_store):
    print("¿Qué deseas obtener?")
    print("[1] Top 10 tweets con más retweets")
    print("[2] Top 10 usuarios con más contenido")
    print("[3] Top 10 días con más tweets")
    print("[4] Top 10 hashtags más usados")
    print("[5] Salir")
    seleccion = input("Seleccione un número: ")
    print()

    if seleccion == "1":
        top_tweets(data_store)
    elif seleccion == "2":
        top_usuarios(data_store)
    elif seleccion == "3":
        top_dias(data_store)
    elif seleccion == "4":
        top_hashtags(data_store)
    else:
        print("Adios!")
        pass

if __name__ == "__main__":
    # Cargamos el JSON
    data_store = []
    # Read JSON data into the datastore variable
    with open('farmers-protest-tweets-2021-03-5.json', 'r') as f:
        for line in f:
            json_data = json.loads(line)
            data_store.append(json_data)
    # Ejecutamos la función
    funcion_inicio(data_store)