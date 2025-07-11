# Flask CI/CD Demo

Ứng dụng Flask đơn giản được triển khai tự động bằng Jenkins và Docker.

## Cấu trúc dự án
- `app.py`: Ứng dụng Flask chính
- `requirements.txt`: Danh sách dependencies
- `Dockerfile`: Cấu hình Docker image
- `Jenkinsfile`: Pipeline CI/CD

## Chạy local
```bash
pip install -r requirements.txt
python app.py
