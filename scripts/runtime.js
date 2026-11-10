const colors={governance:['#5d60be','#eeefff'],production:['#16825a','#e3f8eb'],operations:['#bc7b1b','#fff4df'],commercial:['#167fae','#e4f4fc']};
const state={group:'all',department:'all',category:'all',priority:'all',status:'all',phase:'all',approval:'all',search:'',open:new Set(),details:new Set()};
const STORAGE_KEY='ovn-company-tasks-v1';
let completed={},storageWritable=true,storageMessage='';
try{
 const raw=localStorage.getItem(STORAGE_KEY),saved=JSON.parse(raw||'{}');
 if(!saved||typeof saved!=='object'||Array.isArray(saved))throw Error('invalid');
 completed=saved;
}catch(e){storageWritable=false;storageMessage='Không đọc được dữ liệu tiến độ đã lưu. Dữ liệu cũ được giữ nguyên; thay đổi trong phiên này chưa được lưu. Hãy sao lưu dữ liệu trình duyệt trước khi xử lý.';}
const $=id=>document.getElementById(id),esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const allTasks=DATA.flatMap(d=>d.tasks),departmentNames=Object.fromEntries(DATA.map(d=>[d.id,d.name]));
const isDone=t=>completed[t.id]===true;
const normalize=s=>String(s).normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/đ/g,'d').replace(/Đ/g,'D').toLocaleLowerCase('vi');
function showStorageNotice(){const n=$('storageNotice');n.textContent=storageMessage;n.classList.toggle('hidden',!storageMessage);}
function updateStats(){
 allTasks.forEach(t=>t.status=isDone(t)?'done':'todo');
 const n=allTasks.filter(isDone).length,pct=allTasks.length?Math.round(n/allTasks.length*100):0;
 $('groupTotal').textContent=new Set(DATA.map(d=>d.group)).size;$('deptTotal').textContent=DATA.length;$('taskTotal').textContent=allTasks.length;$('doneTotal').textContent=n;$('todoTotal').textContent=allTasks.length-n;
 $('unassignedTotal').textContent=allTasks.filter(t=>t.responsibleRole==='Chưa phân công').length;
 $('approvalTotal').textContent=allTasks.filter(t=>t.approvalStatus==='Chờ phê duyệt').length;
 for(const p of ['P0','P1','P2'])$('count'+p).textContent=allTasks.filter(t=>t.priority===p).length;
 $('percent').textContent=pct+'%';$('progressText').textContent=n+' / '+allTasks.length+' công việc hoàn thành';$('progressBar').style.width=pct+'%';
 showStorageNotice();
}
function matchesTask(d,t){
 const q=normalize(state.search.trim());
 const text=normalize([t.id,d.name,d.roles,t.title,t.description,t.category,t.responsibleRole,t.deliverable,t.source,t.notes,...t.collaboratingDepartments.map(id=>departmentNames[id])].join(' '));
 return(state.group==='all'||d.group===state.group)&&(state.department==='all'||d.id===state.department)&&(state.category==='all'||t.category===state.category)&&(state.priority==='all'||t.priority===state.priority)&&(state.phase==='all'||String(t.phase)===state.phase)&&(state.approval==='all'||t.approvalStatus===state.approval)&&(!q||text.includes(q))&&(state.status==='all'||(state.status==='done')===isDone(t));
}
function visibleDepartments(){return DATA.map(d=>({...d,shown:d.tasks.filter(t=>matchesTask(d,t))})).filter(d=>d.shown.length);}
function metadata(t){
 const collab=t.collaboratingDepartments.map(id=>departmentNames[id]).join('; ')||'Chưa xác định';
 return `<dl class="taskmeta"><div><dt>Chức danh chủ trì</dt><dd>${esc(t.responsibleRole)}</dd></div><div><dt>Bộ phận phối hợp</dt><dd>${esc(collab)}</dd></div><div class="wide"><dt>Kết quả bàn giao</dt><dd>${esc(t.deliverable)}</dd></div><div class="wide"><dt>Phạm vi thực hiện</dt><dd>${esc(t.description)}</dd></div><div><dt>Nhóm nghiệp vụ</dt><dd>${esc(t.category)}</dd></div><div><dt>Giai đoạn tham chiếu</dt><dd>${esc(t.phase)}</dd></div><div><dt>Phê duyệt chính sách</dt><dd>${esc(t.approvalStatus)}</dd></div><div><dt>Nguồn nội dung</dt><dd>${esc(t.source)}</dd></div><div class="wide"><dt>Ghi chú và căn cứ</dt><dd>${esc(t.notes)}</dd></div></dl>`;
}
function taskMarkup(t,print=false){
 const done=isDone(t),approval=t.approvalStatus!=='Không áp dụng'?`<span class="approval ${t.approvalStatus==='Cần xác minh'?'verify':''}">${esc(t.approvalStatus)}</span>`:'';
 if(print)return `<section class="print-task"><h4>${esc(t.id)} · ${esc(t.title)}</h4><p>${esc(t.priority)} · ${done?'Đã hoàn thành':'Chưa hoàn thành'} · ${esc(t.approvalStatus)}</p>${metadata(t)}</section>`;
 return `<section class="taskcard ${done?'done':''}"><div class="taskline"><input type="checkbox" data-task="${esc(t.id)}" id="task-${esc(t.id)}" ${done?'checked':''}><div class="taskname"><span class="taskcode">${esc(t.id)}</span><label for="task-${esc(t.id)}">${esc(t.title)}</label></div><span class="priority ${esc(t.priority)}">${esc(t.priority)}</span></div><div class="tasksummary"><span>${esc(t.responsibleRole)}</span>${approval}<span class="completion">${done?'✓ Hoàn thành':'Chưa hoàn thành'}</span></div><details data-detail="${esc(t.id)}" ${state.details.has(t.id)?'open':''}><summary>Đầu ra, phối hợp và căn cứ</summary>${metadata(t)}</details></section>`;
}
function render(){
 updateStats();const list=visibleDepartments(),count=list.reduce((n,d)=>n+d.shown.length,0);
 $('departmentGrid').innerHTML=list.length?list.map(d=>{
 const [color,soft]=colors[d.group];
 return `<article class="dept ${state.open.has(d.id)?'expanded':''}" style="--accent:${color};--soft:${soft}"><button type="button" class="depthead" data-toggle="${esc(d.id)}" aria-expanded="${state.open.has(d.id)}" aria-controls="dept-body-${esc(d.id)}"><span class="symbol" aria-hidden="true">${d.emoji}</span><span class="dtitle"><strong>${esc(d.id)}. ${esc(d.name)}</strong><span class="deptdesc">${esc(d.desc)}</span></span><span class="count">${d.shown.length} / ${d.tasks.length} việc</span><span class="chevron" aria-hidden="true">⌄</span></button><div class="body" id="dept-body-${esc(d.id)}"><div class="roles"><b>Cơ cấu đề xuất, chưa phải phân công:</b> ${esc(d.roles)}</div>${d.shown.map(t=>taskMarkup(t)).join('')}</div></article>`;
 }).join(''):'<div class="empty">Không có công việc phù hợp. Hãy điều chỉnh bộ lọc hoặc chọn Đặt lại.</div>';
 $('resultCount').textContent=`Hiển thị ${count} / ${allTasks.length} công việc · ${list.length} / ${DATA.length} bộ phận. Tiến độ dashboard tính trên toàn bộ danh mục.`;
 $('expandBtn').textContent=list.length&&list.every(d=>state.open.has(d.id))?'Thu gọn tất cả':'Mở tất cả';
}
function saveCompletion(id,checked){
 completed[id]=checked;
 if(storageWritable){try{localStorage.setItem(STORAGE_KEY,JSON.stringify(completed));}catch(e){storageMessage='Không lưu được tiến độ trên trình duyệt. Thay đổi hiện chỉ giữ trong phiên này; dữ liệu lưu trước đó không bị xóa.';}}
}
$('departmentGrid').addEventListener('click',e=>{const h=e.target.closest('[data-toggle]');if(h){const id=h.dataset.toggle;state.open.has(id)?state.open.delete(id):state.open.add(id);render();document.querySelector(`[data-toggle="${id}"]`)?.focus();}});
$('departmentGrid').addEventListener('toggle',e=>{const id=e.target.dataset?.detail;if(id){e.target.open?state.details.add(id):state.details.delete(id);}},true);
$('departmentGrid').addEventListener('change',e=>{const id=e.target.dataset.task;if(id&&allTasks.some(t=>t.id===id)){saveCompletion(id,e.target.checked);render();document.querySelector(`[data-task="${id}"]`)?.focus();}});
function updateNav(){document.querySelectorAll('[data-filter]').forEach(b=>{b.classList.toggle('active',b.dataset.filter===state.group);b.setAttribute('aria-pressed',String(b.dataset.filter===state.group));});}
function revealResults(){if(state.search.trim()||['department','category','priority','status','phase','approval'].some(k=>state[k]!=='all'))visibleDepartments().forEach(d=>state.open.add(d.id));}
$('search').addEventListener('input',e=>{state.search=e.target.value;revealResults();render();});
for(const [id,key] of [['groupSelect','group'],['departmentSelect','department'],['categorySelect','category'],['prioritySelect','priority'],['statusSelect','status'],['phaseSelect','phase'],['approvalSelect','approval']]){
 $(id).addEventListener('change',e=>{state[key]=e.target.value;updateNav();revealResults();render();});
}
function options(values){return values.map(([v,label])=>`<option value="${esc(v)}">${esc(label)}</option>`).join('');}
$('departmentSelect').innerHTML='<option value="all">Tất cả bộ phận</option>'+options(DATA.map(d=>[d.id,d.id+'. '+d.name]));
$('categorySelect').innerHTML='<option value="all">Mọi nhóm nghiệp vụ</option>'+options([...new Set(allTasks.map(t=>t.category))].map(c=>[c,c]));
$('phaseSelect').innerHTML='<option value="all">Mọi giai đoạn</option>'+options([...new Set(allTasks.map(t=>t.phase))].sort().map(p=>[String(p),'Giai đoạn '+p]));
$('approvalSelect').innerHTML='<option value="all">Mọi trạng thái phê duyệt</option>'+options([...new Set(allTasks.map(t=>t.approvalStatus))].sort().map(a=>[a,a]));
document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{state.group=b.dataset.filter;$('groupSelect').value=state.group;updateNav();revealResults();render();document.querySelector('.filters').scrollIntoView({behavior:'smooth',block:'start'});}));
$('resetBtn').addEventListener('click',()=>{for(const k of ['group','department','category','priority','status','phase','approval'])state[k]='all';state.search='';$('search').value='';for(const id of ['groupSelect','departmentSelect','categorySelect','prioritySelect','statusSelect','phaseSelect','approvalSelect'])$(id).value='all';updateNav();render();});
$('expandBtn').addEventListener('click',()=>{const visible=visibleDepartments(),full=visible.every(d=>state.open.has(d.id));visible.forEach(d=>full?state.open.delete(d.id):state.open.add(d.id));render();});
function preparePrint(){
 $('printCatalogue').innerHTML='<h2>Công ty Cổ phần Tập đoàn Organic Việt Nam</h2><h3>Danh mục đầy đủ · '+allTasks.length+' công việc / '+DATA.length+' bộ phận</h3><p>Chức danh và chính sách chưa được xác nhận phê duyệt. Tích hoàn thành chỉ phản ánh tiến độ thực hiện.</p>'+DATA.map(d=>`<section class="print-department"><h3>${esc(d.id)}. ${esc(d.name)}</h3>${d.tasks.map(t=>taskMarkup(t,true)).join('')}</section>`).join('');
}
window.addEventListener('beforeprint',preparePrint);
$('printBtn').addEventListener('click',()=>{preparePrint();window.print();});
function csvCell(value){let s=String(value??'');if(/^[\s\u0000-\u001f\u007f]*[=+@-]/.test(s))s="'"+s;return '"'+s.replace(/"/g,'""')+'"';}
function exportCSV(){
 const rows=[['Mã công việc','Bộ phận','Nhóm công việc','Nội dung','Chức danh chịu trách nhiệm','Bộ phận phối hợp','Kết quả bàn giao','Mức độ ưu tiên','Giai đoạn','Trạng thái','Trạng thái phê duyệt','Nguồn dữ liệu']];
 DATA.forEach(d=>d.tasks.forEach(t=>rows.push([t.id,d.name,t.category,t.title,t.responsibleRole,t.collaboratingDepartments.map(id=>departmentNames[id]).join('; '),t.deliverable,t.priority,t.phase,isDone(t)?'Hoàn thành':'Chưa hoàn thành',t.approvalStatus,t.source])));
 return '\ufeff'+rows.map(r=>r.map(csvCell).join(',')).join('\r\n');
}
$('csvBtn').addEventListener('click',()=>{const blob=new Blob([exportCSV()],{type:'text/csv;charset=utf-8;'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='organicvn-danh-muc-cong-viec.csv';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);});
updateNav();render();
