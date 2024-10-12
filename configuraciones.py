class Configuraciones:
    """Una clase para almacenar todas las configuraciones de Invasión
    Alienígena."""
    def __init__(self):
        """Inicializa las configuraciones del juego."""
        # Configuraciones de la pantalla
        self.ancho_pantalla = 1200
        self.alto_pantalla = 800
        self.color_fondo = (230, 230, 230)
        # Configuraciones de la bala
        self.velocidad_bala = 2.5
        self.ancho_bala = 3
        self.alto_bala = 15
        self.color_bala = (60, 60, 60)
        self.balas_permitidas = 50