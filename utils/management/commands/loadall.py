from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load all data files'

    def handle(self, *args, **options):
        call_command('loaddatautf8', 'accounts/seed/accounts.json')
        call_command('loaddatautf8', 'usuario/seed/usuario.json')
        call_command('loaddatautf8', 'inventario/seed/inventario.json')
        call_command('loaddatautf8', 'compra/seed/compra.json')
        call_command('loaddatautf8', 'venta/seed/venta.json')

        self.stdout.write(self.style.SUCCESS('All data files export'))