from time import time

def tempo_de_execucao(func):
    """
    Decorador que mede e exibe o tempo de execução de uma função.

    Ao aplicar este decorador a uma função, ele calcula quanto tempo
    a função levou para ser executada e imprime o resultado no formato:
    'nome_da_função executada em X minuto(s) e Y segundo(s)'.

    Obs: esta versão do decorador só funciona com funções que não recebem argumentos.

    Exemplo:
        @tempo_de_execucao
        def minha_funcao():
            # código que leva tempo para executar
            ...

        minha_funcao()

    """
    inicio = time()
    def wrapper():
        func()
        fim = time()
        duracao = fim - inicio
        minutos = int(duracao // 60)
        segundos = duracao % 60

        print(f"{func.__name__} executada em {minutos} minuto(s) e {segundos:.2f} segundo(s)")

    return wrapper