import os
import logging
import yaml
import shlex

# === CONFIGURAÇÃO DE LOG ===
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)
logger = logging.getLogger(__name__)


# === SCRIPT DE AUTOMAÇÃO ===
base_path = os.getcwd()
file_path = os.path.join(base_path, 'k6', 'execution_plans', 'teste.yaml')

def build_k6_command(script, env=None, output_d=None, output_j=None):
    cmd = ['k6', 'run']

    if env:
        for k, v in env.items():
            cmd += ['--env', f'{k}={v}']

    if output_d:
        cmd += ['--out', output_d]

    if output_j:
        cmd += ['--out', output_j]

    cmd.append(script)
    command = ' '.join(shlex.quote(c) for c in cmd)
    logger.info(f'Comando montado: {command}')

    return command

def load_k6_commands(file_path):
    logger.info(f'Lendo arquivo de configuração: {file_path}')

    if not os.path.exists(file_path):
        logger.error(f'Arquivo não encontrado: {file_path}')
        raise FileNotFoundError(f'Arquivo não encontrado: {file_path}')
    
    with open(file_path, 'r') as file:
        try:
            exec_plans = yaml.safe_load(file)
            logger.info(f'YAML carregado com sucesso ({len(exec_plans)} planos encontrados).')
        except yaml.YAMLError as e:
            logger.exception('Erro ao ler o arquivo YAML.')
            raise e

    commands = []

    for name, config in exec_plans.items():
        logger.info(f'Processando plano: {name}')

        credentials = config.get('credentials', {})
        env = {
            'KEYCLOAK_TOKEN_URL': credentials.get('keycloak_token_url', ''),
            'CLIENT_ID': credentials.get('client_id', ''),
            'CLIENT_SECRET': credentials.get('client_secret', ''),
            'API_URL': credentials.get('api_url', ''),
            'SCENARIO': config.get('scenario', '')
        }

        script = config.get('test', 'script.js')
        output_dashboard = config.get('output-dashboard', '')
        output_json = config.get('output-json', '')

        if not script.endswith('.js'):
            script += '.js'
        
        cmd = build_k6_command(script, env=env, output_d=output_dashboard, output_j=output_json)
        commands.append({'name': name, 'command': cmd})
        logger.info(f'Comando gerado para \'{name}\': {cmd}')

    return commands

def main():
    logger.info('Iniciando geração de comandos K6...')

    try:
        cmds = load_k6_commands(file_path)
        print('\n=== Comandos K6 gerados ===')
        for c in cmds:
            print(f'[{c["name"]}] {c["command"]}')
        logger.info('Processo concluído com sucesso.')
    except Exception as e:
        logger.exception('Erro durante a execução principal.')
        print(f'Erro: {e}')

if __name__ == '__main__':
    main()
