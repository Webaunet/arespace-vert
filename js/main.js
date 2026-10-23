(function(){
var b=document.querySelector('.burger'),n=document.getElementById('nav');
if(!b||!n)return;
function set(o){n.classList.toggle('open',o);b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu')}
b.addEventListener('click',function(){set(b.getAttribute('aria-expanded')!=='true')});
n.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&n.classList.contains('open')){set(false);b.focus()}});
window.addEventListener('resize',function(){if(innerWidth>980)set(false)});
})();
(function(){
var f=document.getElementById('devis');if(!f)return;
var TEL='+33680898896',rules={
nom:function(v){return v.trim().length>=2?'':'Indiquez votre nom.'},
tel:function(v){return /^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.\-]*\d{2}){4}$/.test(v.trim())?'':'Indiquez un numéro valide, par exemple 06 12 34 56 78.'},
commune:function(v){return v.trim().length>=2?'':'Indiquez votre commune.'},
besoin:function(v){return v?'':'Choisissez votre besoin.'}};
function chk(id){var el=f.elements[id],m=rules[id](el.value),e=document.getElementById('e-'+id);
e.textContent=m;e.hidden=!m;el.setAttribute('aria-invalid',m?'true':'false');return !m}
Object.keys(rules).forEach(function(id){f.elements[id].addEventListener('blur',function(){chk(id)})});
var r=document.getElementById('recap'),ta=document.getElementById('recap-txt');
f.addEventListener('submit',function(ev){ev.preventDefault();
var ids=Object.keys(rules),bad=ids.filter(function(i){return !chk(i)});
if(bad.length){f.elements[bad[0]].focus();return}
var g=function(i){return f.elements[i].value.trim()},msg=g('message');
var t='Bonjour, je souhaite un devis auprès d’ARESPACE VERT.\nNom : '+g('nom')+'\nTéléphone : '+g('tel')+'\nCommune : '+g('commune')+'\nBesoin : '+g('besoin')+(msg?'\nMessage : '+msg:'');
ta.value=t;document.getElementById('sms').href='sms:'+TEL+'?body='+encodeURIComponent(t);
r.hidden=false;r.scrollIntoView({behavior:'smooth',block:'nearest'});document.getElementById('recap-h').focus()});
document.getElementById('copy').addEventListener('click',function(){var s=document.getElementById('copy-ok');
function done(m){s.textContent=m}
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(ta.value).then(function(){done('Texte copié.')},function(){ta.select();done('Sélectionné : copiez-le avec Ctrl+C.')})}
else{ta.select();done('Sélectionné : copiez-le avec Ctrl+C.')}});
})();
