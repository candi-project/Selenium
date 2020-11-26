# 1. Import the files
import unittest
from SeleniumFramework.tests.test_ContactFormtest import contactFormTest
from SeleniumFramework.tests.test_EnterText import EnterTextPage

# 2. Create the object of the class using unitTest
cf = unittest.TestLoader().loadTestsFromTestCase(contactFormTest)
et = unittest.TestLoader().loadTestsFromTestCase(EnterTextPage)

# 3. Create TestSuite
regression = unittest.TestSuite([cf, et])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regression)

# Note : All the methods in test files should define in proper run order
