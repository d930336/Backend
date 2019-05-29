#import viewsets
from rest_framework import viewsets,status
from rest_framework import mixins

#import response
from rest_framework.response import Response

# model / Serializers
from .models import Coupon,User
from .serializers import CouponSerializer,UserSerializer
from .models import judge_duplicate_userid,judge_duplicate_username

# only view
class CouponViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


# can't delete
class UserViewSet(mixins.CreateModelMixin
                ,mixins.ListModelMixin
                ,mixins.RetrieveModelMixin
                ,viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self,request,**kwargs):
        try:
            user_id =self.get_object().user_id
            user_name = self.get_object().user_name
        except:
            user_id = request.data
            user_name = request.data
        user_id = user_id.get('user_id')
        user_id_duplicate = judge_duplicate_userid(user_id=user_id)

        user_name = user_name.get('user_name')
        user_name__duplicate = judge_duplicate_username(user_name=user_name)


        if user_id_duplicate:
            return Response('ID已被使用', status=status.HTTP_200_OK)
        if user_name__duplicate:
            return Response('名稱已被使用', status=status.HTTP_200_OK)

        #create method
        user_id = request.data.get('user_id')
        user_name = request.data.get('user_name')
        user_gender = request.data.get('user_gender')
        users = User.objects.create(user_id=user_id, user_name=user_name, user_gender=user_gender)
        serializer = UserSerializer(users, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)