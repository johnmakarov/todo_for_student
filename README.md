# Небольшое TODO FastAPI приложение. 

## Запустить 
1. Установить Poetry - https://python-poetry.org/docs/#installation
2. poetry install --no-root
3. poetry run uvicorn app.main:app --reload

При использованиее флага --reload каждый раз при внесении изменения в проект будет перезапускаться приложение. Из за того что данные хранятся в памяти это может быть не всегда удобно и можно запускать без флага --reload. 