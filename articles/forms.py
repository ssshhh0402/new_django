from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=140, 
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder':'제목입력하거라'
            }
        )
    )
    content = forms.CharField(
        # label 내용 수정
        label='내용',
        # Django form 에서 html 속성 지정 -> widget
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'내용을 입력하세요',
                'row':5,
                'cols':60,
            }
        )
    )