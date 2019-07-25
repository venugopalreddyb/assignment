import unittest
import assignment

class TestAssignment(unittest.TestCase):
    def test_readConfigFile(self):
        urls = assignment.readFromFile('testUrls.txt')
        self.assertEquals(len(urls), 2)

    def test_downloadImage(self):
        testImage = 'https://images.pexels.com/photos/459793/pexels-photo-459793.jpeg?cs=srgb&dl=chalk-chalkboard-exam-459793.jpg&fm=jpg'
        success = assignment.downloadImages(testImage)
        self.assertEquals(success, True)

    def test_verifyFile(self):
        present = assignment.verifyFile('testUrls.txt')
        self.assertEquals(present, True)

if __name__ == '__main__':
    unittest.main()