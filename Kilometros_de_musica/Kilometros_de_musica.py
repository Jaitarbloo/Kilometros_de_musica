
import reflex as rx
from Video_Inicial import video_inicial
from Los_80 import Los_80
from Los_90 import Los_90
from Conciertos import Conciertos
#from Prueba_componente1 import navbar
from BMW_Publicidad import BMW
from Concierto_iconos import Concierto_iconos
from Navbar_trasparente import Navbar_trasparente
from Navbar import Navbar

from rxconfig import config

class State(rx.State):
    
    pass


def index():
    
    return rx.vstack(

                        #Navbar_trasparente(),
                        Navbar(),
                        video_inicial(),
                        Los_80(),
                        Los_90(),
                        Conciertos(),
                        Concierto_iconos(),
                        BMW(),
                        
                        


                    )

    


app = rx.App()
app.add_page(index)