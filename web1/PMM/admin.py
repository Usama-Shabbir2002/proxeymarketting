from django.contrib import admin

# Register your models here.
from .models import Admin
admin.site.register(Admin)

from .models import Pm
admin.site.register(Pm)

from .models import Pmm
admin.site.register(Pmm)

from .models import Adminpaid
admin.site.register(Adminpaid)

from .models import Commission
admin.site.register(Commission)

from .models import Order
admin.site.register(Order)

from .models import Product
admin.site.register(Product)

from .models import Pmmreservation
admin.site.register(Pmmreservation)