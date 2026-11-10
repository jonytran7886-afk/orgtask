# Báo cáo nâng cấp Organic Việt Nam

## Nguồn và phạm vi

Đã đọc HTML gốc (bản Downloads trùng bản repo) và toàn bộ ô có nội dung trong Sheet1 của Excel vận hành. Có 48 dòng nhiệm vụ tại cột B, 9 nhóm có nội dung, mục 10 trống. Bảng đối chiếu lưu nội dung đã khử định danh và tham chiếu ô; không nhập tên cá nhân.

## Số liệu

- Trước: 18 bộ phận, 187 công việc.
- Sau: 18 bộ phận, 240 công việc.
- Bổ sung thực sự: 53 công việc; 23 từ Excel, 12 từ ảnh HCNS, 6 từ ảnh Pháp chế, 3 từ ảnh Kế toán, còn lại theo đặc tả/yêu cầu nâng cấp.
- Mở rộng: 32 công việc cũ; giữ nguyên ID; tên 06-04 cập nhật theo ảnh chỉnh sửa, 06-05/06-08 cập nhật theo yêu cầu tách việc, 04-05/04-08 mở rộng theo ảnh HCNS.
- 0 dòng Excel được bỏ qua vì đã đầy đủ: các dòng có tương đương đều cần thêm đầu ra, phạm vi hoặc trạng thái xác minh.
- 28 dòng Excel có liên hệ công việc cũ được mở rộng; không tạo thêm bản sao cho cùng đầu ra.
- 2 hạng mục cần làm rõ: B12 (DNA), A68 (mục 10 trống).
- Các nội dung pháp lý, tài sản, phân quyền và bổ nhiệm còn phải xác minh/phê duyệt được ghi trong từng nhiệm vụ, độc lập với tiến độ checklist.

## Các quyết định xử lý nguồn

- Không nhập hạn mức trong Excel như quy định chính thức. Nhiệm vụ 05-07 ở trạng thái Chờ phê duyệt, tham chiếu B18.
- Không nhập tên cá nhân ở B16 và B26; thay bằng nội dung công việc theo chức danh/chủ sở hữu cần xác minh.
- B30 không đủ căn cứ ghi vốn chủ sở hữu: tách rà soát phương án pháp lý và ghi nhận theo bản chất giao dịch.
- B22 mô tả hỗ trợ khởi động, không trao quyền điều hành thường xuyên cho HĐQT.
- Domain/tên miền ở B52 hợp nhất một khái niệm; B57 chuẩn hóa lỗi chữ theo ngữ cảnh, ghi rõ trong đối chiếu.
- Tất cả chức danh chịu trách nhiệm mặc định Chưa phân công. Chức danh đề xuất trong ghi chú không phải quyết định bổ nhiệm.

## Giao diện và chức năng

- Giữ bố cục sidebar/dashboard, nhận diện xanh và 18 nhóm. Bổ sung chỉ số chưa hoàn thành, chưa phân công, chờ phê duyệt, cơ cấu P0/P1/P2.
- Bộ lọc khối, bộ phận, nghiệp vụ, mức ưu tiên, tiến độ, giai đoạn và phê duyệt; tìm kiếm cả mã, đầu ra, mô tả, chức danh và nguồn.
- Chi tiết thu gọn có đầu ra, chủ trì, phối hợp, nguồn, mô tả và ghi chú. Tiến độ không đồng nghĩa phê duyệt chính sách.
- Giữ nguyên khóa ovn-company-tasks-v1 và tất cả ID cũ; không migration, không tự ghi đè khi khởi động; không xóa khóa không nhận diện.
- CSV toàn bộ danh mục có UTF-8 BOM, escape dấu nháy và chặn giá trị giống công thức. In toàn bộ danh mục A4, mở chi tiết, độc lập bộ lọc.

## Danh mục theo bộ phận

### 01. Hội đồng quản trị — 9 công việc

