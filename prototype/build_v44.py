import json, os
# Ассеты (лого/иконки в base64) ищем сначала рядом со скриптом в build-assets/,
# иначе — в /tmp (как в исходной сессии). Это делает сборку самодостаточной.
_BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build-assets')
def _asset(name):
    p = os.path.join(_BASE, name)
    return p if os.path.exists(p) else os.path.join('/tmp', name)
logo_white = open(_asset('logo_datauri.txt')).read().strip()
logo_color = open(_asset('logo_color.txt')).read().strip()
d=json.load(open(_asset('icons.json')))
ic=[x['svg'] for x in d['icons']]; szr=[x['svg'] for x in d['szr']]
IC={'udobreniya':ic[0],'szr':ic[1],'semena':ic[2],'agro':ic[3],'diagnostika':ic[4],
    'zernovye':ic[5],'zernobob':ic[6],'kukuruza':ic[7],'podsolnechnik':ic[8],
    'zashita':szr[0],'gerbicid':szr[1],'fungicid':szr[2],'insekticid':szr[3],'protravitel':szr[4]}
def icon(slug,size=44):
    return f'<svg class="ic" viewBox="0 0 96 96" width="{size}" height="{size}" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">{IC[slug]}</svg>'

CSS = r'''<style>
:root{
  --ink:#141210; --ink-soft:#1E1A16; --panel-d:#241F1A;
  --paper:#FAF8F4; --paper-2:#F1ECE4; --paper-3:#F6F1E9; --white:#fff;
  --text-d:#F4EEE7; --muted-d:#B9ADA2; --muted-d2:#8A8078;
  --text-l:#17130F; --muted-l:#726657; --line-l:#E7DFD3;
  --line-d:rgba(255,255,255,.10); --line-d2:rgba(255,255,255,.16);
  --orange:#EE4A0E; --orange-deep:#C43C08; --orange-soft:#FFB48F;
  --green:#2E8B57; --green-deep:#1F6B41; --green-light:#43C47D; --green-soft:#8CDCAE;
  --green-bg:#EAF3EC;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--text-l);font-family:"IBM Plex Sans",system-ui,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3{font-family:"Archivo",sans-serif;margin:0;line-height:1.08;letter-spacing:-.01em}
a{color:inherit;text-decoration:none}
img{max-width:100%}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.ic{color:var(--orange);display:block}
.eyebrow{font-family:"IBM Plex Mono";font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--orange-deep);font-weight:600}
.sec--dark .eyebrow{color:var(--orange-soft)}
.sec-h{font-family:"Archivo";font-weight:800;font-size:clamp(24px,3.2vw,36px);margin-top:10px;letter-spacing:-.02em}
.sec-lead{margin-top:12px;max-width:64ch;font-size:16px}
.sec--light .sec-lead{color:var(--muted-l)} .sec--dark .sec-lead{color:var(--muted-d)}
.btn{display:inline-flex;align-items:center;gap:8px;font-weight:700;font-size:15px;border-radius:11px;padding:13px 22px;border:1.5px solid transparent;cursor:pointer;transition:.15s}
.btn.o{background:var(--orange);color:#fff}.btn.o:hover{background:var(--orange-deep)}
.btn.g{background:var(--green);color:#fff}.btn.g:hover{background:var(--green-deep)}
.btn.sm{padding:9px 15px;font-size:13px;border-radius:9px}
.sec--light .btn.ghost{background:transparent;color:var(--text-l);border-color:var(--line-l)}
.sec--light .btn.ghost:hover{border-color:var(--muted-l)}
.sec--dark .btn.ghost{background:transparent;color:var(--text-d);border-color:var(--line-d2)}
.btn.ghost-w{background:transparent;color:#fff;border-color:rgba(255,255,255,.5)}
.btn.ghost-w:hover{background:rgba(255,255,255,.1)}

/* header */
.hdr{position:sticky;top:0;z-index:40;background:rgba(20,16,12,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line-d)}
.hdr .in{display:flex;align-items:center;gap:22px;height:64px}
.hdr .logo{height:30px;width:auto;aspect-ratio:1212/405;object-fit:contain}
.nav{display:flex;gap:20px;margin-left:8px}
.nav a{color:var(--muted-d);font-size:14px;font-weight:500;white-space:nowrap}
.nav a:hover{color:var(--text-d)}
.hdr .right{margin-left:auto;display:flex;align-items:center;gap:16px}
.hdr .tel{color:var(--text-d);font-weight:700;font-size:15px;font-family:"IBM Plex Mono";white-space:nowrap}
.hdr .burger{display:none}

/* hero (dark, brown-graphite + orange) */
.hero{position:relative;overflow:hidden;padding:56px 0 72px;background:linear-gradient(105deg,#14100c 0%,#1f1710 40%,#7d2c08 92%,var(--orange-deep) 122%);color:var(--text-d)}
.hero .bg-art{position:absolute;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}
.hero .bg-mob{display:none}
.hero::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(0deg,rgba(20,16,12,.5),transparent 55%)}
.hero .in{position:relative;z-index:2;max-width:900px}
.status{display:inline-flex;align-items:center;gap:9px;font-family:"IBM Plex Mono";font-size:12px;letter-spacing:.05em;text-transform:uppercase;color:var(--green-soft);background:rgba(46,139,87,.16);border:1px solid rgba(46,139,87,.45);padding:6px 13px;border-radius:30px}
.status span{width:8px;height:8px;border-radius:50%;background:var(--green-light);display:block}
.hero h1{font-size:clamp(30px,4.6vw,52px);font-weight:900;margin:18px 0 0;letter-spacing:-.02em}
.hero h1 .accent{color:var(--orange-soft)}
.hero p.sub{color:#EBE0D6;margin:18px 0 0;font-size:18px;max-width:56ch}
.hero .cta-row{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.hero .trust{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:26px;font-family:"IBM Plex Mono";font-size:13px;color:#F1E4DA}
.hero .trust .dot{width:5px;height:5px;border-radius:50%;background:var(--orange-soft);display:inline-block}

/* sections */
.sec{padding:70px 0}
.sec--light{background:var(--paper);color:var(--text-l);border-bottom:1px solid var(--line-l)}
.sec--paper2{background:var(--paper-2)}
.sec--paper3{background:var(--paper-3)}
.sec--dark{background:var(--ink);color:var(--text-d);border-bottom:1px solid var(--line-d)}
.sec-head-row{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap}

/* 5 directions */
.dirs{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:30px}
.dir{border-radius:16px;padding:22px 18px;background:var(--white);border:1px solid var(--line-l);transition:.15s;display:flex;flex-direction:column}
.dir:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(20,16,12,.08)}
.dir .ic{margin-bottom:14px}
.dir h3{font-size:17px}
.dir p{font-size:13px;color:var(--muted-l);margin:8px 0 0;flex:1}
.dir .more{margin-top:14px;font-size:13px;font-weight:700;color:var(--green-deep)}
.dir.accent{background:var(--green-bg);border-color:#CFE6D6}
.dir.accent .ic{color:var(--green)}
.dir.accent .more{color:var(--green-deep)}

/* quick подбор */
.podbor{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:28px}
.pcard{background:var(--white);border:1px solid var(--line-l);border-radius:16px;padding:26px}
.pcard .lab{font-family:"IBM Plex Mono";font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted-l);margin-bottom:14px}
.pcard h3{font-size:20px;margin-bottom:4px}
.chips3{display:flex;flex-wrap:wrap;gap:9px;margin-top:14px}
.chip3{display:inline-flex;align-items:center;gap:7px;border:1.4px solid var(--line-l);background:var(--white);border-radius:22px;padding:9px 15px;font-size:13px;font-weight:600;cursor:pointer}
.chip3 .ic{width:18px;height:18px;color:var(--green)}
.chip3.g{background:var(--green-bg);border-color:#CFE6D6;color:var(--green-deep)}
.chip3:hover{border-color:var(--green)}

/* catalog preview (популярные позиции) */
.fil .lab{font-family:"IBM Plex Mono";font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted-d2);margin:16px 0 8px}
.chip2{display:inline-flex;align-items:center;gap:8px;vertical-align:middle;border:1.4px solid var(--line-d2);border-radius:22px;padding:8px 16px;font-size:13px;margin:0 8px 8px 0;color:var(--text-d);background:rgba(255,255,255,.04);cursor:pointer}
.chip2 .ic{width:18px;height:18px}
.chip2.on{background:var(--orange);border-color:var(--orange);color:#fff;font-weight:700}
.chip2.on .ic{color:#fff}
.chip2.on.g{background:var(--green);border-color:var(--green)}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:22px}
.card{border-radius:14px;padding:16px;transition:.15s;background:var(--ink-soft);border:1px solid var(--line-d)}
.card:hover{transform:translateY(-2px)}
.card .img{height:150px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:13px;background:#EFE9E1;border:1px solid #E0D8CB;color:#8A8078}
.card h3{font-size:17px;margin:14px 0 0}
.card .meta{font-size:12.5px;margin:4px 0 0;font-family:"IBM Plex Mono";color:var(--muted-d2)}
.card .price{margin-top:10px;font-family:"Archivo";font-weight:700;font-size:15px;color:var(--orange-soft)}
.card .price small{font-family:"IBM Plex Sans";font-weight:500;color:var(--muted-d2);font-size:12px}
.card .row{display:flex;gap:8px;margin-top:14px}

/* service под ключ (steps) */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:30px}
.step{background:var(--white);border:1px solid var(--line-l);border-radius:16px;padding:24px 20px;position:relative}
.step .n{width:38px;height:38px;border-radius:11px;background:var(--green-bg);color:var(--green-deep);display:grid;place-items:center;font-family:"Archivo";font-weight:800;font-size:17px;margin-bottom:14px}
.step h3{font-size:16px}
.step p{font-size:13px;color:var(--muted-l);margin:7px 0 0}
.diag{margin-top:34px;background:var(--white);border:1px solid var(--line-l);border-left:4px solid var(--green);border-radius:16px;padding:26px 28px}
.diag h3{font-size:20px;display:flex;align-items:center;gap:12px}
.diag h3 .ic{width:28px;height:28px;color:var(--green)}
.diag .flow{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;align-items:center}
.diag .fst{font-size:13px;font-weight:600;background:var(--green-bg);color:var(--green-deep);border-radius:20px;padding:8px 14px}
.diag .arr{color:var(--muted-l);font-weight:700}

/* geography */
.geo{display:grid;grid-template-columns:1.15fr 1fr;gap:30px;margin-top:30px;align-items:center}
.geo .regions{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.region{display:flex;align-items:center;gap:11px;background:rgba(255,255,255,.04);border:1px solid var(--line-d);border-radius:11px;padding:12px 14px;font-size:14px;font-weight:500}
.region .pin{width:9px;height:9px;border-radius:50%;background:var(--green-light);flex:none;box-shadow:0 0 0 4px rgba(46,139,87,.18)}
.geo .mapbox{background:linear-gradient(135deg,#241F1A,#17130F);border:1px solid var(--line-d);border-radius:18px;min-height:300px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;color:var(--muted-d2);text-align:center;padding:26px}
.geo .mapbox .big{font-family:"Archivo";font-weight:800;font-size:52px;color:var(--green-soft)}
.geostat{display:flex;gap:26px;flex-wrap:wrap;margin-top:26px}
.geostat b{font-family:"Archivo";font-size:30px;color:var(--orange-soft);display:block;line-height:1}
.geostat span{color:var(--muted-d);font-size:13px;display:block;margin-top:6px}

/* partners */
.partners{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:28px}
.partners-3{grid-template-columns:repeat(3,1fr);max-width:820px}
.partner{background:var(--white);border:1px solid var(--line-l);border-radius:14px;height:110px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;text-align:center;padding:14px}
.partner b{font-family:"Archivo";font-size:16px;color:var(--text-l)}
.partner span{font-size:11.5px;color:var(--muted-l);font-family:"IBM Plex Mono"}

/* cases */
.cases{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:28px}
.case{background:var(--ink-soft);border:1px solid var(--line-d);border-radius:16px;padding:24px}
.case .big{font-family:"Archivo";font-weight:800;font-size:44px;color:var(--green-light);line-height:1}
.case h3{font-size:16px;margin:10px 0 0}
.case p{font-size:13.5px;color:var(--muted-d);margin:8px 0 0}
.case .who{font-family:"IBM Plex Mono";font-size:12px;color:var(--muted-d2);margin-top:12px}

/* docs */
.docs{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:28px}
.doc{background:#241F1A;border:1px solid rgba(255,255,255,.14);border-radius:12px;height:150px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:#B9ADA2;font-size:13px;text-align:center;padding:14px}
.doc .dic{font-size:32px}

/* contacts */
.cts{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-top:30px}
.person{background:var(--ink-soft);border:1px solid var(--line-d);border-radius:16px;padding:24px;display:flex;gap:18px;align-items:center}
.person .av{width:74px;height:74px;border-radius:14px;background:#EFE9E1;border:1px solid #E0D8CB;flex:none;display:grid;place-items:center;color:#8A8078;font-size:12px;text-align:center}
.person h3{font-size:18px}
.person .role{font-size:13px;color:var(--muted-d);margin-top:3px}
.person .tel{font-family:"IBM Plex Mono";font-weight:600;color:var(--orange-soft);margin-top:10px;font-size:15px}
.person .ch{font-size:13px;color:var(--muted-d);margin-top:4px}

/* form */
.form{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:24px}
.form input,.form select{background:#fff;border:1px solid var(--line-l);border-radius:11px;padding:14px;color:var(--text-l);font-size:14px;font-family:inherit}
.form input::placeholder{color:var(--muted-l)}
.form .full{grid-column:1/-1}
.form .submit{grid-column:1/-1;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.note--light{color:var(--muted-l);font-size:13px}

/* footer */
footer{background:#100d0b;padding:48px 0 60px;color:var(--muted-d)}
.fgrid{display:grid;grid-template-columns:1.5fr 1fr 1.2fr 1fr;gap:24px}
footer img{height:30px;margin-bottom:14px;aspect-ratio:1212/405;object-fit:contain}
footer .col b{display:block;font-size:14px;margin-bottom:12px;font-family:"Archivo";text-transform:uppercase;letter-spacing:.04em;color:var(--text-d)}
footer .col p,footer .col a{color:var(--muted-d);font-size:14px;margin:6px 0;display:block}
footer .copy{color:var(--muted-d2);font-size:13px;margin-top:32px;padding-top:18px;border-top:1px solid var(--line-d);font-family:"IBM Plex Mono"}

@media(max-width:980px){
  .dirs{grid-template-columns:repeat(3,1fr)}
  .geo{grid-template-columns:1fr}
  .steps{grid-template-columns:repeat(2,1fr)}
  .partners,.docs{grid-template-columns:repeat(2,1fr)}
  .cases,.cts{grid-template-columns:1fr}
  .grid{grid-template-columns:1fr 1fr}
  .nav{display:none}
  .hero .bg-art{display:none}
  .hero .bg-mob{display:block;position:absolute;top:0;right:0;width:70%;height:300px;z-index:0;pointer-events:none;-webkit-mask-image:linear-gradient(200deg,#000 0%,#000 42%,transparent 80%);mask-image:linear-gradient(200deg,#000 0%,#000 42%,transparent 80%)}
  .hero .bg-mob svg{position:absolute;inset:0;width:100%;height:100%}
}
@media(max-width:620px){
  .dirs,.podbor,.steps,.partners,.docs,.grid,.form,.fgrid,.geo .regions,.svc2,.about,.terms{grid-template-columns:1fr}
  .hero .cta-row .btn{flex:1 1 100%;justify-content:center}
  .hdr .tel{display:none}
}

/* ===== V4 доработки ===== */
.cat-note{margin-top:18px;font-size:13.5px;line-height:1.6}
.sec--light .cat-note{color:var(--muted-l)} .sec--dark .cat-note{color:var(--muted-d)}
.cat-note a{color:var(--green-deep);font-weight:700}
.sec--dark .cat-note a{color:var(--green-soft)}
/* быстрый подбор — действие */
.podbor-act{display:flex;align-items:center;gap:20px;flex-wrap:wrap;margin-top:22px}
.podbor-alt{font-size:14px;color:var(--muted-l)}
.podbor-alt a{color:var(--green-deep);font-weight:700}
/* сервис — 2 колонки */
.svc2{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:34px}
.svc{background:var(--white);border:1px solid var(--line-l);border-radius:16px;padding:26px 28px;border-top:4px solid var(--green)}
.svc h3{font-size:20px;display:flex;align-items:center;gap:12px}
.svc h3 .ic{width:26px;height:26px;color:var(--green)}
.svc p{color:var(--muted-l);font-size:14.5px;margin:10px 0 0}
.svc ul{margin:16px 0 20px;padding:0;list-style:none;display:grid;gap:9px}
.svc li{position:relative;padding-left:26px;font-size:14px;font-weight:500}
.svc li::before{content:"";position:absolute;left:0;top:7px;width:10px;height:10px;border-radius:50%;background:var(--green-bg);border:2px solid var(--green)}
/* о компании */
.about{display:grid;grid-template-columns:1.3fr 1fr;gap:34px;align-items:center}
.about-btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}
.about-facts{display:grid;gap:12px}
.af{background:rgba(255,255,255,.04);border:1px solid var(--line-d);border-radius:12px;padding:14px 18px}
.af span{font-family:"IBM Plex Mono";font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted-d2);display:block}
.af b{font-size:16px;color:var(--text-d);display:block;margin-top:4px;font-family:"Archivo"}
/* география на светлом */
.geo--light .region{background:var(--white);border:1px solid var(--line-l);color:var(--text-l)}
.geo--light .mapbox{background:linear-gradient(135deg,#241F1A,#17130F);color:var(--muted-d2)}
.geo--light .mapbox .big{color:var(--green-soft)}
.mapleg{font-size:11.5px;font-family:"IBM Plex Mono";margin-top:8px;color:var(--muted-d);line-height:1.7}
/* производители — ссылка */
.plink{display:block;margin-top:8px;font-size:12.5px;font-weight:700;color:var(--green-deep);font-family:"IBM Plex Mono"}
.partner{gap:5px}
/* условия сотрудничества */
.terms{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:28px}
.term{border-radius:14px;padding:22px 20px}
.sec--dark .term{background:var(--ink-soft);border:1px solid var(--line-d)}
.sec--light .term{background:var(--white);border:1px solid var(--line-l)}
.term .ic{margin-bottom:12px}
.term h3{font-size:16px}
.term p{font-size:13px;margin:7px 0 0}
.sec--dark .term p{color:var(--muted-d)} .sec--light .term p{color:var(--muted-l)}
/* кейсы на светлом */
.cases--light .case{background:var(--white);border:1px solid var(--line-l)}
.cases--light .case .big{color:var(--green-deep)}
.cases--light .case h3{color:var(--text-l)}
.cases--light .case p{color:var(--muted-l)}
.cases--light .case .who{color:var(--muted-l)}
@media(max-width:980px){ .terms{grid-template-columns:repeat(2,1fr)} .about{grid-template-columns:1fr;gap:26px} }
@media(max-width:620px){
  .svc2,.about,.terms{grid-template-columns:1fr}
  .podbor-act{flex-direction:column;align-items:flex-start;gap:12px}
  .podbor-act .btn{width:100%;justify-content:center}
}

/* ===== V4.4 правки ===== */
.hmail{font-family:"IBM Plex Mono";font-size:14px;font-weight:600;color:var(--text-d)}
.hmail:hover{color:var(--orange-soft)}
/* минималистичные карточки направлений */
.dir--min{align-items:flex-start;justify-content:center;min-height:150px;gap:0}
.dir--min .ic{margin-bottom:16px}
/* каталог: 3 карточки + кнопка + видимая подпись */
.grid-3{grid-template-columns:repeat(3,1fr)}
.cat-cta{margin-top:24px}
.cat-note--strong{margin-top:22px;font-size:15px;font-weight:600;color:var(--text-d);background:rgba(46,139,87,.14);border:1px solid rgba(46,139,87,.4);border-radius:12px;padding:14px 18px}
/* о компании: фото вместо панели */
.about-photo{background:#EFE9E1;border:1px solid #E0D8CB;border-radius:16px;min-height:240px;display:flex;align-items:center;justify-content:center;color:#8A8078;font-size:14px;text-align:center}
/* производители: логотипы */
.plogo-box{width:100%;height:70px;background:var(--paper-2);border:1px solid var(--line-l);border-radius:10px;display:flex;align-items:center;justify-content:center;color:var(--muted-l);font-size:12px;font-family:"IBM Plex Mono";margin-bottom:12px}
.partner b{margin-top:0}
/* контакты + форма */
.contact{display:grid;grid-template-columns:1fr 1.15fr;gap:24px;margin-top:28px;align-items:start}
.contact-people{display:grid;gap:16px}
.contact-form{background:var(--ink-soft);border:1px solid var(--line-d);border-radius:16px;padding:26px}
.cf-h{font-family:"Archivo";font-weight:800;font-size:20px;margin-bottom:16px}
.form--dark input,.form--dark select{background:rgba(255,255,255,.06);border:1px solid var(--line-d2);color:var(--text-d)}
.form--dark input::placeholder{color:var(--muted-d)}
.form--dark select{color:var(--muted-d)}
.note--dark{color:var(--muted-d);font-size:12.5px;grid-column:1/-1}
@media(max-width:900px){ .contact{grid-template-columns:1fr} .grid-3{grid-template-columns:1fr 1fr} }
@media(max-width:620px){ .grid-3{grid-template-columns:1fr} }
</style>'''

