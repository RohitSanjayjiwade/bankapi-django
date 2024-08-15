from rest_framework import serializers
from .models import Bank, Branch

class BranchSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='branch-detail', lookup_field='ifsc', read_only=True,)
    bank_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Branch
        fields = ['url','ifsc', 'branch', 'address', 'city', 'district', 'state', 'bank_name']
    
    def get_bank_name(self, obj):
        """
        Returns the name of the bank associated with the branch
        """
        return {"Bank Name":obj.bank_id.name}

class BankSerializer(serializers.ModelSerializer):
    branches = serializers.HyperlinkedRelatedField(many=True, view_name='branch-detail', read_only=True, lookup_field='ifsc')

    class Meta:
        model = Bank
        fields = ['url', 'name', 'branches']
