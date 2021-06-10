
from django.urls import path
from Library_App import views
from django.contrib.auth import views as ad

urlpatterns = [
    path('',views.home,name="hm"),
    path('pro/',views.profile,name='profile'),
    path('cp/',views.complaint,name='complaint'),
    path('Books/',views.Books,name='Books'),
    path('abt/',views.about,name="at"),
    path('cnt/',views.contact,name="ct"),
     path('lg/',views.Login_user,name="log"),
   
    path('rg/',views.regi,name="rg"),
    path('ds/',views.dashboard,name="dsh"),
    path('lgo/',ad.LogoutView.as_view(template_name='html/logout.html'),name="logo"),
    path('updf/',views.updf,name="upf"),
    path('ch/',views.cgf,name="cg"),
    path('rst/',ad.PasswordResetView.as_view(template_name="html/resetpass.html"),name="reset_password"),
    path('rst_done/',ad.PasswordResetDoneView.as_view(template_name='html/resetpassworddone.html'),name='password_reset_done'),
    path('rst_confirm/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name='html/resetconfirm.html'),name='password_reset_confirm'),
    path('ba/',views.Books_AvailF,name='books_avail'),
    path('sr/',views.sendrequest,name='send_request'),
    path('bas/',views.studentbooks_avail,name='studentbooks_avail'),
    path('myreq/',views.myreq,name='myreq'),
    path('notedelete/<str:id>',views.datadelete,name="datadelete"),
    path('Bookdelete/<str:id>',views.Bookdelete,name="Bookdelete"),
    path('Bookedit/<str:id>',views.Bookedit,name="Bookedit"),
    path('viewn/',views.viewnt,name='viewn'),
    path('notipending/',views.notipending,name="notipending"),
    path('accepting/',views.accepting,name="accepting"),
    path('rejecting/',views.rejecting,name="rejecting"),
    path('noteaccept/<str:id>',views.acceptadmin,name="acceptadmin"),
    path('notereject/<str:id>',views.rejectadmin,name="rejectadmin"),
    path('books_return/',views.books_return,name='books_return'),
    path('books_st_have/',views.books_st_have,name="bk"),
    path('return_accept/<int:id>',views.return_accept,name='return_accept'),
    path('reqp/',views.requestform,name='pm'),
    path('gper/',views.adminpermissions,name='gperm'),
    path('eper/<int:k>/',views.updatepermissions,name='up'),
    path('fine/',views.fine,name='fine'),
    path('issue_book/',views.issue_book,name='issue_book'),
]