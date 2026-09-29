from Funciones_Recursivas import *

root = Directorio("root")
imagenes = Directorio("imagenes")
proyectos = Directorio("proyectos")
temp = Directorio("temp")

root.archivos.append(Archivo("documento.pdf", 1500))
root.archivos.append(Archivo("config.txt", 0))

imagenes.archivos.append(Archivo("foto1.png", 2000))
imagenes.archivos.append(Archivo("foto2.png", 3500))

proyectos.archivos.append(Archivo("avance.pdf", 800))
temp.archivos.append(Archivo("log.txt", 0))

proyectos.subdirectorios.append(temp)
root.subdirectorios.append(imagenes)
root.subdirectorios.append(proyectos)

tamano_total = calcular_tamano_total(root)
print(f"1. calcular_tamano_total(root) -> {tamano_total} bytes")

pdfs = buscar_por_extension(root, ".pdf")
print(f"2. buscar_por_extension(root, '.pdf') -> {pdfs}")

eliminados = limpiar_archivos_vacios(root)
print(f"3. limpiar_archivos_vacios(root) -> {eliminados} archivos eliminados")