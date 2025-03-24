from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def calcular_diferenca_horario(hora_inicial_1: str, hora_final_1: str, hora_inicial_2: str, hora_final_2: str, hora_inicial_3: str, hora_final_3: str) -> str:
    hora_vazia = '00:00'

    if not hora_inicial_1:
        hora_inicial_1 = hora_vazia
    if not hora_final_1:
        hora_final_1 = hora_vazia
    if not hora_inicial_2:
        hora_inicial_2 = hora_vazia
    if not hora_final_2:
        hora_final_2 = hora_vazia
    if not hora_inicial_3:
        hora_inicial_3 = hora_vazia
    if not hora_final_3:
        hora_final_3 = hora_vazia

    formato = "%H:%M"
    e1 = datetime.strptime(hora_inicial_1, formato)
    s1 = datetime.strptime(hora_final_1, formato)
    e2 = datetime.strptime(hora_inicial_2, formato)
    s2 = datetime.strptime(hora_final_2, formato)
    e3 = datetime.strptime(hora_inicial_3, formato)
    s3 = datetime.strptime(hora_final_3, formato)

    diferenca = (s1 - e1) + (s2 - e2) + (s3 - e3)

    horas = diferenca.seconds // 3600
    minutos = (diferenca.seconds % 3600) // 60

    return f"{horas}:{minutos:02d}"