- 01-01 — Hoàn thiện điều lệ và quy chế hoạt động HĐQT
- 01-02 — Phê duyệt chiến lược phát triển và định hướng dài hạn
- 01-03 — Phê duyệt mô hình kinh doanh, danh mục sản phẩm và thị trường trọng điểm
- 01-04 — Xác định vốn điều lệ, cơ cấu vốn và kế hoạch huy động
- 01-05 — Phê duyệt cơ cấu tổ chức và chính sách phân quyền
- 01-06 — Quyết định chủ trương đầu tư vùng sản xuất, công trình và hệ thống phân phối
- 01-07 — Thiết lập chế độ giám sát, đánh giá hiệu quả đầu tư và quản trị rủi ro
- 01-08 — Lập lịch họp, quản lý nghị quyết và giám sát thực hiện (mở rộng)
- 01-09 — Phân định quản trị chiến lược và hỗ trợ giai đoạn khởi động (mới)

### 02. Ban Tổng Giám đốc — 13 công việc

- 02-01 — Xây dựng kế hoạch kinh doanh và vận hành năm, quý, tháng
- 02-02 — Thiết lập sơ đồ tổ chức, mô tả công việc và phân quyền (mở rộng)
- 02-03 — Giao KPI, ngân sách, nguồn lực và thời hạn từng bộ phận (mở rộng)
- 02-04 — Điều phối kế hoạch chăn nuôi, trồng trọt, sơ chế và thương mại
- 02-05 — Điều phối vốn, đất, thiết bị, nhân lực và tiến độ dự án
- 02-06 — Tổ chức giao ban ngày, tuần và tháng
- 02-07 — Thiết lập quy trình trình ký, phê duyệt chi phí và hợp đồng (mở rộng)
- 02-08 — Theo dõi tiến độ, xử lý điểm nghẽn và sự cố
- 02-09 — Xây dựng báo cáo quản trị trình cấp có thẩm quyền
- 02-10 — Ban hành cơ chế phối hợp liên phòng ban (mở rộng)
- 02-11 — Chuẩn hóa biểu mẫu giao việc và ma trận RACI (mới)
- 02-12 — Chuẩn hóa nội quy khối sản xuất (mới)
- 02-13 — Thiết lập quy trình xử lý vấn đề vượt thẩm quyền (mới)

### 03. Pháp chế – Tuân thủ — 23 công việc

- 03-01 — Rà soát đăng ký doanh nghiệp, ngành nghề và điều lệ (mở rộng)
- 03-02 — Kiểm tra hồ sơ góp vốn, cổ đông, quyền sử dụng đất và thuê đất (mở rộng)
- 03-03 — Lập ma trận giấy phép, điều kiện kinh doanh theo hoạt động
- 03-04 — Rà soát pháp lý chăn nuôi, thú y, giết mổ, sơ chế và ATTP
- 03-05 — Rà soát điều kiện môi trường, xây dựng, PCCC và chất thải
- 03-06 — Kiểm tra điều kiện pháp lý đối với các loài vật nuôi đặc thù
- 03-07 — Soạn và kiểm soát hợp đồng lao động, mua bán, gia công và hợp tác (mở rộng)
- 03-08 — Rà soát pháp lý nhãn, công bố sản phẩm, quảng cáo và truy xuất
- 03-09 — Bảo vệ nhãn hiệu, tên miền và tài sản trí tuệ
- 03-10 — Quản lý hiệu lực giấy phép, hợp đồng và hồ sơ pháp lý (mở rộng)
- 03-11 — Soạn mẫu thỏa thuận bảo mật thông tin (NDA) (mới)
- 03-12 — Làm rõ thuật ngữ DNA trong nguyên tắc bảo mật (mới)
- 03-13 — Chuẩn hóa hồ sơ họp Đại hội đồng cổ đông (mới)
- 03-14 — Rà soát hồ sơ bổ nhiệm chức danh theo thẩm quyền (mới)
- 03-15 — Rà soát phương án giao dịch và chuyển quyền tài sản (mới)
- 03-16 — Rà soát hợp đồng thuê hồ và diện tích mặt nước (mới)
- 03-17 — Thiết lập danh mục hồ sơ quản trị doanh nghiệp (mới)
- 03-18 — Xây dựng hệ thống quản trị rủi ro pháp lý và kiểm soát tuân thủ toàn doanh nghiệp (mới)
- 03-19 — Cập nhật, tư vấn và triển khai các quy định pháp luật liên quan đến hoạt động doanh nghiệp (mới)
- 03-20 — Kiểm soát pháp lý các hoạt động đầu tư, dự án và mở rộng kinh doanh (mới)
- 03-21 — Quản lý tranh chấp, khiếu nại, vi phạm và xử lý các vấn đề pháp lý phát sinh (mới)
- 03-22 — Tổ chức công tác thanh tra, kiểm tra và làm việc với cơ quan quản lý nhà nước (mới)
- 03-23 — Kiểm tra, đánh giá tuân thủ định kỳ và giám sát khắc phục các sai phạm (mới)

