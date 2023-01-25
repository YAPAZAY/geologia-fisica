from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = (
            'title', 'slug', 'short_description', 'publication_type',
            'subject', 'resource_url', 'main_picture'
        )

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Ej. Cuestionario de Meteorización'
                }
            ),
            'slug': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Ej. cuestionario-meteorizacion'
                }
            ),
            'short_description': forms.Textarea(
                attrs={
                    'class': 'textarea',
                    'rows': 3,
                    'placeholder':
                        'Ej. En este cuestionario pondrás '
                        'a prueba tus conocimientos ...'
                }
            ),
            'publication_type': forms.Select(),
            'subject': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Ej. Meteorización'
                }
            ),
            'resource_url': forms.URLInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Ej. https://ejemplo.com/cuestionario'}
            ),
            'main_picture': forms.ClearableFileInput(
                attrs={'class': 'file-input'}
            )
        }
