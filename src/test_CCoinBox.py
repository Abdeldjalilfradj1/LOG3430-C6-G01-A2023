import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def setUp(self):
        self.cb = CCoinBox()

    def test_add25(self):
        self.cb.ajouter_25c()
        self.assertEqual(1, self.cb.get_monnaie_courante())


