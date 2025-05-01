# Програмна реалізація Завдання 2 «Порівняння ефективності OOBTree і словника для діапазонних запитів»

from BTrees.OOBTree import OOBTree
import csv
import timeit
from typing import Dict, List
from collections import defaultdict

# Читання файлу CSV
def load_items_from_csv(file_path: str) -> list:
    items = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append({
                "id": row["ID"],
                "name": row["Name"],
                "category": row["Category"],
                "price": float(row["Price"])
            })
    return items

# Функція додавання до OOBTree: ключ — ціна
def add_item_to_tree(tree: OOBTree, item: Dict):
    price = item["price"]
    if price not in tree:
        tree[price] = []
    tree[price].append(item)

# Функція діапазонний запит у OOBTree
def range_query_tree(tree: OOBTree, min_price: float, max_price: float):
    result = []
    for _, items in tree.items(min_price, max_price):
        result.extend(items)
    return result

# Функція додавання до звичайного словника
def add_item_to_dict(store: Dict, item: Dict):
    store[item["id"]] = item

# Функція діапазонний запит у словнику
def range_query_dict(store: Dict, min_price: float, max_price: float):
    return [item for item in store.values() if min_price <= item["price"] <= max_price]

# Підготовка
items = load_items_from_csv('D:/Документы/TopOld/MINE/Student/ITStudy/Algo_D&A/generated_items_data.csv')
tree = OOBTree()
dict_store = {}

for item in items:
    add_item_to_tree(tree, item)
    add_item_to_dict(dict_store, item)

# Межі діапазону
min_price = 100
max_price = 200

# Вимірювання часу
print("Виконання діапазонних запитів по OOBTree...")
tree_time = timeit.timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)
print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")

print("Виконання діапазонних запитів по Dict...")
dict_time = timeit.timeit(lambda: range_query_dict(dict_store, min_price, max_price), number=100)
print(f"Total range_query time for Dict: {dict_time:.6f} seconds")
