

from django.views.generic import TemplateView
from .models import Post

class IndexView(TemplateView):
    template_name = "index.html"

from django.views.generic import ListView

# ListViewは一覧を簡単に作るためのView

class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    template_name = "list.html"
    model = Post

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    template_name = "create.html"
    model = Post
    
    # 編集対象にするフィールド
    fields = ["title", "body", "category"]
    success_url = reverse_lazy('list')