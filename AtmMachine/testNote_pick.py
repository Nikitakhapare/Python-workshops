from sample import Sample
import unittest

class TestSample(unittest.TestCase):
    def test_notePick(self):
    
        self.assertEqual(Sample.note_pick(5634),{1000:5,500:1,100:1,1:34})

if __name__=="__main__":
    unittest.main()