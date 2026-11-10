# -*- coding: utf-8 -*-
"""Reproducible merge from original committed HTML; source workbook is read-only."""
import json,re,pathlib,subprocess,csv,io,collections
ROOT=pathlib.Path(__file__).resolve().parent.parent
original=subprocess.check_output(['git','show','fd9c2a7:index.html'],cwd=ROOT).decode()
data=json.loads(re.search(r'const DATA=(\[.*?\]);',original,re.S).group(1))
byid={t['id']:t for d in data for t in d['tasks']}
categories={'01':'Quản trị và phân quyền','02':'Điều hành và phối hợp','03':'Pháp lý doanh nghiệp','04':'Tổ chức và nhân sự','05':'Tài chính và ngân sách','06':'Kế toán và giá thành','07':'Kiểm soát và rủi ro','08':'Chăn nuôi và thú y','09':'Đất đai và vùng trồng','10':'Nghiên cứu và thử nghiệm','11':'Chất lượng và an toàn','12':'Hạ tầng và xây dựng','13':'Mua sắm và cung ứng','14':'Kho vận và tài sản','15':'Sản xuất và đóng gói','16':'Giá bán và kinh doanh','17':'Truyền thông và thương hiệu','18':'Hạ tầng số và dữ liệu'}
for d in data:
 for t in d['tasks']:
  t.update(departmentId=d['id'],category=categories[d['id']],title=t['name'],description='Thiết lập phạm vi, điều kiện đầu vào, bước thực hiện và tiêu chí nghiệm thu cho nhiệm vụ: '+t['name']+'.',responsibleRole='Chưa phân công',collaboratingDepartments=[],deliverable='Hồ sơ '+t['name'][0].lower()+t['name'][1:]+'; kèm kết quả rà soát, danh mục tồn tại và bằng chứng nghiệm thu.',status='todo',approvalStatus='Không áp dụng',source='Danh mục HTML ban đầu',notes='Chờ phê duyệt cơ cấu. Chức danh đề xuất: '+d['roles'].split(',')[0]+'. Chưa xác nhận phân công.')
  if any(w in t['name'].lower() for w in ['ban hành','phê duyệt','quy chế','chính sách','hạn mức','phân quyền']):
   t['approvalStatus']='Chờ phê duyệt'
   t['notes']+=' Tên nhiệm vụ mô tả việc cần làm, không xác nhận văn bản đã ban hành.'
for id in ['01-04','01-06','05-01','05-08','12-05']:
 byid[id]['approvalStatus']='Chờ phê duyệt'
 byid[id]['notes']+=' Kế hoạch vốn, ngân sách hoặc chủ trương đầu tư cần trình duyệt; chưa xác nhận có phê duyệt.'
expanded=set();added=[];audit=[]
def edit(id,description,deliverable,collab='',approval=None,source=True,category=None):
 t=byid[id];t.update(description=description,deliverable=deliverable,collaboratingDepartments=collab.split(',') if collab else [])
 if approval:t['approvalStatus']=approval
 if category:t['category']=category
 if source:t['source']='Hợp nhất từ hai nguồn'
 expanded.add(id)
 return id

def add(dep,title,deliverable,collab='',priority='P1',phase=2,approval='Không áp dụng',description='',excel=False,category=None):
 d=next(d for d in data if d['id']==dep);id=dep+'-'+str(max(int(t['id'].split('-')[1]) for t in d['tasks'])+1).zfill(2)
 t=dict(id=id,departmentId=dep,category=category or categories[dep],name=title,title=title,description=description or title+'. Xác định đầu vào, phạm vi và tiêu chí kiểm tra trước khi nghiệm thu.',responsibleRole='Chưa phân công',collaboratingDepartments=collab.split(',') if collab else [],deliverable=deliverable,priority=priority,phase=phase,status='todo',approvalStatus=approval,source='Excel bộ phận vận hành' if excel else 'Đặc tả nâng cấp',notes='Chờ phê duyệt cơ cấu. Chức danh đề xuất: '+d['roles'].split(',')[0]+'. Chưa xác nhận phân công.'+('' if excel else ' Bổ sung theo đặc tả nâng cấp, không phải nội dung trích từ Excel.'))
 d['tasks'].append(t);byid[id]=t;added.append(id);return id

def row(n,summary,ids,action='Mở rộng công việc hiện có',note=''):
 audit.append(dict(cell='Sheet1!B'+str(n),summary=summary,action=action,taskIds=ids.split(','),notes=note))
