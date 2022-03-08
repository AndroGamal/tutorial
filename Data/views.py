from os import access
from rest_framework.decorators import APIView
from Data import permision, test_Serializer,models
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class test_apiview(APIView):
    view=test_Serializer.test_serializer
    def get(self,request,format=None):
        return Response({"test":"done2"})

    def post(self,request):
        all=self.view(data=request.data)
        if all.is_valid():
            name=all.validated_data.get("name")
            email=all.validated_data.get("email")
            password=all.validated_data.get("password")
            return Response({"Name":name,"Email":email,"Password":password})
        else :
            return Response(all.error,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        return Response({"method":"PUT"})

    def patch(self,request,pk=None):
        return Response({"method":"PATCH"})

    def delete(self,request,pk=None):
        return Response({"method":"DELETE"})

class test_veiwset(viewsets.ViewSet):
    veiw=test_Serializer.test_serializer
    def list(self,request):
        a=["kns","jsbkcj","ksdcu"]
        return Response({"test":a})


    def create(self,request):
        all=self.veiw(data=request.data)
        if all.is_valid():
            name=all.validated_data.get("name")
            email=all.validated_data.get("email")
            password=all.validated_data.get("password")
            print(password,email,name)
            return Response({"Name":name,"Email":email,"Password":password})
        else :
            return Response(all.error,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(selrf,request,pk=None):
        return Response({"http_method":"GET"})


    def update(self,request,pk=None):
        return Response({"http_method":"PUT"})


    def partial_update(self,request,pk=None):
        return Response({"http_method":"PATCH"})

    def delete(self,request,pk=None):
        return Response({"http_method":"DELETE"})

# Create your views here.

class test_veiwset_model(viewsets.ModelViewSet):
    serializer_class=test_Serializer.use_test_serializer
    queryset=models.DataBase.objects.all()
    authentication_classes={TokenAuthentication,}
    permission_classes=(permision.owner,)

class Api_login(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES