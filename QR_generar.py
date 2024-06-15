# Generar código QR
import os
import qrcode

def generar_qr_estatico(materia):
    url = f"http://localhost:5000/registrar_asistencia?materia={materia}"
    archivo_salida = os.path.join('static', f"{materia}_qr.png")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(archivo_salida)
    print(f"Código QR generado para {materia}: {archivo_salida}")

# Generar códigos QR para cada materia
materias = [
    "Programacion1",
    "Competencias_Comunicacionales",
    "Bases_de_Datos",
    "Aproximacion_al_Mundo_del_Trabajo",
    "Elementos_de_Matematica_y_Logica",
    "Sistemas_y_Organizaciones"
]

for materia in materias:
    generar_qr_estatico(materia)