#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-26 13:34:46
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-26 13:34:46
@Description:
"""
from django import forms
from django.forms import widgets
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from users.models import UserGroup
from article.models import Article


class DocumentPublishForm(forms.Form):
    DEFAULT_ERROR_MESSAGES = {'required': '请填写该字段', 'invalid_choice': '请正确填写该字段'}
    receiver_group = forms.ChoiceField(required=True, error_messages={'required': '请选择接收用户组', 'invalid_choice': '请选择接收用户组'}, widget=widgets.Select(attrs={"class": "form-control"}))
    title = forms.CharField(required=True, error_messages = DEFAULT_ERROR_MESSAGES)
    number = forms.IntegerField(required=True, error_messages = DEFAULT_ERROR_MESSAGES)
    author = forms.CharField(required=True, error_messages = DEFAULT_ERROR_MESSAGES)
    content = forms.CharField(required=True, error_messages = DEFAULT_ERROR_MESSAGES)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DocumentPublishForm, self).__init__(*args, **kwargs)

        self.fields['receiver_group'].choices = self.get_receiver_group()

        self.fields['title'].widget = widgets.TextInput(attrs={"class": "form-control"})
        self.fields['number'].widget = widgets.NumberInput(attrs={"class": "form-control"})
        self.fields['author'].widget = widgets.TextInput(attrs={"readonly": True, "value": self.user.realname, "class": "form-control"})
        self.fields['content'].widget = CKEditorUploadingWidget()

        self.fields['receiver_group'].label = "接收用户组"
        self.fields['title'].label = "公文标题"
        self.fields['number'].label = "公文编号"
        self.fields['author'].label = "发布人"
        self.fields['content'].label = ""
        
    def get_receiver_group(self):
        receiver_group = (('-1', '请选择接收用户组'),)
        for group in UserGroup.objects.all():
            group_tup = ((str(group.id), group.name),)
            receiver_group += group_tup

        return receiver_group

    def is_valid(self):
        valid = super(DocumentPublishForm, self).is_valid()

        if not valid:
            return valid

        if self.cleaned_data['receiver_group'] == '-1':
            self._errors['no_receiver_group'] = '* 请选择一个接收用户组'
            return False

        return True


class ArticlePublishForm(forms.ModelForm):
    DEFAULT_ERROR_MESSAGES = {'required': '请填写该字段', 'invalid_choice': '请正确填写该字段'}
    
    class Meta:
        model = Article
        fields = ['title', 'category', 'author', 'origin', 'content', 'has_check', 'is_banner']
        widgets = {
            'title': widgets.TextInput(attrs={"class": "form-control"}),
            'category': widgets.Select(attrs={"class": "form-control"}),
            'author': widgets.TextInput(attrs={"class": "form-control"}),
            'origin': widgets.Select(attrs={"class": "form-control"}),
            'content': CKEditorUploadingWidget(),
        }
        labels = {
            'title': "文章标题",
            'category': "文章板块",
            'author': "作者",
            'origin': "单位",
            'content': "",
            'has_check': "是否通过审核",
            'is_banner': "是否用于首页轮播图"
        }
        error_messages = {
            'title': {
                'max_length': "文章题目过长。",
            }, 
        }