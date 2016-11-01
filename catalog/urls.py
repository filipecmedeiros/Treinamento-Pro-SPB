from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.ProductListView.as_view(), name='product_list'),
	url(r'^(?P<slug>[\w_-]+)/$', views.CategoryView.as_view(), name='category'),
	url(r'^produtos/(?P<slug>[\w_-]+)/$', views.product, name='product'),
]