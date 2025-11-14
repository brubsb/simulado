from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto

# ✅ Listar e buscar produtos
def lista_produtos(request):
    query = request.GET.get('q')
    if query:
        produtos = Produto.objects.filter(nome__icontains=query)
    else:
        produtos = Produto.objects.all().order_by('nome')

    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos, 'query': query})

# ✅ Adicionar produto
def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade_estoque')
        estoque_minimo = request.POST.get('estoque_minimo')
        descricao = request.POST.get('descricao')

        # validações simples
        if not nome or not preco:
            messages.error(request, 'Os campos Nome e Preço são obrigatórios.')
            return redirect('adicionar_produto')

        Produto.objects.create(
            nome=nome,
            categoria=categoria,
            preco=preco,
            quantidade_estoque=quantidade or 0,
            estoque_minimo=estoque_minimo or 0,
            descricao=descricao
        )
        messages.success(request, 'Produto cadastrado com sucesso!')
        return redirect('lista_produtos')

    return render(request, 'produtos/form_produto.html', {'acao': 'Adicionar'})

# ✅ Editar produto
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.categoria = request.POST.get('categoria')
        produto.preco = request.POST.get('preco')
        produto.quantidade_estoque = request.POST.get('quantidade_estoque')
        produto.estoque_minimo = request.POST.get('estoque_minimo')
        produto.descricao = request.POST.get('descricao')

        if not produto.nome or not produto.preco:
            messages.error(request, 'Os campos Nome e Preço são obrigatórios.')
            return redirect('editar_produto', id=id)

        produto.save()
        messages.success(request, 'Produto atualizado com sucesso!')
        return redirect('lista_produtos')

    return render(request, 'produtos/form_produto.html', {'produto': produto, 'acao': 'Editar'})

# ✅ Excluir produto
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    messages.success(request, 'Produto excluído com sucesso!')
    return redirect('lista_produtos')
