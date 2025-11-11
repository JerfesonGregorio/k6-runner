import os
from src.logger import logger
from src.loader import load_k6_commands
from src.executor import execute_command

base_path = os.getcwd()
file_path = os.path.join(base_path, 'k6', 'execution_plans', 'template.yaml')

def main():
    logger.info('Iniciando geração de comandos K6...')

    try:
        cmds = load_k6_commands(file_path)
        print('\n=== Comandos K6 gerados ===')
        for c in cmds:
            execute_command(c['name'], c['command'])

        logger.info('Processo concluído com sucesso.')
    except Exception as e:
        logger.exception('Erro durante a execução principal.')
        print(f'Erro: {e}')

if __name__ == '__main__':
    main()
