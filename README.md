# OpenGuard Kids

Công cụ hỗ trợ quản lý việc sử dụng máy tính của trẻ em.
Đây là phiên bản thử nghiệm (Week 1) tập trung vào chức năng gửi Heartbeat tối thiểu và Dashboard đăng nhập cơ bản.

## Môi trường

- Khuyên dùng: Windows 11
- Python: 3.14+ (Sử dụng `venv`)

## Cấu trúc thư mục hiện tại

- `agent/`: Chứa mã nguồn cho Windows Agent (hiện tại là script Python gửi heartbeat).
- `server/`: Chứa mã nguồn cho FastAPI Server và giao diện Dashboard.
- `docs/`: Chứa tài liệu thiết kế và kiến trúc.

## Hướng dẫn chạy (Localhost)

Đảm bảo bạn đang ở thư mục gốc và đã kích hoạt môi trường ảo `.venv`:

```powershell
.venv\Scripts\activate
```

### 1. Chạy Server
Server cung cấp API cho Agent và giao diện Web cho phụ huynh.
```powershell
$env:PYTHONPATH="."; uvicorn server.main:app --host 127.0.0.1 --port 8000
```

### 2. Truy cập Dashboard
- Mở trình duyệt: http://127.0.0.1:8000/login
- **Tài khoản Demo**: `phuhuong` / `Demo@2026`

### 3. Chạy Agent
Mở một terminal mới (nhớ activate venv), chạy:
```powershell
python agent/main.py
```
Agent sẽ gửi heartbeat ngay lập tức và lặp lại mỗi 60 giây. Mở Dashboard để xem trạng thái `Last Seen` được cập nhật.