### 04. Hành chính – Nhân sự — 28 công việc

- 04-01 — Xây dựng định biên theo bộ phận và giai đoạn (mở rộng)
- 04-02 — Thiết lập chức danh, JD và tiêu chuẩn năng lực
- 04-03 — Tổ chức tuyển dụng, thử việc và hội nhập
- 04-04 — Xây dựng lương, phụ cấp, thưởng và đánh giá hiệu suất (mở rộng)
- 04-05 — Quản lý hợp đồng lao động, BHXH, BHYT, BHTN và hồ sơ nhân sự (mở rộng)
- 04-06 — Ban hành nội quy, chấm công, nghỉ phép và kỷ luật (mở rộng)
- 04-07 — Lập kế hoạch đào tạo kỹ thuật, an toàn và văn hóa
- 04-08 — Quản lý văn phòng, văn thư, con dấu và tài sản hành chính (mở rộng)
- 04-09 — Xây dựng quy trình quản lý lao động thời vụ
- 04-10 — Lập phương án nhân sự kế nhiệm và dự phòng
- 04-11 — Xây dựng hệ thống thang bảng lương (mới)
- 04-12 — Chuẩn bị hồ sơ đề xuất bổ nhiệm Phó Tổng Giám đốc (mới)
- 04-13 — Soạn nội quy khối văn phòng (mới)
- 04-14 — Xây dựng quy trình tính lương và đối soát chấm công (mới)
- 04-15 — Thiết kế quy trình đánh giá và xét thưởng (mới)
- 04-16 — Quản lý ban hành, cập nhật và thu hồi tài liệu nội bộ (mới)
- 04-17 — Tính lương, thưởng, phụ cấp định kỳ và phối hợp thanh toán lương (mới)
- 04-18 — Chuẩn bị dữ liệu và phối hợp kê khai, quyết toán thuế TNCN, TNDN (mới)
- 04-19 — Thực hiện chế độ, chính sách và phúc lợi người lao động (mới)
- 04-20 — Thực hiện thủ tục điều chuyển, bổ nhiệm, miễn nhiệm và nghỉ việc (mới)
- 04-21 — Tiếp nhận, xử lý tranh chấp, khiếu nại và quan hệ lao động (mới)
- 04-22 — Xây dựng lộ trình phát triển nghề nghiệp và thăng tiến (mới)
- 04-23 — Tổ chức đánh giá năng lực và hiệu quả làm việc định kỳ (mới)
- 04-24 — Tổ chức khám sức khỏe định kỳ và thực hiện an toàn, vệ sinh lao động (mới)
- 04-25 — Thực hiện báo cáo lao động định kỳ với cơ quan nhà nước (mới)
- 04-26 — Lập ngân sách và kiểm soát chi phí hành chính, nhân sự (mới)
- 04-27 — Kiểm tra, giám sát tuân thủ pháp luật lao động (mới)
- 04-28 — Xây dựng báo cáo, thống kê và phân tích dữ liệu nhân sự (mới)

### 05. Tài chính – Kế hoạch vốn — 12 công việc

