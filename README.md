# Использованные технологии и назначение
* Python - автоматизация процесса обработки данных
* geopandas - чтение, фильтрация и запись пространственных данных
* tippecanoe - формирование векторных тайлов в формате MBTiles
* WSl(ubuntu) - среда выполнения tiopecanoe в Windows
* QGis 3.44.10 - проверка результата и создание контрольной карты
* Git - контроль версий
* GitHub - хранение репозитория
* VS Code - среда разработки

# Запуск проекта
> Для выполнения проекта необходимы:
* Python 3.12 или новее;
* WSL с установленной Ubuntu;
* утилита Tippecanoe (установлена в WSL);
* QGIS 3.44.10 (для проверки результата).

Так как создание MBTiles выполняется с помощью tippecanoe, установленного в WSl, проект запускается с терминалом ubuntu в vs code:
1. Клонируем репозиторий:  git clone https://github.com/natemma/test-task.git
2. Повторно открываем папку в WSL: Shift+Ctrl+P -> Reopen folder with WSL
3. Запускаем виртуальное окружение:  python3 -m venv .venv
   > source .venv/bin/activate
4. Устанавливаем зависимости: pip install -r requirements.txt
5. Запускаем проект:  python3 main.py
            
