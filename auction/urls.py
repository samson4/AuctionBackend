from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuctionView.as_view(),name='auction'),
    
    path('lots/<uuid:id>/',views.LotView.as_view(),name='lots'),
    path('<uuid:id>/lots/',views.LotsListView.as_view(),name='lots-list'),
    path('lots/<uuid:id>/',views.LotCreateView.as_view(),name='create-lots'),
    path('<uuid:id>/',views.AuctionDetailView.as_view() ,name='auction-detail'),
    path('subscribed/',views.AllSubscribedAuctionsView.as_view(),name='auction-subscribed'),
    path('subscribe/<uuid:id>/',views.AuctionSubscribeView.as_view() ,name='auction-subscribe')
]
