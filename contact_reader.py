import pandas as pd

def load_contacts(file_path:str) -> dict:
    """_ Read a xlsx file and return his data
    as a dictionary _

    Args:
        file (str): _Path to the file_

    Raises:
        Exception: _Tell about file errors_

    Returns:
        dict: _A dictionary that contains all the names and emails from the file
        _
    """
    try:
        clientes = pd.read_excel(file_path)
        print('Contatos carregados com sucesso!')
        print(clientes)
        return clientes
    except Exception as e:
        raise Exception(f"Erro ao ler o arquivo: {e}")
