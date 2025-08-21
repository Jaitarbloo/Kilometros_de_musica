import reflex as rx
import math

class State(rx.State):
    show_video: bool = False
    current_video: str = ""

    def open_video(self, event):
        # Reflex pasa un diccionario con info del evento, no el id directamente
        # Extrae el id del target si lo has puesto como atributo data-id
        self.current_video = event.get("target", {}).get("dataset", {}).get("id", "")
        self.show_video = True

    def close_video(self):
        self.show_video = False

# Lista de videos (puedes reemplazar con tus propios videos)
VIDEOS = [
    {"id": "PLRnH7bYJpBdGKsemBId7GHqCIwyp38G_Z&index=2", "title": "Video 1"},
    {"id": "dQw4w9WgXcQ", "title": "Video 2"},
    {"id": "9bZkp7q19f0", "title": "Video 3"},
    {"id": "kJQP7kiw5Fk", "title": "Video 4"},
    {"id": "RgKAFK5djSk", "title": "Video 5"},
    {"id": "JGwWNGJdvx8", "title": "Video 6"},
    {"id": "OPf0YbXqDm0", "title": "Video 7"},
    {"id": "k2qgadSvNyU", "title": "Video 8"},
    {"id": "nYh-n7EOtMA", "title": "Video 9"},
    {"id": "7wtfhZwyrcc", "title": "Video 10"},
]



def Circulos():
    # Coordenadas que siguen el trazado de la carretera (ajustar según tu imagen)
    # Estas coordenadas son aproximadas y deben ajustarse para que coincidan con tu imagen
    road_coordinates = [
        (15, 80),  # Parte inferior izquierda
        (25, 65),
        (35, 55),
        (45, 50),  # Centro inferior
        (55, 50),  # Centro
        (65, 55),
        (75, 65),
        (85, 80),  # Parte inferior derecha
        (75, 90),
        (30, 75),
        (55, 97),  # Centro superior
        (45, 95),
        (35, 90),
        (25, 85),
    ]
    
    # Ajustar el número de coordenadas al número de videos
    n = len(VIDEOS)
    
    road_points = road_coordinates * (n // len(road_coordinates) + 1)
    road_points = road_points[:n]
    
    circle_items = []
    
    for i, (video, (x_pct, y_pct)) in enumerate(zip(VIDEOS, road_points)):
        
        circle_items.append(
                    
                            rx.box(
                
                                    rx.image( src=f"/video_thumbs/{video['id']}.jpg",
                                                width="100%",
                                                height="100%",
                                                border_radius="50%",
                                                object_fit="cover",
                                                border="0.2rem solid white",
                                                cursor="pointer",
                                                on_click=rx.event(State.open_video),
                                                data_id=video['id'],  # <-- Añade esto
                                                box_shadow="0 4px 8px rgba(0,0,0,0.3)",
                                                _hover={ "transform": "scale(1.1)",
                                                         "transition": "transform 0.2s",
                                                         "box_shadow": "0 6px 12px rgba(0,0,0,0.4)",
                                                         "border": "0.2rem solid gold" 
                                                         
                                                         }
                                                ),
                
                                        position="absolute",
                                        left=f"{x_pct}%",
                                        top=f"{y_pct}%",
                                        width="8%",  # Tamaño ajustado para la carretera
                                        height="8%",
                                        transform="translate(-50%, -50%)",
                                        z_index="10",
                                        transition="all 0.3s ease",
            
                                     ),  
        
                            )

    return rx.box( *circle_items )


def video_youtube():
    
        return rx.cond( State.show_video,
        
                        rx.box(
            
                                rx.vstack(
                                            rx.html( f"""<iframe width="560" height="315"
                                                     src="https://www.youtube.com/embed/{State.current_video}?autoplay=1"
                                                     frameborder="0"
                                                     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                                     allowfullscreen></iframe>"""
                                                    ),
                
                                            rx.button( "Cerrar", 
                                                        on_click=State.close_video, 
                                                        bg="red", 
                                                        color="white",
                                                        size="3",
                                                        _hover={"bg": "darkred"}
                
                                                        ),
                
                                    align="center",
                                    spacing="4",
            
                                        ),
            
                        position="fixed",
                        top="50%",
                        left="50%",
                        transform="translate(-50%, -50%)",
                        bg="rgba(0, 0, 0, 0.9)",
                        padding="20px",
                        border_radius="15px",
                        z_index="1000",
                        box_shadow="lg",
       
                            ),
    
                    )


def Prueba():
    return rx.box(
        # Imagen de fondo
        rx.image(
            src="/Carretera1.jpg",
            style={
                "position": "absolute",
                "width": "100vw",
                "height": "100vh",
                "objectFit": "cover",
                "zIndex": 0,
            },
        ),

        # Título arriba centrado
        rx.heading(
            "Los 90 - Música y Coches",
            size="8",
            color="gold",
            text_shadow="2px 2px 4px rgba(0,0,0,0.7)",
            style={
                "position": "absolute",
                "top": "2rem",       # distancia desde arriba
                "left": "50%",
                "transform": "translateX(-50%)",
                "zIndex": 5,
            },
        ),

        # Contenido centrado
        rx.center(
            rx.vstack(
                Circulos(),
                align="center",
                spacing="0",
            ),
            width="100%",
            height="100vh",
        ),

        video_youtube(),
        width="100%",
        height="100vh",
        overflow="hidden",
    )

       












app = rx.App()
app.add_page(Prueba)