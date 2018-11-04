DJANGO BITRIX
---
Python lib for BITRIX API

INSTALLING
---
`$ pip instlal bitrix`
#### CONFIGURE YOUR APP AND BITRIX
1) Create webhook in your Bitrix \
![alt_tag](https://helpdesk.bitrix24.ru/upload/medialibrary/966/%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0_%D0%B2%D0%B5%D0%B1%D1%85%D1%83%D0%BA%D0%B8.png "WEBHOOK EXAMPLE")
2) Copy your webhook url (exclude `profile/`)\
![alt_tag](https://dev.1c-bitrix.ru/images/curs_b24/marketplace/wch_1.png "WEBHOOK URL EXAMPLE")
3) Create `BITRIX_WEBHOOK_URL` parameter in your `settings.py` and set equal to your webhook url
4) Thats's it!

#### USAGE
You can use Bitrix24 class everywhere
1) As mixin
```python
from django.views.generic import View
from bitrix.main import Bitrix24

class ClassBasedView(Bitrix24,View):
    def do_someting(self):
        """
            do something
        """
        params = {
            'key1':'value1',
            'key2':'value2'
        }
        self.call_method("your method",params)
        
```
2) With `django.signals`
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from bitrix.main import Bitrix24

@receiver(post_save, sender=YourModel, dispatch_uid="sell_levels")
def set_level(sender, instance, created, **kwargs):
    """
        do something
    """
    bx24 = Bitrix24()
    params = {
        'key1':'value1',
        'key2':'value2'
    }
    bx24.call_method("method",params)    

```
