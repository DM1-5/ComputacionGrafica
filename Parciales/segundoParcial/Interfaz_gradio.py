import gradio as gr
import libreria


#demo = gr.Interface(libreria.invertir_Color, gr.Image(type="filepath"), "image", api_name="predict")

with gr.Blocks() as demo:
    with gr.Tab("Principal"):
        gr.Markdown("# Procesamiento de imágenes con Numpy")
        gr.Markdown("En esta interfaz, puedes subir una imagen y aplicar diferentes transformaciones utilizando las funciones creadas en la librería `libreria.py`.")
        gr.Markdown("Selecciona la pestaña para aplicar la transformación deseada a tu imagen.")
        gr.Markdown("## Funciones disponibles:")
        gr.Markdown("- **Negativo**: Invierte los colores de la imagen.")
        gr.Markdown("- **Brillo**: Aumenta o disminuye el brillo de la imagen según el valor seleccionado.")
        gr.Markdown("- **Canales**: Permite visualizar los diferentes canales de la imagen (Rojo, Verde, Azul, Cyan, Magenta, Amarillo).")

    with gr.Tab("Negativo"):
        gr.Markdown("## Invertir colores de una imagen")
        gr.Markdown("Sube una imagen y la función `invertir_Color` se encargará de invertir sus colores.")
        with gr.Row():
            input = gr.Image(type="filepath")
            output = gr.Image(type="numpy")
            input.change(libreria.invertir_Color, inputs=input, outputs=output)

    with gr.Tab("Brillo"):
        gr.Markdown("## Aumentar brillo de una imagen")
        gr.Markdown("Sube una imagen y la función `aumentar_Brillo` se encargará de aumentar su brillo.")
        with gr.Row():
            input = gr.Image(type="filepath")
            with gr.Column():
                input_brillo_slider = gr.Slider(-255, 255, value=0, step=1, label="Valor de brillo")
                input_brillo_num = gr.Number(label="Valor de brillo (numérico)", value="0", interactive=True, minimum=-255, maximum=255)
                boton_brillo = gr.Button("Modificar brillo")
            output = gr.Image(type="numpy")
            input_brillo_slider.change(libreria.aumentar_brillo, inputs=[input, input_brillo_slider], outputs=output)
            boton_brillo.click(libreria.aumentar_brillo, inputs=[input, input_brillo_num], outputs=output)

    with gr.Tab("Canales"):
        gr.Markdown("## Canales de una imagen")
        gr.Markdown("Verificaremos los canales de una imagen")
        
        with gr.Accordion("Canal Rojo", open=False):
            gr.Markdown("## Canal Rojo")
            gr.Markdown("Sube una imagen y la función `canal_Rojo` se encargará de retornar su canal rojo.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Rojo, inputs=input, outputs=output)

        with gr.Accordion("Canal Verde", open=False):
            gr.Markdown("## Canal Verde")
            gr.Markdown("Sube una imagen y la función `canal_Verde` se encargará de retornar su canal verde.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Verde, inputs=input, outputs=output)

        with gr.Accordion("Canal Azul", open=False):
            gr.Markdown("## Canal Azul")
            gr.Markdown("Sube una imagen y la función `canal_Azul` se encargará de retornar su canal azul.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Azul, inputs=input, outputs=output)

        with gr.Accordion("Canal Cyan", open=False):
            gr.Markdown("## Canal Cyan")
            gr.Markdown("Sube una imagen y la función `canal_Cyan` se encargará de retornar su canal cyan.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Cyan, inputs=input, outputs=output)

        with gr.Accordion("Canal Magenta", open=False):
            gr.Markdown("## Canal Magenta")
            gr.Markdown("Sube una imagen y la función `canal_Magenta` se encargará de retornar su canal magenta.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Magenta, inputs=input, outputs=output)
    
        with gr.Accordion("Canal Amarillo", open=False):
            gr.Markdown("## Canal Amarillo")
            gr.Markdown("Sube una imagen y la función `canal_Amarillo` se encargará de retornar su canal amarillo.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Amarillo, inputs=input, outputs=output)
        
demo.launch()
