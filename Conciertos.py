import reflex as rx
import math

class State(rx.State):
    
    show_video: bool = False
    current_video: str = ""
    
    def open_video(self, video_url: str):
        self.current_video = video_url
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


def video_circle():
    # Todo en % del contenedor (que será un cuadrado responsive)
    RADIUS_PCT = 47      # radio en % del ancho del contenedor
    ITEM_SIZE_PCT = 24   # diámetro de cada miniatura en %
    CENTER_SIZE_PCT = 34   # diámetro del círculo central en %

    circle_items = []
    n = len(VIDEOS) if VIDEOS else 1

    for i, video in enumerate(VIDEOS):
        angle = 2 * math.pi * i / n
        x_pct = 50 + RADIUS_PCT * math.cos(angle)  # centro (50,50) + radio
        y_pct = 50 + RADIUS_PCT * math.sin(angle)

        circle_items.append(
            rx.box(
                rx.image(
                    src=f"/video_thumbs/{video['id']}.jpg",
                    width="100%",
                    height="100%",
                    border_radius="50%",
                    object_fit="cover",
                    border="0.2rem solid white",
                    cursor="pointer",
                    on_click=lambda video_url=video['id']: State.open_video(video_url),
                ),
                position="absolute",
                left=f"{x_pct}%",
                top=f"{y_pct}%",
                width=f"{ITEM_SIZE_PCT}%",
                height=f"{ITEM_SIZE_PCT}%",
                transform="translate(-50%, -50%)",  # centra el ítem en su (x,y)
                z_index="10",
            )
        )

    return rx.box(
        *circle_items,

        # Círculo central, mismo sistema de unidades (% del contenedor)
        rx.box(
            rx.image(
                src="/modern-talking.webp",
                width="100%",
                height="100%",
                border_radius="50%",
                object_fit="cover",
                border="0.35rem solid gold",
            ),
            position="absolute",
            left="50%",
            top="50%",
            width=f"{CENTER_SIZE_PCT}%",
            height=f"{CENTER_SIZE_PCT}%",
            transform="translate(-50%, -50%)",
            z_index="20",
        ),

        # Contenedor cuadrado y responsive
        position="relative",
        width="min(92vw, 640px)",  # escala con viewport pero con tope
        aspect_ratio="1 / 1",      # mantiene cuadrado (si tu versión no lo soporta, ver nota abajo)
        margin="0 auto",
    )



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
                
                                            rx.button("Cerrar", on_click=State.close_video, bg="red", color="white"),
                
                                    
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

def Conciertos():
    
    return rx.center(
        
                    rx.vstack(

                            rx.image( src="/noches-de-concierto.jpg",  # Imagen de fondo

                                    style={ "position": "absolute",
                                            "width": "100vw",
                                            "height": "100vh",
                                            "objectFit": "cover",
                                            "zIndex": 0,
                                        }
        
                                    ),
                            
                            rx.heading("Los 90 - Música Retro", size="8", color="gold"),
                            video_circle(),
                            video_youtube(),
                            align="center",
                            
                    
                    
                            ),
                
                width="100%",
                
                    
                    )

app = rx.App()
app.add_page(Conciertos)