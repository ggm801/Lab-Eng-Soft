from telnetlib import STATUS
from django.test import TestCase
from .models import Voo, VooReal, Usuario
# Create your tests here.

# Create test


class VooTestCRUD (TestCase):
    @classmethod
    def setUpTestData(cls):
        Voo.objects.create(DH_PREVISTO_SAIDA='2022-10-10 12:40:32',
                           DH_PREVISTO_CHEGADA='2022-10-10 18:40:32',
                           ID_VOO='100',
                           NM_AEROPORTO_SAIDA='Sao Paulo - Viracopos (VCP)',
                           NM_AEROPORTO_CHEGADA='Brasília (BSB)',
                           NM_COMPANHIA_AEREA='AZUL')

    def test_create_id(self):
        Voo_1 = Voo.objects.get(ID_VOO='100')
        self.assertEqual(Voo_1.ID, 1)

    def test_update_(self):
        Voo_1 = Voo.objects.get(ID_VOO='100')
        self.assertEqual(Voo_1.NM_COMPANHIA_AEREA, 'AZUL')
        Voo_1.NM_COMPANHIA_AEREA = 'TAM'
        Voo_1.save()
        self.assertEqual(Voo_1.NM_COMPANHIA_AEREA, 'TAM')

    def test_delete_ID_Voo(self):
        tamOrig = len(Voo.objects.all())
        Voo.objects.filter(ID=1).delete()
        tamFinal = len(Voo.objects.all())
        self.assertEqual(tamFinal, tamOrig - 1)

    def test_retrive_id(self):
        Voo_1 = Voo.objects.get(ID_VOO='100')
        print(Voo_1.DH_PREVISTO_CHEGADA)
        self.assertEqual(Voo_1.ID, 1)
        self.assertEqual(Voo_1.NM_AEROPORTO_CHEGADA, 'Brasília (BSB)')


class VooRealTestCRUD (TestCase):
    @classmethod
    def setUpTestData(cls):
        Voo.objects.create(DH_PREVISTO_SAIDA='2022-10-10 12:40:32',
                           DH_PREVISTO_CHEGADA='2022-10-10 18:40:32',
                           ID_VOO='100',
                           NM_AEROPORTO_SAIDA='Sao Paulo - Viracopos (VCP)',
                           NM_AEROPORTO_CHEGADA='Brasília (BSB)', NM_COMPANHIA_AEREA='AZUL')
        Voo1 = Voo.objects.get(ID_VOO='100')
        VooReal.objects.create(ID_VOO=Voo1, NM_STATUS='Pousando')

    def test_create_ID_VooReal(self):
        VooReal_1 = VooReal.objects.get(ID=1)
        self.assertEqual(VooReal_1.ID, 1)

    def test_delete_ID_VooReal(self):
        VooReal_1 = VooReal.objects.get(ID=1)
        self.assertEqual(VooReal_1.ID, 1)
        tamOrig = len(VooReal.objects.all())
        VooReal.objects.filter(ID=1).delete()
        tamFinal = len(VooReal.objects.all())
        self.assertEqual(tamFinal, tamOrig - 1)

    def test_update_(self):
        Voo_1 = VooReal.objects.get(ID=1)
        self.assertEqual(Voo_1.NM_STATUS, 'Pousando')
        Voo_1.NM_STATUS = 'Stopped'
        Voo_1.save()
        self.assertEqual(Voo_1.NM_STATUS, 'Stopped')


class UsuarioTest (TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(ID_USUARIO='USER1',
                               FIRST_NAME='Kylian',
                               LAST_NAME='Mbappe',
                               SENHA='password',
                               USER_PERMISSION='1')

    def test_create_id(self):
        User1 = Usuario.objects.get(ID_USUARIO='USER1')
        self.assertEqual(User1.ID, 1)

    def test_password_correct(self):
        User1 = Usuario.objects.get(ID_USUARIO='USER1')
        self.assertEqual(User1.SENHA, 'password')

    def test_update(self):
        User1 = Usuario.objects.get(ID_USUARIO='USER1')
        self.assertEqual(User1.ID, 1)
        User1.SENHA = 'new_password'
        User1.save()
        self.assertEqual(User1.SENHA, 'new_password')

    def test_delete_ID_usuario(self):
        tamOrig = len(Usuario.objects.all())
        Usuario.objects.filter(ID=1).delete()
        tamFinal = len(Usuario.objects.all())
        self.assertEqual(tamFinal, tamOrig - 1)

    def test_retrive_permission_usuario(self):
        User1 = Usuario.objects.get(ID='1')
        print(User1.FIRST_NAME)
        self.assertEqual(User1.USER_PERMISSION, 1)
