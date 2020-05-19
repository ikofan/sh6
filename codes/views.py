from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import CodesH6, CodeImg


# Create your views here.


class IndexView(ListView):
    model = CodesH6
    template_name = 'codes/index.html'
    context_object_name = 'codes_list'


class CodeDetailView(DetailView):
    model = CodesH6
    template_name = 'codes/detail.html'
    context_object_name = 'code'


def code_detail(request, code_name_title):
    # code_name_title的格式是G-Front Axle,所以把title分离出来，进行搜索并返回obj
    # 不用title搜索了，数据库中删除了G code
    # code = get_object_or_404(CodesH6, code_name=code_name_title.split('-')[0])
    code = CodesH6.objects.filter(name=code_name_title.split('-')[0])
    # images = get_object_or_404(CodeImg, code_name=code_name_title.split('-')[0])
    # codes.models.CodeImg.MultipleObjectsReturned: get() returned more than one CodeImg -- it returned 3!
    # code = get_object_or_404(CodesH6, title=code_name.upper())
    # get_object_or_404似乎对于多个返回值无法处理报错，用objects.get也不行，所以改为filter，可以返回多个值
    # images是一个code可能对应的多张图片
    images = CodeImg.objects.filter(code_name=code_name_title.split('-')[0])
    context = {'code': code,
               'images': images,
               }

    return render(request, 'codes/detail.html', context=context)
