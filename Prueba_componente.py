import reflex as rx
import random

class State(rx.State):
    show_video: bool = False
    current_video: str = ""

    def open_video(self, video_url: str):
        self.current_video = video_url
        self.show_video = True

    def close_video(self):
        self.show_video = False

# Lista de 20 videos
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
    {"id": "video11", "title": "Video 11"},
    {"id": "video12", "title": "Video 12"},
    {"id": "video13", "title": "Video 13"},
    {"id": "video14", "title": "Video 14"},
    {"id": "video15", "title": "Video 15"},
    {"id": "video16", "title": "Video 16"},
    {"id": "video17", "title": "Video 17"},
    {"id": "video18", "title": "Video 18"},
    {"id": "video19", "title": "Video 19"},
    {"id": "video20", "title": "Video 20"},
]

def ElementosDistribuidos():
    # Crear una distribución uniforme en una cuadrícula 5x4
    filas = 4
    columnas = 4
    
    elementos = []
    
    for i, video in enumerate(VIDEOS):
        # Calcular posición basada en una cuadrícula
        fila = i // columnas
        columna = i % columnas
        
        # Posiciones distribuidas uniformemente con márgenes
        x_pct = (columna + 0.5) * (100 / columnas)
        y_pct = (fila + 0.5) * (85 / filas)   # +10 para dejar espacio para el título
        
        # Pequeñas variaciones aleatorias para no ser perfectamente uniforme
        variacion_x = random.uniform(-5, 5)
        variacion_y = random.uniform(-3, 3)
        
        x_pct += variacion_x
        y_pct += variacion_y
        
        # Asegurar que no se salgan de los límites
        x_pct = max(8, min(x_pct, 92))
        y_pct = max(15, min(y_pct, 90))
        
        # Tamaño similar para todos
        size = "12%"
        
        # Formas variadas pero con bordes redondeados
        formas = ["50%", "40%", "30%", "25%", "35%", "45%"]
        border_radius = random.choice(formas)
        
        # Rotaciones aleatorias leves
        rotation = random.randint(-10, 10)
        
        # Sombras de colores variados pero coherentes
        sombras = [
            "0 4px 10px rgba(255,215,0,0.7)",
            "0 4px 10px rgba(255,105,180,0.7)",
            "0 4px 10px rgba(30,144,255,0.7)",
            "0 4px 10px rgba(50,205,50,0.7)",
        ]
        box_shadow = random.choice(sombras)
        
        # Bordes de colores
        bordes = ["0.15rem solid gold", "0.15rem solid hotpink", 
                 "0.15rem solid deepskyblue", "0.15rem solid limegreen"]
        border = random.choice(bordes)
        
        elementos.append(
            rx.box(
                rx.image(
                    src=f"/video_thumbs/{video['id']}.jpg",
                    width="100%",
                    height="100%",
                    border_radius=border_radius,
                    object_fit="cover",
                    border=border,
                    cursor="pointer",
                    on_click=lambda video_url=video['id']: State.open_video(video_url),
                    box_shadow=box_shadow,
                    transform=f"rotate({rotation}deg)",
                    _hover={
                        "transform": f"scale(1.15) rotate({rotation}deg)",
                        "transition": "transform 0.3s, box-shadow 0.3s",
                        "box_shadow": "0 6px 16px rgba(255,215,0,0.9)",
                        "border": "0.2rem solid gold",
                        "z_index": "20"
                    },
                ),
                position="absolute",
                left=f"{x_pct}%",
                top=f"{y_pct}%",
                width=size,
                height=size,
                transform="translate(-50%, -50%)",
                z_index="10",
                transition="all 0.3s ease",
            )
        )

    return rx.box(
        *elementos,
        width="100%",
        height="100vh",
        position="relative",
    )

def video_youtube():
    return rx.cond(
        State.show_video,
        rx.box(
            rx.vstack(
                rx.html(
                    f"""<iframe width="800" height="450"
                        src="https://www.youtube.com/embed/{State.current_video}?autoplay=1"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen></iframe>"""
                ),
                rx.button(
                    "Cerrar",
                    on_click=State.close_video,
                    bg="red",
                    color="white",
                    size="3",
                    _hover={"bg": "darkred"},
                    margin_top="1rem",
                ),
                align="center",
                spacing="4",
            ),
            position="fixed",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%)",
            bg="rgba(0, 0, 0, 0.95)",
            padding="2rem",
            border_radius="20px",
            z_index="1000",
            box_shadow="0 0 30px rgba(255,215,0,0.5)",
            border="2px solid gold",
        ),
    )

def Prueba():
    return rx.center(
        rx.vstack(
            # Imagen de fondo con overlay para mejor contraste
            rx.box(
                rx.image(
                    src="/Noches de concierto.jpg",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                ),
                position="absolute",
                width="100%",
                height="100%",
                z_index=0,
                _after={
                    "content": "''",
                    "position": "absolute",
                    "top": 0,
                    "left": 0,
                    "width": "100%",
                    "height": "100%",
                    "background": "linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4))",
                    "z_index": 1,
                }
            ),
            
            # Título con estilo mejorado
            rx.heading(
                "Vamos de concierto!",
                size="8",
                color="gold",
                text_shadow="2px 2px 8px rgba(0,0,0,0.8), 0 0 10px rgba(255,215,0,0.5)",
                padding="1.5rem",
                #background="linear-gradient(90deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.5) 50%, rgba(0,0,0,0.7) 100%)",
                border_radius="0 0 20px 20px",
                width="100%",
                text_align="center",
                z_index=5,
                margin_bottom="1rem",
                font_weight="bold",
                letter_spacing="0.1em",
            ),
            
            # Contenedor para los elementos
            rx.box(
                ElementosDistribuidos(),
                width="100%",
                height="90vh",
                position="relative",
            ),
            
            video_youtube(),
            align="center",
            width="100%",
            height="100vh",
            position="relative",
        ),
        width="100%",
        overflow="hidden",
    )

app = rx.App()
app.add_page(Prueba)