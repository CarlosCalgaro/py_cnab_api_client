class ClientError(Exception):
    """Erro relacionado ao cliente da API CNAB."""
    pass

class BankAdapterNotFoundError(Exception):
    """Erro lançado quando um adaptador de banco não é encontrado para um código de banco específico."""
    pass