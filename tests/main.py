import os
import sys
import unittest

absPath = os.path.abspath(__file__) 
dirA = os.path.dirname(absPath)
srcPath = os.path.join(os.path.dirname(dirA),"src" )
sys.path.append(srcPath)

import env_config
from repository_test import TestRepository



if __name__ == '__main__':
    env_config.main()
    # repository_test.main()
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRepository)  
    # Execute os testes
    unittest.TextTestRunner(verbosity=2).run(test_suite)
