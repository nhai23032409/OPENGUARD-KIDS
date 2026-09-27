# OpenGuard Kids — Project Status

## 1. Project overview

OpenGuard Kids là ứng dụng hỗ trợ quản lý việc sử dụng máy tính của trẻ em. Mục tiêu của dự án là thiết lập một công cụ đồng hành an toàn, giúp trẻ cân bằng thời gian học và chơi trên máy tính Windows. Triết lý thiết kế xuyên suốt của dự án (theo SPEC) là sự **minh bạch và bảo vệ quyền riêng tư**: đây không phải là phần mềm gián điệp, mọi dữ liệu thu thập đều tuân theo nguyên tắc tối thiểu và trẻ em có quyền được biết ứng dụng đang hoạt động như thế nào.

## 2. Current status

- **Week 1: COMPLETED**
- **Week 2: NOT STARTED**
- **Week 3: NOT STARTED**
- **Week 4: NOT STARTED**

Giai đoạn Week 1 đã hoàn thành phạm vi skeleton end-to-end theo SPEC. Máy tính của trẻ (Agent) có thể giao tiếp thành công qua mạng tới Máy chủ (Server), dữ liệu được lưu trữ trong CSDL SQLite và hiển thị trên Dashboard. 

## 3. What is currently working

Dưới đây là danh sách chính xác các thành phần đã được implementation chạy thực tế:

* [x] FastAPI server chạy local
* [x] SQLite database tự động khởi tạo bảng
* [x] Parent demo login (demo auth flow)
* [x] Dashboard bằng HTML/Jinja2
* [x] Agent gửi heartbeat bằng `httpx`
* [x] Heartbeat tự động gửi mỗi 60 giây
* [x] Server nhận heartbeat qua API `/heartbeat`
* [x] Heartbeat được lưu vào bảng SQLite
* [x] Dashboard hiển thị device ID, Name, Status và Last Seen (UTC)

## 4. Current architecture

Sơ đồ luồng dữ liệu hiện tại của Week 1:

```text
       Agent (Máy của trẻ)
               |
               | (HTTP POST /heartbeat)
               v
     FastAPI Server (Máy chủ)
               |
               +---> (Lưu trữ) ---> SQLite Database
               |
               v (HTTP GET /dashboard)
    Dashboard (Trình duyệt phụ huynh)
```

**Vai trò từng thành phần:**
- **Agent**: Một script Python chạy trong môi trường thử nghiệm Week 1, định kỳ gửi heartbeat cho Server.
- **FastAPI Server**: Máy chủ trung tâm tiếp nhận yêu cầu từ Agent và từ Trình duyệt phụ huynh.
- **SQLite Database**: Nơi lưu trữ thông tin tài khoản phụ huynh, thiết bị của trẻ và các lần gửi Heartbeat.
- **Dashboard**: Giao diện Web được Server trực tiếp render (Jinja2) giúp phụ huynh theo dõi trạng thái online của thiết bị.

## 5. Repository structure

```text
openguard-kids/
├── agent/
│   ├── main.py
│   └── requirements.txt
├── server/
│   ├── templates/
│   │   ├── login.html
│   │   └── dashboard.html
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── requirements.txt
├── docs/
│   ├── SPEC.md
│   ├── ARCHITECTURE.md
│   ├── PRIVACY.md
│   └── STATUS.md
├── .gitignore
└── README.md
```

*(Lưu ý: Bạn sẽ thấy thư mục `.venv` và tệp `openguard.db` được tạo ra sau khi setup, nhưng chúng không nằm trong source control).*

## 6. Environment

Môi trường thực tế dự án đang sử dụng:

* **OS**: Windows 10/11
* **Python**: 3.14.4
* **Virtual environment**: `.venv` (được tạo ở thư mục gốc)
* **Packages cho Server**: `fastapi`, `uvicorn`, `sqlalchemy`, `jinja2`, `python-multipart`
* **Packages cho Agent**: `httpx`
* **Database Engine**: `sqlite3` (tích hợp sẵn trong Python)

## 7. First-time setup after cloning

Dành cho developer mới join dự án. Bạn chỉ cần thực hiện 1 lần duy nhất sau khi clone source code trên Windows:

### Clone repository
```powershell
git clone <REPOSITORY_URL>
cd openguard-kids
```

### Create virtual environment
Đảm bảo bạn đang sử dụng phiên bản Python tương thích (khuyên dùng Python hiện hành của dự án).
```powershell
python -m venv .venv
```

### Install server dependencies
```powershell
.venv\Scripts\activate
pip install -r server\requirements.txt
```

### Install agent dependencies
```powershell
pip install -r agent\requirements.txt
```

## 8. How to run Week 1

Để chạy toàn bộ hệ thống Week 1, bạn cần mở **2 cửa sổ PowerShell** độc lập.

### Terminal 1 — Server
Khởi động máy chủ và giao diện Dashboard:
```powershell
.venv\Scripts\activate
$env:PYTHONPATH="."
uvicorn server.main:app --host 127.0.0.1 --port 8000
```
*(Server sẽ in ra các dòng seed data và chờ request).*

### Terminal 2 — Agent
Khởi động giả lập máy của trẻ:
```powershell
.venv\Scripts\activate
python agent\main.py
```
*(Expected output của Agent: `[2026-xx-xx ...] Heartbeat sent: 200 - {'status': 'ok', 'policy_version': 1, 'commands': []}` sau đó tự động lặp lại mỗi 60 giây).*

