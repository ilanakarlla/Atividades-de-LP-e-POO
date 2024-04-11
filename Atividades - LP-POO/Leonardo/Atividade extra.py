lass conta_bancaria:
    def __init__(self, titular, saldo):
        self.limite = 0
        self.titular = titular
        self.saldo = saldo
        self.conta_ativa = False

    def sacar(self, quantia):
        if not self.conta_ativa:
            print('A conta não está ativa')
            return
        self.saldo -= quantia
        print(f'Você sacou {quantia} de {self.saldo + quantia}')

    def depositar(self, quantia):
        if not self.conta_ativa:
            print('A conta não está ativa')
            return
        self.saldo += quantia
        print(f'Você depositou {quantia} em {self.saldo - quantia}')

    def bloqueio(self):
        if not self.conta_ativa:
            self.conta_ativa = True
            print('A conta foi ativada')
        else:
            self.conta_ativa = False
            print('A conta foi desativada')

    def verificar_saldo(self):
        if not self.conta_ativa:
            print('A conta não está ativa')
            return
        print(f'{self.saldo}')

    def mudar_limite(self, quantia):
        if not self.conta_ativa:
            print('A conta não está ativa')
            return
        self.limite = quantia


A = conta_bancaria('Carlos', 700)
A.sacar(200)
A.bloqueio()
A.sacar(200)
A.verificar_saldo()
