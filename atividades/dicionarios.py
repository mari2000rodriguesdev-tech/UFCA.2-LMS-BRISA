# Dicionaios
sensor = { "id": 101, "tipo": "temperatura", "valor": 23.5} #São mutáveis, permitindo adicionar, remover ou alterar elementos após a criação.

# Definindo um dicionário de estados de máquinas industriais
estados_maquinas = {
    "maquina_1": "operacional",
    "maquina_2": "manutencao",
    "maquina_3": "parada",
    "maquina_4": "operacional"
}

print(f"O estado da máquina 1 é:", estados_maquinas["maquina_1"]) #acessando o estado de uma maquina específica

#modificando o estado de uma máquina
estados_maquinas["maquina_2"] = "operacional"
print(f"Os estados atualizados das máquinas são: {estados_maquinas}")

# Operações com dicionários
estados_maquinas = {
    "maquina_1": "operacional",
    "maquina_2": "manutencao",
    "maquinia_3": "parada",
    "mauquina_4": "operacional"
}

estados_maquinas.update({"maquina_5": "operacional"}) # update() é utilizado para adicionar ou atualizar elementos no dicionário
estados_maquinas.update({"maquina_6": "manutencao"})
print(f"Estados após adicionar novas máquinas: {estados_maquinas}")

# Acessando estados específicos:
estado_maquina_1 = estados_maquinas["maquina_1"]
estado_maquina_3 = estados_maquinas["maquina_3"]
print(f"O estado da máquina 1 é: {estado_maquina_1}")
print(f"O estado da máquina 3 é: {estado_maquina_3}")

# Modificando um estado:
# Modificar dados em tempo real é importante para controle de processos e correção de erros.
estados_maquinas["maquina_2"] = "operacional"  # Supondo que a máquina 2 voltou a operar
print(f"Estados após atualização: {estados_maquinas}")

# Removendo um estado:
# Gerenciar o tamanho dos dicionários é importante para otimização de memória.
del estados_maquinas["maquina_3"]  # Remove o estado da máquina 3 (desativada)
print(f"Estados após remover uma máquina: {estados_maquinas}")


# Verificando o tamanho do dicionário:
# A função len() permite conhecer o tamanho do dicionário, ajudando no gerenciamento de recursos e na lógica de controle.
print(f"Número total de estados registrados: {len(estados_maquinas)}")

# Listando todas as máquinas cadastradas:
# Você pode fazer isso sem precisar percorrer manualmente o dicionário através de keys().
print(f"Máquinas atualmente registradas: {estados_maquinas.keys()}")

comandos_maquinas = {
    "maquina_A": ["ligar", "monitorar", "desligar"],
    "maquina_B": ["manutencao", "calibrar"],
    "maquina_C": ["ligar", "monitorar"],
    "maquina_D": ["ligar", "desligar"]
}

print(f"\nComandos para as máquinas: {comandos_maquinas}")