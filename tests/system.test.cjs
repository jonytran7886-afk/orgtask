const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),cp=require('node:child_process');
const html=fs.readFileSync('index.html','utf8');
const baseline=cp.execFileSync('git',['show','fd9c2a7:index.html'],{encoding:'utf8'});
function load(saved='{}',blocked=false){
 const elements=new Map();
 const element=id=>{if(!elements.has(id))elements.set(id,{id,value:'all',style:{},dataset:{},textContent:'',innerHTML:'',classList:{toggle(){}},addEventListener(){},setAttribute(){},scrollIntoView(){}});return elements.get(id)};
 const store={'ovn-company-tasks-v1':saved};
 const context=vm.createContext({console,Set,Blob,URL,setTimeout,document:{getElementById:element,querySelectorAll:()=>[],querySelector:()=>element('filters'),body:{appendChild(){}},createElement:()=>({click(){},remove(){}})},window:{print(){},addEventListener(){}},localStorage:{getItem(k){if(blocked)throw Error('blocked');return store[k]??null},setItem(k,v){if(blocked)throw Error('blocked');store[k]=v}}});
 for(const m of html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g))vm.runInContext(m[1],context);
 return {run:code=>vm.runInContext(code,context),store,elements};
}
test('all original tasks retain IDs and departments; every task has complete metadata',()=>{
 const app=load(),old=JSON.parse(baseline.match(/const DATA=(\[.*?\]);/s)[1]);
 assert.equal(app.run('DATA.length'),18);
 for(const d of old)for(const t of d.tasks)assert.equal(app.run(`DATA.find(d=>d.id===${JSON.stringify(d.id)}).tasks.filter(t=>t.id===${JSON.stringify(t.id)}).length`),1);
 assert.equal(app.run('new Set(allTasks.map(t=>t.id)).size'),app.run('allTasks.length'));
 assert.equal(app.run('allTasks.every(t=>t.title&&t.deliverable&&t.departmentId&&t.category&&t.source&&t.responsibleRole&&Array.isArray(t.collaboratingDepartments))'),true);
});
test('old completion persists and new tasks default to pending',()=>{
 const app=load('{"01-01":true,"unknown-id":true}');
 assert.equal(app.run('completed["01-01"]'),true);
 assert.equal(app.elements.get('doneTotal').textContent,1);
 assert.equal(app.run('allTasks.filter(t=>!'+JSON.stringify([...JSON.parse(baseline.match(/const DATA=(\[.*?\]);/s)[1]).flatMap(d=>d.tasks.map(t=>t.id))])+'.includes(t.id)).every(t=>!completed[t.id])'),true);
 assert.equal(app.store['ovn-company-tasks-v1'],'{"01-01":true,"unknown-id":true}');
});
test('CSV neutralizes formulas including control whitespace and escapes quotes',()=>{
 const app=load();
 for(const input of ['=1+1',' +SUM(A1)','\t@SUM(1)','\r-1','\n=2'])assert.match(app.run(`csvCell(${JSON.stringify(input)})`),/^"'/);
 assert.equal(app.run('csvCell(\'a"b,c\')'),'"a""b,c"');
});
test('malformed or blocked storage never crashes or overwrites existing data',()=>{
 for(const input of ['null','[]','"bad"','{bad']){const app=load(input);assert.equal(app.run('Object.keys(completed).length'),0);assert.equal(app.store['ovn-company-tasks-v1'],input)}
 assert.doesNotThrow(()=>load('{}',true));
});
test('multiple filters intersect and search includes deliverables and IDs',()=>{
 const app=load();
 assert.equal(app.run(`(()=>{const d=DATA[0],t=d.tasks[0];Object.assign(state,{department:d.id,category:t.category,phase:String(t.phase),approval:t.approvalStatus,priority:t.priority,search:t.id});return matchesTask(d,t)})()`),true);
 assert.equal(app.run('matchesTask(DATA[1],DATA[1].tasks[0])'),false);
});
test('capital and budget decisions remain pending approval',()=>{
 const app=load();
 for(const id of ['01-04','01-06','05-08','12-05'])assert.equal(app.run(`allTasks.find(t=>t.id==='${id}').approvalStatus`),'Chờ phê duyệt');
});
test('new brief-only tasks have accurate source and full print names the company',()=>{
 const app=load();assert.equal(app.run('allTasks.find(t=>t.id==="16-14").source'),'Đặc tả nâng cấp');
 app.run('preparePrint()');assert.match(app.elements.get('printCatalogue').innerHTML,/Công ty Cổ phần Tập đoàn Organic Việt Nam/);
});
test('business categories group asset work across departments; all source rows mapped once',()=>{
 const app=load();
 assert.equal(app.run('new Set(["06-11","07-04","03-15"].map(id=>allTasks.find(t=>t.id===id).category)).size'),1);
 const audit=JSON.parse(fs.readFileSync('docs/doi-chieu.json','utf8'));
 assert.equal(audit.filter(a=>/!B/.test(a.cell)).length,48);
 assert.equal(new Set(audit.map(a=>a.cell)).size,49);
 for(const a of audit)for(const id of a.taskIds)assert.equal(app.run(`allTasks.some(t=>t.id===${JSON.stringify(id)})`),true);
});
test('accounting tasks retain split IDs; departments outside legal, HR and accounting remain unchanged',()=>{
 const app=load();
 const expected={'06-05':'Theo dõi, kiểm soát nhập – xuất – tồn kho','06-08':'Kiểm tra, đối chiếu bảng lương và thực hiện thanh toán lương','06-14':'Theo dõi và quản lý công nợ phải thu, phải trả','06-15':'Kiểm tra chứng từ và thực hiện thanh toán cho nhà cung cấp'};
 for(const [id,title] of Object.entries(expected))assert.equal(app.run(`allTasks.find(t=>t.id==='${id}')?.title`),title);
 assert.equal(app.run('DATA.find(d=>d.id==="06").tasks.length'),18);
 assert.equal(app.run('allTasks.length'),240);
 const previous=JSON.parse(cp.execFileSync('git',['show','2f775c3:index.html'],{encoding:'utf8'}).match(/const DATA=(\[.*?\]);/s)[1]);
 assert.deepEqual(JSON.parse(app.run('JSON.stringify(DATA.filter(d=>!["03","04","06"].includes(d.id)))')),previous.filter(d=>!['03','04','06'].includes(d.id)));
 const debt=app.run('JSON.stringify(allTasks.find(t=>t.id==="06-14"))');
 for(const detail of ['khách hàng','hợp đồng','hạn thanh toán','nhà cung cấp','đến hạn','xác nhận công nợ','tuổi nợ','quá hạn','cảnh báo rủi ro','thu hồi công nợ'])assert.ok(debt.includes(detail),detail);
});
test('split keeps old completions without marking new responsibilities complete',()=>{
 const app=load('{"06-05":true,"06-08":true,"06-13":true}');
 assert.equal(app.run('allTasks.find(t=>t.id==="06-05").status'),'done');
 assert.equal(app.run('allTasks.find(t=>t.id==="06-08").status'),'done');
 assert.equal(app.run('allTasks.find(t=>t.id==="06-14")?.status'),'todo');
 assert.equal(app.run('allTasks.find(t=>t.id==="06-15")?.status'),'todo');
 app.run('saveCompletion("06-14",true)');
 const saved=JSON.parse(app.store['ovn-company-tasks-v1']);
 assert.deepEqual(saved,{'06-05':true,'06-08':true,'06-13':true,'06-14':true});
});
test('HR supplement covers 16 source items with stable IDs and clear payroll/tax coordination',()=>{
 const app=load(),previous=JSON.parse(cp.execFileSync('git',['show','2f775c3:index.html'],{encoding:'utf8'}).match(/const DATA=(\[.*?\]);/s)[1]);
 assert.equal(app.run('DATA.find(d=>d.id==="04").tasks.length'),28);
 assert.equal(app.run('allTasks.length'),240);
 for(const t of previous.find(d=>d.id==='04').tasks)assert.equal(app.run(`DATA.find(d=>d.id==='04').tasks.filter(t=>t.id==='${t.id}').length`),1);
 const coverage=JSON.parse(fs.readFileSync('docs/doi-chieu-hcns.json','utf8'));
 assert.deepEqual(coverage.map(x=>x.item),Array.from({length:16},(_,i)=>i+1));
 for(const item of coverage)for(const id of item.taskIds)assert.equal(app.run(`allTasks.some(t=>t.id==='${id}')`),true);
 assert.equal(app.run('allTasks.find(t=>t.id==="04-17").description.includes("06-08")'),true);
 const insurance=app.run('JSON.stringify(allTasks.find(t=>t.id==="04-05"))');
 for(const term of ['BHXH','BHYT','BHTN'])assert.ok(insurance.includes(term));
 const taxes=app.run('JSON.stringify(allTasks.find(t=>t.id==="04-18"))');
 for(const term of ['TNCN','TNDN','06-07'])assert.ok(taxes.includes(term));
 for(let n=17;n<=28;n++)assert.equal(app.run(`allTasks.find(t=>t.id==='04-${n}').source`),'Ảnh bổ sung HCNS');
});
test('existing HR checklist persists and added HR tasks start incomplete',()=>{
 const app=load('{"04-05":true,"04-08":true,"06-08":true}');
 for(const id of ['04-05','04-08','06-08'])assert.equal(app.run(`allTasks.find(t=>t.id==='${id}').status`),'done');
 assert.equal(app.run('DATA.find(d=>d.id==="04").tasks.filter(t=>Number(t.id.slice(3))>=17).length'),12);
 assert.equal(app.run('DATA.find(d=>d.id==="04").tasks.filter(t=>Number(t.id.slice(3))>=17).every(t=>t.status==="todo")'),true);
});
test('legal supplement adds six distinct tasks with exact priorities and preserves legacy checklist',()=>{
 const app=load('{"03-01":true,"03-17":true,"07-01":true}');
 assert.equal(app.run('DATA.find(d=>d.id==="03").tasks.length'),23);
 assert.equal(app.run('allTasks.length'),240);
 const source=JSON.parse(fs.readFileSync('scripts/legal-supplement.json','utf8'));
 assert.equal(source.length,6);
 source.forEach((t,i)=>{
  assert.equal(t.id,'03-'+(18+i));
  assert.equal(app.run(`allTasks.find(t=>t.id==='${t.id}')?.title`),t.title);
  assert.equal(app.run(`allTasks.find(t=>t.id==='${t.id}')?.priority`),i<2?'P0':'P1');
  assert.equal(app.run(`allTasks.find(t=>t.id==='${t.id}')?.status`),'todo');
  assert.equal(app.run(`allTasks.find(t=>t.id==='${t.id}')?.source`),'Ảnh bổ sung Pháp chế – Tuân thủ');
 });
 for(const id of ['03-01','03-17','07-01'])assert.equal(app.run(`allTasks.find(t=>t.id==='${id}').status`),'done');
 assert.equal(app.run('allTasks.find(t=>t.id==="03-18").description.includes("07-01")'),true);
 assert.equal(app.run('allTasks.find(t=>t.id==="03-23").description.includes("07-06")'),true);
});
test('accounting supplement adds three tasks with priorities P0/P1/P1 and keeps prior checklist',()=>{
 const app=load('{"06-04":true,"06-06":true,"06-07":true,"06-15":true}');
 assert.equal(app.run('DATA.find(d=>d.id==="06").tasks.length'),18);
 assert.equal(app.run('allTasks.length'),240);
 const source=JSON.parse(fs.readFileSync('scripts/accounting-supplement.json','utf8'));
 assert.equal(source.length,3);
 source.forEach((t,i)=>{
  assert.equal(t.id,'06-'+(16+i));
  assert.equal(app.run(`allTasks.find(t=>t.id==='${t.id}')?.title`),t.title);
  assert.equal(app.run(`allTasks.find(t=>t.id==='${t.id}')?.priority`),i===0?'P0':'P1');
  assert.equal(app.run(`allTasks.find(t=>t.id==='${t.id}')?.status`),'todo');
  assert.equal(app.run(`allTasks.find(t=>t.id==='${t.id}')?.source`),'Ảnh bổ sung Kế toán – Thuế');
 });
 for(const id of ['06-04','06-06','06-07','06-15'])assert.equal(app.run(`allTasks.find(t=>t.id==='${id}').status`),'done');
 for(const [id,reference] of [['06-16','06-06'],['06-17','06-07'],['06-18','06-04']])assert.equal(app.run(`allTasks.find(t=>t.id==='${id}').description.includes('${reference}')`),true);
});
