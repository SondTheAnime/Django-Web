from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.
def ver_produto(request):
    
    produtos = Produto.objects.all()
    print(produtos)
    
    return render(request, "ver_produto.html", {'nome': 'Sond'})
    
    
def inserir_produto(request):
    if request.method == "GET":
        return render(request, "inserir_produto.html")
    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')        
        print(nome, descricao, preco, quantidade)
        
        if nome == "Sond":
            print("SOND VIADO")
        produto = Produto.objects.filter(nome=nome)
        
        if produto.exists():
            print("Produto já existe")
            return HttpResponse("Produto ja e")
        else:
            produto = Produto(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
            produto.save()
            return HttpResponse("Produto cadastrado com sucesso.")