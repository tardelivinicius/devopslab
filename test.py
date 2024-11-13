# -*- coding: utf-8 -*-
from app import app
import unittest

class Test(unittest.TestCase):
    
    def setUp(self):
        # Cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # Envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # Compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # Verifica o retorno do conteudo da pagina
        self.assertEqual(self.result.data.decode('utf-8'), "Vini v1.0 - System Check")
