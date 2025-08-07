# 1. Query trong Django

---

### 🏗️ 1. Tạo và lưu đối tượng
- **Tạo mới**: Dùng `Model()` rồi `.save()` hoặc `Model.objects.create()`.
  ```python
  b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
  b.save()
  ```
- **Cập nhật**: Gán giá trị mới rồi gọi `.save()`.

---

### 🔍 2. Truy vấn dữ liệu với QuerySet
- **Truy xuất tất cả**: `Model.objects.all()`
- **Lọc dữ liệu**: `filter()`, `exclude()`, `get()`
  ```python
  Entry.objects.filter(pub_date__year=2006)
  Entry.objects.get(pk=1)
  ```
- **Chaining**: Có thể nối nhiều filter/exclude để tạo truy vấn phức tạp.

---

### 🧠 3. QuerySet with "Lazy"
- Không truy vấn DB cho đến khi bạn **thực sự dùng** dữ liệu (in, vòng lặp, list…).
- Giúp tối ưu hiệu suất, nhưng cần cẩn thận khi dùng lại để tránh truy vấn lặp.

---

### 🧮 4. Field Lookups (truy vấn theo điều kiện)
- Dùng cú pháp `field__lookup=value`, ví dụ:
- `exact`, `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `gt`, `gte`, `lt`, `lte`, `in`, `isnull`, `range`, `regex`, `iregex`, `date`, `year`, `iso_year`, `month`, `day`, `week`, `week_day`, `quarter`, `time`, `hour`, `minute`, `second`
  ```python
  Entry.objects.filter(headline__icontains="Lennon")
  ```

---

### 🔗 5. Truy vấn qua quan hệ
- Dùng `__` để truy vấn qua ForeignKey hoặc ManyToMany:
  ```python
  Entry.objects.filter(blog__name="Beatles Blog")
  Blog.objects.filter(entry__headline__contains="Lennon")
  ```

---

### 🧮 6. So sánh giữa các trường với `F()`
- Dùng `F()` để so sánh giữa các field trong cùng một model:
- Ví dụ: Có một model Product có hai trường current_stock (số lượng tồn kho) và reorder_threshold (ngưỡng cần đặt hàng lại). Muốn tìm tất cả các sản phẩm có số lượng tồn kho thấp hơn ngưỡng đặt hàng lại.
  ```python
  products_to_reorder = Product.objects.filter(current_stock__lt=F('reorder_threshold'))
  ```

---

### 🧠 7. Truy vấn phức tạp với `Q()`
- Dùng `Q()` để tạo điều kiện OR, NOT, AND:

| Toán tử | Ý nghĩa |
| :--- | :--- |
| `&` | AND |
| `\|` | OR |
| `~` | NOT |

  
  ```python
  # Tìm các bài viết có tiêu đề chứa 'Django' VÀ KHÔNG phải của tác giả 'John'
posts = Post.objects.filter(
    Q(title__icontains='Django') & ~Q(author_name='John')
)

# Lấy các bài viết đã được xuất bản (filter thông thường)
# VÀ (tiêu đề chứa 'python' HOẶC tác giả là 'Jane')
posts = Post.objects.filter(is_published=True).filter(
    Q(title__icontains='python') | Q(author_name='Jane')
)
  ```

---

### 🧹 8. Xóa và cập nhật hàng loạt
- **Xóa**: `Model.objects.filter(...).delete()`
- **Cập nhật**: `Model.objects.filter(...).update(field=value)`
  ```python
  Entry.objects.update(number_of_pingbacks=F("number_of_pingbacks") + 1)
  ```

---

### 🧬 9. Truy vấn JSONField
- Dùng `data__key=value`, `contains`, `has_key`, `isnull`, v.v.
  ```python
  Dog.objects.filter(data__owner__name="Bob")
  ```

---

### ⚡ 10. Truy vấn bất đồng bộ (async)
- Dùng `aget()`, `afirst()`, `adelete()` trong môi trường async.
  ```python
  user = await User.objects.filter(username="hong").afirst()
  ```

---

