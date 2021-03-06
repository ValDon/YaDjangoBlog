from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
# from rest_framework.filters import OrderingFilter

from groceries.models import CompanyCategory, Company
from .base import BaseAPIView


# 普通view
from django.views.generic.base import View
from django.http import HttpResponse,JsonResponse


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# 公司
class CompanyCatetorySerializer(serializers.ModelSerializer):
    companys = CompanySerializer(source='company_set', many=True, read_only=True)

    class Meta:
        model = CompanyCategory
        fields = ('id', 'name', 'companys')

class WebResourceyLogoAPIView(BaseAPIView):
    def get(self, request):
        bc = CompanyCategory.objects.all()
        serializer = CompanyCatetorySerializer(bc, many=True)
        res = {"results": serializer.data}
        return Response(res)

class BaikeKgAPIView(BaseAPIView):
    def get(self, request, name):

        from pymongo import MongoClient
        from bson import json_util
        import json

        client = MongoClient('mongodb', 27017)        
        db = client.KG
        collection = db.baike
        data = collection.find({'name': name})
        data = json.loads(json_util.dumps(data))

        # if data: 
        #     # data.pop('_id')

        res = {"results": data}
        return Response(res)