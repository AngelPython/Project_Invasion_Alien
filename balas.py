import pygame
from pygame.sprite import Sprite
class Bala(Sprite):
    """Una clase para gestionar las balas disparadas desde la nave."""
    def __init__(self, ai_juego):
        """Crear un objeto bala en la posición actual de la nave."""
        super().__init__()
        self.pantalla = ai_juego.pantalla
        self.configuraciones = ai_juego.configuraciones#??
        self.color = self.configuraciones.color_bala
        # Crear un rectángulo para la bala en (0, 0) y luego establecer la posición correcta.
        self.rect = pygame.Rect(0, 0, self.configuraciones.ancho_bala,self.configuraciones.alto_bala)
        self.rect.midtop = ai_juego.nave.rect.midtop
        # Almacenar la posición de la bala como un número flotante.
        self.y = float(self.rect.y)
    def update(self):
        """Mover la bala hacia arriba en la pantalla."""
        # Actualizar la posición exacta de la bala.
        self.y -= self.configuraciones.velocidad_bala
        # Actualizar la posición del rectángulo.
        self.rect.y = self.y
    def dibujar_bala(self):
        """Dibujar la bala en la pantalla."""
        pygame.draw.rect(self.pantalla, self.color, self.rect)