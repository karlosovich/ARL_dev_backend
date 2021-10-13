from django.conf                                  import settings
from rest_framework                               import generics, status
from rest_framework.response                      import Response
from rest_framework.permissions                   import IsAuthenticated
from rest_framework_simplejwt.backends            import TokenBackend

from authAppExample.models.deposit                import Deposit
from authAppExample.models.account                import Account
from authAppExample.serializers.depositSerializer import DepositSerializer
from authAppExample.serializers.accountSerializer import AccountSerializer


class DepositDetailView(generics.RetrieveAPIView):
    serializer_class   = DepositSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Deposit.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)


class DepositsAccountView(generics.ListAPIView):
    serializer_class   = DepositSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Deposit.objects.filter(account_id=self.kwargs['account'])
        return queryset


class DepositCreateView(generics.CreateAPIView):
    serializer_class   = DepositSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = DepositSerializer(data=request.data['deposit_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        account = Account.objects.get(id=request.data['deposit_data']['account'])
        account.balance += request.data['deposit_data']['amount']
        account.save()

        return Response("Consignación exitosa", status=status.HTTP_201_CREATED)