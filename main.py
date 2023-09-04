import spacy
import pytextrank
from textblob import TextBlob
from deep_translator import GoogleTranslator


while 1:
    print("Bienvenido al proyecto final de la materia de programación")
    decision = int(input("¿Qué desea hacer con el texto del .txt?\n1)Clasificar por positivo o negativo\n2)Identificar entidades\n3)Generar resumen\n4)Clasificador de verbos, adjetivos, adverbios, etc.\n5)Generador de citas\n6)Salir\n>"))

    if decision == 1:
        try:
            with open("texto.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

                texto_inglich = GoogleTranslator(source="es", target="en").translate(contenido)

                blob = TextBlob(texto_inglich)
                polaridad = blob.sentiment.polarity

                if polaridad < 0:
                    print("El texto es negativo")
                elif polaridad > 0:
                    print("El texto es positivo")
                else:
                    print("El texto es neutro")

                print("\n")
        except FileNotFoundError:
            print("Error en el programa")

    if decision == 2:
        nombre_archivo = "texto.txt"

        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:

                contenido = archivo.read()
                nlp = spacy.load('en_core_web_sm')

                texto_ingles = GoogleTranslator(source='es', target='en').translate(contenido)

                doc = nlp(texto_ingles)

                etiquetas_descripciones = {
                    "NORP": "Grupo étnico o nacionalidad",
                    "FAC": "Edificio o lugar",
                    "GPE": "Lugar",
                    "LOC": "Lugar",
                    "PRODUCT": "Producto",
                    "EVENT": "Evento",
                    "WORK_OF_ART": "Obra de arte",
                    "LAW": "Ley",
                    "LANGUAGE": "Idioma",
                    "DATE": "Fecha",
                    "TIME": "Hora",
                    "PERCENT": "Porcentaje",
                    "MONEY": "Moneda",
                    "QUANTITY": "Cantidad",
                    "ORDINAL": "Ordinal",
                    "CARDINAL": "Cardinal"
                }

                entidades_por_etiqueta = {}

                for entidad in doc.ents:
                    entidad_ingles = entidad.text
                    entidad_espanol = GoogleTranslator(source='en', target='es').translate(entidad_ingles)
                    etiqueta = entidad.label_
                    descripcion = etiquetas_descripciones.get(etiqueta, etiqueta)

                    # Si no existe, se agrega la entrada al diccionario, caso contrario si encuentra que sí existe, solamente lo añadirá al final del índice
                    if descripcion not in entidades_por_etiqueta:
                        entidades_por_etiqueta[descripcion] = [entidad_espanol]
                    else:
                        entidades_por_etiqueta[descripcion].append(entidad_espanol)

                # Imprimir las entidades agrupadas por etiqueta con descripciones en lenguaje natural
                for descripcion, entidades in entidades_por_etiqueta.items():
                    if descripcion != "PERSON" and descripcion != "ORG":
                        print(f"{descripcion}: {entidades}")

            print("\n")
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no existe.")
        except IOError:
            print(f"Error al intentar leer el archivo '{nombre_archivo}'.")

    if decision == 3:
        # Leer el texto ingresado de un archivo txt y verificar que se encuentre
        nombre_archivo = "texto.txt"

        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

                nlp = spacy.load("en_core_web_lg")

                nlp.add_pipe("textrank")

                contenido_ingles = GoogleTranslator(source="es", target="en").translate(contenido)

                doc = nlp(contenido_ingles)

                for enviado in doc._.textrank.summary(limit_sentences=5):
                    print(GoogleTranslator(source="en", target="es").translate(str(enviado)))

                print("\n")
                # rankeo de frases y su posicion
                frases_y_rangos = [(phrase.chunks[0], phrase.rank) for phrase in doc._.phrases]
                print(frases_y_rangos[:10])
                print("\n")
                print("\n")
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no existe.")
        except IOError:
            print(f"Error al intentar leer el archivo '{nombre_archivo}'.")

    if decision == 4:
        nombre_archivo = "texto.txt"
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:

                nlp = spacy.load("es_dep_news_trf")
                contenido = archivo.read()

                pos_descriptions = {
                    'PROPN': 'Nombre propio',
                    'VERB': 'Verbo',
                    'ADJ': 'Adjetivo',
                    'ADV': 'Adverbio',
                    'AUX': 'Auxiliar',
                    'CCONJ': 'coordinación de la conjunción',
                    'DET': 'Determinante',
                    'INTJ': 'Intersección',
                    'NOUN': 'Sustantivo',
                    'NUM': 'Numeral',
                    'PRON': 'Pronombre',
                    'SYM': 'Símbolo'
                }

                doc = nlp(contenido)

                # se crea un diccionario llamado pos_descriptions donde las claves son las etiquetas y su valor asociado es vacío
                tokens_por_clasificacion = {description: set() for description in pos_descriptions.values()}


                for token in doc:
                    pos = token.pos_

                    # utiliza la etiqueta POS para buscar la descripción que le corresponda en POS_descriptions
                    description = pos_descriptions.get(pos)

                    # si encuentra la etiqueta en el diccionario entra acá
                    if description:

                        # se agrupan las palabras en un mismo lugar
                        tokens_por_clasificacion[description].add(token.text)

                # se itera a través del del diccionario
                for description, tokens in tokens_por_clasificacion.items(): #.items() regresa tuplas
                    if tokens:
                        print(f"{description}: {tokens}")

                print("\n")

        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no existe.")
        except IOError:
            print(f"Error al intentar leer el archivo '{nombre_archivo}'.")

    if decision==5:

        while 1:

            seleccion = int(input("¿Qué deseas citar?:\n1)Sitio Web\n2)Artículo de revita\n3)Libro\n4)Vídeo\n5)Artículo de noticias en línea\n6)Salir\n>"))

            if seleccion==1:
                print("Ingrese los datos del sitio web:")
                autores = input("Autores (separados por comas): ").split(", ")
                año = input("Año de publicación: ")
                titulo = input("Título de la página o artículo: ")
                sitio_web = input("Nombre del sitio web: ")
                enlace = input("Enlace: ")
                autores_apa = " & ".join(autores)
                cita = f"{autores_apa} ({año}). {titulo}. {sitio_web}. {enlace}."

                print("\nCita en formato APA:")
                print(cita)

                with open('citas.txt', 'a') as f:
                    f.write("\n")
                    f.write(cita)

            if seleccion == 2:
                print("Ingrese los datos de la revista:")
                autores = input("Autores (separados por comas): ").split(", ")
                anio = input("Año de publicación: ")
                titulo = input("Título del artículo: ")
                revista = input("Nombre de la revista: ")
                volumen = input("Volumen: ")
                numero = input("Número: ")
                paginas = input("Páginas: ")

                autores_apa = " & ".join(autores)

                cita = f"{autores_apa} ({anio}). {titulo}. {revista}, {volumen}({numero}), {paginas}."

                print(cita)

                with open('citas.txt', 'a') as f:
                    f.write("\n")
                    f.write(cita)

            if seleccion == 3:
                print("Ingrese los datos del libro:")
                autores = input("Autores (separados por comas): ").split(", ")
                año = input("Año de publicación: ")
                titulo = input("Título del libro: ")
                editorial = input("Editorial: ")

                autores_apa = " & ".join(autores)
                cita = f"{autores_apa} ({año}). {titulo}. {editorial}."

                print(cita)

                with open('citas.txt', 'a') as f:
                    f.write("\n")
                    f.write(cita)

            if seleccion == 4:
                print("Ingrese los datos del vídeo:")
                autores = input("Autores (separados por comas): ").split(", ")
                año = input("Año de publicación: ")
                titulo = input("Título del vídeo: ")
                plataforma = input("Plataforma: ")
                enlace = input("Enlace: ")

                autores_apa = " & ".join(autores)
                cita = f"{autores_apa} ({año}). {titulo} [Video]. {plataforma}. {enlace}."

                print("\nCita en formato APA:")
                print(cita)

                with open('citas.txt', 'a') as f:
                    f.write("\n")
                    f.write(cita)

            if seleccion == 5:
                print("Ingrese los datos del artículo de noticias en línea:")
                autores = input("Autores (separados por comas): ").split(", ")
                año = input("Año de publicación: ")
                titulo = input("Título del artículo: ")
                fuente = input("Nombre de la fuente: ")
                enlace = input("Enlace: ")

                autores_apa = " & ".join(autores)
                cita = f"{autores_apa} ({año}). {titulo}. {fuente}. {enlace}."

                print(cita)

                with open('citas.txt', 'a') as f:
                    f.write("\n")
                    f.write(cita)

            if seleccion == 6:
                break

    if decision == 6:
        break