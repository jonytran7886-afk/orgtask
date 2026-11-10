# Kế hoạch nâng cấp Organic Việt Nam — 10/11/2026

Nguồn yêu cầu: bản đặc tả người dùng cung cấp trong phiên làm việc.

1. Đọc HTML gốc và Sheet1 của Excel vận hành; giữ nguyên 18 bộ phận và 187 ID hiện hữu.
2. Lập đối chiếu theo địa chỉ ô; chỉ lưu nội dung đã loại tên cá nhân. Nội dung bổ nhiệm, phân quyền, góp vốn phải ghi rõ chưa được phê duyệt/xác minh. Ô B12 ghi “DNA” cần làm rõ; mục 10 trống không tự thêm nội dung.
3. Mở rộng việc đã có bằng mô tả, đầu ra và phối hợp; chỉ thêm nhiệm vụ có đầu ra độc lập. Phân biệt nguồn Excel, HTML và phần chuẩn hóa theo đặc tả.
4. Cập nhật trực tiếp index.html, giữ sidebar/dashboard và màu xanh. Bổ sung bộ lọc, chi tiết, chỉ số động; giữ khóa localStorage ovn-company-tasks-v1, không cần migration.
5. Kiểm thử ID, nguồn, hoàn thành cũ, nhiều bộ lọc đồng thời, CSV chống công thức, lỗi storage, in toàn bộ chi tiết và responsive.
6. Bàn giao HTML, báo cáo và bảng đối chiếu theo từng dòng Excel; xác minh trước khi commit/push.

## Các quyết định triển khai
- Tiếp tục dùng một file HTML chạy độc lập, không thêm backend hay thư viện vào sản phẩm.
- Chức danh gợi ý không đồng nghĩa phân công đã duyệt: mặc định “Chưa phân công”; chức danh đề xuất nằm trong ghi chú.
- Giữ nguyên trường name để tương thích, bổ sung title và các trường chuẩn hóa.
- Checkbox chỉ xác nhận tiến độ thực hiện, không thay đổi trạng thái phê duyệt chính sách.
- In danh mục đầy đủ, độc lập với bộ lọc đang xem; CSV xuất toàn bộ, trạng thái lấy từ trình duyệt hiện tại.
- Không nhập nguyên bản có tên cá nhân hoặc hạn mức chưa duyệt vào sản phẩm/bảng đối chiếu. Chỉ lưu tóm tắt đã khử định danh và tham chiếu ô nguồn.
