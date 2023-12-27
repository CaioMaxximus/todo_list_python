import os


class Themes(object):
    _instance = None
    themes = {
        'synthwave':{
            'big_background': "#8d03b2",
            'big_background_lighter' : "#ce05db",
            'big_background_darker' : '#6c01a2',
            'element_1': '#f7aa21',
            "element_2" : "#f67a27",
            "correct" : "#76C929",
            "error" : "#FF4218"

        }
    }

   

    def __init__(self , type):
        dirName = os.path.dirname(os.path.abspath(__file__))
        icons_path = os.path.join(dirName , "..",".." ,"assets" , "icons")
        print(icons_path)
        self.icons_path = icons_path
        self.theme_type = type
        self.icons = {}
        self.__set_icons__()

    def __set_icons__(self):
        self.icons = {
        "back_arrow" : self.icons_path + "/arrow-turn-down-left.png"
            }
        
    def get_color(self,element):
        return self.themes[self.theme_type][element]

    def get_icon(self,element):
        return self.icons[element]
    def __new__(obj, *args , **kwargs):
        if obj._instance == None:
            obj._instance = object.__new__(obj)
        
        return obj._instance
    
if __name__ == '__main__':
    theme1 = Themes('synthwave')
    print(theme1)
    theme2 = Themes('synthwave')
    print(theme1 == theme2)
    print(theme1.get_color("big_background_darker"))
    print(theme1.get_icon("back_arrow"))

