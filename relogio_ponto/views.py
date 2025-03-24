from django.shortcuts import render, redirect, get_object_or_404
from .models import Horario
from datetime import datetime, timedelta
from .utils import calcular_diferenca_horario

def adicionar_horario(request):
    if request.method == 'GET':
        horarios = Horario.objects.all().order_by('entrada_1')
        return render(request, 'adicionar_horarios.html', {'horarios': horarios})
    
    elif request.method == 'POST':

        data = request.POST.get('data')
        entrada_1 = request.POST.get('entrada_1')
        saida_1 = request.POST.get('saida_1')
        entrada_2 = request.POST.get('entrada_2')
        saida_2 = request.POST.get('saida_2')
        entrada_3 = request.POST.get('entrada_3')
        saida_3 = request.POST.get('saida_3')

        hora_digitada_entrada_1 = datetime.strptime(entrada_1, '%H:%M')
        hora_entrada_1 = hora_digitada_entrada_1.strftime("%H:%M:%S")
        data_hora_entrada_1 = data + ' ' + hora_entrada_1

        print('#' * 50)
        print(data)
        print(hora_digitada_entrada_1)
        print(hora_entrada_1)
        print('#' * 50)
        print(data_hora_entrada_1)
        
        if not saida_1:
            data_hora_saida_1 = None
        else:
            hora_digitada_saida_1 = datetime.strptime(saida_1, '%H:%M')
            hora_saida_1 = hora_digitada_saida_1.strftime("%H:%M:%S")
            data_hora_saida_1 = data + ' ' + hora_saida_1

        if not entrada_2:
            data_hora_entrada_2 = None
        else:
            hora_digitada_entrada_2 = datetime.strptime(entrada_2, '%H:%M')
            hora_entrada_2 = hora_digitada_entrada_2.strftime("%H:%M:%S")
            data_hora_entrada_2 = data + ' ' + hora_entrada_2

        if not saida_2:
            data_hora_saida_2 = None
        else:
            hora_digitada_saida_2 = datetime.strptime(saida_2, '%H:%M')
            hora_saida_2 = hora_digitada_saida_2.strftime("%H:%M:%S")
            data_hora_saida_2 = data + ' ' + hora_saida_2

        if not entrada_3:
            data_hora_entrada_3 = None
        else:
            hora_digitada_entrada_3 = datetime.strptime(entrada_3, '%H:%M')
            hora_entrada_3 = hora_digitada_entrada_3.strftime("%H:%M:%S")
            data_hora_entrada_3 = data + ' ' + hora_entrada_3

        if not saida_3:
            data_hora_saida_3 = None
        else:
            hora_digitada_saida_3 = datetime.strptime(saida_3, '%H:%M')
            hora_saida_3 = hora_digitada_saida_3.strftime("%H:%M:%S")
            data_hora_saida_3 = data + ' ' + hora_saida_3

        
        horario = Horario(
            entrada_1 = data_hora_entrada_1,
            saida_1 = data_hora_saida_1,
            entrada_2 = data_hora_entrada_2,
            saida_2 = data_hora_saida_2,
            entrada_3 = data_hora_entrada_3,
            saida_3 = data_hora_saida_3
        )
        
        horario.save()
        return redirect('adicionar_horario')
    
def excluir_horario(request, id):
    horario = get_object_or_404(Horario, id=id)
    horario.delete()
    return redirect('adicionar_horario')

def atualizar_horario(request, id):
    horario = get_object_or_404(Horario, id=id)
    data_atualizacao = request.POST.get('data_atualizacao')
    entrada_1 = request.POST.get('entrada_1')
    saida_1 = request.POST.get('saida_1')
    entrada_2 = request.POST.get('entrada_2')
    saida_2 = request.POST.get('saida_2')
    entrada_3 = request.POST.get('entrada_3')
    saida_3 = request.POST.get('saida_3')

    horario.entrada_1 = data_atualizacao + ' ' + entrada_1
    horario.saida_1 = data_atualizacao + ' ' + saida_1
    horario.entrada_2 = data_atualizacao + ' ' +  entrada_2
    horario.saida_2 = data_atualizacao + ' ' + saida_2

    if not entrada_3:
        horario.entrada_3 = None
    else:
        horario.entrada_3 = data_atualizacao + ' ' + entrada_3

    if not saida_3:
        horario.saida_3 = None
    else:
        horario.saida_3 = data_atualizacao + ' ' + saida_3
    
    total_horas_dia = calcular_diferenca_horario(entrada_1, saida_1, entrada_2, saida_2, entrada_3, saida_3)
    print(total_horas_dia)
    print('$' * 50)
    request.session['diferenca_horario'] = total_horas_dia

    horario.save()

    return redirect('adicionar_horario')