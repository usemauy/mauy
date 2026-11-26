#!/usr/bin/env python3
"""Aplica o diagnóstico do squad ao index.html da loja MAUY.
Uso: python3 aplicar_diagnostico.py index.html [https://seudominio.com.br/] [img/og.jpg]
- Faz backup em index.html.bak
- Extrai as imagens Base64 para a pasta img/ (cache separado)
- Lista no fim qualquer trecho que não foi encontrado (nada é alterado em silêncio)"""
import sys, re, hashlib, pathlib, shutil
f = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'index.html')
site = (sys.argv[2].rstrip('/') + '/') if len(sys.argv) > 2 else ''
og = sys.argv[3] if len(sys.argv) > 3 else ''
html = f.read_text(encoding='utf-8'); shutil.copy(f, str(f) + '.bak'); miss = []

def rep(old, new, n=1):
    global html
    if html.count(old) != n: miss.append(old[:70]); return
    html = html.replace(old, new)

# ---------- CSS ----------
rep('--wine:#59283B;--ti:#59283B;--card:#fff', '--wine:var(--brand,#59283B);--ti:var(--brand,#59283B);--card:#fff')
rep('--wine:#8A4660;--ti:#E9DDD3;', '--wine:var(--brand,#8A4660);--ti:#E9DDD3;')
rep("if(m.cor1){root.style.setProperty('--wine',m.cor1);root.style.setProperty('--ti',m.cor1)}", "if(m.cor1)root.style.setProperty('--brand',m.cor1);")
rep('</style>', r'''.btn.l{background:#F5F1EB}
body:has(.md.on),body:has(.dr.on){overflow:hidden}
.sr{position:absolute;left:-9999px}
.mb .ey{color:var(--ti)!important}.off{color:var(--ti)}
.gm.z{touch-action:none}
.rasc{position:fixed;top:0;left:0;right:0;z-index:90;background:#29292B;color:#fff;padding:8px 14px;font-size:12px;display:flex;gap:12px;justify-content:center;align-items:center}
.falha{text-align:center;padding:90px 20px}.falha .btn{margin-top:18px}
@media(max-width:850px){.mb .x{position:fixed;right:24px;top:24px;width:40px;height:40px;border-radius:50%;background:var(--sand)}.ac{position:sticky;bottom:0;background:var(--sand);padding:10px 0;z-index:3}}
</style>''')

# ---------- HTML: Open Graph inicial, diálogos, rodapé ----------
tags = '<meta property="og:site_name" content="MAUY Fitness"><meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:title" content="MAUY Fitness · Loja virtual"><meta property="og:description" content="Força em cada detalhe. Moda fitness feminina e acessórios."><meta name="twitter:card" content="summary_large_image">'
if site: tags += f'<meta property="og:url" content="{site}"><link rel="canonical" href="{site}">'
if site and og: tags += f'<meta property="og:image" content="{site}{og.lstrip("/")}">'
rep('Moda fitness feminina e acessórios.">', 'Moda fitness feminina e acessórios.">' + tags)
rep('<aside class="dr" id="dr" aria-label="Sua sacola">', '<aside class="dr" id="dr" role="dialog" aria-modal="true" aria-label="Sua sacola">')
rep('<div class="mb" id="mb"></div>', '<div class="mb" id="mb" role="dialog" aria-modal="true" aria-label="Produto"></div>')
rep('<p id="ft" style="margin-top:12px"></p>', '<p id="ft" style="margin-top:12px"></p><p id="leg" style="margin-top:10px;font-size:11px;opacity:.7"></p><div id="lnk"></div>')
rep("$('#ft').textContent=s.rodape||'';", r'''$('#ft').textContent=s.rodape||'';$('#leg').textContent=[s.razaoSocial,s.cnpj?'CNPJ '+s.cnpj:'',s.endereco].filter(Boolean).join(' · ');$('#lnk').innerHTML=[[s.linkTrocas,'Trocas e devoluções'],[s.linkPrivacidade,'Política de privacidade']].filter(x=>/^(https?:\/\/|\/|#)/.test(x[0]||'')).map(x=>`<a href="${esc(x[0])}">${x[1]}</a>`).join('');''')

# ---------- Estoque, frete, Pix ----------
rep('(s>=free?0:S.frete)', '(free>0&&s>=free?0:S.frete)', 2)
rep('v:+D.site.freteBase||24.9', 'v:isNaN(parseFloat(D.site.freteBase))?24.9:parseFloat(D.site.freteBase)')
rep('const r=freteDe(v);S.frete=r.v;', "const r=freteDe(v);if(!r.uf){S.frete=null;S.cm='CEP não encontrado. Confira os números.';return}S.frete=r.v;")
rep('''<div style="font-size:12px">${s==0?`Frete grátis acima de ${brl(free)}`:s>=free?'Você ganhou frete grátis':`Faltam ${brl(free-s)} para o frete grátis`}</div><div class="bar"><i style="width:${Math.min(100,free?s/free*100:0)}%"></i></div>''',
    '''${free>0?`<div style="font-size:12px">${s==0?`Frete grátis acima de ${brl(free)}`:s>=free?'Você ganhou frete grátis':`Faltam ${brl(free-s)} para o frete grátis`}</div><div class="bar"><i style="width:${Math.min(100,s/free*100)}%"></i></div>`:''}''')
