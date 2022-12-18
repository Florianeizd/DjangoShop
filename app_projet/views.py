from django.shortcuts import render
from .models import Article
from .models import ArticleForm
from django.shortcuts import redirect
from .models import Order
from .models import Cart

def index(request):
    list_articles = Article.objects.all()
    context = {'list_articles': list_articles}
    return render(request, 'index.html' , context)

# def article(request):  
#     if request.method == "POST":  
#         form = ArticleForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect('/app_projet')  
#             except:  
#                 pass  
#     else:  
#         form = ArticleForm()  
#     return render(request,'article.html',{'form':form})  

def article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/app_projet')
    return render(request, "article.html", {'form': form})


def show(request):  
   articles = Article.objects.all()  
   return render(request,"show.html",{'articles':articles})  

def edit(request, id):  
    article = Article.objects.get(id=id)  
    return render(request,'edit.html', {'article':article})  

def update(request, id):  
    article = Article.objects.get(id=id)  
    form = ArticleForm(request.POST, instance = article)  
    if form.is_valid():  
        form.save()  
        return redirect("/app_projet")  
    return render(request, 'edit.html', {'article': article})  

def destroy(request, id):  
    article = Article.objects.get(id=id)  
    article.delete()  
    return redirect("/app_projet")

def addtocart(request):
    cart = Cart()
    cart.save()
    order = Order()
    order.article = Article.objects.get(id=1)
    order.quantity = 1
    order.save()
    cart.orders.add(order)
    cart.save()
    request.session['cart_id'] = cart.id
    return redirect('/app_projet')

def cart(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    context = {'cart': cart}
    return render(request, 'cart.html', context)