# NOTE:
#   omni.kit.test - std python's unittest module with additional wrapping to add suport for async/await tests
#   For most things refer to unittest docs: https://docs.python.org/3/library/unittest.html
import omni.kit.test

# Extnsion for writing UI tests (simulate UI interaction)
import omni.kit.ui_test as ui_test

# Import extension python module we are testing with absolute import path, as if we are external user (other extension)
import omni.etm.github_posting_expected_pass

# Having a test class dervived from omni.kit.test.AsyncTestCase declared on the root of module will make it auto-discoverable by omni.kit.test
class Test(omni.kit.test.AsyncTestCase):
    async def setUp(self):
        """Runs Before each test"""
        pass

    async def tearDown(self):
        """ Runs after each test"""
        pass
    
    def test_example_one(self):
        """Example extension test one"""
        self.assertEqual(True, True)

    def test_example_two(self):
        """Example extension test one"""
        self.assertEqual(1, 1)    

