from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from boards import views
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls


urlpatterns = [
    url(r'^$', views.BoardListView.as_view(), name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/account/$', accounts_views.my_account, name='my_account'),
    url(r'^settings/account/(?P<user_pk>\d+)/$', accounts_views.UserListView.as_view(), name='user_account'),
    url(r'^settings/account/(?P<user_pk>\d+)/letter/$', accounts_views.letter, name='letter'),
    url(r'^settings/account/(?P<user_pk>\d+)/letter/(?P<letter_pk>\d+)/read/$', accounts_views.letter_read, name='letter_read'),
    url(r'^settings/account/(?P<user_pk>\d+)/letter/(?P<letter_pk>\d+)/handle/$', accounts_views.letter_handle, name='letter_handle'),
    url(r'^settings/account/(?P<user_pk>\d+)/follow/$', accounts_views.follow, name='follow'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    url(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/favor/$', views.favorite, name='favorite'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/join/$', views.join, name='join'), # join 和 quit 写在同一个视图中
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/changestate/$', views.changestate, name='changestate'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/changepercent/(?P<percent>\d+)/$', views.changepercent, name='changepercent'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/giveup/$', views.giveup, name='giveup'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/submit/$', views.submit, name='submit'),
    # url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/quit/$', views.quit, name='quit'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/letter/(?P<letter_pk>\d+)/accept/$', accounts_views.accept, name='accept'), # 同意入团
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/letter/(?P<letter_pk>\d+)/allow/$', accounts_views.allow, name='allow'), # 允许退团
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/letter/(?P<letter_pk>\d+)/acceptgiveup/$', accounts_views.acceptgiveup, name='acceptgiveup'), # 允许解散
    url(r'^admin/', admin.site.urls),
    url(r'^search/(?P<pk>.+)/$', views.search, name='search'), #搜索内容直接加在url
    url(r'^inbox/notifications/', include(notifications.urls, namespace='notifications')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

