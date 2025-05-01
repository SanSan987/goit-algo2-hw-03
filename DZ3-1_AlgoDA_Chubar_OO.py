# Програмна реалізація Завдання 1 «Застосування алгоритму максимального потоку для логістики товарів»

import networkx as nx
from prettytable import PrettyTable

# Побудова графа
G = nx.DiGraph()

# Додаємо ребра з пропускною здатністю (термінали до складів)
G.add_edge('T1', 'S1', capacity=25)
G.add_edge('T1', 'S2', capacity=20)
G.add_edge('T1', 'S3', capacity=15)
G.add_edge('T2', 'S3', capacity=15)
G.add_edge('T2', 'S4', capacity=30)
G.add_edge('T2', 'S2', capacity=10)

# Склади до магазинів
G.add_edge('S1', 'M1', capacity=15)
G.add_edge('S1', 'M2', capacity=10)
G.add_edge('S1', 'M3', capacity=20)
G.add_edge('S2', 'M4', capacity=15)
G.add_edge('S2', 'M5', capacity=10)
G.add_edge('S2', 'M6', capacity=25)
G.add_edge('S3', 'M7', capacity=20)
G.add_edge('S3', 'M8', capacity=15)
G.add_edge('S3', 'M9', capacity=10)
G.add_edge('S4', 'M10', capacity=20)
G.add_edge('S4', 'M11', capacity=10)
G.add_edge('S4', 'M12', capacity=15)
G.add_edge('S4', 'M13', capacity=5)
G.add_edge('S4', 'M14', capacity=10)

# Додаємо джерело та стік
G.add_edge('SOURCE', 'T1', capacity=1000)
G.add_edge('SOURCE', 'T2', capacity=1000)

# З’єднуємо магазини до стоку
for i in range(1, 15):
    G.add_edge(f'M{i}', 'SINK', capacity=1000)

# Застосування алгоритму Едмондса-Карпа
flow_value, flow_dict = nx.maximum_flow(G, 'SOURCE', 'SINK')

print(f"\nМаксимальний потік у мережі: {flow_value}\n")

# Побудова очищеної таблиці: тільки потоки Термінал → Магазин
table = PrettyTable()
table.field_names = ["Термінал", "Магазин", "Фактичний Потік (одиниць)"]

for terminal in ['T1', 'T2']:
    for warehouse in flow_dict[terminal]:
        if flow_dict[terminal][warehouse] > 0:
            # Перевіряємо, чи є склад у словнику потоку
            if warehouse in flow_dict:
                for shop in flow_dict[warehouse]:
                    flow = flow_dict[warehouse][shop]
                    if flow > 0 and shop.startswith("M"):
                        table.add_row([terminal, shop, flow])

print("Потоки між терміналами та магазинами:")
print(table)