- 05-01 — Lập tổng mức đầu tư theo dự án và hạng mục
- 05-02 — Lập ngân sách CAPEX và OPEX (mở rộng)
- 05-03 — Dự báo dòng tiền tuần, tháng, quý
- 05-04 — Xác định nhu cầu vốn lưu động theo đàn và vùng trồng
- 05-05 — Xây dựng giá thành, doanh thu và lợi nhuận theo sản phẩm (mở rộng)
- 05-06 — Phân tích điểm hòa vốn, hoàn vốn và kịch bản rủi ro
- 05-07 — Xây dựng hạn mức chi và kiểm soát ngân sách (mở rộng)
- 05-08 — Quản lý nguồn vốn, công nợ và phương án huy động
- 05-09 — Đánh giá hiệu quả đầu tư cơ sở vật chất và thiết bị
- 05-10 — Lập báo cáo tài chính quản trị và cảnh báo dòng tiền
- 05-11 — Xác định nhu cầu và tổ chức thẩm định giá độc lập (mới)
- 05-12 — Xây dựng quy chế tài chính và hồ sơ trình duyệt (mới)

### 06. Kế toán – Thuế — 18 công việc

- 06-01 — Thiết lập chế độ kế toán và phần mềm kế toán (mở rộng)
- 06-02 — Quản lý hóa đơn điện tử, chữ ký số và tài khoản ngân hàng (mở rộng)
- 06-03 — Xây dựng quy trình chứng từ thu, chi, mua, bán, tạm ứng
- 06-04 — Hạch toán các nghiệp vụ kinh tế phát sinh (mở rộng)
- 06-05 — Theo dõi, kiểm soát nhập – xuất – tồn kho (mở rộng)
- 06-06 — Tập hợp chi phí theo mã đàn, lô và đơn vị sản xuất (mở rộng)
- 06-07 — Thực hiện kê khai, nộp thuế và báo cáo đúng kỳ
- 06-08 — Kiểm tra, đối chiếu bảng lương và thực hiện thanh toán lương (mở rộng)
- 06-09 — Kiểm kê, đối chiếu quỹ, ngân hàng và kho
- 06-10 — Lập báo cáo tài chính và số liệu quản trị
- 06-11 — Lập kế hoạch kiểm kê tài sản hiện hữu theo chủ sở hữu (mới)
- 06-12 — Lập danh mục tài sản và đánh giá tình trạng sử dụng (mới)
- 06-13 — Bàn giao và cập nhật sổ tài sản sau giao dịch (mới)
- 06-14 — Theo dõi và quản lý công nợ phải thu, phải trả (mới)
- 06-15 — Kiểm tra chứng từ và thực hiện thanh toán cho nhà cung cấp (mới)
- 06-16 — Kiểm soát doanh thu, giá vốn và xác định kết quả kinh doanh (mới)
- 06-17 — Tổ chức công tác quyết toán thuế, kiểm toán và giải trình với cơ quan chức năng (mới)
- 06-18 — Kiểm soát hồ sơ, chứng từ và quyết toán kế toán các dự án đầu tư, xây dựng cơ bản (mới)

### 07. Kiểm soát nội bộ — 10 công việc

- 07-01 — Thiết lập ma trận rủi ro toàn doanh nghiệp
- 07-02 — Xây dựng kiểm soát mua hàng, thanh toán, kho và tài sản
- 07-03 — Tách biệt đề xuất, phê duyệt, thực hiện và nghiệm thu
- 07-04 — Kiểm kê định kỳ vật nuôi, vật tư và thành phẩm (mở rộng)
- 07-05 — Kiểm soát hao hụt, thất thoát và gian lận
- 07-06 — Rà soát tuân thủ quy trình và hồ sơ nội bộ
- 07-07 — Thiết lập báo cáo sai phạm và theo dõi khắc phục
- 07-08 — Kiểm tra độ tin cậy của KPI, chi phí và doanh thu
- 07-09 — Kiểm tra xung đột lợi ích và nhà cung cấp
- 07-10 — Báo cáo rủi ro trọng yếu qua cơ chế độc lập

