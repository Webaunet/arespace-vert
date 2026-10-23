import sys,os,re,threading,http.server,functools,glob
from playwright.sync_api import sync_playwright
R='/home/claude/arespace-vert'
pages=[os.path.basename(p) for p in glob.glob(R+'/*.html')]
h=functools.partial(http.server.SimpleHTTPRequestHandler,directory=R)
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(s,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),lambda *a,**k:Q(*a,directory=R,**k))
threading.Thread(target=srv.serve_forever,daemon=True).start()
B='http://127.0.0.1:%d/'%srv.server_port
W=[360,414,768,821,981,1280,1920] if 'full' in sys.argv else [390,768,1280]
bad=[]
with sync_playwright() as p:
    b=p.chromium.launch();
    for pg in pages:
        for w in W:
            c=b.new_page(viewport={'width':w,'height':800});
            c.route('**/fonts.g*/**',lambda r:r.abort())
            c.goto(B+pg,wait_until='load');c.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')");c.wait_for_timeout(300)
            r=c.evaluate('''()=>{const o=[],vh=innerHeight,de=document.documentElement;
            if(de.scrollWidth>innerWidth)o.push('hscroll '+de.scrollWidth);
            document.querySelectorAll('p,li,a,h1,h2,h3,span,small').forEach(e=>{const f=parseFloat(getComputedStyle(e).fontSize);if(e.offsetParent&&f<16&&e.innerText.trim()&&!e.closest('.pill')&&getComputedStyle(e).display!='none'&&e.tagName!='SMALL'&&!e.matches('.eyebrow'))o.push('font '+f+' '+e.innerText.slice(0,20))});
            document.querySelectorAll('a,button').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&r.height&&(r.height<44||r.width<44)&&getComputedStyle(e).display!='inline')o.push('tap '+Math.round(r.width)+'x'+Math.round(r.height)+' '+(e.innerText||e.ariaLabel).slice(0,20))});
            document.querySelectorAll('img').forEach(i=>{if(!i.complete||!i.naturalWidth)o.push('img KO '+i.src);else if(i.naturalWidth<i.clientWidth*0.95)o.push('img agrandie '+i.src.split('/').pop())});
            document.querySelectorAll('main>section,.band-wrap>section,.cta-wrap>section').forEach(s=>{const r=s.offsetHeight/vh;if(r>1.35)o.push('section '+(s.id||s.className)+' '+r.toFixed(2)+'vh')});
            const ft=document.querySelector('footer');if(ft&&ft.offsetHeight>vh*.3)o.push('footer '+ft.offsetHeight);
            o.push('H='+(de.scrollHeight/vh).toFixed(1)+'ecrans');return o}''')
            for x in r:
                if not x.startswith('H=') or pg=='index.html' and w==1280: bad.append('%s@%d %s'%(pg,w,x))
            c.close()
    b.close()
for f in glob.glob(R+'/**/*.html',recursive=True):
    t=open(f,encoding='utf8').read()
    for l in re.findall(r'(?:href|src)="([^"#:]+)"',t):
        if not os.path.exists(os.path.join(R,l.split('?')[0])) and not l.startswith('http'):bad.append('lien '+os.path.basename(f)+' -> '+l)
tot=sum(os.path.getsize(f) for f in glob.glob(R+'/images/*'))
bad.append('images %d Ko'%(tot//1024))
print('\n'.join(bad) if bad else 'tout est OK')
