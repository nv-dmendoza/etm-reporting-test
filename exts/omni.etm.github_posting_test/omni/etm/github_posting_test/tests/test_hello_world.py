# NOTE:
#   omni.kit.test - std python's unittest module with additional wrapping to add suport for async/await tests
#   For most things refer to unittest docs: https://docs.python.org/3/library/unittest.html
import omni.kit.test

# Extnsion for writing UI tests (simulate UI interaction)
import omni.kit.ui_test as ui_test

# Import extension python module we are testing with absolute import path, as if we are external user (other extension)
import omni.etm.github_posting_test

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
        self.assertEqual(True, False)

    def test_example_two(self):
        """Example extension test one"""
        self.assertEqual(1, 0)    

    # use "async" for tests that require UI input
    async def test_window_button(self):
        """Simulates clicking the add and reset buttons"""

        # Find a label in our window
        label = ui_test.find("My Window//Frame/**/Label[*]")

        # Find buttons in our window
        add_button = ui_test.find("My Window//Frame/**/Button[*].text=='Add'")
        reset_button = ui_test.find("My Window//Frame/**/Button[*].text=='Reset'")

        # Click reset button
        await reset_button.click()
        self.assertEqual(label.widget.text, "empty")

        await add_button.click()
        self.assertEqual(label.widget.text, "count: 2")

        await add_button.click()
        self.assertEqual(label.widget.text, "count: 4")

