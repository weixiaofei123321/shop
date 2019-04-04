from django.shortcuts import render,get_object_or_404
from  .models import 产品列表 ,商品类别表
# Create your views here.
def 总览页(request):
    所有类别 = 商品类别表.objects.all()
    类别与商品 = []
    for 每个类别 in 所有类别:
        类别与商品.append((每个类别,产品列表.objects.filter(所属类别=每个类别,已上架 = True)[:3]))
    content = {'类别与商品': 类别与商品,'所有类别':所有类别}
    return render(request,'shopping/home.html',content)


def 单类页(request,每个类别_id):
    所有类别 = 商品类别表.objects.all()
    所需类别 = get_object_or_404(商品类别表,id = 每个类别_id)
    类别与商品 = [(所需类别,产品列表.objects.filter(所属类别 = 所需类别,已上架 = True)[:5])]

    content = {'类别与商品': 类别与商品,'所有类别':所有类别}
    return render(request,'shopping/home.html',content)

def 详情页(request,每个类别_id,每件商品_id):
    所有类别 = 商品类别表.objects.all()
    商品 = get_object_or_404(产品列表,id = 每件商品_id)

    if 商品.已上架:
        content = {'商品': 商品, '所有类别': 所有类别}
        return render(request, 'shopping/detail.html', content)

