#  1. Django Models

---

### 🧱 Khái niệm cơ bản về Model
- Mỗi model là một lớp Python kế thừa từ `django.db.models.Model`.
- Mỗi thuộc tính trong lớp là một trường dữ liệu tương ứng với cột trong bảng cơ sở dữ liệu.
- Django tự động tạo API để truy vấn dữ liệu từ model.

---

### ✍️ Cách sử dụng Model
- Khai báo model trong `models.py`.
- Thêm app vào `INSTALLED_APPS` trong `settings.py`.
- Chạy `makemigrations` và `migrate` để tạo bảng dữ liệu.

---

### 🔢 Các loại trường dữ liệu (Fields)
- Ví dụ: `CharField`, `IntegerField`, `DateField`, `ForeignKey`, `ManyToManyField`, `OneToOneField`.
- Mỗi trường có các tùy chọn như:
  - `null`, `blank`: cho phép giá trị rỗng.
  - `choices`: danh sách lựa chọn cố định.
  - `default`, `db_default`: giá trị mặc định.
  - `primary_key`, `unique`: khóa chính và tính duy nhất.

---

### 🔗 Quan hệ giữa các Model
- **Many-to-One**: dùng `ForeignKey`.
- **Many-to-Many**: dùng `ManyToManyField`, có thể thêm model trung gian với `through`.
- **One-to-One**: dùng `OneToOneField`.

---

### 🧠 Kế thừa Model
- **Abstract base class**: dùng để chia sẻ thuộc tính chung, không tạo bảng riêng.
- **Multi-table inheritance**: mỗi lớp con có bảng riêng.
- **Proxy models**: thay đổi hành vi Python mà không thay đổi cấu trúc dữ liệu.

---

### 🛠️ Các phương thức và thuộc tính quan trọng
- `objects`: Manager mặc định để truy vấn dữ liệu.
- `__str__()`: hiển thị chuỗi đại diện cho đối tượng.
- `get_absolute_url()`: trả về URL của đối tượng.
- Có thể override `save()` và `delete()` để tùy chỉnh hành vi.

---

### 📦 Tổ chức nhiều model
- Có thể chia nhỏ `models.py` thành nhiều file trong thư mục `models/` và import vào `__init__.py`.

```python
from .organic import Person
from .synthetic import Robot
```

---



