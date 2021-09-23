class Conta:
    def __init__(self, **kwargs):
        """
        Construtor da classe Conta.
        Recebe via kwargs :
        - nome
        - limite
        - saldo

        Raises:
            ValueError: Nome Informado seja vazio.
            ValueError: Saldo seja menor que zero.
        """
        self.extrato = []
        self.limite = kwargs.get('limite', 500)
        self.nome = kwargs.get('nome', None)
        if self.nome == None:
            raise ValueError('Nome não informado')
        self.saldo = 0
        saldo = kwargs.get('saldo', self.saldo)
        if saldo < 0:
            raise ValueError('Saldo negativo')
        self.saldo = saldo
        self.extrato.append(('I', saldo))

