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
