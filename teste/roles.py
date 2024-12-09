from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions ={
        'cadastrar_produtos': True,
        'liberar_descontos': True,
        'cadastrar_gerente': True,
        'cadastrar_vendedor': True,
        'cadastrar_cliente': True
    }
class vendedor(AbstractUserRole):
    available = {
        'realizar_venda': True,
        'cadastrar_cliente': True
    }