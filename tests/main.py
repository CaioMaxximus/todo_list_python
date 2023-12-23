import os
import sys

# print(sys.path)
absPath = os.path.abspath(__file__) 
dirA = os.path.dirname(absPath)
# dbTestPath = os.path.join(absPath ,"databaseTest.db")
srcPath = os.path.join(os.path.dirname(dirA),"src" )
sys.path.append(srcPath)
print(sys.path)

import env_config
import repository_test



env_config.main()
repository_test.main()
