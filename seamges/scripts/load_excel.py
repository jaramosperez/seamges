import csv  # https://docs.python.org/3/library/csv.html
import codecs

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from pacientes.models import Paciente
from patologias.models import Patologia
from casos.models import Caso

def run():
    with codecs.open('casos/monitoreo.csv', encoding='utf-8', errors='ignore') as fdata:
        reader = csv.reader(fdata)
        next(reader) # AVANZA PARA NO CONTAR LOS TITULOS DE LAS COLUMNAS

        Paciente.objects.all().delete()
        Patologia.objects.all().delete()
        Caso.objects.all().delete()

        for row in reader:
            print(row)

            paciente, created = Paciente.objects.get_or_create(run=row[(1)],dv=row[2],nombres=row[4],apellidos=row[3])
            patologia, created = Patologia.objects.get_or_create(nombre=row[0])

            caso, created = Caso.objects.get_or_create(patologia=patologia, paciente=paciente, fecha_inicio=row[5], fecha_limite=row[6])
