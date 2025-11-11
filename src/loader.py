import os
import shlex
import yaml
from src.logger import logger

base_path = os.getcwd()

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
            'SCENARIO': config.get('scenario', ''),
            'PAYLOAD': config.get('payload', '')
        }   

        script = config.get('test', 'script.js')

        if not script.endswith('.js'):
            script += '.js'
        
        script_path = base_path + '/k6/tests/' + script
        output_dashboard = config.get('output-dashboard', '')
        output_json = config.get('output-json', '')
        
        cmd = build_k6_command(script_path, env=env, output_d=output_dashboard, output_j=output_json)
        commands.append({'name': name, 'command': cmd})
        logger.info(f'Comando gerado para \'{name}\': {cmd}')

    return commands
