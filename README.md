# Tạo 1 app trong Django
Để tạo một app mới trong dự án Django, bạn sẽ sử dụng lệnh `startapp` của `manage.py`.

```bash
python manage.py startapp <name> [đường_dẫn_tùy_chọn]
```
Đăng kí app với project
Sau khi bạn đã tạo ứng dụng, Django cần biết về sự tồn tại của nó. Việc này được thực hiện bằng cách "đăng ký" ứng dụng với dự án của bạn.

Mở file settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Các ứng dụng của bạn sẽ được thêm vào đây
]
```

Lưu ý: Cấu hình đặt tên cấu hình trong file app của apps.py trong application