import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_golve_default_weight(self):
        glove = BoxingGlove("Test Glove")
        self.assertEqual(glove.weight, 10)

    def test_stealability(self):
        prod = Product('Test Product')
        steal = prod.stealability()
        self.assertEqual(steal, 'Kinda stealable')

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        ADJECTIVES = [['Awesome'], ['Shiny'], ['Impressive'], ['Portable'], ['Improved']]
        NOUNS = [['Anvil'], ['Catapult'], ['Disguise'], ['Mousetrap'], ['???']]
        mergedlist = ADJECTIVES + NOUNS
        
        products = generate_products()
        product_name_lst = []
        for product in products:
            product_name_lst.append(product.name)
        
        new_lst = []
        for product_name in product_name_lst:
            new_lst.append(product_name.split())
        
        newer_lst = []
        for name in new_lst:
            newer_lst.append(name)

        for lst in newer_lst:
            for word in lst:
                    self.assertIn(str(word), mergedlist)
        

if __name__ == '__main__':
    unittest.main()
