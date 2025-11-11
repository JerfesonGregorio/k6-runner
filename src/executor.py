import os
from src.logger import logger

def execute_command(name, command):
    logger.info(f'INICIANDO plano: [ {name} ]')
    try:
        return_code = os.system(command)
        if return_code != 0:
            raise Exception(f'Comando retornou um código de saída não-zero: {return_code}')
        
        logger.info(f'CONCLUÍDO plano: [ {name} ]')
        return f"Sucesso: {name}"
    except Exception as e:
        logger.error(f'ERRO no plano: [ {name} ] - {e}')
        raise e