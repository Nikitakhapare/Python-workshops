from sample2 import Sample
import unittest

class TestSample(unittest.TestCase):
    def test_notePick(self):
    
        self.assertEqual(Sample.bill_calculator(50),0)
        self.assertEqual(Sample.bill_calculator(150),100)
        self.assertEqual(Sample.bill_calculator(300),650)



if __name__=="__main__":
    unittest.main()