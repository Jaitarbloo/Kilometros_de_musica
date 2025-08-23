import reflex as rx
from rxconfig import config

def Navbar_trasparente() -> rx.Component:
    return rx.vstack(
        # rx.center se usa para centrar horizontalmente el bloque de contenido (enlaces + línea)
        rx.center(
            rx.vstack(  # Este vstack contiene los enlaces y la línea, y su ancho se ajusta al contenido
                rx.hstack(
                    rx.link(
                        rx.text("Desarrollo y Diseño", size="6", color="white"),
                        href="https://reflex.dev",
                    ),
                    rx.link(
                        rx.text("Frameworks modernos", size="6", color="white"),
                        href="https://reflex.dev",
                    ),
                    rx.link(
                        rx.text("Trato cercano", size="6", color="white"),
                        href="https://reflex.dev",
                    ),
                    rx.link(
                        rx.text("Contáctame", size="6", color="white"),
                        href="https://reflex.dev",
                    ),
                    spacing="9",  # Espaciado entre los enlaces
                    align="center", # Alinea los elementos verticalmente en el hstack
                ),
                # La línea fina debajo de las palabras, ahora con color blanco sólido
                rx.box(
                    height="1px",
                    width="100%",  # Ocupa el 100% del ancho de su contenedor padre (el rx.vstack con width="fit_content")
                    bg="white", # Color de fondo cambiado a blanco sólido para mayor visibilidad
                    margin_top="0.5em", # Pequeño margen para separar la línea del texto
                ),
                width="fit_content",  # Importante: Este vstack se ajusta al ancho de su contenido (los enlaces)
                margin_x="auto",      # Asegura que este vstack esté centrado horizontalmente
                spacing="0",  # Elimina el espacio vertical predeterminado entre el hstack y la línea
                align="center",  # Centra los hijos (hstack y box) horizontalmente dentro de este vstack
                height=rx.breakpoints(initial="60px", sm="80px", lg="100px"), # Altura total para el área de enlaces + línea
                justify="center",  # Centra verticalmente el hstack y la línea dentro de la altura de este vstack
            ),
            width="100%", # rx.center ocupa todo el ancho para poder centrar a su hijo
        ),
        background="transparent", # Fondo transparente para todo el navbar
        position="fixed",  # Fija el navbar en la parte superior
        top="0",
        z_index="999",
        width="100%",
        spacing="0", # Elimina cualquier espaciado vertical adicional en el vstack principal
    )

app = rx.App()
app.add_page(Navbar_trasparente)