HERO_WAVES = '''<svg class="bg-art" viewBox="0 0 1440 900" preserveAspectRatio="xMaxYMax slice" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<defs><linearGradient id="g1" x1="0" y1="0" x2="0.7" y2="1"><stop offset="0" stop-color="#FF9A5A"/><stop offset="1" stop-color="#F0490F"/></linearGradient>
<linearGradient id="g2" x1="0.1" y1="0" x2="0.8" y2="1"><stop offset="0" stop-color="#F5560F"/><stop offset="1" stop-color="#C43C08"/></linearGradient>
<linearGradient id="g3" x1="0.1" y1="0" x2="0.9" y2="1"><stop offset="0" stop-color="#D53E08"/><stop offset="1" stop-color="#9A2D05"/></linearGradient></defs>
<path d="M 905,0 C 890,25 802,97 815,150 C 828,203 971,262 985,320 C 999,378 888,443 900,500 C 912,557 1015,607 1060,660 C 1105,713 1142,780 1170,820 C 1198,860 1220,887 1230,900 L 1440,900 L 1440,0 Z" fill="url(#g1)"/>
<path d="M 1120,70 C 1106,100 1022,190 1035,250 C 1048,310 1185,368 1195,430 C 1205,492 1086,558 1095,620 C 1104,682 1216,753 1250,800 C 1284,847 1292,883 1300,900 L 1440,900 L 1440,70 Z" fill="url(#g2)"/>
<path d="M 1285,230 C 1272,263 1197,367 1205,430 C 1213,493 1327,548 1335,610 C 1343,672 1253,752 1255,800 C 1257,848 1330,883 1345,900 L 1440,900 L 1440,230 Z" fill="url(#g3)"/></svg>
<div class="bg-mob"><svg viewBox="0 0 280 260" preserveAspectRatio="xMaxYMin slice" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<defs><linearGradient id="m1" x1="0" y1="0" x2="0.7" y2="1"><stop offset="0" stop-color="#FF9A5A"/><stop offset="1" stop-color="#F0490F"/></linearGradient>
<linearGradient id="m2" x1="0.1" y1="0" x2="0.8" y2="1"><stop offset="0" stop-color="#F5560F"/><stop offset="1" stop-color="#C43C08"/></linearGradient>
<linearGradient id="m3" x1="0.1" y1="0" x2="0.9" y2="1"><stop offset="0" stop-color="#D53E08"/><stop offset="1" stop-color="#9A2D05"/></linearGradient></defs>
<path d="M 120,-20 C 108,25 60,70 78,115 C 96,160 210,190 235,235 L 300,300 L 300,-40 Z" fill="url(#m1)"/>
<path d="M 175,-20 C 163,20 108,80 126,125 C 142,165 235,200 258,245 L 300,300 L 300,-40 Z" fill="url(#m2)"/>
<path d="M 225,-15 C 214,22 170,88 185,132 C 197,170 262,205 285,245 L 300,285 L 300,-30 Z" fill="url(#m3)"/></svg></div>'''

