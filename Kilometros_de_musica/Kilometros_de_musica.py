
import reflex as rx
from Video_Inicial import video_inicial
from Los_80 import Los_80
from Los_90 import Los_90
from Navbar import navbar
from Conciertos import Conciertos
from Prueba_componente1 import Prueba
from BMW_Publicidad import BMW

from rxconfig import config

class State(rx.State):
    
    pass


def index():
    
    return rx.vstack(

                        navbar(),
                        video_inicial(),
                        Los_80(),
                        Los_90(),
                        Conciertos(),
                        Prueba(),
                        BMW(),
                        
                        


                    )

    


app = rx.App()
app.add_page(index)