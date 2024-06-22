class computador:
    def __init__(self, *args, *kwargs):
        self.marca = kwargs.get('marca')
        self.memoria = kwargs.get('memoria')def 
        self.placa_video = kwargs.get('placa_video')
        self.usuario = kwargs.get('usuario')
        self.senha = kwargs.get('senha')
        self.liga = False
    @property
    def ligar(self):
        return None
    
    @ligar.setter
    def ligar(self, opcao):
        if opcao == 1:

    text = 'Escolha a opção: \n'
    text += '1 -> Desligar \n'
    text += '2 -> Ligar \n'
    ligar = input(text)
    if ligar == '2':
        usuario_digita = input('Digite o usuário: ')
        senha_digita = input('Digite a senha: ')
        if usuario_digita == usuario and senha_digita == senha:
            text = f'marca do computador: {marca} \n'
            text += f'a memoria do computador: {memoria_ram} \n'
            text += f'a placa de video do computador: {placa_video} \n'
        else: 
            text = 'O usuari e senha digitado não confere!'
    else:
        text = 'Irei desligar agora!'
    print(text)


computador()
    