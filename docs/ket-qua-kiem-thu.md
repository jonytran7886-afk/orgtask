# Kết quả kiểm thử — 10/11/2026

## Dữ liệu và logic

`node --test tests/system.test.cjs`: **14/14 đạt**, không thất bại.

- Giữ 18 bộ phận, đủ 187 ID cũ ở đúng bộ phận; 240 ID duy nhất.
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

Tải CSV thật: BOM UTF-8, 12 cột, 240 dòng nhiệm vụ và 1 dòng tiêu đề. Xuất dùng toàn bộ danh mục, lấy tiến độ từ trình duyệt hiện tại.

Kiểm tra viewport 375, 768, 1440 px không tràn ngang tài liệu; đã xem ảnh desktop/mobile. Sidebar mobile cuộn ngang có chủ ý; các badge ưu tiên tự xuống dòng.

## In / PDF

Kiểm tra media print và tạo PDF QA từ Chrome khi bộ lọc màn hình không có kết quả: vẫn có đủ 240 việc, đầy đủ trường chi tiết, ẩn sidebar và bộ lọc.

PDF A4 có 102 trang trong môi trường kiểm thử. Đã đọc toàn bộ text PDF, xác nhận đủ 240 mã, tiêu đề doanh nghiệp và không có text nằm ngoài chiều cao trang. Đã render các trang 1, 2, 51, 102. CSS và runtime giữ nguyên so với bản đã xem trực quan trước đó; nhiệm vụ tiếp tục dùng quy tắc giữ liền khối khi in. Phân trang thực tế có thể khác theo trình duyệt/cấu hình in.

Ảnh, PDF và CSV QA được tạo bằng hồ sơ trình duyệt tạm; trạng thái hoàn thành phục vụ kiểm thử không được ghi vào dữ liệu bàn giao.

## Rà soát độc lập

Đã rà soát mã và phép đối chiếu bằng tác nhân độc lập. Hai vấn đề về mặc định phê duyệt và nguồn bổ sung đã được sửa, có kiểm thử hồi quy. Lần kiểm tra lại không phát hiện thiếu sót trọng yếu trong phạm vi đọc mã.

## Những điểm cần xác nhận nghiệp vụ

- Sheet1!B12: DNA chưa rõ nghĩa; tạo nhiệm vụ làm rõ, chưa coi là NDA.
- Sheet1!A68: mục 10 trống; không tự bổ sung nội dung nguồn.
- Phân công, bổ nhiệm, hạn mức, chính sách và giao dịch tài sản chưa có chứng cứ hiệu lực được giữ ở trạng thái chờ phê duyệt/cần xác minh. Đây là dữ liệu cần đơn vị có thẩm quyền xác nhận.

## Hồi quy tách công việc bộ phận 06

- 06-05 và 06-08 giữ ID, lần lượt phụ trách kho và thanh toán lương. Thêm 06-14 quản lý công nợ, 06-15 thanh toán nhà cung cấp; bộ phận có 15 việc, dashboard tổng 240.
- Đối chiếu dữ liệu với commit 2f775c3: tất cả bộ phận khác giữ nguyên; CSS, markup giao diện và runtime không thay đổi.
- Kiểm thử khởi tạo với 06-05/06-08 đã hoàn thành: checklist cũ giữ nguyên; 06-14/06-15 chưa hoàn thành. Đánh dấu việc mới giữ các khóa đã lưu trước đó.
- Kiểm thử trình duyệt: lọc bộ phận 06 có 15 việc; tìm “tuổi nợ” trả về đúng 06-14; tích công nợ không tự tích thanh toán nhà cung cấp.

## Bổ sung HCNS từ ảnh 16 mục

