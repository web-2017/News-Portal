from django.contrib import admin

# Register your models here.
from .models import News, Category


# class редактор - это что будет показано в админке
class NewsAdmin(admin.ModelAdmin):
	# перечисляем какие поля будут отображаться в списке таблицы березтся из .models
	list_display = ('id', 'category', 'title', 'created_at', 'updated_at', 'is_published',)
	list_display_links = ('id', 'title', 'created_at')  # переход в статью по ссылке на статью в админке
	search_fields = ['title', 'content']  # поля по котормы мы можем искать
	list_editable = ('is_published',)  # Можно редактировать прям в заголовках поле
	list_filter = ('is_published', 'category')  # Указываем поля для сортировки


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')
	list_display_links = ('id', 'title')  # переход в статью по ссылке на статью в админке
	search_fields = ['title', 'category']  # поля по котормы мы можем искать


# регистрация в админка раздела News, + NewsAdmin
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
