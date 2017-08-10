from django.core.signals import request_started
from django.dispatch import receiver

#from library.models import Book
#from xf_crud.auth.permission_mixin import PermissionMixin
from xf_system.views import XFNavigationViewMixin
from xf_system.xf_navigation import add_navigation


def load_navigation(sender, navigation_trees, request):

    # Each app can create one navigation tree. Navigation trees from multiple apps cannot be merged, by design
    # In this example, the app name is "library"
    #if not navigation_trees.has_key("library"):
    # PYTHON3 UPDATE
    if not "library" in navigation_trees:
        navigation_tree = []
        navigation_trees["library"] = navigation_tree

    #PermissionMixin.user_has_model_perm(Book, "view")

    navigation_tree = navigation_trees["library"]

    add_navigation(navigation_tree, 'Library', "Books", "/library/book/", "fa-world", "Books")
    add_navigation(navigation_tree, 'Library', "Books", "/library/category/", "fa-world", "Categories")
    add_navigation(navigation_tree, 'Library', "Authors", "/library/author/", "fa-world", "Authors")

    #add_navigation(navigation_tree, 'Header', "Section 1", "", "fa-world", "BBC")
    #add_navigation(navigation_tree, 'Header', "Section 1", "www.cnn.com", "fa-world", "CNN")

    #add_navigation(navigation_tree, 'Header', "Section 1", "www.aljazeera.com", "fa-world", "Al Jazeera")
    #add_navigation(navigation_tree, 'Header', "Section 1", "www.bbc.com/international", "fa-world", "BBC International", "BBC")
    #add_navigation(navigation_tree, 'Header', "Section 1", "www.bbc.com/UK", "fa-world", "BBC UK", "BBC")

    return



XFNavigationViewMixin.navigation_tree_observers.append(load_navigation)