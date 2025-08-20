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
    radius = 250  # Radio del círculo
    center_x = 300  # Centro X
    center_y = 300  # Centro Y
    
    # Crear los elementos del círculo
    circle_items = []
    for i, video in enumerate(VIDEOS):
        angle = 2 * math.pi * i / len(VIDEOS)
        x = center_x + radius * math.cos(angle) - 50  # Ajustar posición
        y = center_y + radius * math.sin(angle) - 50  # Ajustar posición
        
        circle_items.append(
            rx.box(
                rx.image(
                    src=f"/video_thumbs/{video['id']}.jpg",
                    width="100px",
                    height="100px",
                    border_radius="50%",
                    border="2px solid white",
                    cursor="pointer",
                    on_click=lambda video_url=video['id']: State.open_video(video_url)
                ),
                position="absolute",
                left=f"{x}px",
                top=f"{y}px",
                z_index="10",
            )
        )
    
    return rx.box(
        *circle_items,
        rx.image(
            src="/Modern talking.webp",
            width="150px",
            height="150px",
            border_radius="50%",
            border="4px solid gold",
            position="absolute",
            left=f"{center_x - 75}px",
            top=f"{center_y - 75}px",
            z_index="20",
        ),
        position="relative",
        width="600px",
        height="600px",
    )

def video_modal():
    return rx.cond(
        State.show_video,
        rx.box(
            rx.vstack(
                rx.html(
                    f"""<iframe width="560" height="315"
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
        )
    )

def Prueba():
    return rx.center(
        rx.vstack(
            rx.heading("Los 90 - Música Retro", size="7", color="gold"),
            video_circle(),
            video_modal(),
            align="center",
            spacing="8",
        ),
        bg="linear-gradient(to right, #0f0c29, #302b63, #24243e)",
        min_h="100vh",
        padding="2rem",
    )

app = rx.App()
app.add_page(Prueba)