- Đối chiếu đủ 16 mục, không bỏ mục nào: thêm 04-17 đến 04-28; mở rộng 04-05 (bảo hiểm) và 04-08 (văn thư, con dấu, tài sản). HCNS hiện có 28 việc.
- 04-17 tính lương và chuyển hồ sơ cho 06-08 thanh toán; 04-18 chuẩn bị/đối soát dữ liệu TNCN, TNDN và phối hợp Kế toán chủ trì kê khai tại 06-07. Không tạo thêm nhiệm vụ tại các bộ phận khác.
- Kiểm thử giữ checklist 04-05, 04-08, 06-08 đã hoàn thành; toàn bộ 12 việc HCNS mới chưa hoàn thành. Mọi ID cũ tiếp tục tồn tại.
- Trên Chrome: lọc HCNS có 28 việc, tìm BHYT trả đúng nhiệm vụ 04-05, tìm thăng tiến có 04-22; tích 04-17 không tự tích 04-18.
- Xuất CSV thực tế đủ 240 nhiệm vụ, 12 cột và BOM. Bản in đủ 240 mã công việc; không có text ngoài chiều cao trang. CSS, runtime và bố cục được giữ nguyên.
- Nguồn ảnh ghi riêng, không tự xác lập mức tiền, ngày hoàn thành hoặc phê duyệt chính sách/bổ nhiệm.

## Bổ sung Pháp chế – Tuân thủ từ ảnh 6 mục

- Thêm đúng 03-18 đến 03-23, giữ nguyên tên nhiệm vụ và mức ưu tiên trong ảnh: P0, P0, P1, P1, P1, P1. Bộ phận 03 có 23 việc.
- So sánh với bản ngay trước bổ sung: 17 nhiệm vụ Pháp chế cũ và toàn bộ bộ phận khác giữ nguyên từng trường; CSS, markup và runtime không thay đổi.
- Kiểm thử khởi tạo với checklist 03-01/03-17/07-01 đã hoàn thành: trạng thái giữ nguyên, sáu nhiệm vụ mới chưa hoàn thành.
- Trên Chrome: lọc Pháp chế có 23 việc, tìm 03-18 thấy P0; tìm 03-23 thấy P1; tích một việc mới không làm việc mới khác hoàn thành. Không phát sinh lỗi JavaScript trong các thao tác kiểm thử.
- CSV tải thực tế đủ 240 nhiệm vụ/12 cột, sáu mã mới duy nhất và đúng ưu tiên. PDF A4 QA có 102 trang, đủ toàn bộ mã công việc, không có text ngoài chiều cao trang.
- Nguồn ảnh được ghi riêng. Phân biệt quản trị rủi ro pháp lý và đánh giá tuân thủ pháp luật với kiểm soát độc lập của KSNB; việc chuẩn bị/phối hợp thanh tra không được diễn giải thành thẩm quyền thanh tra nhà nước.

## Bổ sung Kế toán – Thuế từ ảnh sau loại trùng

- Thêm đúng 06-16, 06-17, 06-18 với ưu tiên P0/P1/P1; bộ phận 06 có 18 việc, toàn danh mục 240 việc.
- So với bản ngay trước thay đổi: giữ nguyên 15 việc kế toán cũ và toàn bộ dữ liệu bộ phận khác; không thay CSS, markup hay runtime.
- Kiểm thử giữ checklist 06-04/06-06/06-07/06-15 đã hoàn thành; ba việc mới mặc định chưa hoàn thành.
- Đầu ra mới phân biệt với 06-06 (tập hợp chi phí), 06-07 (kê khai định kỳ), 06-04 (hạch toán) và 06-10 (báo cáo); nguồn ảnh riêng, không xác nhận đã kiểm toán/quyết toán hoặc tự phê duyệt.
- Chrome: lọc bộ phận 06 có 18 việc; tìm 06-16 thấy P0, 06-18 thấy P1; checklist mới độc lập. Không có lỗi JavaScript trong bộ thao tác kiểm thử.
- CSV tải thực tế có 240 nhiệm vụ, 12 cột và BOM; ba ID mới duy nhất, đúng ưu tiên. PDF QA A4 có 102 trang, đủ toàn bộ mã nhiệm vụ, không có text ngoài chiều cao trang.
