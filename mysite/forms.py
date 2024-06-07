from django import forms#表單推薦用這種寫法 ppt50幾頁
from mysite import models
from mysite.models import Comment,  Member

# mysite/forms.py
from django import forms
from .models import Member

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'email', 'password', 'borndate', 'gender', 'phoneNum']
        widgets = {
            # 'password': forms.PasswordInput(),
            'username':forms.TextInput(attrs={'class':'form-control'}),
        }

    password_confirm = forms.CharField(label='確認密碼', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "密碼不匹配")

        return cleaned_data

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'score']
        widgets = {
            'score': forms.RadioSelect(choices=Comment.Score)
        }
