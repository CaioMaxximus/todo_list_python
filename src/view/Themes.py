def Themes(object):
    _instance = None
    themes = {
        'synthwave':{
            'big_background': "#8d03b2",
            'big_background_lighter' : "#ce05db",
            'big_background_darker' : '#6c01a2',
            'element_1': '#f7aa21',
            "element_2" : "#f67a27"

        }
    }

    def __init__(self , type):
        self.theme_type = type

    def get_color(self,element):
        return self.themes[self.theme_type][element]

    def __new__(obj, *args , **kwargs):
        if obj._instance == None:
            obj._instance = object.__new__(obj)
        
        return obj._instance
    
if __name__ == '__main__':
    theme1 = Themes('synthwave')
    theme2 = Themes('synthwave')
    print(theme1 == theme2)
