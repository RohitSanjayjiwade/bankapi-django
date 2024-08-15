from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

@api_view(['GET'])
def index(request, format=None):
    return Response({
        "Bank-List": reverse("bank-list", request=request, format=format),
        "Branch-List": reverse("branch-list", request=request, format=format)
    })

class BankList(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

bank_list = BankList.as_view()

class BankDetail(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    lookup_field = 'pk'

bank_detail = BankDetail.as_view()


class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

branch_list = BranchList.as_view()

class BranchDetail(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'
    
branch_detail = BranchDetail.as_view()