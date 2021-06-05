from crud import serialize
from crud.models import DetailsModel
from crud.serialize import DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class DetailsTable(APIView):
    def get(self,request):
        detailsObj=DetailsModel.objects.all()
        dlSerializeObj=DetailsSerializer(detailsObj,many=True)
        return Response(dlSerializeObj.data)
    
    def post(self,request):
        serializeobj=DetailsSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class DetailsUpdate(APIView):
    def post(self,request,pk):
        try:
            detailObj=DetailsModel.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")

        serializeobj=DetailsSerializer(detailObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)


class DetailsDelete(APIView):
    def post(self,request,pk):
        try:
            detailObj=DetailsModel.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        detailObj.delete()
        return Response(200)