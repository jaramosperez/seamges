import csv  # https://docs.python.org/3/library/csv.html
import codecs

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# COMANDO PARA CARGAR PROFESIONES
# pipenv run manage.py runscript load_profesionales

# IMPORTANDO ENTIDAD
from profesionales.models import Profesional
from profesiones.models import Profesion


def run():
    with codecs.open('media/ListadoProfesionales.csv', encoding='utf-8', errors='ignore') as fdata:
        reader = csv.reader(fdata)
        next(reader)  # AVANZA PARA NO CONTAR LOS TITULOS DE LAS COLUMNAS

        Profesional.objects.all().delete()

        # RECORRE EL DOCUMENTO FILA POR FILA [YA VIENE EXCLUIDO LAS CABECERAS DE ]
        for row in reader:
            print(row)
            # REALIZA LA VERIFICACIÓN SI EXISTE LA PROFESIÓN O LA CREA
            profesion, created = Profesion.objects.get_or_create(nombre=row[0])
            profesional, created = Profesional.objects.get_or_create(profesion=profesion, run=row[1], nombres=row[2], primer_apellido=row[3], segundo_apellido=row[4])
