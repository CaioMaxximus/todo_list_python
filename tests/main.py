import os
import sys
import unittest

absPath = os.path.abspath(__file__) 
dirA = os.path.dirname(absPath)
srcPath = os.path.join(os.path.dirname(dirA),"src" )
sys.path.append(srcPath)

import env_config
from repository_test import TestRepository
from service_test import TestService




if __name__ == '__main__':
    env_config.main()
    # repository_test.main()
    test_suite_repository = unittest.TestLoader().loadTestsFromTestCase(
        TestRepository)  
    test_suite_service = unittest.TestLoader().loadTestsFromTestCase(
        TestService)  
    # Execute os testes
    unittest.TextTestRunner(verbosity=2).run(test_suite_repository)
    unittest.TextTestRunner(verbosity=2).run(test_suite_service)
