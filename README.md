# Tạo 1 app trong Django
Tài liệu Django hướng dẫn: [Link](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)

Để tạo một app mới trong dự án Django, bạn sẽ sử dụng lệnh `startapp` của `manage.py`.

```bash
python manage.py startapp <name> [đường_dẫn_tùy_chọn]
```
Ví dụ:
```bash
python manage.py startapp polls app/polls
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
    # 'app.polls'

    # Các ứng dụng của bạn sẽ được thêm vào đây
]
```

Lưu ý: Cấu hình đặt tên cấu hình trong file app của apps.py trong application

# Setup database
Tài liệu hướng dẫn setup kêt nối tới database: [Link](https://docs.djangoproject.com/en/5.2/topics/install/#database-installation)

Nếu không biết chọn thư viện python nào để kết nối tới database như MSSQL, MySQL, MariaDB, Oracle, PostgreSQL,... thì đây là tài liệu: [Link](https://docs.djangoproject.com/en/5.2/topics/install/#database-installation)

Vì Project này chọn Mysql làm DB thì chọn thư viện mysqlclient. Câu hỏi đặt ra là có nhiều thư viện tại sao chọn thư viện mysqlclient? Muốn biết được câu trả lời thì đọc ở đây [Link](https://docs.djangoproject.com/en/5.2/ref/databases/#mysql-notes)
    
```bash
uv add mysqlclient
```

Vì Project này code và chạy ở Việt Nam, nên cần chỉnh múi giờ thành ở **settings.py**

```python
TIME_ZONE = "Asia/Ho_Chi_Minh"
```

Theo mặc định **INSTALLED_APPS** trong **settings.py** gồm có:

```python
INSTALLED_APPS = [
    'django.contrib.admin', #Kích hoạt trang admin siêu tiện lợi của Django để quản lý dữ liệu trực tiếp qua giao diện web
    'django.contrib.auth', #Xử lý xác thực người dùng (login, logout, quyền truy cập, nhóm người dùng)
    'django.contrib.contenttypes', #Cho phép app tương tác linh hoạt với các model khác nhau, kể cả khi không biết chính xác kiểu
    'django.contrib.sessions', #Quản lý session
    'django.contrib.messages', #Gửi các thông báo (message) tạm thời cho người dùng, ví dụ: “Đăng nhập thành công!”
    'django.contrib.staticfiles', #Hỗ trợ xử lý file tĩnh như CSS, JavaScript, hình ảnh
]
```

Cấu hình kết nối MySQL trong **setting.py** như sau [link](https://docs.djangoproject.com/en/5.2/ref/databases/):

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "db_name",
        "USER": "your_user_name",
        "PASSWORD": "your_password",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```

Khi đã có sẵn table DB, muốn đỡ mất công tạo models bằng code tay thì dùng câu lệnh sau:

```bash
python manage.py inspectdb table1 table2 > your_app_name/models.py
```


