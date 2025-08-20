import reflex as rx

config = rx.Config(
    app_name="Kilometros_de_musica",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)