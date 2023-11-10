import unittest
import sys
# sys.path.append("C:\\Users\\caios\Documents\\ProjetosPessoaisLinguagens\\Python\\to_do_list\\")
sys.path.append("..\\src")
# sys.path.append("repository")
# sys.path.append("services")
from repository import task_repository as tk


class test_repository(unittest.TestCase):
    
    def test_generate_id(self):
        
        generated_id = tk.generate_id()     
        self.assertEqual(len(generated_id) , 10 ,"Size should be equal to 10")
        
        
    
if __name__ =='__main__':
    unittest.main()