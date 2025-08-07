#  QuerySet API Reference 

---

## 🧠 1. Khi nào QuerySet được thực thi
- QuerySet **Lazy**: không truy vấn DB cho đến khi bạn thực sự dùng nó.
- Các cách khiến QuerySet thực thi:
  - Duyệt vòng lặp (`for` hoặc `async for`)
  - Gọi `list()`, `len()`, `bool()`, `repr()`
  - Dùng `exists()` hoặc `count()` để kiểm tra nhanh

---

## 🔍 2. Các phương thức truy vấn phổ biến
| Phương thức        | Mô tả |
|-------------------|------|
| `filter()`        | Lọc theo điều kiện (AND) |
| `exclude()`       | Loại bỏ theo điều kiện |
| `get()`           | Lấy một đối tượng duy nhất |
| `annotate()`      | Thêm trường tính toán (Count, Sum…) |
| `alias()`         | Tạo biểu thức để tái sử dụng |
| `order_by()`      | Sắp xếp kết quả |
| `reverse()`       | Đảo ngược thứ tự |
| `distinct()`      | Loại bỏ bản ghi trùng lặp |
| `values()`        | Trả về dict thay vì model |
| `values_list()`   | Trả về tuple thay vì model |

---

## 🧮 3. Truy vấn nâng cao
- **`F()`**: So sánh giữa các trường trong cùng một model
  ```python
  Entry.objects.filter(num_comments__gt=F("num_pingbacks"))
  ```
- **`Q()`**: Tạo điều kiện OR, NOT
  ```python
  Entry.objects.filter(Q(headline__startswith="A") | Q(pub_date__year=2023))
  ```

---

## 🔗 4. Truy vấn quan hệ
- **`select_related()`**: Truy vấn theo ForeignKey (JOIN SQL)
- **`prefetch_related()`**: Truy vấn theo ManyToMany hoặc reverse FK (truy vấn riêng, ghép bằng Python)

---

## 🧰 5. Các phương thức đặc biệt
- `none()`: Trả về QuerySet rỗng
- `all()`: Trả về bản sao của QuerySet
- `union()`, `intersection()`, `difference()`: Kết hợp nhiều QuerySet
- `defer()`: Trì hoãn tải một số trường
- `extra()`: Thêm SQL thủ công (không khuyến khích)

---

## 📅 6. Truy vấn theo thời gian
- `dates(field, kind)`: Trả về danh sách ngày (year, month, day…)
- `datetimes(field, kind)`: Trả về datetime theo kiểu (hour, minute…)

---

## 🧪 7. Truy vấn JSONField
- Truy vấn theo key: `data__key=value`
- Dùng `contains`, `has_key`, `isnull`…

---

## 🚀 Gợi ý thực hành nhanh
1. Tạo một model Blog và Entry
2. Dùng `filter()`, `exclude()`, `annotate()` để truy vấn
3. Dùng `select_related()` và `prefetch_related()` để tối ưu
4. Thử `values()` và `values_list()` để lấy dữ liệu nhẹ

---