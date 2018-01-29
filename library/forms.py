from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError

from library.models import Book
from xf_crud.generic_forms import XFModelForm
from xf_crud.generic_lists import XFModelList

from crispy_forms.layout import Layout, Div, Field
from crispy_forms.bootstrap import  TabHolder, Tab
from django import forms
from django.core.urlresolvers import reverse



class BookForm(XFModelForm):

    class Meta:
        model = Book
        fields = ["title", "author", "publication_date", "category"]
        title = "Booooooooook me"

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Enter the book's title"
        self.fields['publication_date'].widget.attrs['class'] = "date-field datepicker"

        self.helper.layout = Layout(
            TabHolder(
                Tab('Book',
                    Field('title', 'publication_date',)
                ),
                Tab('Author',
                    Field('author', 'category', )
                )
            )
        )


class SmallBookForm(XFModelForm):

    class Meta:
        model = Book
        fields = ["title"]

        title = "Quickly add a book"

    def __init__(self, *args, **kwargs):
        super(SmallBookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Enter the book's title"

    def clean_title(self):

        title = self.cleaned_data['title']
        if title.find("2") >= 0:
            raise forms.ValidationError("Can't have the word 2 in the title when adding a small book.")

        return title


class SmallBookList(XFModelList):

    def __init__(self, model):
        super(SmallBookList, self).__init__(model)
        self.list_field_list = (("title",))
        self.list_description = "List of small books below."
        self.list_title = "Our smallbooks"
        self.list_hint = "Below is a list of the small books that you can borrow."
        self.default_permissions = ('add', 'change', 'delete', 'view')
        self.search_field = "title"
        self.preset_filters = {
            '': 'All',
            'recent': 'Only with "Ze"',
        }


    def get_queryset(self, search_string, model, preset_filter):

        if preset_filter == 'recent':
            return Book.objects.filter(title__contains='Ze').filter(title__contains=search_string)
        else:
            return super(SmallBookList, self).get_queryset(search_string, model, preset_filter)

class BookList(XFModelList):

    def __init__(self, model):
        super(BookList, self).__init__(model)
        self.form_field_list = (("title", "publication_date", "category", "author"))
        self.list_description = "List of books below."
        self.list_title = "Our books"
        self.list_hint = "Below is a list of the books that you can borrow."
        self.default_permissions = ('add', 'change', 'delete', 'view')
        self.search_field = "title"
