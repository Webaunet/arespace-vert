(function(){
var b=document.querySelector('.burger'),n=document.getElementById('nav');
if(!b||!n)return;
function set(o){n.classList.toggle('open',o);b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu')}
b.addEventListener('click',function(){set(b.getAttribute('aria-expanded')!=='true')});
n.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&n.classList.contains('open')){set(false);b.focus()}});
window.addEventListener('resize',function(){if(innerWidth>980)set(false)});
})();
