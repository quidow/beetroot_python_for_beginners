"""
1. Проверьте есть ли папка cache если нет то создайте с правами на запись.
2. Создайте в цикле там пяток файлов с рандомным именем и расширением .bak
можно использовать random.choice а можно модуль uuid для генерации рандомной 
строки.
3. Просканируйте директорию cache и выведите только файлы bak
"""

import os
import uuid

cache_dir = './cache/'

if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)
    os.chmod(cache_dir, 755)

for i in range(5):
    with open(cache_dir + str(uuid.uuid1()) + ".bak", "w") as f:
        f.close()

for f in os.listdir(cache_dir):
    if f.endswith(".bak"):
        print(f)
