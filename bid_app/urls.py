from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.Logout, name="logout"),
    path('add_product', views.Add_Product, name="add_product"),
    path('view_product', views.view_product, name="view_product"),
    path('delete_product/<int:pid>', views.delete_product, name="delete_product"),
    path('product_detail/<int:pid>', views.product_detail, name="product_detail"),
    path('make_participants/<int:pid>', views.make_participants, name="make_participants"),
    path('getbidhistory/<int:pid>', views.getbidhistory, name="getbidhistory"),
    path('startbidding/<int:pid>', views.startbidding, name="startbidding"),
    path('changelivetocomplete/<int:pid>', views.changelivetocomplete, name="changelivetocomplete"),
    path('changeupcomingtolive/<int:pid>', views.changeupcomingtolive, name="changeupcomingtolive"),
    path('delete_admin_product/<int:pid>', views.delete_admin_product, name="delete_admin_product"),
    path('delete_category/<int:pid>', views.delete_category, name="delete_category"),
    path('change_status/<int:pid>', views.change_status, name="change_status"),
    path('delete_sub_category/<int:pid>', views.delete_sub_category, name="delete_sub_category"),
    path('delete_user/<int:pid>', views.delete_user, name="delete_user"),
    path('delete_participant/<int:pid>', views.delete_participant, name="delete_participant"),
    path('profile/<int:pid>', views.profile, name="profile"),
    path('email_verify/<int:pid>', views.email_verify, name="email_verify"),
    path('generateotp/<int:pid>', views.generateotp, name="generateotp"),
    path('admin_product_detail/<int:pid>', views.admin_product_detail, name="admin_product_detail"),
    path('bidder_detail/<int:pid>', views.bidder_detail, name="bidder_detail"),
    path('seller_detail/<int:pid>', views.seller_detail, name="seller_detail"),
    path('edit_product/<int:pid>', views.edit_product, name="edit_product"),
    path('edit_profile', views.Edit_profile, name="edit_profile"),



    path('load-courses/', views.load_courses, name='ajax_load_courses'),
    path('meetwinners/', views.meetwinners, name='meetwinners'),
    path('all_product/', views.all_product, name='all_product'),


    path('admin-home/', views.admin_home, name='admin_home'),
    path('loginadmin', views.Admin_Login, name="loginadmin"),
    path('view_seller_user/', views.view_seller_user, name="view_seller_user"),
    path('view_buyer_user', views.view_buyer_user, name="view_buyer_user"),
    path('admin_view_product', views.Admin_product, name="admin_view_product"),
    path('add_categary', views.Add_Categary, name="add_categary"),
    path('view_categary', views.View_Categary, name="view_categary"),
    path('add_sub_categary', views.Add_Sub_Categary, name="add_sub_categary"),
    path('view_sub_category', views.View_Sub_Categary, name="view_sub_category"),
    path('view_participants', views.view_participants, name="view_participants"),
    path('view_winner', views.View_winner, name="view_winner"),
    path('change_password', views.Change_Password, name="change_password"),



    path('change_user_status/<int:pid>', views.change_user_status, name="change_user_status"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)