from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.core import serializers

from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver

from .models import Project

import time

# Create your views here.

def get_url(page_number):
    variable_url = f"https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?nombre=&_paginador_refresh=1&_paginador_fila_actual={page_number}"
    return variable_url

def create_dict(headers):
        dict_data = {}
        for key in headers:
            dict_data[key] = ""
        return dict_data

def create_dict_data(data, headers):
        list_dict = []
        dict_data = create_dict(headers)

        for row in data:
            count_row = 0
            dict_data = create_dict(headers)
            for value in row:
                dict_data[headers[count_row]] = value
                count_row += 1
            list_dict.append(dict_data)

        return list_dict

def get_list_data(driver, total_pages):
    
        lista_datos = []
        lista = []
        
        for page in range(total_pages+1):

            try:
        
                driver.get(get_url(page))
            
            except NoSuchElementException:
                time.sleep(2)
            
            table = driver.find_elements("xpath",".//*[@class='tabla_datos']/tbody/tr")
            
            for row in table:
                lista = []
                for i in row.find_elements(By.TAG_NAME,"td"):
                    lista.append(i.text)
                lista_datos.append(lista)
                
        return lista_datos

def load_data(request):

    url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"

    options = webdriver.ChromeOptions()
    

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    headers = driver.find_elements("xpath","//*[@class='tabla_datos']/thead/tr/th")
    list_headers = [row.text for row in headers]
    total_pages = int(driver.find_elements("xpath",".//select[@name='pagina_offset']")[-1].text.split("\n")[-1])

    
    proyects = create_dict_data(get_list_data(driver, total_pages), list_headers)

    

    for proyect in proyects:
        Project.objects.create(
            id=proyect[list_headers[0]],
            nombre=proyect[list_headers[1]],
            tipo=proyect[list_headers[2]],
            region=proyect[list_headers[3]],
            tipologia=proyect[list_headers[4]],
            titular=proyect[list_headers[5]],
            inversion=proyect[list_headers[6]],
            fecha=proyect[list_headers[7]],
            estado=proyect[list_headers[8]]
        )

    driver.close()

    return HttpResponseRedirect(reverse_lazy('projects:list'))


def get_json(request):
    projects = Project.objects.all()
    projects_list = serializers.serialize('json', projects)
    return HttpResponse(projects_list, content_type="text/json-comment-filtered")


class ProyectListView(ListView):
    model = Project
    template_name = "project/projects_list.html"
    