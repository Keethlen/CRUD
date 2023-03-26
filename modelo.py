from dataclasses import dataclass

#Anotações: as classes iniciam com o @
#Classes iniciam com letras maiusculas
@dataclass
class Dono:
    nome: str
    telefone: int
    email: str
    tipo: str
    raca: str
    tamanho_animal: str


