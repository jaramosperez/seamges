from openpyxl import load_workbook
from django.utils.dateparse import parse_date
# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from pacientes.models import Paciente
from patologias.models import Patologia
from casos.models import Caso
from establecimientos.models import Establecimiento

def run():
    Paciente.objects.all().delete()
    Patologia.objects.all().delete()
    Caso.objects.all().delete()
    wb = load_workbook(filename='scripts/despliegaColasAction.xlsx')
    sheet = wb.get_sheet_by_name('despliegaColasAction')

    for row in sheet.rows:
        paciente, created = Paciente.objects.get_or_create(run=row[(1)],dv=row[2],nombres=row[4],apellidos=row[3])
        patologia, created = Patologia.objects.get_or_create(nombre=row[0])
        establecimiento, created = Establecimiento.objects.get_or_create(nombre=row[9])

        caso, created = Caso.objects.get_or_create(patologia=patologia, paciente=paciente, fecha_inicio=parse_date(row[5]), fecha_limite=parse_date(row[6]), establecimiento=establecimiento)

        # RECORRE EL DOCUMENTO FILA POR FILA [YA VIENE EXCLUIDO LAS CABECERAS DE]