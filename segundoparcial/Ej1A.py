class Anuncio:
    def __init__(self, descripcion, precio):
        self.descripcion = descripcion
        self.precio = precio

class Artista:
    def __init__(self, nombre, experiencia):
        self.nombre = nombre
        self.experiencia = experiencia

class Pintura:
    def __init__(self, titulo, artista, anuncio=None):
        self.titulo = titulo
        self.artista = artista
        self.anuncio = anuncio 

    def agregar_anuncio(self, descripcion, precio):
        self.anuncio = Anuncio(descripcion, precio)

    def obtener_nombre_artista(self):
        return self.artista.nombre

    def obtener_experiencia_artista(self):
        return self.artista.experiencia

artista1 = Artista("Pablo Picasso", 40)
artista2 = Artista("Salvador Dalí", 35)

pintura1 = Pintura("Guernica", artista1, Anuncio("Venta privada", 5000))
pintura2 = Pintura("La persistencia de la memoria", artista2)

if pintura1.obtener_experiencia_artista() > pintura2.obtener_experiencia_artista():
    print(f"El artista con más experiencia es {pintura1.obtener_nombre_artista()}.")
else:
    print(f"El artista con más experiencia es {pintura2.obtener_nombre_artista()}.")
pintura2.agregar_anuncio("Venta pública", 4500)
monto_total = pintura1.anuncio.precio + pintura2.anuncio.precio
print(f"El monto total de venta de ambas pinturas es: ${monto_total}.")
