from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import json
import requests
from time import sleep
from random import randint
from selenium import webdriver

#Funcion write_json es para incluir diccionarios de información de tablas en json
def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["data_seia"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

main_url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"

def search_url(page_number):
    return f"https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?nombre=&_paginador_refresh=1&_paginador_fila_actual={page_number}"



# Primero se llama a la url principal

main_url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"

r = requests.get(main_url).text

soup = BeautifulSoup(r, features="html.parser")


total_pages_div = soup.find("select", {"name": "pagina_offset"})

#Se obtiene el total de paginas
total_pages = [page.text for page in total_pages_div][-1]

#se lee la tabla de la página
table = soup.find(class_="tabla_datos")

#se leen las variables relacionadas a cada columna
table_head = table.find("thead")("th")

#se genera una lista de datos correspondiente a cada columna
# table_data = [[cell.text for cell in row.find_all("td")]
#                         for row in table("tr")]

# # se limpia los dos primeros elementos
# table_data.pop(0)
# table_data.pop(0)

# se genera una lista con cada titulo de columna
values_head = [value.text for value in table_head]


# # A continuación se genera un json con cada valor 
# dict_data = {}

# for key in values_head:
#     dict_data[key] = ""

# for row in table_data:
#     count_head = 0
#     for value in row:
#         dict_data[values_head[count_head]] = value
#         count_head+=1
#     write_json(dict_data)

driver = webdriver.Chrome()

for page in range(4):

    if page == 0:
        driver.get(main_url)
        sleep(randint(1,2))

        soup = BeautifulSoup(driver.page_source, features="html.parser")

        #se genera una lista de datos correspondiente a cada columna
        table_data = [[cell.text for cell in row.find_all("td")]
                                for row in table("tr")]

        # se limpia los dos primeros elementos
        table_data.pop(0)
        table_data.pop(0)

        # A continuación se genera un json con cada valor 
        dict_data = {}

        for key in values_head:
            dict_data[key] = ""

        for row in table_data:
            count_head = 0
            for value in row:
                dict_data[values_head[count_head]] = value
                count_head+=1
            write_json(dict_data)

    elif page == 1: continue

    else:

        
        driver.get(search_url(page))
        sleep(randint(1,2))

        #r = requests.get(search_url(page)).text

        soup = BeautifulSoup(driver.page_source, features="html.parser")

        #se genera una lista de datos correspondiente a cada columna
        table_data = [[cell.text for cell in row.find_all("td")]
                                for row in table("tr")]

        # se limpia los dos primeros elementos
        table_data.pop(0)
        table_data.pop(0)

        # A continuación se genera un json con cada valor 
        dict_data = {}

        for key in values_head:
            dict_data[key] = ""

        for row in table_data:
            count_head = 0
            for value in row:
                dict_data[values_head[count_head]] = value
                count_head+=1
            write_json(dict_data)








