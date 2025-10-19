# Небольшое TODO приложение

## Запустить бэк
1. cd app 
2. Установить Poetry - https://python-poetry.org/docs/#installation
3. poetry install --no-root
4. poetry run uvicorn main:app --reload

При использованиее флага --reload каждый раз при внесении изменений в проект будет перезапускаться приложение. Из за того что данные хранятся в памяти (список в python) это может быть не всегда удобно и можно запускать без флага --reload. 