import csv  # https://docs.python.org/3/library/csv.html
import codecs

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# COMANDO PARA CARGAR PROFESIONES
# pipenv run manage.py runscript load_prestaciones

# IMPORTANDO ENTIDAD
from prestaciones.models import Prestacion


def run():
    with codecs.open('media/ListadoPrestaciones.csv', encoding='utf-8', errors='ignore') as fdata:
        reader = csv.reader(fdata)
        next(reader)  # AVANZA PARA NO CONTAR LOS TITULOS DE LAS COLUMNAS

        Prestacion.objects.all().delete()

        # RECORRE EL DOCUMENTO FILA POR FILA [YA VIENE EXCLUIDO LAS CABECERAS DE ]
        for row in reader:
            print(row)
            # REALIZA LA VERIFICACIÓN SI EXISTE LA PROFESIÓN O LA CREA
            prestacion, created = Prestacion.objects.get_or_create(nombre=row[0])