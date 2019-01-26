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
from django.conf import settings
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from users.models import UserGroup
from .models import Document


class DocumentPublishForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['receiver_group', 'receiver', 'title', 'number', 'author', 'content']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DocumentPublishForm, self).__init__(*args, **kwargs)

        self.fields['receiver_group'].widget = widgets.Select(choices=self.get_receiver_group())
        self.fields['receiver'].widget = widgets.Textarea(attrs={"readonly": True, "cols": "40", "rows": "4"})
        self.fields['title'].widget = widgets.TextInput()
        self.fields['number'].widget = widgets.NumberInput()
        self.fields['author'].widget = widgets.TextInput(attrs={"readonly": True, "value": self.user.realname})
        self.fields['content'].widget = CKEditorUploadingWidget()

    def get_receiver_group(self):
        RECEIVER_GROUP = ()
        for group in UserGroup.objects.all():
            group_tup = ((str(group.id), group.name),)
            RECEIVER_GROUP += group_tup

        return RECEIVER_GROUP