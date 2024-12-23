# Шаги для запуска приложения
## При запуске на локальной машине без docker:
```bash
uvicorn main:app --forwarded-allow-ips='*' --proxy-headers --log-level debug --reload --port 8001
```

## При запуске через докер (включая сборку):
1. Сборка образа
```bash
docker build -t urfu_study_short_url_prj .
```
2. Запуск контейнера
```bash
docker run -d -p 8001:80 -v shorturl_data:/app/data urfu_study_short_url_prj
```

## При запуске через докер (пулл с docker hub):
### ❗❗❗ Только для arm-архитектуры ❗❗❗
```bash
docker run -d -p 8001:80 -v todo_data:/app/data alexskvorz76/urfu_study_short_url_prj:latest
```