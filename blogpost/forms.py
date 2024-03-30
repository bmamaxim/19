from django import forms

from blogpost.models import BlogPost


class BlogPostForms(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'preview',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
