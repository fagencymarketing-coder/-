const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const base = 'file://'+process.cwd()+'/site-prototype-v44.html';
  // desktop screenshot
  let p = await b.newPage({ viewport:{width:1280,height:900}, deviceScaleFactor:1 });
  await p.goto(base,{waitUntil:'load'}); await p.waitForTimeout(1000);
  const ov = await p.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth+1);
  console.log('desktop overflow=', ov, 'scrollW=', await p.evaluate(()=>document.documentElement.scrollWidth));
  await p.screenshot({path:'v44-desk.png', fullPage:true});
  // mobile screenshot
  let m = await b.newPage({ viewport:{width:390,height:844}, deviceScaleFactor:2 });
  await m.goto(base,{waitUntil:'load'}); await m.waitForTimeout(1000);
  const ovm = await m.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth+1);
  console.log('mobile overflow=', ovm, 'scrollW=', await m.evaluate(()=>document.documentElement.scrollWidth));
  await m.screenshot({path:'v44-mob.png', fullPage:true});
  // PDF
  let pp = await b.newPage({ viewport:{width:1280,height:900}, deviceScaleFactor:2 });
  await pp.goto(base,{waitUntil:'load'});
  await pp.emulateMedia({media:'screen'}); await pp.waitForTimeout(1000);
  const H = await pp.evaluate(()=>document.body.scrollHeight);
  await pp.pdf({path:'Saturn-prototype-v44.pdf', width:'1280px', height:H+'px', printBackground:true, pageRanges:'1'});
  console.log('pdf H=',H);
  await b.close();
})();