edit('04-01','Lập danh mục chức danh, định biên và tình trạng hồ sơ tuyển dụng/nhân sự theo bộ phận; không lưu tên cá nhân trong danh mục công việc.','Bảng chức danh, số lượng dự kiến, tiêu chuẩn tuyển và danh mục hồ sơ cần có; trạng thái cơ cấu chờ phê duyệt.','02','Chờ phê duyệt');row(3,'Danh sách nhân sự — chuẩn hóa thành danh mục chức danh và hồ sơ','04-01',note='Không nhập danh sách hoặc tên nhân sự.')
edit('04-04','Soạn cơ cấu lương, phụ cấp, thưởng; trình duyệt theo thẩm quyền, không tự đặt mức tiền.','Dự thảo chính sách lương thưởng và phiếu trình duyệt có kiểm soát phiên bản.','05,06','Chờ phê duyệt');row(4,'Cơ chế lương thưởng','04-04')
x=add('04','Xây dựng hệ thống thang bảng lương','Bộ thang bảng lương theo chức danh, nguyên tắc xếp bậc và hồ sơ trình duyệt.','03,05',approval='Chờ phê duyệt',excel=True);row(5,'Xây dựng thang bảng lương',x,'Thêm công việc mới')
edit('03-07','Soạn bộ mẫu hợp đồng lao động, mua bán, gia công và hợp tác; kiểm tra điều khoản, thẩm quyền ký và phiên bản.','Bộ mẫu hợp đồng có checklist rà soát pháp lý và danh mục điều khoản cần phê duyệt.','04,13','Chờ phê duyệt');row(6,'Khung hợp đồng lao động','03-07')
x=add('03','Soạn mẫu thỏa thuận bảo mật thông tin (NDA)','Mẫu NDA, phạm vi thông tin mật, nghĩa vụ bảo mật và quy trình ký/lưu hồ sơ.','04,18',approval='Chờ phê duyệt',excel=True);row(7,'Hợp đồng bảo mật',x,'Thêm công việc mới')
edit('02-03','Hướng dẫn từng bộ phận xây dựng KPI cho các cấp phụ trách; thống nhất chỉ tiêu, dữ liệu chứng minh và quy trình đánh giá; ngân sách và thời hạn chỉ giao khi có căn cứ.','Ma trận KPI từng cấp, phiếu giao chỉ tiêu, nguồn dữ liệu và quy trình rà soát/trình duyệt.','04,05','Chờ phê duyệt');row(8,'Tiêu chí KPI theo cấp và bộ phận','02-03')
edit('03-01','Đối chiếu điều lệ, đăng ký doanh nghiệp, ngành nghề và phiên bản hồ sơ; ghi rõ điểm thiếu, sai khác và nhu cầu sửa đổi.','Bảng rà soát điều lệ/đăng ký doanh nghiệp, danh mục hồ sơ còn thiếu và đề xuất cập nhật.','01,02','Cần xác minh');row(11,'Điều lệ công ty','03-01')
x=add('03','Làm rõ thuật ngữ DNA trong nguyên tắc bảo mật','Biên bản xác nhận thuật ngữ, phạm vi và loại văn bản cần xây dựng; liên kết NDA nếu được xác nhận.','04,18',approval='Cần xác minh',description='Nguồn ghi DNA, chưa đủ căn cứ xác định là NDA hoặc tài liệu khác; cần làm rõ trước khi nhập chính sách.',excel=True);row(12,'Nguyên tắc bảo mật — thuật ngữ DNA chưa rõ',x,'Cần làm rõ','Không tự sửa DNA thành NDA.')
row(13,'Giấy phép/đăng ký kinh doanh','03-01')
x=add('03','Chuẩn hóa hồ sơ họp Đại hội đồng cổ đông','Danh mục tài liệu họp, mẫu biên bản/nghị quyết và checklist hồ sơ theo thẩm quyền.','01',approval='Chờ phê duyệt',excel=True)
edit('01-08','Lập lịch họp HĐQT; chuẩn hóa biên bản, nghị quyết, đăng ký theo dõi và giám sát thực hiện; không xác nhận nghị quyết đã ban hành nếu thiếu chứng cứ.','Lịch họp, bộ mẫu biên bản/nghị quyết HĐQT, sổ theo dõi hiệu lực và hành động sau họp.','03','Chờ phê duyệt');row(14,'Biên bản họp cổ đông và Hội đồng quản trị','01-08,'+x,'Mở rộng và thêm công việc con')
x=add('03','Rà soát hồ sơ bổ nhiệm chức danh theo thẩm quyền','Ma trận thẩm quyền bổ nhiệm, mẫu quyết định và danh mục hồ sơ cần xác minh cho từng chức danh.','01,02,04',approval='Cần xác minh',excel=True);row(15,'Hồ sơ bổ nhiệm các chức danh',x,'Thêm công việc mới')
y=add('04','Chuẩn bị hồ sơ đề xuất bổ nhiệm Phó Tổng Giám đốc','Bộ hồ sơ theo chức danh, tiêu chuẩn, ý kiến thẩm định và tờ trình bổ nhiệm; chưa có quyết định hiệu lực.','01,02,03',approval='Chờ phê duyệt',excel=True);row(16,'Đề xuất bổ nhiệm Phó Tổng Giám đốc',y,'Thêm công việc mới','Loại tên cá nhân; không coi nội dung nguồn là quyết định bổ nhiệm.')
edit('02-07','Thiết kế luồng trình ký chứng từ/hợp đồng, phạm vi ủy quyền theo chức danh, thời hạn và điều kiện thu hồi; chỉ áp dụng sau phê duyệt.','Sơ đồ trình ký, ma trận ký chứng từ và dự thảo ủy quyền kèm sổ hiệu lực.','03,05,06','Chờ phê duyệt');row(17,'Ủy quyền ký hồ sơ chứng từ theo chức danh','02-07')
edit('05-07','Lập ma trận hạn mức phê duyệt tài chính theo chức danh; kiểm tra điều kiện đăng ký và duyệt ngân sách tổng. Mọi hạn mức trong nguồn là đề xuất chưa được phê duyệt.','Dự thảo ma trận hạn mức, điều kiện ngân sách, luồng trình vượt thẩm quyền và hồ sơ trình duyệt.','01,02,03,07','Chờ phê duyệt');row(18,'Đề xuất hạn mức tài chính theo chức danh và điều kiện ngân sách','05-07',note='Không nhập các mức tiền như quy định chính thức; cần xác minh căn cứ và trình duyệt.')
x=add('02','Chuẩn hóa biểu mẫu giao việc và ma trận RACI','Mẫu phiếu giao việc với đầu ra, chức danh chủ trì/phối hợp/phê duyệt/tham vấn và ma trận RACI liên phòng ban.','04,07',approval='Chờ phê duyệt',excel=True);row(19,'Mẫu phân công công việc phụ trách',x,'Thêm công việc mới')
x=add('01','Phân định quản trị chiến lược và hỗ trợ giai đoạn khởi động','Ma trận quyền hạn HĐQT/Ban điều hành; phạm vi, thời điểm rà soát và cơ chế báo cáo của hỗ trợ khởi động.','02,03,07',priority='P0',phase=1,approval='Chờ phê duyệt',description='Xác định hỗ trợ khởi động trong xây dựng, nuôi trồng và chăn nuôi; không suy ra quyền điều hành thường xuyên hoặc thay thế Ban Tổng Giám đốc.',excel=True);row(22,'Phạm vi HĐQT hỗ trợ điều hành trong giai đoạn đầu',x,'Thêm công việc mới')
edit('02-02','Thiết kế sơ đồ tổ chức, JD và phạm vi điều hành của từng chức danh, bao gồm Phó Tổng Giám đốc; đối chiếu ủy quyền và cơ chế báo cáo.','Sơ đồ tổ chức đề xuất, ma trận quyền hạn và JD theo chức danh có trạng thái duyệt.','01,03,04','Chờ phê duyệt');row(23,'Phạm vi điều hành chung theo chức danh Phó Tổng Giám đốc','02-02',note='Không coi mô tả trong Excel là ủy quyền có hiệu lực.')
x=add('06','Lập kế hoạch kiểm kê tài sản hiện hữu theo chủ sở hữu','Kế hoạch kiểm kê, biểu mẫu, phạm vi tài sản và phân loại cá nhân/công ty/bên thứ ba.','03,07,08,09,12',priority='P0',phase=1,approval='Cần xác minh',excel=True);row(26,'Kế hoạch kiểm kê tài sản hiện hữu',x,'Thêm công việc mới','Loại tên chủ tài sản; quyền sở hữu cần xác minh.')
edit('07-04','Phối hợp đơn vị sử dụng, kế toán và pháp chế kiểm kê vật nuôi, vật tư, thành phẩm và tài sản; đối chiếu độc lập với hồ sơ.','Biên bản kiểm kê, bảng chênh lệch, phân loại quyền sở hữu và kiến nghị xử lý.','06,03,08,09,14','Cần xác minh');row(27,'Phối hợp kế toán và pháp chế kiểm kê','07-04')
x=add('06','Lập danh mục tài sản và đánh giá tình trạng sử dụng','Sổ tài sản có mã, vị trí, chủ sở hữu cần xác minh, tình trạng, hồ sơ chứng minh và cơ sở giá trị.','03,07,12',approval='Cần xác minh',excel=True);row(28,'Danh mục và đánh giá giá trị tài sản',x,'Thêm công việc mới')
x=add('05','Xác định nhu cầu và tổ chức thẩm định giá độc lập','Danh sách tài sản cần thẩm định, tiêu chí đơn vị độc lập, hồ sơ cung cấp và báo cáo thẩm định khi cần.','03,06,13',approval='Cần xác minh',excel=True);row(29,'Chuyển đơn vị thẩm định giá',x,'Thêm công việc mới')
x=add('03','Rà soát phương án giao dịch và chuyển quyền tài sản','Hồ sơ so sánh góp vốn/mua bán/thuê/chuyển giao; điều kiện, thẩm quyền và thủ tục chuyển quyền theo phương án được duyệt.','05,06,07',approval='Cần xác minh',description='Xác minh chủ sở hữu, quyền chuyển giao và bản chất giao dịch trước khi chọn phương án; không mặc định tài sản cá nhân trở thành vốn chủ sở hữu.',excel=True)
edit('06-04','Ghi nhận đầu tư, chi phí và tài sản theo bản chất giao dịch và hồ sơ hợp lệ; chỉ ghi nhận vốn chủ sở hữu khi đủ căn cứ.','Bộ chứng từ, biên bản bàn giao, đối chiếu giá trị và bảng hạch toán theo từng loại giao dịch.','03,05,07','Cần xác minh');row(30,'Phương án chuyển tài sản và ghi nhận kế toán phù hợp',x+',06-04','Mở rộng và thêm công việc con','Không tự ghi nhận tài sản cá nhân thành vốn chủ sở hữu.')
edit('03-02','Phân loại đất dự kiến góp vốn, đất thuê và mặt nước; kiểm tra hồ sơ quyền sử dụng, thời hạn, mục đích, giới hạn sử dụng và điều kiện chuyển quyền/góp vốn.','Sổ pháp lý từng khu đất/mặt nước, checklist điều kiện, hợp đồng và danh sách rủi ro cần xử lý.','09,05,12','Cần xác minh');row(33,'Đất cá nhân dự kiến góp vốn','03-02',note='Chưa xác nhận đủ điều kiện góp vốn.')
row(34,'Đất thuê và hợp đồng thuê','03-02')
x=add('03','Rà soát hợp đồng thuê hồ và diện tích mặt nước','Hồ sơ chủ thể cho thuê, ranh giới diện tích, mục đích/thời hạn sử dụng, điều kiện khai thác và lịch theo dõi hợp đồng.','09,05,12',approval='Cần xác minh',excel=True);row(35,'Thuê hồ và hợp đồng thuê hồ',x,'Thêm công việc mới')
edit('04-06','Soạn nội quy tổng thể, nội quy lao động, chấm công, nghỉ phép, kỷ luật; phân biệt quy định quản trị và tài liệu cần thủ tục ban hành phù hợp.','Bộ dự thảo nội quy, quy định chấm công/kỷ luật và checklist thủ tục ban hành, phổ biến, theo dõi hiệu lực.','03,02','Chờ phê duyệt');row(38,'Nội quy tổng thể doanh nghiệp','04-06')
x=add('04','Soạn nội quy khối văn phòng','Dự thảo nội quy văn phòng về nơi làm việc, tài sản, an toàn, thông tin và trách nhiệm phổ biến.','03,18',approval='Chờ phê duyệt',excel=True);row(39,'Nội quy khối văn phòng',x,'Thêm công việc mới')
x=add('02','Chuẩn hóa nội quy khối sản xuất','Dự thảo nội quy sản xuất và checklist triển khai tại chăn nuôi, trồng trọt, sơ chế; phân biệt nội quy và SOP.','08,09,11,15,04',approval='Chờ phê duyệt',excel=True);row(40,'Nội quy khối sản xuất',x,'Thêm công việc mới')
edit('02-10','Thiết kế SOP từng bộ phận và quy trình liên phòng ban; chỉ định đầu vào/đầu ra, điểm bàn giao và cơ chế báo cáo, xử lý chậm trễ/vượt thẩm quyền.','Danh mục SOP, sơ đồ phối hợp, biểu mẫu bàn giao, lịch báo cáo và ma trận đầu mối theo chức danh.','04,07','Chờ phê duyệt');row(41,'Quy trình từng bộ phận và liên phòng ban','02-10')
x=add('17','Xây dựng quy chế truyền thông và phát ngôn','Dự thảo quy chế truyền thông, ma trận duyệt nội dung, phân loại thông tin và quy trình xử lý sự cố.','03,02,18',approval='Chờ phê duyệt',excel=True);row(42,'Quy chế truyền thông',x,'Thêm công việc mới')
x=add('05','Xây dựng quy chế tài chính và hồ sơ trình duyệt','Dự thảo quy chế tài chính, nguyên tắc ngân sách, thanh toán, quản lý tài sản, kiểm soát và ma trận văn bản liên quan.','06,03,07',priority='P0',phase=1,approval='Chờ phê duyệt',excel=True);row(43,'Quy chế tài chính',x,'Thêm công việc mới')
row(44,'Nội quy lao động','04-06');row(45,'Quy định chấm công','04-06')
x=add('04','Xây dựng quy trình tính lương và đối soát chấm công','SOP tính lương, biểu mẫu đầu vào/đối soát/phê duyệt bảng lương và kiểm soát sai lệch.','06,03',approval='Chờ phê duyệt',excel=True);row(46,'Quy định tính lương',x,'Thêm công việc mới')
row(47,'Quy định đánh giá KPI','02-03')
x=add('04','Thiết kế quy trình đánh giá và xét thưởng','Bộ tiêu chí đánh giá, phiếu xét thưởng, quy trình khiếu nại và tờ trình theo thẩm quyền; không tự xác lập mức thưởng.','02,05,06',approval='Chờ phê duyệt',excel=True);row(48,'Quy định xét thưởng',x,'Thêm công việc mới')
edit('13-01','Tổng hợp nhu cầu vật tư, giống, dịch vụ, bàn ghế và thiết bị làm việc; tách nhu cầu, dự toán, trình duyệt, đặt mua, nghiệm thu và bàn giao.','Danh mục nhu cầu theo bộ phận, cấu hình/số lượng đề xuất và liên kết hồ sơ ngân sách, mua sắm, nghiệm thu.','04,18,05','Chờ phê duyệt');row(51,'Bàn ghế và thiết bị văn phòng','13-01')
x=add('18','Lập nhu cầu hạ tầng máy tính, mạng, server và tên miền','Danh mục cấu hình, yêu cầu hosting/server, máy tính, mạng, tên miền; dự toán đề xuất và tiêu chí nghiệm thu.','04,13,05',approval='Chờ phê duyệt',excel=True)
edit('18-08','Thiết kế email doanh nghiệp và lưu trữ tập trung; tách lập nhu cầu, phê duyệt, mua dịch vụ, nghiệm thu và cấp quyền sử dụng.','Danh mục tài khoản theo vai trò, cấu hình dịch vụ, biên bản kiểm tra gửi nhận, sao lưu và bàn giao.','04,13','Chờ phê duyệt');row(52,'Server, domain/tên miền và email',x+',18-08','Mở rộng và thêm công việc con','Domain và tên miền là cùng một hạng mục.')
x=add('18','Đăng ký và nghiệm thu kết nối internet','Yêu cầu đường truyền, đề xuất nhà cung cấp, hồ sơ phê duyệt/đăng ký và biên bản kiểm tra kết nối.','13,04',approval='Chờ phê duyệt',excel=True);row(53,'Đăng ký Internet',x,'Thêm công việc mới')
edit('06-01','Xác định chế độ kế toán và nhu cầu phần mềm; lập yêu cầu, trình ngân sách, phối hợp mua, kiểm thử dữ liệu và đào tạo trước sử dụng.','Tài liệu yêu cầu phần mềm kế toán, hồ sơ lựa chọn/phê duyệt và biên bản nghiệm thu triển khai.','18,13,05','Chờ phê duyệt')
edit('06-02','Xác định nhu cầu hóa đơn điện tử, chữ ký số và tài khoản ngân hàng; tổ chức đăng ký, kiểm thử và bàn giao quyền sử dụng có kiểm soát.','Hồ sơ đăng ký/phê duyệt, biên bản kiểm thử hóa đơn/chữ ký số và sổ quản lý quyền sử dụng.','18,03,13','Chờ phê duyệt');row(54,'Phần mềm kế toán và hóa đơn điện tử','06-01,06-02')
edit('10-04','Lập đề cương thử nghiệm chăn nuôi: nghiệm thức, lô đối chứng, chỉ tiêu tăng trưởng, an toàn, chi phí, phương pháp và khả năng lặp lại.','Đề cương thử nghiệm và ma trận nghiệm thức/đối chứng/chỉ tiêu; tờ trình trước thực hiện.','08,11,06','Chờ phê duyệt');row(57,'Nghiên cứu nghiệm thức chăn nuôi','10-04',note='Chuẩn hóa lỗi chữ nghiệp thức theo ngữ cảnh nghiên cứu; không coi thử nghiệm là SOP sản xuất đã duyệt.')
x=add('10','Thiết kế nghiệm thức thử nghiệm cây trồng','Đề cương cây trồng với nghiệm thức, lô đối chứng, số lần lặp, chỉ tiêu sinh trưởng/năng suất/chi phí và phương pháp ghi chép.','09,11,06',approval='Chờ phê duyệt',excel=True);row(58,'Nghiên cứu nghiệm thức cây trồng',x,'Thêm công việc mới')
edit('06-06','Xây dựng phương pháp giá vốn; tập hợp và phân bổ chi phí theo sản phẩm, mã đàn, lô, đơn vị sản xuất; kiểm tra cơ sở phân bổ.','Quy tắc tính giá vốn, danh mục đối tượng tập hợp chi phí và bảng đối soát chi phí từng lô/sản phẩm.','05,08,09,15','Chờ phê duyệt');row(61,'Giá vốn','06-06')
edit('16-05','Soạn chính sách giá bán, chiết khấu, công nợ, giao hàng; thẩm định giá vốn/biên lợi nhuận và trình cấp có thẩm quyền trước ban hành.','Dự thảo chính sách và bảng giá, mô hình tác động, hồ sơ thẩm định/phê duyệt và lịch rà soát.','05,06,03','Chờ phê duyệt');row(62,'Giá bán','16-05')
edit('05-02','Lập riêng ngân sách đầu tư CAPEX và vận hành OPEX; ghi rõ giả định, nhu cầu, căn cứ và tình trạng duyệt; không tự tạo số tiền.','Hai danh mục CAPEX/OPEX, bảng tổng hợp theo hạng mục, nguồn vốn và tờ trình ngân sách.','02,06,12,13','Chờ phê duyệt');row(63,'Chi phí CAPEX','05-02');row(64,'Chi phí OPEX','05-02')
x=add('16','Lập ngân sách bán hàng và phân phối theo kênh','Danh mục chi phí bán hàng/phân phối, cơ sở phân bổ theo kênh và hồ sơ trình duyệt ngân sách.','05,06,14,17',approval='Chờ phê duyệt',excel=True);row(65,'Chi phí bán hàng',x,'Thêm công việc mới')
edit('05-05','Xây dựng mô hình giá thành, doanh thu và biên lợi nhuận mục tiêu theo sản phẩm; tách giả định đề xuất khỏi số liệu được xác nhận.','Mô hình đầu vào có nguồn, phương pháp tính và tờ trình mục tiêu lợi nhuận; không điền tỷ lệ chưa xác nhận.','06,16','Chờ phê duyệt');row(66,'Lợi nhuận mong muốn','05-05')
audit.append(dict(cell='Sheet1!A68',summary='Mục 10 để trống',action='Cần làm rõ',taskIds=[],notes='Không tạo nhiệm vụ từ tiêu đề trống.'))
# Additional independently verifiable deliverables required by the supplied upgrade brief.
add('03','Thiết lập danh mục hồ sơ quản trị doanh nghiệp','Sổ hồ sơ điều lệ, đăng ký doanh nghiệp, cổ đông, nghị quyết, bổ nhiệm, ủy quyền; phân quyền lưu trữ và thời hạn hiệu lực.','01,02,04',approval='Cần xác minh')
edit('03-10','Quản lý hiệu lực giấy phép, quyết định, ủy quyền, hợp đồng; chuẩn hóa lưu trữ, nhắc rà soát và thu hồi văn bản hết hiệu lực.','Sổ hiệu lực với mã văn bản, nguồn chứng minh, kỳ rà soát, quyền truy cập và danh mục cần gia hạn.','01,02,04',source=False)
add('02','Thiết lập quy trình xử lý vấn đề vượt thẩm quyền','Sơ đồ tiếp nhận, đánh giá, trình cấp có thẩm quyền, phản hồi và theo dõi xử lý; biểu mẫu báo cáo ngoại lệ.','01,03,07',approval='Chờ phê duyệt')
add('06','Bàn giao và cập nhật sổ tài sản sau giao dịch','Biên bản bàn giao tài sản theo phương án được duyệt, hồ sơ kế toán đối chiếu và sổ tài sản cập nhật.','03,07,14',approval='Cần xác minh')
edit('09-01','Kiểm kê và lập bản đồ đất hiện hữu/dự kiến, tài sản trên đất; liên kết từng khu với hồ sơ pháp lý, mục đích, thời hạn và nguồn dữ liệu.','Bản đồ quản lý đất/tài sản, mã khu đất, bảng diện tích và danh mục hồ sơ liên kết.','03,12,05',source=False)
add('12','Đánh giá rủi ro pháp lý đất trước đầu tư xây dựng','Checklist mặt bằng, mục đích sử dụng, hạn chế, điều kiện xây dựng và báo cáo rủi ro trước quyết định đầu tư.','03,09,05',priority='P0',phase=1,approval='Cần xác minh')
add('04','Quản lý ban hành, cập nhật và thu hồi tài liệu nội bộ','Danh mục phân loại chính sách/quy chế/quy định/SOP/biểu mẫu/hướng dẫn; quy trình phiên bản, duyệt, phổ biến và thu hồi.','03,02,11',approval='Chờ phê duyệt')
edit('13-04','Thiết kế quy trình mua sắm theo ngân sách: yêu cầu nhu cầu → thẩm định → phê duyệt → đặt hàng → nghiệm thu → bàn giao đưa vào dùng; tách vai trò kiểm soát.','SOP mua sắm, phiếu đề xuất, phiếu duyệt, đơn mua và biểu mẫu nghiệm thu/bàn giao có liên kết ngân sách.','05,06,07,04,18','Chờ phê duyệt',source=False)
add('13','Nghiệm thu và bàn giao thiết bị sau mua sắm','Biên bản nghiệm thu theo yêu cầu đã duyệt, danh mục mã tài sản, bảo hành và bàn giao đơn vị sử dụng.','04,18,06,12',phase=3)
edit('10-07','Ghi nhận tăng trưởng, năng suất, an toàn và chi phí theo nghiệm thức; lấy mẫu, phân tích, nghiệm thu và lưu phiên bản để tái lập thử nghiệm.','Nhật ký thí nghiệm, dữ liệu gốc, báo cáo phân tích, biên bản nghiệm thu và hồ sơ tái lập.','08,09,11,06',source=False)
edit('10-10','Chuyển giao công thức và SOP sau thẩm định/nghiệm thu; chỉ đưa vào sản xuất khi có phê duyệt phù hợp, theo dõi phiên bản và giới hạn áp dụng.','Bộ hồ sơ chuyển giao, SOP có phiên bản, biên bản đào tạo và chấp thuận áp dụng.','08,09,15,11','Chờ phê duyệt',source=False)
add('16','Định kỳ rà soát và đề xuất điều chỉnh chính sách giá','Báo cáo hiệu quả theo kênh, biến động giá vốn, kiến nghị điều chỉnh và tờ trình phiên bản giá mới.','05,06,17',phase=4,approval='Chờ phê duyệt')
# Business categories intentionally span departments; they are not a new org chart.
category_ranges=[(3,8,'Tổ chức và nhân sự'),(11,19,'Pháp lý doanh nghiệp và quản trị nội bộ'),(22,23,'Phân quyền và điều hành'),(26,30,'Kiểm kê và chuyển giao tài sản'),(33,35,'Pháp lý và quản lý đất đai'),(38,48,'Hệ thống tài liệu nội bộ'),(51,54,'Mua sắm và hạ tầng'),(57,58,'Nghiên cứu và thử nghiệm'),(61,66,'Chính sách tài chính và kinh doanh')]
categorized=set()
for a in audit:
 if '!B' not in a['cell']:continue
 n=int(a['cell'].split('!B')[1])
 category=next(label for lo,hi,label in category_ranges if lo<=n<=hi)
 for id in a['taskIds']:
  if id not in categorized:byid[id]['category']=category;categorized.add(id)
