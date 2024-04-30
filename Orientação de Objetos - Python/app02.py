from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Rodrigo', 2.3)
restaurante_praca.receber_avaliacao('Carla', 4.7)
restaurante_praca.receber_avaliacao('Jesus', 3.2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()