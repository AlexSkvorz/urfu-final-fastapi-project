# Шаги для запуска приложения
## При запуске на локальной машине без docker:
```bash
uvicorn main:app --forwarded-allow-ips='*' --proxy-headers --log-level debug --reload
```

## При запуске через докер (включая сборку):
1. Сборка образа
```bash
docker build -t urfu_study_todo_prj .
```
2. Запуска образа
```bash
docker run -d -p 8000:80 -v todo_data:/app/data urfu_study_todo_prj
```

## При запуске через докер (пулл с docker hub):
### ❗❗❗ Только для arm-архитектуры ❗❗❗
```bash
docker run -d -p 8000:80 -v todo_data:/app/data alexskvorz76/urfu_study_todo_prj:latest
```