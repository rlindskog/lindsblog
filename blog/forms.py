from django import forms

class CategoryForm(forms.Form):
    CATEGORY_CHOICES = (
        ('All', 'All'),
        ('Tech', 'Tech'),
        ('Sports', 'Sports'),
        ('Music', 'Music'),
        ('Philosophy', 'Philosophy'),
    )
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='category')