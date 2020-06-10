from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import News, Category
from .forms import NewsForm


# Create your views here.
class HomeNews(ListView):
	model = News # заменяет News.objects.all()
	template_name = 'news/index.html' # тут мы говорим какая страница для News
	context_object_name = 'news' # тут определяем как будет назваться объект для рендера в темплейте
	# extra_context = {'title': 'Главная'} # только для статичных данных extra_context

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Главная страница'
		return context

	# get_queryset - переопределяет в классе запрос
	def get_queryset(self):
		return News.objects.filter(is_published=True).order_by('-created_at')


# def index(request):
# 	# print(dir(request))
# 	# ожно тут делать сортировку, но лучше в моделях в class Meta
# 	# news = News.objects.order_by('-created_at') сортировка по дате
# 	# news = News.objects.all() обычно, все данные без сортировки
#
# 	news = News.objects.order_by('-created_at')
# 	# categories = Category.objects.all() # объединили в templatetags
# 	context = {
# 		'news': news,
# 		'title': 'Список новостей',
# 	}
# 	return render(request, 'news/index.html', context)

class NewsCategory(ListView):
	model = News
	template_name = 'news/category.html'
	context_object_name = 'news'
	allow_empty = False # 404 запрет на показ несуществующих даннах


	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
		return context

	def get_queryset(self):
		return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

# def get_category(request, category_id):
# 	news = News.objects.filter(category_id=category_id)
# 	# categories = Category.objects.all() # объединили в templatetags
# 	category = Category.objects.get(pk=category_id)
# 	context = {'news': news, 'category': category}
# 	return render(request, 'news/category.html', context=context)


def view_news(request, news_id):
	# news_item = News.objects.get(pk=news_id)
	news_item = get_object_or_404(News, pk=news_id)
	context = {'news_item': news_item}
	return render(request, 'news/view_news.html', context=context)


def add_news(request):
	if request.method == 'POST':
		form = NewsForm(request.POST)

		if form.is_valid():
			# **form.cleaned_data - это очищенные полученные данные, где ** распаковка данных словаря
			# print(form.cleaned_data)
			# news = News.objects.create(**form.cleaned_data)
			# redirect на конкретную страницу
			# return redirect('home')
			# т.к objects.create возвращает нам объект с данными, то мы можем
			# сразу на конкретную новость сделать редирект, передав переменную в redirect
			news = form.save()
			return redirect(news)
	else:
		# либо форма пустая
		form = NewsForm()
	return render(request, 'news/add_news.html', {'form': form})