## 9. How to verify Week 1

Sau khi đã bật Server và Agent, hãy thực hiện bài kiểm tra sau để xác nhận hệ thống chạy đúng:

1. Mở `http://127.0.0.1:8000/docs` bằng trình duyệt.
   - **Expected**: Thấy giao diện Swagger UI màu xanh (HTTP 200) liệt kê các API.
2. Mở `http://127.0.0.1:8000/login`.
   - **Expected**: Thấy giao diện đăng nhập (login page).
3. Login bằng demo account (xem mục 10).
   - **Expected**: Trình duyệt chuyển hướng thành công.
4. Mở Dashboard (tự động chuyển hướng hoặc vào `/dashboard`).
   - **Expected**: Thấy thiết bị `demo-device-001` đang hiển thị.
5. Kiểm tra Terminal Agent.
   - **Expected**: Agent vẫn đang in ra các dòng `Heartbeat sent: 200`.
6. Chờ khoảng 60 giây để đảm bảo Agent tự động gửi Heartbeat lần 2.
7. Xem cửa sổ Terminal Server.
   - **Expected**: Thấy dòng log `POST /heartbeat HTTP/1.1" 200 OK`.
8. Trở lại trình duyệt và F5 (Refresh) trang Dashboard.
9. **Verify**: Cột `Last Seen (UTC)` của thiết bị sẽ cập nhật mốc thời gian mới nhất khớp với lúc nhận Heartbeat.

## 10. Demo account

Dự án hiện đang sử dụng bộ credential cứng sau (được tạo tự động trong SQLite khi khởi động Server lần đầu tiên):

- **Username**: `phuhuong`
- **Password**: `Demo@2026`
- **Device ID**: `demo-device-001`

*(Tuyệt đối không tự sửa hay tạo credentials mới ở Week 1)*.

## 11. Important implementation limitations

Vì đây là scope giới hạn của Week 1, các tính năng sau **CỐ Ý** chưa được thực hiện. Vui lòng không báo lỗi (bug) cho những phần này:

* Agent chỉ đang chạy dưới dạng một Python script lặp vô hạn ở Console, chưa đóng gói thành hệ thống Windows Service.
* Authentication (Đăng nhập) hiện tại chỉ dùng cơ chế plaintext cookie đơn giản nhất để demo luồng chuyển trang, chưa mã hóa password và chưa có JWT.
* Chưa có quy trình ghép đôi thiết bị (Enrollment) qua mã 8 ký tự.
* Chưa có các chức năng áp đặt Quota (giới hạn thời gian), Grace period.
* Chưa có Weekly Schedule (khung giờ cho phép sử dụng trong tuần).
* Chưa có khả năng Lock máy tính Windows.
* Chưa có hệ thống DNS Proxy, chưa có Block Application.
* Hệ thống Report và Audit Log chưa triển khai đầy đủ.
* Toàn bộ hệ thống chưa trải qua quá trình Security hardening (chưa dùng HTTPS, chưa mã hóa AES...).

## 12. Week 2 starting point

Bắt đầu từ Week 2, chúng ta sẽ bắt tay vào tính năng **F1** và **Lõi F4**. Dựa trên SPEC, mục tiêu Week 2 bao gồm:

* Daily quota (Hạn mức ngày).
* Weekly schedule 7×48 (Ma trận quản lý lịch tuần với độ phân giải 30 phút).
* Real usage counting (Đếm thời gian sử dụng máy thực tế).
* Cảnh báo thời gian (Warnings) trước 10, 5, 1 phút.
* Grace period (Thời gian ân hạn 60 giây).
* Clock tamper resistance (Chống chỉnh đồng hồ hệ thống).
* Machine lock (Cơ chế khóa màn hình).
* Remote policy propagation (Đẩy cấu hình luật từ server xuống thiết bị).
* Policy version & Policy integrity (Kiểm soát phiên bản luật và tính toàn vẹn).
* Audit log (Nhật ký kiểm toán sự thay đổi).

## 13. Reading order for new developers

Để nhanh chóng nắm bắt dự án, một thành viên mới **BẮT BUỘC** phải đọc tài liệu theo thứ tự sau:

1. `docs/STATUS.md` (Tài liệu bạn đang đọc - Nắm rõ hiện trạng và cách cài đặt).
2. `README.md` (Thông tin project và khởi chạy cơ bản).
3. `docs/SPEC.md` (Source of truth của toàn bộ dự án).
4. `docs/ARCHITECTURE.md` (Mô hình tổng quan đầu cuối hiện tại).
5. `docs/PRIVACY.md` (Nguyên tắc bảo vệ dữ liệu).
6. `agent/main.py` (Mã nguồn giả lập Windows Agent).
7. `server/main.py` (Mã nguồn hệ thống API, Routes và Jinja).
8. Các file model, schema, database, templates đi kèm trong thư mục `server/`.

## 14. Development rule

* Mọi tính năng mới đều phải đối chiếu với `docs/SPEC.md` làm tiêu chuẩn (Source of Truth).
* Tuân thủ triệt để nguyên tắc Tối giản hóa. Đang làm Week 2 thì tuyệt đối không tự tiện cài đặt các tính năng thuộc Week 3/4.
* Không được sửa mã nguồn nếu chưa thực sự hiểu luồng chạy hiện tại. 
* Sau khi clone source code, mọi lập trình viên **phải chạy thành công bài test Week 1** (Mục 9 trong tài liệu này) trước khi viết thêm bất kỳ dòng code nào mới!
