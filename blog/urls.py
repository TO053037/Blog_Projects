from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('<int:category_pk>', views.ArticleList.as_view(), name='category'),
                  path('show_user_detail/<int:user_mode>', views.ArticleList.as_view(), name='show_user_detail'),
                  path('', views.ArticleList.as_view(), name='index'),
                  path('detail/<int:pk>', views.ArticleDetail.as_view(), name='detail_article'),
                  path('get_good_count_ajax/<int:article_pk>',
                       views.get_good_count_ajax, name='get_good_count_ajax'),
                  path('create_comment/<int:article_pk>',
                       views.CreateCommentView.as_view(), name='create_comment'),
                  path('edit_commet/<int:pk>/<int:article_pk>/',
                       views.EditComment.as_view(), name='edit_comment'),
                  # path('delete/comment/<int:pk>/<int:article_pk>',
                  # views.DeleteComment.as_view(), name='delete_comment'),
                  path('delete_comment_Ajax', views.delete_comment_ajax, name='delete_comment_Ajax'),
                  path('show_user_comment', views.ShowUserComment.as_view(), name='show_user_comment'),
                  path('do_good_ajax/<int:article_pk>', views.do_good_ajax, name='do_good_ajax'),
                  path('read_later_ajax', views.read_later_ajax, name='read_later_ajax'),
                  path('get_all_is_read_later', views.get_all_is_read_later, name='get_all_is_read_later'),
                  path('get_category_title_ajax', views.get_category_title_ajax, name='get_category_title_ajax'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
