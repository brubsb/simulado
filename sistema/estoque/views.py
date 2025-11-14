from django.shortcuts import render, redirect
from django.contrib import messages
from produtos.models import Produto
from .models import Movimentacao
from datetime import date

def gestao_estoque(request):
    # Lista de produtos em ordem alfabética (algoritmo bubble sort)
    produtos = list(Produto.objects.all())
    movimentacoes = Movimentacao.objects.select_related('produto').order_by('-data')[:10]


    # Ordena manualmente (Bubble Sort)
    n = len(produtos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if produtos[j].nome.lower() > produtos[j + 1].nome.lower():
                produtos[j], produtos[j + 1] = produtos[j + 1], produtos[j]

    # Registrar movimentação
    if request.method == 'POST':
        produto_id = request.POST.get('produto')
        tipo = request.POST.get('tipo')
        quantidade = int(request.POST.get('quantidade'))

        if not produto_id or not tipo or quantidade <= 0:
            messages.error(request, 'Preencha todos os campos corretamente.')
            return redirect('gestao_estoque')

        produto = Produto.objects.get(id=produto_id)

        if tipo == 'entrada':
            produto.quantidade_estoque += quantidade
        elif tipo == 'saida':
            if produto.quantidade_estoque < quantidade:
                messages.error(request, 'Quantidade em estoque insuficiente.')
                return redirect('gestao_estoque')
            produto.quantidade_estoque -= quantidade

        produto.save()

        # Cria o registro da movimentação
        Movimentacao.objects.create(
            produto=produto,
            tipo=tipo,
            quantidade=quantidade,
            data=date.today()
        )

        # Verifica alerta de estoque mínimo
        if produto.quantidade_estoque < produto.estoque_minimo:
            messages.warning(request, f"Atenção: {produto.nome} está abaixo do estoque mínimo!")

        messages.success(request, 'Movimentação registrada com sucesso!')
        return redirect('gestao_estoque')

    return render(request, 'estoque/gestao_estoque.html', {
        'produtos': produtos,
        'movimentacoes': movimentacoes
    })

