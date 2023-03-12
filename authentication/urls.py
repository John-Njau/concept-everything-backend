from django.urls import path

from .views import UserView, PostList

#
# router = routers.DefaultRouter()
# router.register('posts', PostList)

urlpatterns = [
    # path('', include(router.urls)),
    path('user/', UserView.as_view()),
    path('posts/', PostList.as_view()),

]
