class Livro:
    def __init__(self, *args, *kwargs)) -> None:
        self.titulo = kwargs.get('titulo')
        self.autor = kwargs.get('auto')
        self.ano_publicacao = kwargs.get('ano_publicacao')
        self.disponivel = kwargs.get('disponivel')
        self.text = ''
    
    def empresta(self):
        if self.disponivel:
            self.disponivel = False
            self.text = f'livro {self.titulo} emprestado'
        else:
            self.text = f'livro {self.titulo} não esta disponivel'
    print(self.text)


    def devolver(self):
        self.disponivel = True

    def exibir_intormacoes(self):
        self.text = f'O livro: {self.titulo} \n'
        self.text += f'O autor: {self.autor} \n'
        self.text += f'Ano: {self.ano_publicacao} \n'
        self.text += f'Esta disponivel {self.disponivel}
        print(self.text)
    

class Biblioteca:
    def __init__(self, *args, *kwargs)) -> None:
        self.nome = kwargs.get('nome')
        self.livros = []
        self.text = ''

    @property
    def adicionar_livro(self):
        return None
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    @property
    def remover_livro(self):
        None

    @remover_livro.setter
    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(titulo)

        self.livro.titulo = ''

    @property
    def buscar_livro(self):
        return None
    
    @buscar_livro.setter
    def buscar_livro(self):
        self.livro.exibir_intormacoes

    @property
    def exibir_livros_disponiveis(self):
        return None

    @exibir_livros_disponiveis.setter
    def exibir_livros_disponiveis(self):
        self.livro.exibir_intormacoes