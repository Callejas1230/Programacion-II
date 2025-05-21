class Anuncio:
    """Clase que representa un anuncio de venta."""
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
class Artista:
    """Clase que representa a un artista con años de experiencia."""
    def __init__(self, nombre, ci, años_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.años_experiencia = años_experiencia
class Obra:
    """Clase que representa una obra de arte, incluyendo materiales y artistas."""
    def __init__(self, titulo, material, artistas, anuncio):
        self.titulo = titulo
        self.material = material
        self.artistas = artistas 
        self.anuncio = anuncio 
class Pintura:
    """Clase que representa una pintura con su género artístico."""
    def __init__(self, genero, obra):
        self.genero = genero
        self.obra = obra
anuncio1 = Anuncio(numero=1, precio=100)
anuncio2 = Anuncio(numero=2, precio=200)
artista1 = Artista(nombre="Juan Pérez", ci="123456", años_experiencia=10)
artista2 = Artista(nombre="Fernando Loza", ci="789012", años_experiencia=15)
obra1 = Obra(titulo="Obra1", material="Óleo", artistas=[artista1], anuncio=anuncio1)
obra2 = Obra(titulo="Obra2", material="Acrílico", artistas=[artista2], anuncio=anuncio2)
pintura1 = Pintura(genero="Abstracto", obra=obra1)
pintura2 = Pintura(genero="Realismo", obra=obra2)
def promedio_años_experiencia(pinturas):
    total_años = sum(artista.años_experiencia for pintura in pinturas for artista in pintura.obra.artistas)
    total_artistas = sum(len(pintura.obra.artistas) for pintura in pinturas)
    return total_años / total_artistas if total_artistas > 0 else 0
promedio_experiencia = promedio_años_experiencia([pintura1, pintura2])
print(f"Promedio de años de experiencia de los artistas: {promedio_experiencia}")
def incrementar_precio(pinturas, nombre_artista, incremento):
    for pintura in pinturas:
        for artista in pintura.obra.artistas:
            if artista.nombre == nombre_artista:
                pintura.obra.anuncio.precio += incremento
incrementar_precio([pintura1, pintura2], "Juan Pérez", 50)
print(f"Nuevo precio de la pintura de 'Juan Pérez': {pintura1.obra.anuncio.precio}")