rep('D.site=D.site||{};', 'D.site=D.site||{};D.site.pix=isFinite(parseFloat(D.site.pix))?parseFloat(D.site.pix):0;')
rep('<span class="px">· ${brl(p.preco*(1-D.site.pix/100))} no Pix</span>', '${D.site.pix>0?`<span class="px">· ${brl(p.preco*(1-D.site.pix/100))} no Pix</span>`:\'\'}')
rep('${brl(p.preco*(1-(+D.site.pix||0)/100))} no Pix · ', "${D.site.pix>0?brl(p.preco*(1-D.site.pix/100))+' no Pix · ':''}")
rep('<div class="pix"><b>Pix: ${brl(tot*(1-D.site.pix/100))}</b><br>${D.site.pix}% de desconto no pagamento à vista.</div>',
    '${D.site.pix>0?`<div class="pix"><b>Pix: ${brl(tot*(1-D.site.pix/100))}</b><br>${D.site.pix}% de desconto no pagamento à vista.</div>`:\'\'}')

# ---------- Navegação, busca, listas ----------
rep("if(c){S.cat=c.dataset.c;head();grid();if(c.closest('nav'))$('#loja')?.scrollIntoView()}",
    "if(c){const doTopo=!!c.closest('nav');S.cat=c.dataset.c;head();grid();if(doTopo)$('#loja')?.scrollIntoView({behavior:'smooth'})}")
rep("$('#si').oninput=e=>{S.q=e.target.value;grid()};",
    "$('#si').oninput=e=>{S.q=e.target.value;if(S.q)S.cat='Todos';grid();if(S.q&&!S.sc){S.sc=1;$('#loja')?.scrollIntoView({behavior:'smooth'})}if(!S.q)S.sc=0};")
rep('p.nome.toLowerCase().includes(S.q.toLowerCase())', "norm([p.nome,p.categoria,p.descricao].join(' ')).includes(norm(S.q))")
rep('all.slice(-8).includes(p)', '(all.length>8&&all.slice(-8).includes(p))')
rep(r'''const url=u=>String(u||'').replace(/["'\\()]/g,'');''',
    r'''const url=u=>String(u||'').replace(/["'\\]/g,'').replace(/\(/g,'%28').replace(/\)/g,'%29').replace(/ /g,'%20');
const norm=t=>String(t||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();''')
rep("function store(){$('#yr').textContent=new Date().getFullYear();head();secs();grid();cart();seoHome()}",
    "function store(){$('#yr').textContent=new Date().getFullYear();head();secs();grid();cart();if(!document.querySelector('h1'))$('#secs').insertAdjacentHTML('afterbegin','<h1 class=\"sr\">'+esc(D.site.nome||'MAUY Fitness')+'</h1>');seoHome()}")
rep('.filter(i=>i.p);', '.filter(i=>i.p&&i.p.ativo!==false);')

# ---------- Produto: histórico, foco, zoom por toque ----------
rep("function openP(id){const p=D.produtos.find(x=>x.id==id);if(!p)return;Object.assign(S,{pid:p.id,sz:null,col:null,qty:1,tab:0,ci:0});prodView();$('#md').classList.add('on');$('#sh').classList.add('on');seoProduct(p);try{history.replaceState(null,'','#p-'+encodeURIComponent(p.id))}catch(e){}}",
    "function openP(id){const p=D.produtos.find(x=>x.id==id&&x.ativo!==false);if(!p)return;S.foco=S.foco||document.activeElement;Object.assign(S,{pid:p.id,sz:null,col:null,qty:1,tab:0,ci:0});prodView();$('#md').classList.add('on');$('#sh').classList.add('on');seoProduct(p);track('ver_produto',{id:p.id,nome:p.nome});const h='#p-'+encodeURIComponent(p.id);try{if(location.hash!==h){if(S.pushed||/^#p-/.test(location.hash))history.replaceState(null,'',h);else{history.pushState(null,'',h);S.pushed=true}}}catch(e){}$('#mb .x')?.focus()}")
rep("function shut(){['dr','md','sh'].forEach(i=>$('#'+i).classList.remove('on'));if(S.pid){S.pid=null;seoHome();try{if(/^#p-/.test(location.hash))history.replaceState(null,'',location.pathname+location.search)}catch(e){}}}",
    "function shut(pop){['dr','md','sh'].forEach(i=>$('#'+i).classList.remove('on'));if(S.pid){S.pid=null;seoHome();try{if(!pop&&S.pushed){S.pushed=false;history.back()}else if(/^#p-/.test(location.hash))history.replaceState(null,'',location.pathname+location.search)}catch(e){}}if(pop)S.pushed=false;if(S.foco){try{S.foco.focus()}catch(e){}S.foco=null}}")
