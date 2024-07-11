from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name = "topics" ),
    path("topics/<int:topic_id>/", views.topic, name = "topic"),
    path('new_topic/', views.new_topic, name ="new_topic"),
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
    path('topics/<int:pk>/delete/', views.TopicDeleteView.as_view(), name = 'topic_delete'),
    path('new_comment/<int:entry_id>/', views.new_comment, name='new_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
