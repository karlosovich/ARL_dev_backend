from authAppExample.models.account import Account
from authAppExample.models.user    import User
from rest_framework                import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Account
        fields = ['balance', 'lastChangeDate', 'isActive']

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.user)
        account = Account.objects.get(id=obj.id)
        return {
            'id'             : account.id,
            'balance'        : account.balance,
            'lastChangeDate' : account.lastChangeDate,
            'isActive'       : account.isActive,
            'user' : {
                'id'    : user.id,
                'name'  : user.name,
                'email' : user.email
            }
        }