### 08. Chăn nuôi – Thú y – Trang trại — 12 công việc

- 08-01 — Kiểm kê đàn hiện hữu và lập kế hoạch nhập giống
- 08-02 — Phân khu theo loài, tuổi, trọng lượng, sức khỏe và mục đích
- 08-03 — Thiết kế quy trình tiếp nhận, cách ly, chăm sóc, xuất bán
- 08-04 — Lập khẩu phần, lịch ăn uống và bổ sung thảo dược
- 08-05 — Xác định định mức thức ăn, hao hụt và chi phí
- 08-06 — Thiết lập lịch thú y, giám sát dịch bệnh và cách ly
- 08-07 — Xây dựng quy trình vệ sinh, sát trùng, đệm lót và chất thải
- 08-08 — Ghi nhật ký tăng trọng, tỷ lệ sống và hệ số chuyển đổi thức ăn
- 08-09 — Thiết lập lịch gối đàn và kế hoạch các nhóm vật nuôi
- 08-10 — Phối hợp thử nghiệm vi sinh và công thức thức ăn
- 08-11 — Lập kế hoạch xuất chuồng, vận chuyển và bàn giao
- 08-12 — Đào tạo nhân công và ứng phó sự cố

### 09. Trồng trọt – Vùng nguyên liệu — 12 công việc

- 09-01 — Kiểm kê và lập bản đồ quỹ đất hiện hữu, dự kiến (mở rộng)
- 09-02 — Đánh giá đất, nước, địa hình, cây trồng và hạ tầng
- 09-03 — Quy hoạch cây ăn quả, rau củ, dược liệu và cây thức ăn
- 09-04 — Lập kế hoạch giống, gieo trồng, chăm sóc và thu hoạch
- 09-05 — Phát triển vùng sâm và các nhóm thảo dược trọng tâm
- 09-06 — Triển khai cây dâu, chùm ngây gieo hạt và cây phụ trợ
- 09-07 — Quản lý vườn cam bưởi và kế hoạch sản lượng
- 09-08 — Thiết lập tưới, phân bón, phòng trừ sâu bệnh và cải tạo đất
- 09-09 — Tính năng suất, định mức vật tư và giá thành trên diện tích
- 09-10 — Điều phối lịch thu hoạch theo nhu cầu sản xuất
- 09-11 — Thiết lập nhật ký canh tác, mã lô và truy xuất
- 09-12 — Phối hợp bảo quản và giao nguyên liệu

### 10. Nghiên cứu & Phát triển – R&D — 11 công việc

- 10-01 — Xây dựng danh mục đề tài R&D ưu tiên
- 10-02 — Nghiên cứu công thức thức ăn theo loài vật nuôi
- 10-03 — Đánh giá thảo dược, vi sinh, rỉ mật và phụ phẩm
- 10-04 — Thiết kế thử nghiệm có đối chứng về hiệu quả và kinh tế (mở rộng)
- 10-05 — Nghiên cứu công nghệ băm, nghiền, trộn, ủ, sấy và bảo quản
- 10-06 — Xác định chỉ tiêu dinh dưỡng, an toàn và thời hạn sử dụng
- 10-07 — Thiết lập lấy mẫu, ghi nhận kết quả và nghiệm thu thử nghiệm (mở rộng)
- 10-08 — Nghiên cứu tận dụng phụ phẩm và nguồn protein thay thế
- 10-09 — Phối hợp viện nghiên cứu, phòng thử nghiệm và nhà chế tạo máy
- 10-10 — Chuyển giao công thức và SOP đã thẩm định (mở rộng)
- 10-11 — Thiết kế nghiệm thức thử nghiệm cây trồng (mới)

### 11. QA/QC – An toàn chất lượng — 10 công việc

