from django.test import TestCase
from notas.servicos.models import Tipo
from notas.servicos.models import Servico



class TipoModelTest(TestCase):
    def setUp(self):
        self.obj = Tipo(
            title = 'Notas A1',
            description = 'Notas do tipo A1'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Tipo.objects.exists())



