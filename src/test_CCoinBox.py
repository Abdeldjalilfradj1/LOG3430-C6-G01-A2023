import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):
    
    def test_pass(self):
        pass
    def test_ajouter_25c(self):
        self.coinBox = CCoinBox()
        self.coinBox.ajouter_25c()
        self.assertFalse(self.coinbox.get_vente_permise())

    def test_vente(self):
        self.coinBox = CCoinBox()
        self.coinBox.ajouter_25c()
        self.coinBox.ajouter_25c()
        self.coinBox.ajouter_25c()
        self.coinBox.ajouter_25c()
        self.coinBox.vente()
        self.assertTrue(self.coinbox.get_vente_permise())