- 11-01 — Ban hành chính sách chất lượng và tiêu chuẩn sản phẩm
- 11-02 — Kiểm soát chất lượng đầu vào giống, nguyên liệu và nước
- 11-03 — Kiểm tra an toàn sinh học trang trại và vùng trồng
- 11-04 — Kiểm soát chất lượng sơ chế, đóng gói và bảo quản
- 11-05 — Xây dựng truy xuất nguồn gốc theo lô, đàn và thành phẩm
- 11-06 — Lập kế hoạch lấy mẫu và kiểm nghiệm theo rủi ro
- 11-07 — Rà soát nhãn, hạn sử dụng và điều kiện bảo quản
- 11-08 — Xử lý hàng không phù hợp, khiếu nại và thu hồi
- 11-09 — Đánh giá cơ sở giết mổ, gia công và nhà cung cấp
- 11-10 — Đào tạo nhân viên về vệ sinh, ATTP và hồ sơ

### 12. Xây dựng – Hạ tầng – Bảo trì — 11 công việc

- 12-01 — Khảo sát mặt bằng, hạ tầng và điều kiện xây dựng
- 12-02 — Quy hoạch chuồng, kho, xưởng, đường và khu phụ trợ
- 12-03 — Thiết kế chuồng gà, lợn, bò và khu nuôi chim
- 12-04 — Thiết kế khu cách ly, sân chơi, cấp thoát nước và chất thải
- 12-05 — Lập dự toán, khối lượng, tiến độ và ngân sách
- 12-06 — Lựa chọn nhà thầu, giám sát thi công và nghiệm thu
- 12-07 — Thiết kế điện 3 pha, bơm, bồn, thông gió và sưởi
- 12-08 — Thiết kế kho nguyên liệu, xưởng, khu sơ chế và cửa hàng
- 12-09 — Thiết lập bảo trì định kỳ và hồ sơ thiết bị
- 12-10 — Kiểm soát an toàn công trình và điều kiện đưa vào sử dụng
- 12-11 — Đánh giá rủi ro pháp lý đất trước đầu tư xây dựng (mới)

### 13. Thu mua – Cung ứng — 11 công việc

- 13-01 — Lập danh mục vật tư, giống, nguyên liệu và dịch vụ cần mua (mở rộng)
- 13-02 — Xây dựng danh sách và hồ sơ năng lực nhà cung cấp
- 13-03 — Thu thập báo giá và so sánh chất lượng, chi phí, điều kiện
- 13-04 — Thiết lập yêu cầu mua, phê duyệt, đặt hàng và nghiệm thu (mở rộng)
- 13-05 — Tìm nguồn con giống phù hợp yêu cầu kỹ thuật và pháp lý
- 13-06 — Tìm nguồn thảo dược, vi sinh, nguyên liệu thức ăn và bao bì
- 13-07 — Đàm phán hợp đồng, giá, tiến độ và điều khoản xử lý
- 13-08 — Theo dõi đơn hàng, giao nhận, công nợ và đánh giá NCC
- 13-09 — Thiết lập mức tồn tối thiểu và nguồn cung dự phòng
- 13-10 — Phối hợp QC kiểm tra nguyên liệu đầu vào
- 13-11 — Nghiệm thu và bàn giao thiết bị sau mua sắm (mới)

### 14. Kho vận – Logistics — 10 công việc

- 14-01 — Quy hoạch kho khô, kho mát, kho đông và khu vật tư
- 14-02 — Thiết lập mã hàng, mã lô và vị trí lưu trữ
- 14-03 — Ban hành nhập, xuất, chuyển kho và trả hàng
- 14-04 — Quản lý nhiệt độ, độ ẩm và vệ sinh kho
- 14-05 — Áp dụng FIFO/FEFO phù hợp từng loại hàng
- 14-06 — Lập tuyến giao hàng, phương tiện và đối tác vận tải
- 14-07 — Đo chi phí vận chuyển, hao hụt và giao đúng hạn
- 14-08 — Kiểm soát chuỗi lạnh và chứng từ giao hàng
- 14-09 — Kiểm kê và xử lý chênh lệch, hàng hỏng
- 14-10 — Phối hợp kinh doanh để dự báo nhu cầu

