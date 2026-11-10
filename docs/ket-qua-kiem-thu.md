# Kết quả kiểm thử — 10/11/2026

## Dữ liệu và logic

`node --test tests/system.test.cjs`: **8/8 đạt**, không thất bại.

- Giữ 18 bộ phận, đủ 187 ID cũ ở đúng bộ phận; 217 ID duy nhất.
- Tất cả công việc có metadata, tiêu đề, đầu ra, nguồn và bộ phận hợp lệ.
- Trạng thái hoàn thành cũ và khóa không nhận diện được giữ nguyên; việc mới chưa hoàn thành.
- Dữ liệu localStorage null, mảng, chuỗi, JSON hỏng hoặc bị chặn không làm trang lỗi hay ghi đè dữ liệu cũ.
- Lọc nhiều điều kiện cùng lúc; tìm theo mã và đầu ra.
- CSV escape dấu nháy, chặn công thức với dấu =, +, -, @ kể cả sau ký tự trắng/điều khiển.
- Các quyết định vốn/đầu tư và ngân sách được gắn chờ phê duyệt; việc thêm theo đặc tả có nguồn riêng.
- Danh mục in có tên công ty; nhóm nghiệp vụ kiểm kê tài sản gom được việc từ nhiều bộ phận.
- Đối chiếu có đủ 48 dòng Excel cột B và 1 mục trống cần làm rõ, không trùng ô nguồn; mọi mã tham chiếu tồn tại.

## Trình duyệt Chrome

`tests/browser.cjs`: **đạt**, không có sự kiện lỗi JavaScript.

Đã thao tác thật: mở bộ phận, đánh dấu hoàn thành, tải lại và xác nhận trạng thái; giữ khóa lạ đã lưu; giữ chi tiết mở khi checklist thay đổi; lọc bộ phận kết hợp phê duyệt; tìm kiếm có và không có kết quả; đặt lại và mở tất cả; kiểm tra ID DOM duy nhất.

Tải CSV thật: BOM UTF-8, 12 cột, 217 dòng nhiệm vụ và 1 dòng tiêu đề. Xuất dùng toàn bộ danh mục, lấy tiến độ từ trình duyệt hiện tại.

Kiểm tra viewport 375, 768, 1440 px không tràn ngang tài liệu; đã xem ảnh desktop/mobile. Sidebar mobile cuộn ngang có chủ ý; các badge ưu tiên tự xuống dòng.

## In / PDF

Kiểm tra media print và tạo PDF QA từ Chrome khi bộ lọc màn hình không có kết quả: vẫn có đủ 217 việc, đầy đủ trường chi tiết, ẩn sidebar và bộ lọc.

PDF A4 có 89 trang trong môi trường kiểm thử. Đã đọc toàn bộ text PDF, xác nhận đủ 217 mã, tiêu đề doanh nghiệp và không có text nằm ngoài chiều cao trang. Đã render và xem các trang 1, 2, 44, 89; mỗi nhiệm vụ giữ liền khối, không cắt chữ ở các trang đã xem. Phân trang thực tế có thể khác theo trình duyệt/cấu hình in.

Ảnh, PDF và CSV QA được tạo bằng hồ sơ trình duyệt tạm; trạng thái hoàn thành phục vụ kiểm thử không được ghi vào dữ liệu bàn giao.

## Rà soát độc lập

Đã rà soát mã và phép đối chiếu bằng tác nhân độc lập. Hai vấn đề về mặc định phê duyệt và nguồn bổ sung đã được sửa, có kiểm thử hồi quy. Lần kiểm tra lại không phát hiện thiếu sót trọng yếu trong phạm vi đọc mã.

## Những điểm cần xác nhận nghiệp vụ

- Sheet1!B12: DNA chưa rõ nghĩa; tạo nhiệm vụ làm rõ, chưa coi là NDA.
- Sheet1!A68: mục 10 trống; không tự bổ sung nội dung nguồn.
- Phân công, bổ nhiệm, hạn mức, chính sách và giao dịch tài sản chưa có chứng cứ hiệu lực được giữ ở trạng thái chờ phê duyệt/cần xác minh. Đây là dữ liệu cần đơn vị có thẩm quyền xác nhận.
