import gradio as gr
import libreria

def aplicar_brillo_por_canal(img, valor, canal):
    if not canal or canal == "-1":  # ninguno seleccionado -> aplicar brillo global
        return libreria.aumentar_brillo(img, valor)
    return libreria.aumentar_brillo_Canal(img, valor, canal)

def aplicar_escala_grises(img1, metodo):
    if metodo == "Average":
        return libreria.gris_Average(img1)
    elif metodo == "Luminosity":
        return libreria.gris_Luminosity(img1)
    elif metodo == "MidGray":
        return libreria.gris_MidGray(img1)

with gr.Blocks() as demo:

    # PRINCIPAL
    with gr.Tab("Principal"):
        gr.Markdown("""# Procesamiento de imágenes con Numpy
        ### En esta interfaz, puedes subir una imagen y aplicar diferentes transformaciones utilizando las funciones creadas en la librería `libreria.py`.

        ### Selecciona la pestaña para aplicar la transformación deseada a tu imagen.
        ## Funciones disponibles:
        - **Negativo**: Invierte los colores de la imagen. 
        - **Brillo y Brillo por canal**: Aumenta o disminuye el brillo de la imagen según el valor seleccionado.    
        - **Canales**: Permite visualizar los diferentes canales de la imagen **_(Rojo, Verde, Azul, Cyan, Magenta, Amarillo)._**
        - **Escala de grises**: Convierte la imagen a escala de grises utilizando diferentes tecnicas **_(Average, Luminosity, MidGray):_**.
        - **Umbralización**: Binariza la imagen según un valor de umbral seleccionado.
        - **Reducción de resolución**: Reduce la resolución de la imagen por un factor dado.
        - **Rotación**: Rota la imagen según un ángulo seleccionado.
        - **Zoom**: Recorta y amplia la imagen según un factor seleccionado.
        - **Recorte**: Recorta la imagen según las coordenadas dadas.
        - **Suma de imágenes**: Permite sumar dos imágenes pixel a pixel, con un factor de mezcla opcional (alpha) para ponderar la suma.
        - **Histograma**: Muestra el histograma de la imagen para el canal seleccionado. 

        """)

    # NEGATIVO / INVERSION 
    with gr.Tab("Negativo"):
        gr.Markdown("## Invertir colores de una imagen")
        gr.Markdown("Selecciona una imagen y la función `invertir_Color()` se encargará de invertir sus colores.")
        with gr.Row():
            input = gr.Image(type="filepath")
            output = gr.Image(type="numpy")
            input.change(libreria.invertir_Color, inputs=input, outputs=output)

    # BRILLO 
    with gr.Tab("Brillo"):
        gr.Markdown("## Aumentar brillo de una imagen")
        gr.Markdown("Sube una imagen y la función `aumentar_Brillo()` y `aumentar_brillo_Canal()` aumentará el brillo según el valor seleccionado.")
        gr.Markdown("Selecciona el canal al que deseas aplicar el brillo o selecciona 'Todos' para aplicarlo a toda la imagen. Luego, ajusta el valor de brillo utilizando el slider o el número y haz clic en 'Modificar brillo' para ver el resultado.")
        with gr.Row():
            input = gr.Image(type="filepath")
            with gr.Column():
                selector_canal = gr.Dropdown(choices=[("Todos", "-1"),("Rojo", "0" ), ("Verde", "1"), ("Azul", "2")], label="Selecciona el canal a modificar", interactive=True)
                input_brillo_slider = gr.Slider(-255, 255, value=0, step=1, label="Valor de brillo")
                input_brillo_num = gr.Number(label="Valor de brillo (numérico)", value=10, interactive=True, minimum=-255, maximum=255)
                boton_brillo = gr.Button("Modificar brillo")
            output = gr.Image(type="numpy")
            # Hacer que tanto el slider como el botón usen el wrapper y pasen el canal
            input_brillo_slider.change(aplicar_brillo_por_canal, inputs=[input, input_brillo_slider, selector_canal], outputs=output)
            boton_brillo.click(aplicar_brillo_por_canal, inputs=[input, input_brillo_num, selector_canal], outputs=output)

    # CANALES 
    with gr.Tab("Canales"):
        gr.Markdown("## Canales de una imagen")
        gr.Markdown("Aislar cada canal de color RGB y CMY")
        gr.Markdown("Selecciona una imagen y la función correspondiente se encargará de retornar el canal seleccionado.")

        with gr.Accordion("Canal Rojo", open=False):
            gr.Markdown("## Canal Rojo")
            gr.Markdown("Sube una imagen y la función `canal_Rojo()` se encargará de retornar su canal rojo.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Rojo, inputs=input, outputs=output)

        with gr.Accordion("Canal Verde", open=False):
            gr.Markdown("## Canal Verde")
            gr.Markdown("Sube una imagen y la función `canal_Verde()` se encargará de retornar su canal verde.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Verde, inputs=input, outputs=output)

        with gr.Accordion("Canal Azul", open=False):
            gr.Markdown("## Canal Azul")
            gr.Markdown("Sube una imagen y la función `canal_Azul()` se encargará de retornar su canal azul.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Azul, inputs=input, outputs=output)

        with gr.Accordion("Canal Cyan", open=False):
            gr.Markdown("## Canal Cyan")
            gr.Markdown("Sube una imagen y la función `canal_Cyan()` se encargará de retornar su canal cyan.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Cyan, inputs=input, outputs=output)

        with gr.Accordion("Canal Magenta", open=False):
            gr.Markdown("## Canal Magenta")
            gr.Markdown("Sube una imagen y la función `canal_Magenta()` se encargará de retornar su canal magenta.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Magenta, inputs=input, outputs=output)
    
        with gr.Accordion("Canal Amarillo", open=False):
            gr.Markdown("## Canal Amarillo")
            gr.Markdown("Sube una imagen y la función `canal_Amarillo()` se encargará de retornar su canal amarillo.")
            with gr.Row():
                input = gr.Image(type="filepath")
                output = gr.Image(type="numpy")
                input.change(libreria.canal_Amarillo, inputs=input, outputs=output)

    # ESCALA DE GRISES
    with gr.Tab("Grises"):
        gr.Markdown("## Conversión a escala de grises")
        gr.Markdown("""Sedlecciona una imagen y selecciona metodo, luego las funciones
        `gris_Average()`, `gris_Luminosity()` o `gris_MidGray()` convertirán la imagen a escala de grises según el método seleccionado.""")
        with gr.Row():
            input = gr.Image(type="filepath")
            with gr.Column():
                tipo_gris = gr.Radio(["Average", "Luminosity", "MidGray"], label="Método", info="Selecciona el método de conversión")
                boton_convertir_grises = gr.Button("Convertir a escala de grises")
                #boton_grises_promedio = gr.Button("Convertir por metodo promedio")
                #boton_grises_midgray = gr.Button("Convertir por metodo ponderado")
                #boton_grises_luminosity = gr.Button("Convertir por metodo luminosity")
            output = gr.Image(type="numpy")
            boton_convertir_grises.click(aplicar_escala_grises, inputs=[input, tipo_gris], outputs=output)
            #boton_grises_promedio.click(libreria.gris_Average, inputs=input, outputs=output)
            #boton_grises_midgray.click(libreria.gris_Luminosity, inputs=input, outputs=output)
            #boton_grises_luminosity.click(libreria.gris_MidGray, inputs=input, outputs=output)

    # BINARIZACION / UMBRALIZACION
    with gr.Tab("Umbralizacion"):
        gr.Markdown("## Umbralización de una imagen")
        gr.Markdown("Sube una imagen y la función `binarizar` se encargará de umbralizar la imagen según el valor seleccionado.")
        with gr.Row():
            input = gr.Image(type="filepath")
            with gr.Column():
                input_umbral_slider = gr.Slider(0, 256, value=128, step=1, label="Valor de umbralización")
                input_umbral_num = gr.Number(label="Valor de umbralización (numérico)", value=128, interactive=True, minimum=0, maximum=255)
                boton_umbral = gr.Button("Aplicar umbralización")
            output = gr.Image(type="numpy")
            input_umbral_slider.change(libreria.binarizar, inputs=[input, input_umbral_slider], outputs=output)
            boton_umbral.click(libreria.binarizar, inputs=[input, input_umbral_num], outputs=output)

    # REDUCCION DE RESOLUCION
    with gr.Tab("Reduccion de resolución"):
        gr.Markdown("## Reducción de resolución de una imagen")
        gr.Markdown("Sube una imagen y la función `reducir_Resolucion` se encargará de reducir su resolución según el factor seleccionado.")
        with gr.Row():
            input = gr.Image(type="filepath")
            with gr.Column():
                input_factor_slider = gr.Slider(1, 10, value=2, step=1, label="Factor de reducción")
                input_factor_num = gr.Number(label="Factor de reducción (numérico)", value=2, interactive=True, minimum=1, maximum=10)
                boton_reduccion = gr.Button("Aplicar reducción")
            output = gr.Image(type="numpy")
            input_factor_slider.change(libreria.reduccion_Resolucion, inputs=[input, input_factor_slider], outputs=output)
            boton_reduccion.click(libreria.reduccion_Resolucion, inputs=[input, input_factor_num], outputs=output)

    # ROTACION
    with gr.Tab("Rotacion"):
        gr.Markdown("## Rotación de una imagen")
        gr.Markdown("Sube una imagen y la función `rotar` se encargará de rotarla según el ángulo seleccionado.")
        with gr.Row():
            input = gr.Image(type="filepath")
            with gr.Column():
                input_angulo_slider = gr.Slider(0, 360, value=90, step=1, label="Ángulo de rotación")
                input_angulo_num = gr.Number(label="Ángulo de rotación (numérico)", value=90, interactive=True, minimum=0, maximum=360)
                boton_rotacion = gr.Button("Aplicar rotación")
            output = gr.Image(type="numpy")
            input_angulo_slider.change(libreria.rotar, inputs=[input, input_angulo_slider], outputs=output)
            boton_rotacion.click(libreria.rotar, inputs=[input, input_angulo_num], outputs=output)
    # ZOOM
    with gr.Tab("Zoom"):
        gr.Markdown("## Zoom de una imagen")
        gr.Markdown("Sube una imagen y la función `zoom` se encargará de hacer zoom según el factor seleccionado.")
        with gr.Row():
            input = gr.Image(type="filepath")
            with gr.Column():
                input_zoom_tam = gr.Number(label="Tamaño de zoom (numérico)", value=0, interactive=True)
                input_zoom_fact = gr.Number(label="Factor de zoom (numérico)", value=1.0, interactive=True, minimum=0.1, maximum=10.0)
                boton_zoom = gr.Button("Aplicar zoom")
            output = gr.Image(type="numpy")
            boton_zoom.click(libreria.zoom, inputs=[input, input_zoom_tam, input_zoom_fact], outputs=output)
    
    # RECORTE 
    with gr.Tab("Recorte"):
        gr.Markdown("## Recorte de una imagen")
        gr.Markdown("Sube una imagen y la función `recortar` se encargará de recortarla según las coordenadas seleccionadas.")
        with gr.Row():
            input = gr.Image(type="filepath")
            with gr.Column():
                with gr.Row():
                        input_recorte_x1 = gr.Number(label="Coordenada X1 (numérico)", value=0, interactive=True)
                        input_recorte_x2 = gr.Number(label="Coordenada X2 (numérico)", value=0, interactive=True)
                        input_recorte_y1 = gr.Number(label="Coordenada Y1 (numérico)", value=0, interactive=True)
                        input_recorte_y2 = gr.Number(label="Coordenada Y2 (numérico)", value=0, interactive=True)
                boton_recorte = gr.Button("Aplicar recorte")
            output = gr.Image(type="numpy")
            boton_recorte.click(libreria.recorte, inputs=[input, input_recorte_x1, input_recorte_x2, input_recorte_y1, input_recorte_y2], outputs=output)

    # SUMA DE IMAGENES
    with gr.Tab("Suma de imágenes"):
        gr.Markdown("## Suma de dos imágenes")
        gr.Markdown("Sube dos imágenes y la función `suma_Imagenes` se encargará de sumarlas pixel a pixel.")
        with gr.Row():
            input1 = gr.Image(type="filepath", label="Fondo")
            input2 = gr.Image(type="filepath", label="Superposición")
            with gr.Column():
                alpha = gr.Slider(0, 1, value=0.5, step=0.01, label="Factor de mezcla (alpha)")
                boton_suma = gr.Button("Sumar imágenes")
            output = gr.Image(type="numpy", label="Resultado")
            boton_suma.click(libreria.sumar_Imagenes, inputs=[input1, input2, alpha], outputs=output)
            alpha.change(libreria.sumar_Imagenes, inputs=[input1, input2, alpha], outputs=output)

    # HISTOGRAMA
    with gr.Tab("Histograma"):
        gr.Markdown("## Histograma de una imagen")
        gr.Markdown("Sube una imagen y la función `histograma` se encargará de mostrar su histograma.")
        with gr.Row():
            input = gr.Image(type="filepath")
            with gr.Column():
                selector_canal = gr.Dropdown(choices=[("Rojo", "rojo" ), ("Verde", "verde"), ("Azul", "azul")], label="Selecciona el canal a modificar", interactive=True)
                boton_histograma = gr.Button("Mostrar histograma")
            output = gr.Image(type="numpy")
            boton_histograma.click(libreria.histograma, inputs=[input, selector_canal], outputs=output)

demo.launch(theme=gr.Theme.from_hub("lone17/kotaemon"))