### 15. Sơ chế – Chế biến – Đóng gói — 11 công việc

- 15-01 — Thẩm định đối tác giết mổ thuê ngoài đủ điều kiện
- 15-02 — Thiết kế tiếp nhận sản phẩm sau giết mổ và QC đầu vào
- 15-03 — Quy hoạch khu tiếp nhận, pha lóc, đóng gói và bảo quản
- 15-04 — Ban hành quy cách gà nguyên con, nửa con và phụ phẩm
- 15-05 — Ban hành quy cách đóng khay, hút chân không và nhãn
- 15-06 — Lập danh mục thiết bị, dụng cụ, cân và kho lạnh
- 15-07 — Xác lập định mức hao hụt, tỷ lệ thành phẩm và công suất
- 15-08 — Lập lịch sản xuất theo đơn hàng và kế hoạch xuất chuồng
- 15-09 — Kiểm soát nhiệt độ, thời gian, vệ sinh và truy xuất lô
- 15-10 — Quản lý vệ sinh, bảo trì và phế phụ phẩm
- 15-11 — Đào tạo và chạy thử dây chuyền trước thương mại

### 16. Kinh doanh – Phát triển thị trường — 14 công việc

- 16-01 — Nghiên cứu thị trường, nhu cầu, đối thủ và giá bán
- 16-02 — Phân khúc cá nhân, cơ quan, trường học, chợ, đại lý
- 16-03 — Thẩm định kế hoạch tiêu thụ theo kênh và khu vực
- 16-04 — Lập danh sách khách hàng mục tiêu và lịch tiếp cận
- 16-05 — Ban hành bảng giá, chiết khấu, công nợ và giao hàng (mở rộng)
- 16-06 — Lập kế hoạch doanh số ngày, tuần, tháng
- 16-07 — Thiết lập báo giá, hợp đồng, đơn hàng và thu hồi công nợ
- 16-08 — Lập kế hoạch cửa hàng trưng bày, bán lẻ và đại lý
- 16-09 — Phối hợp sản xuất dự báo nhu cầu, lịch giao hàng
- 16-10 — Thiết lập CRM và đo chuyển đổi, khách hàng quay lại
- 16-11 — Đánh giá lợi nhuận sản phẩm và kênh phân phối
- 16-12 — Tuyển dụng, đào tạo và giao chỉ tiêu kinh doanh
- 16-13 — Lập ngân sách bán hàng và phân phối theo kênh (mới)
- 16-14 — Định kỳ rà soát và đề xuất điều chỉnh chính sách giá (mới)

### 17. Marketing – Thương hiệu – CSKH — 12 công việc

- 17-01 — Hoàn thiện bộ nhận diện và quy chuẩn thương hiệu
- 17-02 — Xây dựng thông điệp, câu chuyện và hồ sơ giới thiệu
- 17-03 — Vận hành website và các kênh truyền thông chính thức
- 17-04 — Lập kế hoạch nội dung, hình ảnh và video hàng tháng
- 17-05 — Thiết kế bao bì, nhãn, POSM và biển hiệu cửa hàng
- 17-06 — Xây dựng hồ sơ năng lực, catalogue và tài liệu đối tác
- 17-07 — Lập kế hoạch truyền thông ra mắt và khai trương
- 17-08 — Kiểm duyệt tuyên bố quảng cáo về chất lượng, thảo dược
- 17-09 — Thiết lập chăm sóc khách hàng và xử lý khiếu nại
- 17-10 — Theo dõi hiệu quả chi phí, chuyển đổi và chiến dịch
- 17-11 — Quản lý thư viện hình ảnh, video và tài sản thương hiệu
- 17-12 — Xây dựng quy chế truyền thông và phát ngôn (mới)

### 18. CNTT – Chuyển đổi số — 13 công việc

