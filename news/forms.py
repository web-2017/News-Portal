from django import forms

from .models import News, Category
import re
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
	# Вот так независымые формы делаются
	# widget = forms.TextInput(attrs={'class': 'form-control'}) передаем классы bootstrap нашей формы
	# title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
	# content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
	# 	'class': 'form-control',
	# 	'rows': 5
	# }))
	# is_published = forms.BooleanField(label='Опубликовано', initial=True)
	# categories = Category.objects.all()
	# category = forms.ModelChoiceField(queryset=categories, label='Категория', empty_label='Выбирите категорию', widget=forms.Select(attrs={'class': 'form-control'}))

	# Вот так формы наследуются из моделй все поля
	class Meta:
		model = News
		# fields = '__all__'
		fields = ['title', 'content', 'is_published', 'category']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
			'category': forms.Select(attrs={'class': 'form-control'})
		}

	# валидация
	def clean_title(self):
		title = self.cleaned_data['title']
		if re.match(r'\d', title):
			raise ValidationError('Название не должно называться с цифры')
		return title