Nguồn: [Link](https://docs.djangoproject.com/en/5.2/topics/db/models/)

# 2. Django Model Fields

---

### 🧩 Các loại Field trong Django
Django cung cấp nhiều loại trường dữ liệu để ánh xạ với các kiểu dữ liệu trong cơ sở dữ liệu:

| Loại Field           | Mô tả ngắn gọn                          |
|----------------------|-----------------------------------------|
| `CharField`          | Chuỗi ngắn, cần `max_length`            |
| `TextField`          | Chuỗi dài                              |
| `IntegerField`       | Số nguyên                              |
| `DecimalField`       | Số thập phân chính xác cao             |
| `BooleanField`       | True/False                             |
| `DateField`, `TimeField`, `DateTimeField` | Ngày, giờ, ngày giờ |
| `EmailField`, `URLField` | Email, URL                          |
| `FileField`, `ImageField` | Tập tin, hình ảnh                  |
| `ForeignKey`, `ManyToManyField`, `OneToOneField` | Quan hệ giữa các model |

---

### ⚙️ Các tùy chọn chung cho Field
- `null`: cho phép lưu giá trị NULL trong DB.
- `blank`: cho phép bỏ trống trong form.
- `default`: giá trị mặc định.
- `choices`: danh sách lựa chọn cố định.
- `unique`: giá trị duy nhất trong bảng.
- `primary_key`: đánh dấu là khóa chính.
- `db_index`: tạo chỉ mục DB.
- `editable`: có hiển thị trong form hay không.
- `help_text`: mô tả hiển thị trong form.
- `validators`: danh sách hàm kiểm tra dữ liệu.

---

### 🧠 Enum và Choices nâng cao
- Có thể dùng `TextChoices`, `IntegerChoices` để định nghĩa lựa chọn rõ ràng và dễ quản lý.
- Ví dụ:

```python
class YearInSchool(models.TextChoices):
    FRESHMAN = "FR", "Freshman"
    SOPHOMORE = "SO", "Sophomore"
```

---

### 🧪 Một số Field đặc biệt
- `JSONField`: lưu dữ liệu dạng JSON.
- `SlugField`: dùng cho URL thân thiện.
- `UUIDField`: lưu UUID thay cho ID tự tăng.
- `GeneratedField`: trường được tính toán tự động từ các trường khác.

---

### 🚀 Gợi ý thực hành nhanh
1. Tạo một model đơn giản với các loại field khác nhau.
2. Thêm `choices`, `default`, `help_text` để hiểu rõ cách hoạt động.
3. Dùng `makemigrations` và `migrate` để tạo bảng.
4. Tạo dữ liệu bằng `python manage.py shell` hoặc admin.

---

# 3. Model Meta options

---

### 🧠 Meta là gì?
- `class Meta:` là lớp nội bộ trong mỗi model để định nghĩa các **tùy chọn siêu dữ liệu** (metadata).
- Không ảnh hưởng đến logic xử lý dữ liệu, nhưng điều chỉnh cách Django tương tác với model và cơ sở dữ liệu.

---

### 🔧 Các tùy chọn Meta phổ biến

| Tùy chọn             | Mô tả ngắn gọn                                                                 |
|----------------------|--------------------------------------------------------------------------------|
| `db_table`           | Tên bảng trong DB. Mặc định là `app_model`.                                   |
| `ordering`           | Sắp xếp mặc định khi truy vấn (VD: `["-created_at"]`).                         |
| `verbose_name`       | Tên hiển thị của model (số ít).                                                |
| `verbose_name_plural`| Tên hiển thị số nhiều.                                                         |
| `unique_together`    | Tổ hợp các trường phải duy nhất.                                              |
| `constraints`        | Ràng buộc như `CheckConstraint`, `UniqueConstraint`.                          |
| `managed`            | Nếu `False`, Django không tạo bảng cho model này.                             |
| `permissions`        | Thêm quyền tùy chỉnh ngoài `add`, `change`, `delete`, `view`.                 |
| `default_permissions`| Tùy chỉnh hoặc tắt các quyền mặc định.                                        |
| `get_latest_by`      | Trường dùng cho `latest()` hoặc `earliest()`.                                 |
| `proxy`              | Nếu `True`, model là proxy (không tạo bảng mới).                              |
| `indexes`            | Tạo chỉ mục DB tùy chỉnh.                                                      |
| `order_with_respect_to` | Sắp xếp theo một trường liên kết (thường là `ForeignKey`).              |

---

### 📌 Một số tùy chọn nâng cao

- `app_label`: Dùng khi model nằm ngoài app trong `INSTALLED_APPS`.
- `db_table_comment`: Ghi chú cho bảng DB, hữu ích khi làm việc trực tiếp với DB.
- `default_related_name`: Tên mặc định cho quan hệ ngược.
- `required_db_vendor`: Chỉ đồng bộ model với DB cụ thể (VD: chỉ PostgreSQL).
- `select_on_save`: Điều chỉnh cách `save()` hoạt động với DB.

---

### 🚀 Ví dụ
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "shop_product"  # Tên bảng tùy chỉnh
        ordering = ["-created_at"]  # Sắp xếp mặc định theo ngày tạo mới nhất
        verbose_name = "Sản phẩm"  # Tên hiển thị trên UI/Docs số ít
        verbose_name_plural = "Các sản phẩm"  # Tên hiển thị trên UI/Docs số nhiều
        get_latest_by = "created_at"  # Dùng cho latest()
        db_table_comment = "Danh sách sản phẩm trong cửa hàng"  # Ghi chú bảng
        constraints = [
            models.UniqueConstraint(fields=["name", "category"], name="unique_product_category")
        ]

```

# 4. Model Class Reference

---

### ⚙️ Các thuộc tính đặc biệt của Model

#### 1. `DoesNotExist`
- Là một **exception** riêng cho từng model.
- Được raise khi không tìm thấy đối tượng với `QuerySet.get()`.
- Giúp bạn bắt lỗi cụ thể cho từng model:
  ```python
  try:
      obj = MyModel.objects.get(id=999)
  except MyModel.DoesNotExist:
      print("Không tìm thấy đối tượng!")
  ```

#### 2. `MultipleObjectsReturned`
- Exception này được raise khi `get()` trả về nhiều hơn một đối tượng.
- Cũng là thuộc tính riêng của từng model:
  ```python
  try:
      obj = MyModel.objects.get(name="Trung")
  except MyModel.MultipleObjectsReturned:
      print("Có nhiều đối tượng trùng tên!")
  ```

#### 3. `objects`
- Là **Manager mặc định** của model, dùng để truy vấn dữ liệu.
- Nếu bạn không khai báo, Django sẽ tự tạo `objects = models.Manager()`.
- Bạn hoàn toàn có thể thay đổi tên của `Manager` mặc định từ `objects` sang một tên khác để code của bạn rõ ràng hơn. Điều này đặc biệt hữu ích khi bạn có nhiều `Manager` tùy chỉnh.

**Ví dụ:**
Hãy xem xét lại ví dụ trong tài liệu.

```python
from django.db import models

class Person(models.Model):
    # Thay vì dùng tên mặc định 'objects', ta đặt tên là 'people'
    people = models.Manager()

    # Các trường của model
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

Sau khi thay đổi, bạn sẽ **không thể** sử dụng `Person.objects.all()`. Thay vào đó, bạn phải sử dụng tên mới:


- Bạn cũng có thể tạo các `Manager` tùy chỉnh để thêm các phương thức truy vấn riêng biệt, giúp code gọn gàng và dễ tái sử dụng hơn.

**Ví dụ:**
Giả sử bạn muốn có một phương thức để chỉ lấy các sản phẩm đang có sẵn (còn hàng).

```python
from django.db import models

class AvailableProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    # Manager mặc định
    objects = models.Manager()

    # Manager tùy chỉnh
    available_products = AvailableProductManager()
```

Bây giờ, bạn có thể thực hiện các truy vấn sau:

  * Để lấy **tất cả** sản phẩm:
    ```python
    all_products = Product.objects.all()
    ```
  * Để lấy **chỉ các** sản phẩm còn hàng:
    ```python
    only_available = Product.available_products.all()
    ```

Như vậy, `objects` là tên mặc định nhưng có thể được tùy chỉnh để làm cho mã của bạn trở nên rõ ràng và linh hoạt hơn.

----