- 18-01 — Lập kiến trúc CNTT và lộ trình chuyển đổi số
- 18-02 — Phát triển website giới thiệu doanh nghiệp
- 18-03 — Thiết lập phân quyền, tài khoản và quy trình phê duyệt
- 18-04 — Xây dựng phương án ERP hoặc phân hệ vận hành
- 18-05 — Thiết kế quản lý đàn, vùng trồng và nhật ký sản xuất
- 18-06 — Chuẩn hóa mã sản phẩm, nguyên liệu, kho và khách hàng
- 18-07 — Thiết kế ứng dụng thương mại độc lập và kết nối API
- 18-08 — Thiết lập email doanh nghiệp và lưu trữ tập trung (mở rộng)
- 18-09 — Triển khai MFA, sao lưu, khôi phục và bảo mật
- 18-10 — Xây dựng dashboard KPI và báo cáo điều hành
- 18-11 — Kiểm thử, đào tạo người dùng và quản lý sự cố
- 18-12 — Lập nhu cầu hạ tầng máy tính, mạng, server và tên miền (mới)
- 18-13 — Đăng ký và nghiệm thu kết nối internet (mới)

## Cập nhật riêng bộ phận 06

- 06-05 giữ ID, chuyển thành theo dõi/kiểm soát nhập – xuất – tồn kho.
- 06-08 giữ ID, chuyển thành kiểm tra/đối chiếu và thanh toán lương.
- Thêm 06-14 quản lý phải thu/phải trả và 06-15 kiểm tra chứng từ/thanh toán nhà cung cấp.
- Sau lần tách việc, bộ phận 06 có 15 việc; lần bổ sung ảnh sau đó đưa lên 18 việc. Không bổ sung nhiệm vụ trùng ở Kinh doanh hoặc Thu mua.
- Giữ nguyên khóa localStorage và ID hiện hữu, không cần migration. Hai việc mới mặc định chưa hoàn thành.

## Bổ sung HCNS từ ảnh

- Đối chiếu đủ 16 nội dung trong ảnh, bổ sung 12 nhiệm vụ (04-17 đến 04-28), mở rộng 04-05 và 04-08; giữ các ID/checklist hiện hữu.
- HCNS tính lương và chuẩn bị hồ sơ thuế; Kế toán giữ đầu mối thanh toán tại 06-08 và kê khai tại 06-07. Thu mua giữ đầu mối mua sắm, Pháp chế giữ kiểm soát pháp lý.
- Bộ phận 04 hiện có 28 công việc. Xem [đối chiếu 16 mục HCNS](doi-chieu-hcns.json).

## Bổ sung Pháp chế – Tuân thủ từ ảnh

- Thêm 03-18 đến 03-23: hai việc P0, bốn việc P1; giữ nguyên 17 mã cũ. Bộ phận 03 hiện có 23 việc.
- Phân biệt quản trị rủi ro/tuân thủ pháp luật của Pháp chế với kiểm soát độc lập của KSNB; không tạo thêm nhiệm vụ tại KSNB hoặc HCNS.
- Mỗi việc có đầu ra, phối hợp và nguồn ảnh riêng; checklist mới chưa hoàn thành, không tự phê duyệt chính sách hoặc xác lập thẩm quyền.

## Bổ sung Kế toán – Thuế sau loại trùng

- Thêm 06-16 kiểm soát doanh thu/giá vốn/kết quả kinh doanh (P0), 06-17 quyết toán thuế/kiểm toán/giải trình (P1), 06-18 kiểm soát và quyết toán kế toán dự án (P1). Bộ phận 06 hiện có 18 việc.
- Đầu ra riêng, có tham chiếu tới 06-06 (tập hợp chi phí), 06-07 (kê khai định kỳ), 06-04 (hạch toán) và 06-10 (báo cáo); giữ nguyên các nhiệm vụ và checklist cũ.
- Nguồn ảnh ghi riêng, không tự xác nhận tình trạng đã kiểm toán hoặc kết luận thuế/phê duyệt dự án.

## Kiểm thử và nguồn

Xem [kết quả kiểm thử](ket-qua-kiem-thu.md) và [định danh nguồn đầu vào](nguon-du-lieu.md). Workbook gốc không được đưa lên repo.
