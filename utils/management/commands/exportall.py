from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load all data files'

    def handle(self, *args, **options):
        call_command('dumpdatautf8', 'accounts', '--indent', '4', '--output', 'accounts/seed/accounts.json')
        call_command('dumpdatautf8', 'usuario', '--indent', '4', '--output', 'usuario/seed/usuario.json')
        call_command('dumpdatautf8', 'inventario', '--indent', '4', '--output', 'inventario/seed/inventario.json')
        call_command('dumpdatautf8', 'compra', '--indent', '4', '--output', 'compra/seed/compra.json')
        call_command('dumpdatautf8', 'venta', '--indent', '4', '--output', 'venta/seed/venta.json')

        self.stdout.write(self.style.SUCCESS('All data files export'))