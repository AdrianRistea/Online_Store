from django.urls import path
from store import views
from store.views import remove_from_cart

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home_page'),
    path('', views.HomeTemplateView.as_view(), name='base'),
    path('login', views.HomeTemplateView.as_view(), name='login'),
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('category/<int:pk>', views.CategoryProductsView.as_view(), name='category_list'),
    path('product_detail/<int:product_id>/', views.product_details, name='product-detail'),
    path('create_product/', views.ProductCreateView.as_view(), name="create-product"),
    path('modify_product/<int:pk>/', views.ProductUpdateView.as_view(), name="modify-product"),
    path('delete_product/<int:product_id>/', views.delete_product, name="delete-product"),
    path('open-cart/', views.open_cart_view, name='open_cart'),
    path('add-product-to-cart/', views.add_product_to_cart, name='add_product_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove-product-from-cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove-product-from-cart'),
    path('contact/', views.contact, name='contact'),
    path('contact-confirm/', views.contact_confirm_view, name='contact_confirm'),
    path('search/', views.search_results, name='search_results'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('proceed_to_payment/', views.proceed_to_payment, name='proceed_to_payment'),
    path('add-category/', views.CategoryCreateView.as_view(), name="add_category"),
    path('produse-reduse/', views.reduced_products, name="reduced-products"),
    path('comenzile_mele/', views.IstoricCumparaturiView.as_view(), name='comenzile-mele'),
    path('multumim/', views.SuccesPaymentView.as_view(), name='ms'),
    path('mail_contact/', views.SuccesMailView.as_view(), name='mail-contact'),

    path('send_email/', views.send_email, name='send-email'),

]
