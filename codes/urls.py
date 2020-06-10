from django.urls import path, include
from .views import IndexView, CodeDetailView, code_detail

urlpatterns = [
    # path(r'<code_name>/', code_details, name='code_detail'),
    path('', IndexView.as_view(), name='codes_list'),
    # 路由配置url地址http://127.0.0.1:8000/A1C-Front%20axle%207.5%20t/包括了name和title，主要是有G code，只从code上面无法去路由，所以需要搜索title
    path(r'<code_name>/', code_detail, name='code_detail'),

]



