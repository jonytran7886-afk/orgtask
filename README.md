# Organic Việt Nam — Danh mục công việc

Mở `index.html` trực tiếp bằng trình duyệt. Trang chạy độc lập, không cần cài đặt hay backend.

Bản nâng cấp giữ 18 bộ phận và 187 mã công việc cũ; hiện có 240 việc, bổ sung 53 và mở rộng nghiệp vụ của 32 việc cũ. Bộ lọc nghiệp vụ có thể nhóm công việc từ nhiều bộ phận.

Checklist lưu trên trình duyệt bằng khóa `ovn-company-tasks-v1`; checkbox không xác nhận phê duyệt chính sách. Các chức danh chỉ là đề xuất và chưa có phân công được duyệt. Nguồn bổ sung từ đặc tả được ghi riêng với nguồn HTML/Excel.

- [Báo cáo thay đổi và danh mục theo bộ phận](docs/bao-cao-thay-doi.md)
- [Bảng đối chiếu từng dòng Excel (CSV UTF-8 BOM)](docs/bang-doi-chieu.csv)
- [Đối chiếu dạng JSON](docs/doi-chieu.json)
- [Kế hoạch và quyết định triển khai](docs/implementation-plan.md)
- [Kết quả kiểm thử](docs/ket-qua-kiem-thu.md)

## Kiểm thử

Kiểm thử dữ liệu, lưu trữ, bộ lọc và CSV bằng Node.js:

```sh
node --test tests/system.test.cjs
```

Kiểm thử tương tác, tải CSV, responsive và bản in bằng Playwright, với Chrome có sẵn:

```sh
PLAYWRIGHT_PATH=/path/to/playwright CHROME_PATH=/path/to/chrome node tests/browser.cjs
```

`PLAYWRIGHT_PATH` có thể bỏ qua nếu Playwright được cài trong môi trường Node. Kết quả QA mặc định lưu tại `/tmp/orgtask-qa`, có thể đổi bằng `QA_OUTPUT`.

## Duy trì mã nguồn

`index.html` là file bàn giao hoàn chỉnh. Các file trong `scripts/` lưu phép hợp nhất đã khử định danh và phần mở rộng giao diện; không chứa workbook gốc hay tên nhân sự. Chạy `python3 scripts/upgrade.py` trong repo để tạo lại HTML và báo cáo từ commit gốc `fd9c2a7`. Trước khi sửa dữ liệu, giữ ổn định ID để bảo toàn checklist.

Nguồn Excel được đọc từ Downloads trong phiên nâng cấp, không đưa workbook chứa dữ liệu cá nhân lên Git. Đối chiếu ghi địa chỉ ô và nội dung đã khử định danh. Hai nội dung chưa rõ: thuật ngữ DNA ở B12 và mục 10 trống ở A68.

Lần tách việc bộ phận 06 đưa danh mục lên 15 việc: 06-05 giữ nhiệm vụ kho, 06-08 giữ thanh toán lương; thêm 06-14 quản lý công nợ và 06-15 thanh toán nhà cung cấp. Không cần migration vì ID cũ và cấu trúc lưu trữ được giữ nguyên.

Ảnh bổ sung HCNS có 16 mục: thêm 12 nhiệm vụ từ 04-17 đến 04-28 và mở rộng 04-05/04-08. HCNS hiện có 28 việc. Xem [bảng đối chiếu HCNS](docs/doi-chieu-hcns.json); nguồn ảnh được ghi riêng trong dữ liệu và CSV.

Ảnh bổ sung Pháp chế – Tuân thủ: thêm 03-18 đến 03-23, gồm 2 việc P0 và 4 việc P1. Bộ phận 03 hiện có 23 việc; giữ nguyên 17 mã cũ và checklist.

Ảnh bổ sung Kế toán – Thuế sau loại trùng: thêm 06-16 (P0), 06-17 và 06-18 (P1). Bộ phận 06 hiện có 18 việc; các nhiệm vụ mới có đầu ra riêng và tham chiếu rõ việc giá vốn, kê khai, hạch toán hiện có.
