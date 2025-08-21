
import reflex as rx
from Video_Inicial import video_inicial
from Los_90 import Los_90
from Navbar import navbar
from Conciertos import Conciertos
from Prueba_componente import Prueba

from rxconfig import config

class State(rx.State):
    
    pass


def index():
    
    return rx.vstack(

                        #navbar(),
                        #video_inicial(),
                        #Los_90(),
                        #Conciertos(),
                        Prueba(),


                    )

    


app = rx.App()
app.add_page(index)