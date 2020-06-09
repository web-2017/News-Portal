from django.db import models
from django.urls import reverse_lazy


# Create your models here.

class News(models.Model):
	# blank=True означает не обязательное поле
	# verbose_name имя заголовка поля
	# max_length макс длина контена
	# FileField - любой тип а ImageField - только картинки
	# upload_to = куда загружать
	# /%Y/%m/%d/ разбить на года, месяцы и дни
	title = models.CharField(max_length=150, verbose_name='Наименование')
	content = models.TextField(blank=True, verbose_name='Контент')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
	photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото', blank=True)
	is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

	# Если в категории есть новости, то models.PROTECT не даст удалить категорию
	category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

	def test_str(self):
		return 'Hello World'

	def get_absolute_url(self):
		# reverse_lazy('название маршрута', kwards={для построения маршрута, нужен id})
		return reverse_lazy('view_news', kwargs={'news_id': self.pk})

	# Чтобы вернуть в виде строки заголовки статей,
	# надо вернуть в __str__ по дефолту вернет Object Object
	def __str__(self):
		return self.title

	# Изменения  в админке и в views и в templates везде применятся
	class Meta:
		verbose_name = 'Новость'  # заголовоки
		verbose_name_plural = 'Новости'
		ordering = ['created_at']  # дополнительная сортировка, если первая не прошла


# Создаем категорию
class Category(models.Model):
	# db_index индексирует это поле title, и делает его более быстрым для поиска
	title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

	def get_absolute_url(self):
		# reverse_lazy('название маршрута', kwards={для построения маршрута, нужен id})
		return reverse_lazy('category', kwargs={'category_id': self.pk})

	# Для того чтобы возвращался в выпадающем спике выбора категории не объект а название категории
	# вернет на страницу html заголовок статьи а не Object Object
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Категория'  # заголовоки
		verbose_name_plural = 'Категории'
		ordering = ['title']