rep("$('#cb').onclick=openCart;$('#cx').onclick=shut;$('#sh').onclick=shut;", "$('#cb').onclick=openCart;$('#cx').onclick=()=>shut();$('#sh').onclick=()=>shut();$('#md').onclick=e=>{if(e.target.id==='md')shut()};")
rep("const openCart=()=>{$('#dr').classList.add('on');$('#sh').classList.add('on')};", "const openCart=()=>{S.foco=S.foco||document.activeElement;$('#dr').classList.add('on');$('#sh').classList.add('on');$('#cx').focus()};")
rep("else if(S.pid)shut()}", "else if(S.pid)shut(true)}")
rep("window.addEventListener('hashchange',()=>route());", "window.addEventListener('hashchange',()=>route());window.addEventListener('popstate',()=>route());")
rep("$('#mb').addEventListener('mousemove',e=>{", "$('#mb').addEventListener('pointermove',e=>{")
rep("const sc=$('#mb').scrollTop;", r'''const sc=$('#mb').scrollTop,fa=document.activeElement,fk=fa&&fa.closest&&fa.closest('#mb')?[...fa.attributes].filter(a=>/^data-/.test(a.name)).map(a=>`[${a.name}="${CSS.escape(a.value)}"]`).join(''):'';''')
rep("$('#mb').scrollTop=sc}", "$('#mb').scrollTop=sc;if(fk){const n=$('#mb').querySelector(fk);if(n&&!n.disabled)n.focus({preventScroll:true})}}")

# ---------- Pedido: CEP obrigatório, SKU, métricas ----------
rep("if(id=='co'){const L=lines();if(!L.length)return;", "if(id=='co'){const L=lines();if(!L.length)return;if(S.frete==null)return toast('Calcule o frete com o seu CEP antes de finalizar.');track('finalizar',{itens:L.length});")
rep("`• ${i.p.nome} | Tam. ", "`• ${i.p.nome}${i.p.sku?' ('+i.p.sku+')':''} | Tam. ")
rep("keep();cart();shut();return openCart()}", "track('add_sacola',{id:p.id,qtd:k});keep();cart();shut();return openCart()}")

# ---------- Carregamento: erro claro em vez de catálogo de demonstração ----------
rep("(async()=>{try{const r=await fetch('dados.json?'+Date.now(),{cache:'no-store'});if(r.ok)D=await r.json()}catch(e){}",
    r'''const track=(n,d)=>{try{(window.dataLayer=window.dataLayer||[]).push({event:n,...d});if(window.gtag)gtag('event',n,d);if(window.plausible)plausible(n,{props:d})}catch(e){}};
function falha(){const w=String(D.site&&D.site.whatsapp||'').replace(/\D/g,'');$('#secs').innerHTML=`<section class="wrap falha"><h1>Não conseguimos carregar a loja agora</h1><p>Tente novamente em instantes ou fale com a gente.</p>${w?`<a class="btn" href="https://wa.me/${w}" target="_blank" rel="noopener">Atendimento WhatsApp</a>`:''}<br><button class="btn g" onclick="location.reload()">Tentar de novo</button></section>`}
function rascunho(){const b=document.createElement('div');b.className='rasc';b.innerHTML='<span>Visualizando rascunho local (não publicado)</span><button class="btn s">Descartar rascunho</button>';b.querySelector('button').onclick=()=>{try{localStorage.removeItem('mauy_draft')}catch(e){}location.reload()};document.body.prepend(b)}
document.addEventListener('error',e=>{const i=e.target;if(i&&i.tagName==='IMG'){const ph=i.closest('.ph');if(ph){i.remove();ph.classList.add('ne')}}},true);
(async()=>{$('#secs').innerHTML='<p class="empty">Carregando a loja…</p>';let ok=false;try{const c=new AbortController(),t=setTimeout(()=>c.abort(),8000);const r=await fetch('dados.json?'+Date.now(),{cache:'no-store',signal:c.signal});clearTimeout(t);if(r.ok){const j=await r.json();if(j&&Array.isArray(j.produtos)&&j.produtos.length){D=j;ok=true}}}catch(e){}''')
rep("const draft=LS.g('mauy_draft',null);if(draft){D=draft;toast('Visualizando rascunho local (não publicado)')}",
    "const draft=LS.g('mauy_draft',null);if(draft){D=draft;ok=true;rascunho()}if(!ok)return falha();")

# ---------- Base64 -> arquivos em img/ ----------
out = f.parent / 'img'; out.mkdir(exist_ok=True); seen = {}
import base64
def ext(m):
    h = hashlib.sha1(m.group(2).encode()).hexdigest()[:10]; e = {'jpeg':'jpg','svg+xml':'svg'}.get(m.group(1), m.group(1))
    p = out / f'{h}.{e}'
    if not p.exists(): p.write_bytes(base64.b64decode(m.group(2)))
    seen[p.name] = 1; return f'img/{p.name}'
html = re.sub(r'data:image/([a-z+]+);base64,([A-Za-z0-9+/=]+)', ext, html)

f.write_text(html, encoding='utf-8')
print(f'OK. {len(seen)} imagem(ns) extraída(s) para img/.')
if miss:
    print('ATENÇÃO: não encontrei estes trechos (o index.html pode ter sido editado):'); [print(' -', m) for m in miss]
