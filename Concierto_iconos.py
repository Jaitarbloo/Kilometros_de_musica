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

# Lista de 16 videos (todos con el mismo video que solicitaste)
VIDEOS = [
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
    {"id": "WMPM1q_Uyxc", "title": "Fiat Uno Turbo"},
]

def ElementosDistribuidos():
    # Crear una distribución uniforme en una cuadrícula 4x4
    filas = 4
    columnas = 4
    
    elementos = []
    
    for i, video in enumerate(VIDEOS):
        # Calcular posición basada en una cuadrícula
        fila = i // columnas
        columna = i % columnas
        
        # Posiciones distribuidas uniformemente con márgenes
        x_pct = (columna + 0.5) * (100 / columnas)
        y_pct = (fila + 0.5) * (85 / filas) + 10  # +10 para dejar espacio para el título
        
        # Pequeñas variaciones aleatorias para no ser perfectamente uniforme
        variacion_x = random.uniform(-4, 4)
        variacion_y = random.uniform(-2, 2)
        
        x_pct += variacion_x
        y_pct += variacion_y
        
        # Asegurar que no se salgan de los límites
        x_pct = max(8, min(x_pct, 92))
        y_pct = max(15, min(y_pct, 90))
        
        # Tamaño similar para todos
        size = "12%"
        
        # Formas variadas pero con bordes redondeados
        formas = ["50%", "40%", "30%", "25%", "35%", "45%", "20%", "15%"]
        border_radius = random.choice(formas)
        
        # Rotaciones aleatorias leves
        rotation = random.randint(-12, 12)
        
        # Sombras de colores variados pero coherentes
        sombras = [
            "0 4px 10px rgba(255,0,0,0.7)",      # Rojo - color de coche deportivo
            "0 4px 10px rgba(255,100,0,0.7)",    # Naranja
            "0 4px 10px rgba(255,215,0,0.7)",    # Oro
            "0 4px 10px rgba(200,0,0,0.7)",      # Rojo oscuro
        ]
        box_shadow = random.choice(sombras)
        
        # Bordes de colores relacionados con coches
        bordes = ["0.15rem solid red", "0.15rem solid darkorange", 
                 "0.15rem solid gold", "0.15rem solid crimson"]
        border = random.choice(bordes)
        
        elementos.append(
            rx.box(
                rx.image(
                    src="/fiat-uno-turbo.jpg",  # Usando la imagen del Fiat Uno Turbo
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
                        "box_shadow": "0 6px 16px rgba(255,0,0,0.9)",
                        "border": "0.2rem solid red",
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
                        src="https://www.youtube.com/embed/{State.current_video}?autoplay=1&mute=0"
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
            box_shadow="0 0 30px rgba(255,0,0,0.5)",
            border="2px solid red",
        ),
    )

def Concierto_iconos():
    return rx.center(
        rx.vstack(
            # Imagen de fondo original con overlay para mejor contraste
            rx.box(
                rx.image(
                    src="/noches-de-concierto.jpg",  # Imagen de fondo original
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
                "Nos vamos de concierto!",
                size="7",
                color="red",
                text_shadow="2px 2px 8px rgba(0,0,0,0.8), 0 0 10px rgba(255,0,0,0.5)",
                padding="1.5rem",
                #background="linear-gradient(90deg, rgba(0,0,0,0.8) 0%, rgba(100,0,0,0.6) 50%, rgba(0,0,0,0.8) 100%)",
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
app.add_page(Concierto_iconos)