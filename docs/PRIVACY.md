# Chính sách quyền riêng tư (Bản nháp Week 1)

Tuân thủ nguyên tắc tối thiểu hóa dữ liệu (NT2 theo SPEC), đây là danh sách các dữ liệu đang được thu thập trong phạm vi Week 1.

## 1. Dữ liệu thực tế được thu thập trong Week 1

Phiên bản Week 1 chỉ ghi nhận những dữ liệu cơ bản sau nhằm xác minh thiết bị có thể kết nối thành công tới máy chủ (chức năng Heartbeat):

| Trường dữ liệu  | Mục đích thu thập (Thực tế Week 1)              |
|-----------------|-------------------------------------------------|
| `device_id`     | Định danh thiết bị để phân biệt các máy của trẻ |
| `timestamp`     | Ghi nhận thời điểm thiết bị kết nối lên hệ thống|
| `status`        | Ghi nhận trạng thái kết nối (VD: online)        |
| `policy_version`| Dấu hiệu nhận biết máy đang áp dụng phiên bản luật nào |

*Lưu ý về thời hạn lưu trữ (Retention)*: Thiết kế hệ thống đặt thời hạn lưu trữ dữ liệu là 90 ngày. Cơ chế tự động xóa dữ liệu quá 90 ngày chưa được triển khai trong Week 1.

## 2. Những dữ liệu KHÔNG BAO GIỜ được thu thập

Xuyên suốt toàn bộ dự án OpenGuard Kids, để tôn trọng quyền riêng tư của trẻ, hệ thống sẽ KHÔNG thu thập:
- Nội dung tin nhắn của trẻ.
- Nội dung email.
- Tài liệu, tệp tin cá nhân.
- Nội dung gõ phím (keystrokes).
- Ảnh chụp màn hình (screenshots).
- Đường dẫn trang web chi tiết (full URL) hay tiêu đề cửa sổ màn hình (window title).

## 3. Các tính năng sẽ hỗ trợ trong các giai đoạn sau (Week 2–4)

Dự án OpenGuard Kids hoàn chỉnh ở các tuần tiếp theo sẽ được bổ sung tính năng theo thiết kế, nhưng vẫn tiếp tục tuân thủ nghiêm ngặt quyền riêng tư:
- Thu thập thêm thông tin về tên ứng dụng (app), tên miền trang web (domain) và thời lượng sử dụng.
- Cung cấp biểu đồ trực quan về thời gian sử dụng máy tính.
- Cung cấp nút "Xin thêm giờ" hoặc khiếu nại "Bị chặn nhầm" để trẻ chủ động gửi yêu cầu đến phụ huynh.
- Cơ chế chặn website/ứng dụng đi kèm với màn hình giải thích rõ ràng lý do chặn và người đặt luật chặn.
- Danh sách ngoại lệ an toàn khẩn cấp để các dịch vụ an toàn cần thiết vẫn có thể được truy cập khi áp dụng chính sách.

---

## 4. Phiên bản dành cho trẻ (Trẻ em cần biết)

Chào em! Ứng dụng OpenGuard Kids được cài đặt trên máy tính để giúp em sử dụng máy tính an toàn, cân bằng thời gian học và chơi. Ứng dụng này là người bạn đồng hành của em, tuyệt đối **không phải phần mềm theo dõi lén lút**. 

Dưới đây là những điều em cần biết về phiên bản hiện tại (Week 1):

1. **Ứng dụng này hiện đang ghi lại những gì?**
   - Trong phiên bản Week 1 hiện tại, OpenGuard Kids chỉ ghi nhận thông tin rất cơ bản để biết máy tính của em đang hoạt động và có thể kết nối tới máy chủ OpenGuard Kids.
   - Hiện tại ứng dụng chưa ghi nhận em đang dùng phần mềm hay trang web nào.

2. **Ứng dụng KHÔNG BAO GIỜ thu thập những gì?**
   - Nội dung tin nhắn của em.
   - Nội dung Email.
   - Tài liệu, bài tập của em.
   - Những nội dung em gõ trên phím.
   - Ảnh chụp màn hình máy tính.
   - Địa chỉ trang web chi tiết (URL) hay tiêu đề cửa sổ em đang xem.

3. **Trong tương lai, ứng dụng sẽ có thêm gì?**
   - Ở các phiên bản sắp tới, ứng dụng sẽ bắt đầu ghi nhận thời gian em dùng các phần mềm và trang web để vẽ thành biểu đồ. **Chính em** cũng sẽ được xem những biểu đồ này giống hệt bố mẹ.
   - Em sẽ có nút **"Xin thêm giờ"** nếu đang làm dở bài tập.
   - Nếu em thấy trang web học tập bị chặn, em có quyền ấn nút báo cho bố mẹ là trang này đang bị chặn nhầm.
   - Khi có trang web bị khóa, ứng dụng sẽ hiện rõ lý do vì sao khóa chứ không im lặng giả vờ "lỗi mạng".
