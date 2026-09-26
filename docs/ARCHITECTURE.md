# Kiến trúc hệ thống (Week 1)

## Sơ đồ tổng thể (Mức độ Proof of Concept)

```text
MÁY CỦA TRẺ (Agent)                         MÁY CHỦ (Server)
+-------------------+                       +--------------------------+
| agent/main.py     |    HTTP POST          | server/main.py (FastAPI) |
| Python script loop|---------------------->| Giao diện Web (Jinja2)   |
| (60s interval)    |    /heartbeat         | CSDL: SQLite             |
+-------------------+                       +--------------------------+
```

## Các thành phần
1. **Agent**: Một đoạn mã Python sử dụng thư viện `httpx` để định kỳ 60s gửi thông báo trạng thái hoạt động ("nhịp tim") lên máy chủ.
2. **Server**: Xây dựng bằng FastAPI, tiếp nhận nhịp tim và lưu vào cơ sở dữ liệu.
3. **Database**: Sử dụng SQLite (qua SQLAlchemy ORM) để thiết lập nhanh, không cần cấu hình database engine ngoài.
4. **Dashboard**: Ứng dụng Server-side Rendering (HTML/Jinja2 trả trực tiếp từ FastAPI) phục vụ mục đích đăng nhập và kiểm tra dữ liệu ở mức tối thiểu.

## Các quyết định thiết kế cho Week 1
Để giữ tính tinh gọn và đáp ứng yêu cầu "tối thiểu hóa", các thành phần sau CỐ Ý bị bỏ qua trong Week 1:
- Không sử dụng Windows Service (Agent chỉ chạy script).
- Không có JWT/Bcrypt cho xác thực (dùng Plaintext và Cookie giả lập để test luồng login).
- Không dùng Alembic cho migration (Dùng `Base.metadata.create_all`).
- Không có PostgreSQL/Redis.
