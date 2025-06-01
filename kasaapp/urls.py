# kasaapp/urls.py
from .views import login_view, logout_view
from django.urls import path
from .views import gun_sonu_devir_view, transaction_list_view, islem_ekle_view, kasa_durumu

urlpatterns = [
    path('gun-sonu-devir/', gun_sonu_devir_view, name='gun_sonu_devir'),
    path('islemler/', transaction_list_view, name='transaction_list'),  # bir sonraki adımda eklenecek
    path('islem-ekle/', islem_ekle_view, name='islem_ekle'),  # işlem ekleme sayfası
    path('kasa-durumu/', kasa_durumu, name='kasa_durumu'),  # kasa durumu sayfası
    path('login/', login_view, name='login'),  # giriş sayfası
    path('logout/', logout_view, name='logout'),  # çıkış sayfası
]
