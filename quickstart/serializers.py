from django.contrib.auth.models import User, Group
from rest_framework import serializers


#我们要定义一些序列化程序、我们创建一个名为serializers.py的文件、 来用做我们的数据库表示
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')