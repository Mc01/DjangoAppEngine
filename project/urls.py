from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.contrib.staticfiles.views import serve
from rest_framework import serializers, viewsets, routers
from rest_framework.permissions import IsAuthenticated


from django.contrib import admin
admin.autodiscover()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = (
    url(r'^api/', include(router.urls)),
    url(r'^_ah/', include('djangae.urls')),
    url(r'^csp/', include('cspreports.urls')),
    url(r'^auth/', include('djangae.contrib.gauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

if settings.DEBUG:
    urlpatterns += tuple(static(settings.STATIC_URL, view=serve, show_indexes=True))
