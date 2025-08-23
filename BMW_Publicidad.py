import reflex as rx

def BMW() -> rx.Component:
    return rx.box(
        # Contenedor con imagen de fondo y overlay degradado
        rx.hstack(
            # Columna izquierda con textos y botones
            rx.vstack(
                rx.heading(
                    "BMW i EL PRIMER BMW iX2. 100% ELÉCTRICO.",
                    size="8",
                    color="white",
                    font_weight="bold"
                ),
                rx.text(
                    "Desde 299 € al mes.",
                    size="8",
                    color="white",
                    margin_top="1rem"
                ),
                rx.text(
                    "Entrada: 10.447,30 €. Cuota final: 28.777,03 €*",
                    size="8",
                    color="white"
                ),
                rx.text(
                    "Financiando con BMW Bank.",
                    size="8",
                    color="white"
                ),
                rx.text(
                    "Mantenimiento incluido",
                    size="8",
                    color="white",
                    margin_bottom="2rem"
                ),
                # Botones
                rx.hstack(
                    rx.button(
                        "Más información",
                        bg_color="#0066b2",
                        color="white",
                        border_radius="md",
                        padding_x="2rem",
                        _hover={"bg_color": "#004d86"}
                    ),
                    rx.button(
                        "Solicitar prueba",
                        bg_color="white",
                        color="#0066b2",
                        border="2px solid #0066b2",
                        border_radius="md",
                        padding_x="2rem",
                        _hover={"bg_color": "#f0f0f0"}
                    ),
                    spacing="2",
                    margin_bottom="2rem"
                ),
                align_items="start",
                justify="center",
                padding_x="2rem",
                width="40%"
            ),

            # Icono Instagram a la derecha
            rx.vstack(
                rx.link(
                    rx.image(
                        src="https://cdn-icons-png.flaticon.com/512/174/174855.png",
                        width="50px",
                        height="50px",
                        _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"}
                    ),
                    href="https://www.instagram.com/bmw/",
                    is_external=True
                ),
                align_items="center",
                justify="center",
                width="20%",
                padding_right="2rem"
            ),

            align_items="center",
            justify="between",
            width="100%",
            min_height="80vh"
        ),
        # Imagen de fondo + overlay negro degradado
        background_image="linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.4) 40%, rgba(0,0,0,0) 60%), url('/bmw-publicidad.webp')",
        background_size="cover",
        background_position="center",
        min_height="100vh",
        width="100%"
    )

app = rx.App()
app.add_page(BMW)

