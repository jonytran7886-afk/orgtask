# Organic Việt Nam — Danh mục công việc

Mở `index.html` trực tiếp bằng trình duyệt. Trang chạy độc lập, không cần cài đặt hay backend.

Bản nâng cấp giữ 18 bộ phận và 187 mã công việc cũ; hiện có 217 việc, bổ sung 30 và mở rộng nghiệp vụ của 28 việc cũ. Bộ lọc nghiệp vụ có thể nhóm công việc từ nhiều bộ phận.

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
