#invasion_alienigena.py
import sys
import pygame
from configuraciones import Configuraciones
from nave import Nave
from balas import Bala
class InvasionAlienigena:
    """Clase general para gestionar los recursos y el comportamiento del
    juego."""
    def __init__(self):
        """Inicializa el juego y crea los recursos del juego."""
        pygame.init()
        self.fuente = pygame.font.SysFont(None, 28)  # Carga una fuente
        self.reloj = pygame.time.Clock()
        self.configuraciones = Configuraciones()
        self.pantalla = pygame.display.set_mode((self.configuraciones.ancho_pantalla, self.configuraciones.alto_pantalla))
        self.ancho_pantalla = self.configuraciones.ancho_pantalla
        self.alto_pantalla = self.configuraciones.alto_pantalla
        pygame.display.set_caption("Invasión Alienígena")
        self.nave = Nave(self)
        self.balas = pygame.sprite.Group()
        self.fullscreen = False
    def ejecutar_juego(self):
        """Inicia el bucle principal para el juego."""
        while True:
            self._check_events()
            self.nave.actualizar()  # Llamada para actualizar la posición de la nave
            self.balas.update()#balas.update
            for bala in self.balas.copy():
                if bala.rect.bottom <= 0:
                    self.balas.remove(bala)
            #print(len(self.balas))  # Mostrar cuántas balas quedan
            self._update_screen()
            self.reloj.tick(60)
    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos del ratón."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                self._verificar_eventos_keydown(evento)
            elif evento.type == pygame.KEYUP:
                self._verificar_eventos_keyup(evento)
    def _verificar_eventos_keydown(self, event):
        """Responder a las pulsaciones de teclas."""
        if event.key == pygame.K_RIGHT:
            self.nave.moviendo_derecha = True
        elif event.key == pygame.K_LEFT:
            self.nave.moviendo_izquierda = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_f:
            self._cambiar_pantalla_completa()
        elif event.key == pygame.K_SPACE:
            self._disparar_bala()
    def _verificar_eventos_keyup(self, event):
        """Responder a las teclas liberadas."""
        if event.key == pygame.K_RIGHT:
            self.nave.moviendo_derecha = False
        elif event.key == pygame.K_LEFT:
            self.nave.moviendo_izquierda = False
    def _cambiar_pantalla_completa(self):
        """Cambia entre modo ventana y pantalla completa."""
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.pantalla = pygame.display.set_mode((self.ancho_pantalla, self.alto_pantalla))
        self.nave.rect_pantalla = self.pantalla.get_rect()
        self.nave.rect.midbottom = self.nave.rect_pantalla.midbottom
    def _disparar_bala(self):
        """Crear una nueva bala y agregarla al grupo de balas."""
        if len(self.balas) < self.configuraciones.balas_permitidas:
            nueva_bala = Bala(self)
            self.balas.add(nueva_bala)
    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y cambia a la nueva pantalla."""
        self.pantalla.fill(self.configuraciones.color_fondo)
        self.nave.dibujar_nave()
        texto_balas = f'Balas restantes: {self.configuraciones.balas_permitidas-len(self.balas)}'
        superficie_texto = self.fuente.render(texto_balas, True, (0, 0, 0))  # Texto negro
        self.pantalla.blit(superficie_texto, (10, 10))  # Dibuja el texto en la esquina superior izquierda
        for bala in self.balas.sprites():
            bala.dibujar_bala()
        pygame.display.flip()
if __name__ == '__main__':
    # Crea una instancia del juego y ejecuta el juego.
    ia = InvasionAlienigena()
    ia.ejecutar_juego()