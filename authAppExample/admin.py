from django.contrib      import admin
from .models.user        import User
from .models.account     import Account
from .models.transaction import Transaction
from .models.deposit     import Deposit

# Register your models here.
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Deposit)