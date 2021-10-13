from django.db import models
from .account  import Account

class Deposit(models.Model):
    id              = models.AutoField(primary_key=True)
    account         = models.ForeignKey(Account, related_name='deposit_account', on_delete=models.CASCADE)
    amount          = models.IntegerField(default=0)
    register_date   = models.DateTimeField(auto_now_add=True, blank=True)
    note            = models.CharField(max_length=100)
    depositer_name  = models.CharField(max_length=50)