from django.urls import path, include, re_path
from .views import Dashboard, Edit_order, order_list, UserLoginView, UserLogoutView, online_order_list, delete_waiting

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    # path('enter/', DashHome.as_view(), name='home'),
    re_path('(?P<start>\d{4}-\d{2}-\d{2})/', Dashboard.as_view(), name='dashboard'),
    path('post/', Dashboard.as_view(), name='dashboard_post'),
    path('edit/', Edit_order.as_view(), name='edit'),
    path('order-list/', order_list, name="order_list"),
    path('online-order-list/', online_order_list, name="online-order_list"),
    path('delete_waiting/<int:pk>', delete_waiting, name="delete_waiting"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name='logout'),

]
