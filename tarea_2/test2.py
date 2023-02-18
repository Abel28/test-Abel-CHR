from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import json
import requests
from time import sleep
from random import randint
from selenium import webdriver

main_url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"

def search_url(page_number):
    return f"https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_refresh=1&_paginador_fila_actual={page_number}"



for i in range(3):
    driver = webdriver.Chrome()
    driver.get(search_url(i))
    sleep(randint(2,10))
    soup = BeautifulSoup(driver.page_source, "html.parser")

    