for ids,category in [(['06-13'],'Kiểm kê và chuyển giao tài sản'),(['09-01','12-11'],'Pháp lý và quản lý đất đai'),(['04-16','03-17'],'Hệ thống tài liệu nội bộ'),(['13-04','13-11'],'Mua sắm và hạ tầng'),(['02-13'],'Phân quyền và điều hành'),(['16-14'],'Chính sách tài chính và kinh doanh')]:
 for id in ids:byid[id]['category']=category
# Attach exact source cells to task notes without importing personal source text.
for a in audit:
 for id in a['taskIds']:
  t=byid[id]; t['notes']+=' Tham chiếu '+a['cell']+'.'
  if a['notes']:t['notes']+=' '+a['notes']
for d in data:
 for t in d['tasks']:
  if t['id'] in expanded and t['source']=='Danh mục HTML ban đầu':t['notes']+=' Mở rộng theo đặc tả nâng cấp.'
base=re.sub(r'const DATA=\[.*?\];',lambda m:'const DATA='+json.dumps(data,ensure_ascii=False,indent=2)+';',original,count=1,flags=re.S)
(ROOT/'docs/doi-chieu.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
# Runtime and styling are authored separately and injected to keep the delivered page standalone.
base=base[:base.index('const colors=')]+(ROOT/'scripts/runtime.js').read_text()+'\n</script></body></html>\n'
base=base.replace('</style>',(ROOT/'scripts/extra.css').read_text()+'\n</style>',1)
base=base.replace('BỘ KHUNG QUẢN TRỊ • V1.0','DANH MỤC ĐIỀU HÀNH • V2.0')
base=base.replace('4 khối điều hành','<span id="groupTotal">—</span> khối điều hành')
base=base.replace('>18</div>','>—</div>').replace('>187</div>','>—</div>').replace('0 / 187 công việc hoàn thành','Đang tính tiến độ')
base=base.replace('</section>\n<section class="panel">','</section>\n'+(ROOT/'scripts/dashboard.html').read_text()+'\n<section class="panel">',1)
base=base.replace('<div id="departmentGrid"', '<p id="resultCount" class="tiny" aria-live="polite"></p><p id="storageNotice" class="notice hidden" role="status"></p><div id="departmentGrid"')
base=base.replace('<div class="filters">','<div class="filters">'+(ROOT/'scripts/filters.html').read_text(),1)
base=base.replace('<div class="foot">','<div id="printCatalogue" class="print-only"></div><div class="foot">',1)
base=base.replace('có thể phân công nhiều người phối hợp.','có thể phối hợp nhiều bộ phận.').replace('người phê duyệt','chức danh phê duyệt')
(ROOT/'index.html').write_text(base)
# BOM CSV audit trail, with sanitized source summaries only.
buf=io.StringIO();w=csv.writer(buf);w.writerow(['Ô nguồn','Nội dung nguồn đã khử định danh','Xử lý','Mã công việc','Ghi chú'])
for a in audit:w.writerow([a['cell'],a['summary'],a['action'],', '.join(a['taskIds']),a['notes']])
(ROOT/'docs/bang-doi-chieu.csv').write_text('\ufeff'+buf.getvalue())
counts=collections.Counter(a['action'] for a in audit)
report=['# Báo cáo nâng cấp Organic Việt Nam','', '## Nguồn và phạm vi','', 'Đã đọc HTML gốc (bản Downloads trùng bản repo) và toàn bộ ô có nội dung trong Sheet1 của Excel vận hành. Có 48 dòng nhiệm vụ tại cột B, 9 nhóm có nội dung, mục 10 trống. Bảng đối chiếu lưu nội dung đã khử định danh và tham chiếu ô; không nhập tên cá nhân.','', '## Số liệu','',f'- Trước: 18 bộ phận, 187 công việc.',f'- Sau: {len(data)} bộ phận, {len(byid)} công việc.',f'- Bổ sung thực sự: {len(added)} công việc; {sum(byid[i]["source"]=="Excel bộ phận vận hành" for i in added)} từ Excel, còn lại theo đặc tả nâng cấp.',f'- Mở rộng: {len(expanded)} công việc cũ; giữ nguyên ID và tên nhiệm vụ cũ.', '- 0 dòng Excel được bỏ qua vì đã đầy đủ: các dòng có tương đương đều cần thêm đầu ra, phạm vi hoặc trạng thái xác minh.',f'- {sum(a["action"] in ["Mở rộng công việc hiện có","Mở rộng và thêm công việc con"] for a in audit)} dòng Excel có liên hệ công việc cũ được mở rộng; không tạo thêm bản sao cho cùng đầu ra.', '- 2 hạng mục cần làm rõ: B12 (DNA), A68 (mục 10 trống).', '- Các nội dung pháp lý, tài sản, phân quyền và bổ nhiệm còn phải xác minh/phê duyệt được ghi trong từng nhiệm vụ, độc lập với tiến độ checklist.','', '## Các quyết định xử lý nguồn','', '- Không nhập hạn mức trong Excel như quy định chính thức. Nhiệm vụ 05-07 ở trạng thái Chờ phê duyệt, tham chiếu B18.', '- Không nhập tên cá nhân ở B16 và B26; thay bằng nội dung công việc theo chức danh/chủ sở hữu cần xác minh.', '- B30 không đủ căn cứ ghi vốn chủ sở hữu: tách rà soát phương án pháp lý và ghi nhận theo bản chất giao dịch.', '- B22 mô tả hỗ trợ khởi động, không trao quyền điều hành thường xuyên cho HĐQT.', '- Domain/tên miền ở B52 hợp nhất một khái niệm; B57 chuẩn hóa lỗi chữ theo ngữ cảnh, ghi rõ trong đối chiếu.', '- Tất cả chức danh chịu trách nhiệm mặc định Chưa phân công. Chức danh đề xuất trong ghi chú không phải quyết định bổ nhiệm.','', '## Giao diện và chức năng','', '- Giữ bố cục sidebar/dashboard, nhận diện xanh và 18 nhóm. Bổ sung chỉ số chưa hoàn thành, chưa phân công, chờ phê duyệt, cơ cấu P0/P1/P2.', '- Bộ lọc khối, bộ phận, nghiệp vụ, mức ưu tiên, tiến độ, giai đoạn và phê duyệt; tìm kiếm cả mã, đầu ra, mô tả, chức danh và nguồn.', '- Chi tiết thu gọn có đầu ra, chủ trì, phối hợp, nguồn, mô tả và ghi chú. Tiến độ không đồng nghĩa phê duyệt chính sách.', '- Giữ nguyên khóa ovn-company-tasks-v1 và tất cả ID cũ; không migration, không tự ghi đè khi khởi động; không xóa khóa không nhận diện.', '- CSV toàn bộ danh mục có UTF-8 BOM, escape dấu nháy và chặn giá trị giống công thức. In toàn bộ danh mục A4, mở chi tiết, độc lập bộ lọc.', '', '## Danh mục theo bộ phận','']
for d in data:
 report+=['### '+d['id']+'. '+d['name']+f' — {len(d["tasks"])} công việc','']
 report += ['- '+t['id']+' — '+t['title']+(' (mới)' if t['id'] in added else ' (mở rộng)' if t['id'] in expanded else '') for t in d['tasks']];report+=['']
(ROOT/'docs/bao-cao-thay-doi.md').write_text('\n'.join(report))
print('Tasks:',len(byid),'Added:',len(added),'Expanded:',len(expanded),'Audit:',len(audit),'Actions:',dict(counts))