REGIONS = ["Алтайский край","Красноярский край","Новосибирская область","Омская область",
           "Амурская область","Ростовская область","Ставропольский край","Краснодарский край"]
regions_html = "".join(f'<div class="region"><span class="pin"></span>{r}</div>' for r in REGIONS)

HTML = f'''<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Сатурн · Прототип сайта V4</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
{CSS}</head><body>

<!-- HEADER -->
<header class="hdr"><div class="wrap in">
  <img class="logo" src="{logo_white}" alt="Сатурн">
  <nav class="nav">
    <a href="#catalog">Каталог</a>
    <a href="#agro">Агросопровождение</a><a href="#about">О компании</a><a href="#contacts">Контакты</a>
  </nav>
  <div class="right"><span class="tel">+7 960 953-48-88</span><a class="hmail" href="mailto:nilov@sssaturn.ru">nilov@sssaturn.ru</a></div>
</div></header>

<!-- 1. HERO (тёмный) -->
<section class="hero">{HERO_WAVES}
  <div class="wrap in">
    <h1>Семена, удобрения<br>и <span class="accent">защита растений</span><br>для сельхозпроизводителей</h1>
    <p class="sub">Подбираем решения под культуру, регион и задачи хозяйства. Организуем поставку, хранение, диагностику и агрономическое сопровождение.</p>
    <div class="cta-row">
      <a class="btn g" href="#dirs">Подобрать решение</a>
      <a class="btn ghost-w" href="#catalog">Перейти в каталог</a>
    </div>
  </div>
</section>

<!-- 2. ПЯТЬ НАПРАВЛЕНИЙ (светлый) -->
<section class="sec sec--light" id="dirs"><div class="wrap">
  <h2 class="sec-h">Пять направлений — один поставщик</h2>
  <p class="sec-lead">От диагностики поля и подбора схемы до поставки, хранения и сопровождения применения. Всё в одном месте.</p>
  <div class="dirs">
    <div class="dir dir--min">{icon('udobreniya',40)}<h3>Удобрения</h3></div>
    <div class="dir dir--min">{icon('szr',40)}<h3>СЗР</h3></div>
    <div class="dir dir--min">{icon('semena',40)}<h3>Семена</h3></div>
    <div class="dir accent">{icon('diagnostika',40)}<h3>Диагностика</h3><p>Выявление дефицитов питания и мониторинг состояния посевов.</p><span class="more">Подробнее →</span></div>
    <div class="dir accent">{icon('agro',40)}<h3>Агросопровождение</h3><p>Подбор схем, нормы применения и консультации специалистов.</p><span class="more">Подробнее →</span></div>
  </div>
</div></section>

<!-- 3. ПРОИЗВОДИТЕЛИ (светлый тёплый) -->
<section class="sec sec--paper3" id="partners"><div class="wrap">
  <h2 class="sec-h">Поставляем продукцию</h2>
  <div class="partners partners-3">
    <div class="partner"><div class="plogo-box">логотип</div><b>Фертика</b><span>минеральные удобрения</span></div>
    <div class="partner"><div class="plogo-box">логотип</div><b>Волски Биохим</b><span>питание растений</span></div>
    <div class="partner"><div class="plogo-box">логотип</div><b>Relict Organics</b><span>удобрения и СЗР</span></div>
  </div>
</div></section>

<!-- 4. ПОПУЛЯРНЫЕ ПОЗИЦИИ (тёмный, превью каталога) -->
<section class="sec sec--dark" id="catalog"><div class="wrap">
  <div class="sec-head-row">
    <h2 class="sec-h">Популярные позиции</h2>
    <a class="btn ghost">Весь каталог →</a>
  </div>
  <div class="fil">
    <span class="chip2 on">Все</span>
    <span class="chip2">{icon('udobreniya',18)}Удобрения</span>
    <span class="chip2">{icon('szr',18)}СЗР</span>
    <span class="chip2">{icon('semena',18)}Семена</span>
  </div>
  <div class="grid grid-3">
    <div class="card"><div class="img">Фото продукта</div><h3>Фертика STARTER 13-40-13</h3><div class="meta">Фертика · комплексное удобрение</div><div class="price">от 227 ₽/кг <small>· цена по запросу</small></div><div class="row"><a class="btn ghost sm">Подробнее</a><a class="btn o sm">Получить предложение</a></div></div>
    <div class="card"><div class="img">Фото продукта</div><h3>Реликт М Кремний</h3><div class="meta">Реликт · листовая подкормка</div><div class="price">от 470 ₽/л <small>· цена по запросу</small></div><div class="row"><a class="btn ghost sm">Подробнее</a><a class="btn o sm">Получить предложение</a></div></div>
    <div class="card"><div class="img">Фото продукта</div><h3>Гербицид (пример)</h3><div class="meta">СЗР · гербицид</div><div class="price">Цена по запросу</div><div class="row"><a class="btn ghost sm">Подробнее</a><a class="btn o sm">Получить предложение</a></div></div>
  </div>
  <p class="cat-note cat-note--strong">Доставка, хранение и сопровождение включаются в предложение. Итоговая стоимость зависит от объёма, региона и условий поставки.</p>
</div></section>

<!-- 5. СЕРВИС В 4 ЭТАПА + ДИАГНОСТИКА/АГРОСОПРОВОЖДЕНИЕ (светлый) -->
<section class="sec sec--light" id="service"><div class="wrap">
  <p class="sec-lead">«Сатурн» — не просто продажа продукции. Мы ведём хозяйство на всех этапах сезона.</p>
  <div class="steps">
    <div class="step"><div class="n">1</div><h3>Подбор</h3><p>Продукция под культуру и регион.</p></div>
    <div class="step"><div class="n">2</div><h3>Диагностика</h3><p>Листовая диагностика посевов.</p></div>
    <div class="step"><div class="n">3</div><h3>Поставка</h3><p>Доставка и хранение оптом.</p></div>
    <div class="step"><div class="n">4</div><h3>Сопровождение</h3><p>Контроль в течение сезона.</p></div>
  </div>

  <div class="svc2">
    <div class="svc" id="diag">
      <h3>{icon('diagnostika',26)}Диагностика</h3>
      <p>Функциональная листовая диагностика: определяем дефициты питания и корректируем схему под конкретное поле.</p>
      <ul>
        <li>Обследование посевов</li>
        <li>Отбор материала</li>
        <li>Листовая диагностика</li>
        <li>Определение дефицитов</li>
        <li>Рекомендации по корректировке</li>
      </ul>
      <a class="btn g" href="#form">Заказать диагностику</a>
    </div>
    <div class="svc" id="agro">
      <h3>{icon('agro',26)}Агросопровождение</h3>
      <p>Ведём культуру от подбора схемы до контроля результата в течение всего сезона.</p>
      <ul>
        <li>Подбор продукции</li>
        <li>Разработка схемы</li>
        <li>Расчёт норм</li>
        <li>Консультации по применению</li>
        <li>Контроль и корректировка в течение сезона</li>
      </ul>
      <a class="btn g" href="#form">Обсудить задачу с агрономом</a>
    </div>
  </div>
</div></section>

<!-- 6. О КОМПАНИИ (тёмный) -->
<section class="sec sec--dark" id="about"><div class="wrap">
  <div class="about">
    <div>
      <h2 class="sec-h">«Сатурн» — поставщик решений для растениеводства</h2>
      <p class="sec-lead">Обеспечиваем сельхозпроизводителей семенами, удобрениями и средствами защиты растений. Подбираем продукцию под культуру и регион, организуем поставку и сопровождаем применение.</p>
      <div class="about-btns"><a class="btn ghost">Подробнее о компании</a><a class="btn ghost">Скачать реквизиты (PDF)</a></div>
    </div>
    <div class="about-photo">фото компании / поля / склада</div>
  </div>
</div></section>

<!-- 7. ГЕОГРАФИЯ (светлый) -->
<section class="sec sec--light" id="geo"><div class="wrap">
  <h2 class="sec-h">География поставок</h2>
  <p class="sec-lead">Организуем оптовые поставки и агросопровождение в аграрных регионах России. Доставка в другие регионы — по запросу.</p>
  <div class="geo geo--light">
    <div class="regions">{regions_html}</div>
    <div class="mapbox"><span class="big">8</span>регионов регулярных поставок<br><span class="mapleg">● офис — Барнаул &nbsp; ● регионы поставок &nbsp; ○ доставка по запросу</span></div>
  </div>
</div></section>

<!-- ИСПЫТАНИЯ И РЕЗУЛЬТАТЫ (светлый) -->
<section class="sec sec--light" id="cases"><div class="wrap">
  <h2 class="sec-h">Результаты производственных испытаний</h2>
  <div class="cases cases--light">
    <div class="case"><div class="big">до +15%</div><h3>Пшеница</h3><p>Результат производственного испытания препаратов в конкретных условиях хозяйства.</p><div class="who">Хозяйство: АО «СибАгро»</div></div>
    <div class="case"><div class="big">+4%</div><h3>Соя</h3><p>Результат испытания продукции в конкретном хозяйстве.</p><div class="who">Хозяйство: АО «СибАгро»</div></div>
    <div class="case"><div class="big">🌾</div><h3>Ваше поле?</h3><p>Проведём диагностику, подберём схему и покажем результат в вашем хозяйстве.</p><div class="who">оставьте заявку →</div></div>
  </div>
</div></section>

<!-- 11. ДОКУМЕНТЫ И СЕРТИФИКАТЫ (светлый) -->
<section class="sec sec--light sec--paper2" id="docs"><div class="wrap">
  <div class="eyebrow">Документы</div>
  <h2 class="sec-h">Документы и сертификаты</h2>
  <div class="docs">
    <div class="doc"><span class="dic">📄</span>Свидетельство<br>о госрегистрации (СГР)</div>
    <div class="doc"><span class="dic">📄</span>Сертификаты<br>соответствия</div>
    <div class="doc"><span class="dic">📄</span>Инструкции<br>по применению</div>
    <div class="doc"><span class="dic">📄</span>Паспорта<br>безопасности</div>
  </div>
</div></section>

<!-- СПЕЦИАЛИСТЫ + ФОРМА (тёмный) -->
<section class="sec sec--dark" id="contacts"><div class="wrap">
  <div class="eyebrow">Контакты</div>
  <h2 class="sec-h">Свяжитесь со специалистом</h2>
  <div class="contact">
    <div class="contact-people">
      <div class="person"><div class="av">фото</div><div><h3>Алексей Нилов</h3><div class="role">коммерческий руководитель</div><div class="tel">+7 960 953-48-88</div><div class="ch">nilov@sssaturn.ru</div></div></div>
      <div class="person"><div class="av">фото</div><div><h3>Андрей Хаблак</h3><div class="role">специалист по поставкам</div><div class="tel">+7 963 502-38-55</div><div class="ch">по вопросам поставок и сопровождения</div></div></div>
    </div>
    <div class="contact-form" id="form">
      <div class="cf-h">Получить предложение</div>
      <div class="form form--dark">
        <input placeholder="Имя">
        <input placeholder="Телефон *">
        <input placeholder="Регион">
        <select><option>Что требуется</option><option>Удобрения</option><option>СЗР</option><option>Семена</option><option>Диагностика</option><option>Агросопровождение</option><option>Консультация</option></select>
        <input class="full" placeholder="Комментарий (необязательно)">
        <div class="submit"><button class="btn o">Получить предложение</button></div>
        <span class="note--dark">Нажимая кнопку, вы соглашаетесь с политикой обработки персональных данных.</span>
      </div>
    </div>
  </div>
</div></section>

<!-- ПОДВАЛ (тёмный) -->
<footer><div class="wrap">
  <div class="fgrid">
    <div class="col"><img src="{logo_white}" alt="Сатурн"></div>
    <div class="col"><b>Разделы</b><a href="#catalog">Каталог</a><a href="#diag">Диагностика</a><a href="#agro">Агросопровождение</a><a href="#about">О компании</a><a href="#geo">География</a><a href="#contacts">Контакты</a></div>
    <div class="col"><b>Контакты</b><a>☎ +7 960 953-48-88</a><a>☎ +7 963 502-38-55</a><a>nilov@sssaturn.ru</a><p>г. Барнаул, пр. Ленина 56 / Шевченко 52А, пом. Н13</p></div>
    <div class="col"><b>Реквизиты</b><p>ООО «Сатурн»</p><p>ИНН 2801274078</p><p>КПП 280101001</p><p>ОГРН 1232800002709</p><p>Юр. адрес: 656056, Алтайский край,<br>г. Барнаул, пл. Баварина 2, офис 11/09</p></div>
  </div>
  <div class="copy">© 2026 ООО «Сатурн» · sssaturn.ru</div>
</div></footer>

</body></html>'''
open('site-prototype-v44.html','w').write(HTML)
print("written site-prototype-v44.html size", len(HTML))
