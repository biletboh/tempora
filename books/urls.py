from django.conf.urls import url

from . import views


app_name = 'books'


urlpatterns = [
            url(r'^$', views.BookList.as_view(), name='list'),
            url(r'^create/$', views.CreateBook.as_view(),
                name='create'),
            url(r'^(?P<slug>[-\w]+)/$', views.BookPage.as_view(), name='page'),
            url(r'^update/list/$', views.UpdateBookList.as_view(),
                name='update_list'),
            url(r'^update/(?P<slug>[-\w]+)/$',
                views.UpdateBook.as_view(),
                name='update'),
            url(r'^delete/(?P<pk>[0-9]+)/$',
                views.DeleteBook.as_view(),
                name='delete'),
            url(r'^create/order/$', views.CreateOrder.as_view(),
                name='create_order'),
            url(r'^process/order/(?P<pk>[0-9]+)/$',
                views.ProcessOrder.as_view(),
                name='process_order'),
            url(r'^orders/list/$', views.OrderList.as_view(),
                name='order_list'),
            ]
