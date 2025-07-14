from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos': True,
        'liberar_descontos': True,
        'cadastrar_gerente': True,
        'editar_gerente': False,
        'excluir_gerente': False,
        'cadastrar_vendedor': True,
        'cadastrar_cliente': True,
        'realizar_venda': True
    }
class vendedor(AbstractUserRole):
    available_permissions = {
        'realizar_venda': True,
        'cadastrar_cliente': True,
    }