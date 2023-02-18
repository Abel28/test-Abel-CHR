# test-Abel-CHR

## Introducción

Para poder ejecutar este proyecto que conta de dos proyectos Django, se necesita una maquina virtual. En este caso yo utilicé pipenv y dejare las instrucciones sobre como se utilza.


## 1. Entorno Virtual

Para instalar pipenv se debe ejecutar desde la terminal lo siguiente:

```
pip install pipenv
```

### 2. Clonar Proyecto

Luego clonamos el proyecto en una carpeta que acomode al desarrollador:

```
git clone https://github.com/Abel28/test-Abel-CHR.git
```

Estando dentro de la carpeta del proyecto desde la terminal, procedemos a instalar el entorno virtual:

```
pipenv shell
```

Este comando, creará un entorno virtual con el nombre de la carpeta que contiene al proyecto y tambien para futuras ocaciones que se requiera lanzar el código, arrancará el entorno virtual.

### 3. Instalación de Librerias Requeridas

Para faciliar la instalación de los paquetes utilizados en este proyecto, existe el archivo requirements.txt. Con este, debemos ejecutar el siguiente comando desde la terminal dentro de la carpeta del proyecto:

```
pip install -r requirements.txt
```
---

### 4. Configuración de Base de datos

A continuación es importante configurar la base de datos PostgreSQL ya que es necesario para este test. Al existir dos proyectos Django independientes se debe cambiar los siguientes parametros, desde el archivo settings.py ubicado en tarea_1/tarea_1/settings.py y tarea_2/tarea_2/settings.py.

```

#Se debe considerar que los parametros de a continuación son los que se obtienen por defecto al instalar PostgreSQL en local
#Aqui dejo los datos por defecto que se crean al instalar postgresql:

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME' : 'postgres',
            'USER' : 'postgres',
            'PASSWORD': '',
            'PORT': ''
        }
}
```

Nota: Si no se tuvise instalado PostgreSQL aqui dejo el link donde están las instrucciones: [PostgreSQL Download](https://www.postgresql.org/download/)

## Tarea 1

El proyecto tarea_1 consta de la lectura de una API con información de estaciones de bicicletas. Y almacenarla en la base de datos, mostrarla desde el admin y generar una vista con la información.

### 1. Migración de Datos

Desde el directorio inicial tarea_1 se deben ejecutar las siguientes lineas de código para proceder con la migración de los modelos creados para esta ocación.

```
python manage.py makemigrations
```

```
python manage.py migrate
```

### 2. Creación de Super Usuario

Para poder tener visualización de la vista de administrador, se debe ejecutar el siguiente comando:

```
python manage.py createsuperuser
```

En esta parte se pedirá información exclusiva de quien ejecute este proyecto y para motivos prácticos de puede dejar Email en blanco.

Posteriormente se podrá ver desde el sitio http://127.0.0.1:8000/admin la información que almacenaremos desde la API

### 3. Arranque de servidor local

Para poder arrancar el proyecto se debe ejecutar el siguiente comando desde tarea_1/:

```
python manage.py runserver
```

Luego nos dirigimos a http://127.0.0.1:8000 y veremos una tabla vacía con un boton de Actualizar lista el cual debemos presionar y llamara a la vista que extrae la API y al finalizar se observa la tabla con todos los datos obtenidos.

Tambien si se quiere ver la información desde el administrador, nos dirigimos a http://127.0.0.1:8000/admin ingresamos los datos de usuario y contraseña que se crearon en unas instrucciones atrás, y tendremos a la vista en el panel izquierdo el modelo Estaciones el cual cuenta con una vista de algunas columnas con la información obtenida.

Ademas este proyecto cuenta con una vista Detail, la cual se puede acceder presionando el nombre de la estación y se mostrará información adicional obtenida en la API.


## Tarea 2

El proyecto tarea_2 consta de la lectura a travez de Selenium de una tabla de la página web de SEIA con la información de proyectos. Esta se debe almacenar en una base de datos, mostrarla desde el admin, generar una vista con la información y extraerla en .json.

### 1. Migración de Datos

Desde el directorio inicial tarea_2 se deben ejecutar las siguientes lineas de código para proceder con la migración de los modelos creados para esta ocación.

```
python manage.py makemigrations
```

```
python manage.py migrate
```

### 2. Creación de Super Usuario

Para poder tener visualización de la vista de administrador, se debe ejecutar el siguiente comando:

```
python manage.py createsuperuser
```

En esta parte se pedirá información exclusiva de quien ejecute este proyecto y para motivos prácticos de puede dejar Email en blanco.

Posteriormente se podrá ver desde el sitio http://127.0.0.1:8000/admin la información que almacenaremos desde la pagina web.

### 3. Arranque de servidor local

Para poder arrancar el proyecto se debe ejecutar el siguiente comando desde tarea_2/:

```
python manage.py runserver
```

NOTA IMPORTANTE: Al necesitarse selenium para acceder a estos datos, al momento de ejecutar Actualizar lista, se cargaran alrededor de 2800 páginas en donde se encuentran las tablas con la información, por lo que considere lo siguiente:

* Si va a ejecutar todas las páginas, considere que el pc no se puede suspender sino fallará la ejecución de obtención del archivo
* El ejecutar la totalidad de las páginas, dependiendo del rendimiento de cada computador, esto tomará un largo periodo de tiempo (en mi caso 2 horas aproximadamente)
* Sin embargo, podemos reducir la extención, ya que esto lo lee automaticamente, pero podemos cambiar la siguiente variable del archivo views.py en la linea 86 del código.

```
# Condición por defecto
proyects = create_dict_data(get_list_data(driver, total_pages), list_headers)


#Condición actualizada, la variable total_pages en este caso se cambia por 300 que significa que el codigo obtendrá las 300 primeras páginas.

proyects = create_dict_data(get_list_data(driver, 300), list_headers)
```

Luego nos dirigimos a http://127.0.0.1:8000 y veremos una tabla vacía con un boton de Actualizar lista el cual debemos presionar y llamara a la vista que extrae la información y al finalizar se observa la tabla con todos los datos obtenidos.

Tambien si se quiere ver la información desde el administrador, nos dirigimos a http://127.0.0.1:8000/admin ingresamos los datos de usuario y contraseña que se crearon en unas instrucciones atrás, y tendremos a la vista en el panel izquierdo el modelo Proyectos el cual cuenta con una vista de algunas columnas con la información obtenida.
