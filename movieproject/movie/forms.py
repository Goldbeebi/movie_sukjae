from django import forms

class SearchForm(forms.Form): #검색받을 Form 설정
    search = forms.CharField(label = 'Search For Movies...', max_length=100)