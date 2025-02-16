import os


class Themes(object):
    _instance = None
    themes = {
        'synthwave':{
            "colors" :{
                'big_background': "#8d03b2",
                'big_background_lighter' : "#ce05db",
                'big_background_darker' : '#6c01a2',
                'element_1': '#f7aa21',
                "element_2" : "#f67a27",
                "correct" : "#76C929",
                "error" : "#FF4218",
                "font_1" : "white"
            },
            "fonts": {

                "painel": "GOOD TIMES"
            },
            "font_size":{
                "main-painel" : 14,
            }
        },
        'synthwave2':{
            "colors" :{
                'big_background': "#3C1C64",
                'big_background_lighter' : "#632E80",
                'big_background_darker' : '#150947',
                'element_1': '#FCCC2A',
                "element_2" : "#F87E3E",
                "correct" : "#4AD30F",
                "error" : "#DF1025",
                "font_1" : "white"
            },
            "fonts": {

                # "painel": "GOOD TIMES",
                "painel" : "COPPERPLATE GOTHIC BOLD",
                "content" : "Courier"
            },
            "font_size":{
                "presentation" : 8,
                "small-title" : 10,
                "median-title" : 14,
                "big-title" : 16
            }
        },
        "office_vibes":{
            "colors" :{
                'big_background': "#F5F5F5",
                'big_background_lighter' : "#FFFFFF",
                'big_background_darker' : '#E0E0E0',
                'element_1': '#2B2B2B',
                "element_2" : "#4B4B4B",
                "correct" : "#28A745",
                "error" : "#DC3545",
                "font_1" : "#000000"
            },
            "fonts": {
                "painel" : "Arial",
                "content" : "Times New Roman"
            },
            "font_size":{
                "presentation" : 9,
                "small-title" : 12,
                "median-title" : 16,
                "big-title" : 20
            }
        },
        "cyberpunk_vibes":{
            "colors" :{
                'big_background': "#1B1F23",
                'big_background_lighter' : "#3C4A51",
                'big_background_darker' : '#0F1215',
                'element_1': '#00FF00',
                "element_2" : "#FF00FF",
                "correct" : "#00FFFF",
                "error" : "#FF0033",
                "font_1" : "#FFFFFF"
            },
            "fonts": {
                "painel" : "Orbitron",
                "content" : "VT323"
            },
            "font_size":{
                "presentation" : 8,
                "small-title" : 10,
                "median-title" : 14,
                "big-title" : 16
            }
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
        "back_arrow" : self.icons_path + "/small-arrow-left.png",
        "cross" : self.icons_path + "/cross.png",
        "filter" : self.icons_path + "/filter.png",
        "add-circle" : self.icons_path + "/add.png",
        "delete" :self.icons_path + "/lixeira-xmark.png",
        "check" : self.icons_path + "/check.png"
            }
        
    def get_color(self,name):
        return self.themes[self.theme_type]["colors"][name]

    def get_font(self,name):
        return self.themes[self.theme_type]["fonts"][name]

    def get_font_size(self,name):
        return self.themes[self.theme_type]["font_size"][name]

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

