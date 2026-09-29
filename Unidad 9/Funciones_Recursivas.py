class Archivo:
    def __init__(self, nombre: str, tamano_bytes: int):
        self.nombre = nombre
        self.tamano_bytes = tamano_bytes

class Directorio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.archivos = []
        self.subdirectorios = []

def calcular_tamano_total(directorio: Directorio) -> int:
    tamano_archivos = sum(archivo.tamano_bytes for archivo in directorio.archivos)
    tamano_subdirectorios = sum(calcular_tamano_total(sub) for sub in directorio.subdirectorios)
    
    return tamano_archivos + tamano_subdirectorios
def buscar_por_extension(directorio: Directorio, extension: str) -> list[str]:
    archivos_encontrados = []

    for archivo in directorio.archivos:
        if archivo.nombre.endswith(extension):
            archivos_encontrados.append(archivo)

    for subdirectorio in directorio.subdirectorios:
        archivos_encontrados.extend(buscar_por_extension(subdirectorio, extension))

    return archivos_encontrados

def limpiar_archivos_vacios(directorio: Directorio) -> int:
    archivos_eliminados = 0

    for archivo in directorio.archivos:
        if archivo.tamano_bytes == 0:
            directorio.archivos.remove(archivo)
            archivos_eliminados += 1

    for subdirectorio in directorio.subdirectorios:
        archivos_eliminados += limpiar_archivos_vacios(subdirectorio)

    return archivos_eliminados