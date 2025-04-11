import platform


sistema_operacional = platform.system()
versao_sistema = platform.version()
arquitetura_processador = platform.machine()


print(f"Sistema Operacional: {sistema_operacional}")
print(f"Versão do Sistema: {versao_sistema}")
print(f"Arquitetura do Processador: {arquitetura_processador}")
