import reflex as rx


def video() -> rx.Component:
    
                return rx.box(
                                rx.video( url="VID-20250427-WA0001_480x480.mp4",
                                          width="100%",
                                          height="auto",
                                          controls=True,
                                          playing=False,
                                          loop=True
                                        ),

                                rx.box(
            
                                        rx.heading("Título del Video", size="9", color="white"),
                                
                                        rx.box(
                                        
                                        rx.text("Texto descriptivo que aparece sobre el video",
                                                color="white",
                                                display="inline-block",
                                                white_space="nowrap"
                                                ),
                                                animation="slide 10s linear infinite",
                                                style={"@keyframes slide": 
                                           
                                                        { "0%": {"transform": "translateX(100vw)"},
                                                        "100%": {"transform": "translateX(-100%)"}}
                                                        },
                                                width="100%",
                                                overflow="hidden"
                                       
                                                ),
            
                                position="absolute",
                                top="50%",
                                left="0",
                                right="0",
                                transform="translateY(-50%)",
                                text_align="center",
                                bg="rgba(0,0,0,0.0)",
                                p=4,
                                border_radius="lg"
                        
                                        ),


                        position="relative",
                        width="100%",
                        overflow="hidden"
    
                        )

def video_inicial() -> rx.Component:
    
    
    return rx.center(
            
                        video(),
                        
                                                                
       
                        padding_top="2em",
                        width="100%"
        
                  )


app = rx.App()
app.add_page(video_inicial)

