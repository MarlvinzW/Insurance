from django.db.models.signals import post_save
from django.dispatch import receiver

from payments.models import AccountBalance
from users.models import User


@receiver(post_save, sender=User)
def account_balance(sender, instance, created, **kwargs):
    user = User.objects.get(id=instance.id)
    if created:
        if not user.is_staff:
            AccountBalance.objects.create(
                holder=user
            )

