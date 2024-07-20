# Инструкция для Приёмки-01 от 2024-07-20

1. Установить Python 3.11.2
    https://www.python.org/downloads/release/python-3112/
    выбрать Windows installer (64-bit)
    выбрать Add python.exe to PATH
2. Установить Git 2.45.2
    https://git-scm.com/download/win/
    выбрать Add a Git Bash Profile to Windows Terminal
    выбрать Enable symbolic links
3. Запустить Git Bash
4. Проверить работу Python и Git
    выполнить: python --version
    выполнить: git --version
5. Склонировать прототип
    выполнить: git clone https://github.com/kornerr/proto-hotel
6. Установить зависимости проекта
    выполнить: ./setup.w
7. Запустить проект 
    выполнить: ./run.w
8. В случае пробле с питоном
    обновить файл python
        прописать путь до питона напрямую
    обновить файлы setup.w и run.w
        заменить python на ./python
