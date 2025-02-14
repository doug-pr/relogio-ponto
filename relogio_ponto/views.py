from django.shortcuts import render, redirect, get_object_or_404
from .models import Horario
from datetime import datetime

def adicionar_horario(request):
    if request.method == 'GET':
        horarios = Horario.objects.all().order_by('entrada_1')
        return render(request, 'adicionar_horarios.html', {'horarios': horarios})
    
    elif request.method == 'POST':
        entrada_1 = request.POST.get('entrada_1')

        data_hora = datetime.strptime(entrada_1, '%Y-%m-%d %H:%M:%S')
        hora = data_hora.strftime("%H:%M:%S")

        data = request.POST.get('data')
        saida_1 = request.POST.get('saida_1')
        entrada_2 = request.POST.get('entrada_2')
        saida_2 = request.POST.get('saida_2')
        entrada_3 = request.POST.get('entrada_3')
        saida_3 = request.POST.get('saida_3')

        print('#' * 50)
        print(data)
        print('#' * 50)

        if not saida_1:
            saida_1 = None

        if not entrada_2:
            entrada_2 = None

        if not saida_2:
            saida_2 = None

        if not entrada_3:
            entrada_3 = None

        if not saida_3:
            saida_3 = None

        '''
        horario = Horario(
            entrada_1 = entrada_1,
            saida_1 = saida_1,
            entrada_2 = entrada_2,
            saida_2 = saida_2,
            entrada_3 = entrada_3,
            saida_3 = saida_3
        )
        '''
        #horario.save()
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

    data_atual = datetime.now()
    data = data_atual.strftime('%Y-%m-%d')
    print(data)
    print('#' * 50 + 'Entrada 1:')
    print(data + ' ' + entrada_1)
    print('#' * 50 + 'Data Atualização:')
    print(data_atualizacao)

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
    
    
    horario.save()

    return redirect('adicionar_horario')