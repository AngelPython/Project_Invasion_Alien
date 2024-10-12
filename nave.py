import pygame
class Nave:
    """Clase para gestionar la nave."""
    def __init__(self, juego_ia):
        """Inicializa la nave y establece su posición inicial."""
        self.pantalla = juego_ia.pantalla
        self.configuraciones = juego_ia.configuraciones
        self.rect_pantalla = juego_ia.pantalla.get_rect()
        # Cargar la imagen de la nave y obtener su rectángulo.
        self.imagen = pygame.image.load('imagenes/nave.bmp')
        self.rect = self.imagen.get_rect()
        # Comienza cada nueva nave en el centro inferior de la pantalla.
        self.rect.midbottom = self.rect_pantalla.midbottom
        # Almacenar un valor decimal para la posición horizontal de la nave.
        self.x = float(self.rect.x)
        # Bandera de movimiento
        self.moviendo_derecha = False
        self.moviendo_izquierda = False
    def actualizar(self):
        """Actualizar la posición de la nave según las banderas de movimiento."""
        if self.moviendo_derecha and self.rect.right < self.rect_pantalla.right:
            self.rect.x += 2
        if self.moviendo_izquierda and self.rect.left > 0:
            self.rect.x -= 2
        self.x = self.rect.x
    def dibujar_nave(self):
        """Dibuja la nave en su ubicación actual."""
        self.pantalla.blit(self.imagen, self.rect)