import re,os
R='/home/claude/arespace-vert/'
idx=open(R+'index.html',encoding='utf8').read()
LOGO='https://webaunet.github.io/arespace-vert/'
idx=re.sub(r'(<a class="logo" href=")[^"]*"',r'\1'+LOGO+'"',idx,1)
open(R+'index.html','w',encoding='utf8').write(idx)
HEADER=re.search(r'<header class="hd">.*?</header>',idx,re.S).group(0)
FOOT=re.search(r'<div class="ft-wrap">.*?</div></footer></div>',idx,re.S).group(0)
FAV=re.search(r'<link rel="icon"[^>]*>',idx).group(0)
FONTS=re.search(r'<link rel="preconnect".*?display=swap">',idx,re.S).group(0)
HEADER=HEADER.replace(' aria-current="page"','')
def hdr(cur):
    return HEADER if not cur else HEADER.replace('<a href="%s">'%cur,'<a href="%s" aria-current="page">'%cur)
def page(fn,title,desc,cur,main):
    h='<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>%s</title>\n<meta name="description" content="%s">\n<meta name="robots" content="noindex, nofollow">\n%s\n%s\n<link rel="stylesheet" href="css/style.css">\n</head>\n<body>\n%s\n<main>\n%s\n</main>\n%s\n<script src="js/main.js"></script>\n</body>\n</html>\n'%(title,desc,FAV,FONTS,hdr(cur),main,FOOT)
    open(R+fn,'w',encoding='utf8').write(h)
def ico(p):return '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'%p
I_PEN='<path d="M4 20l1-4L16 5l3 3L8 19z"/><path d="M14 7l3 3"/>'
I_LEAF='<path d="M12 21c-5-2-7-7-4-13 5 1 9 4 9 9 0 2-1 3-2 4z"/><path d="M12 21c0-5 1-8 4-11"/>'
I_TREE='<path d="M12 21v-6"/><path d="M12 15c-4 0-7-3-7-7a7 7 0 0 1 14 0c0 4-3 7-7 7z"/>'
I_PATH='<path d="M4 21c4-3 4-6 8-9s4-6 8-9"/><path d="M8 21h12M4 13h4"/>'
I_CHAT='<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>'
I_SUN='<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>'
I_MED='<circle cx="12" cy="9" r="5"/><path d="M8.5 13.5L7 21l5-3 5 3-1.5-7.5"/>'
I_RUL='<path d="M3 17L17 3l4 4L7 21z"/><path d="M8 12l2 2M11 9l2 2M14 6l2 2"/>'
TEL='<a class="btn btn-o" href="tel:+33680898896">Appeler le 06 80 89 88 96</a>'

# ---------------- PRESTATIONS
main='''<section class="ph duo">
 <div class="wrap">
  <div>
   <span class="eyebrow">Nos prestations</span>
   <h1>Création, entretien, élagage : tout pour votre jardin</h1>
   <p class="lead">Quatre domaines d'intervention à Garancières et dans les Yvelines, menés par une équipe d'artisans paysagistes.</p>
   <div class="acts"><a class="btn btn-p" href="contact.html">Demander un devis</a>'''+TEL+'''</div>
  </div>
  <div class="mosaic">
   <img src="images/conception.jpg" width="1000" height="545" alt="Projet de jardin présenté sur une tablette devant une maison avec muret en pierre">
   <img src="images/tonte-robot.jpg" width="1000" height="545" alt="Pelouse tondue par un robot, massif fleuri et muret en pierre devant une maison">
   <img src="images/taille-reduction.jpg" width="1000" height="545" alt="Élagueur en hauteur dans un grand chêne après une taille de réduction">
  </div>
 </div>
</section>
<section class="sec" id="domaines">
 <div class="wrap">
  <div class="head"><span class="eyebrow">Domaines d'intervention</span><h2>Ce que nous faisons pour vous</h2></div>
  <div class="svc">
   <article class="sv a" id="architecture">'''+ico(I_PEN)+'''<h3>Architecture paysagère</h3><p>Artisan spécialisé dans la création d'espaces verts, nous vous accompagnons dans la réalisation de vos idées.</p><ul><li>Écoute de vos envies, même les plus originales</li><li>Mise en œuvre dans le respect des bonnes pratiques</li></ul></article>
   <article class="sv b" id="entretien">'''+ico(I_LEAF)+'''<h3>Entretien de votre jardin</h3><p>Pour que votre jardin soit toujours bien entretenu, confiez-nous :</p><ul><li>la tonte de votre pelouse</li><li>le débroussaillage</li><li>la taille de vos haies</li></ul></article>
   <article class="sv c" id="elagage">'''+ico(I_TREE)+'''<h3>Élagage</h3><p>Maîtriser la pousse des arbres, ça nous connaît ! Notre équipe s'occupe de vos arbres dans le respect des saisons.</p></article>
   <article class="sv d" id="allees-svc">'''+ico(I_PATH)+'''<h3>Aménagement d'allées</h3><p>Un cheminement pensé avec votre jardin, vos plantations et l'architecture de votre maison.</p></article>
  </div>
 </div>
</section>
<section class="sec sand" id="allees">
 <div class="wrap split rev">
  <div>
   <span class="eyebrow">À chaque chantier</span>
   <h2>Une même exigence de qualité</h2>
   <p>Qu'il s'agisse de créer un jardin, de l'entretenir ou de s'occuper d'un arbre, nous effectuons des prestations de qualité, appuyées sur une longue expérience de l'entretien de jardin.</p>
   <ul class="check"><li>Un devis adapté à votre projet</li><li>Une équipe qui vous écoute</li><li>Un travail soigné jusqu'au dernier détail</li></ul>
  </div>
  <img src="images/allee-paves.jpg" width="1000" height="545" loading="lazy" alt="Allée en dalles de pierre bordée d'un muret et de massifs fleuris menant à une maison">
 </div>
</section>
<section class="bd-s"><div class="wrap"><div class="bd"><div><h2>Un chantier en tête ?</h2><p>Décrivez-nous votre projet : nous vous recontactons.</p></div><div class="acts" style="margin:0"><a class="btn btn-d" href="contact.html">Demander un devis</a><a class="btn btn-dl" href="tel:+33680898896">06 80 89 88 96</a></div></div></div></section>'''
page('prestations.html','Prestations – ARESPACE VERT, paysagiste à Garancières (78)','Architecture paysagère, entretien de jardin, élagage et aménagement d\'allées : les prestations d\'ARESPACE VERT, paysagiste à Garancières dans les Yvelines.','prestations.html',main)

# ---------------- APPROCHE
main='''<section class="ph img slim">
 <img src="images/terrasse-bois.jpg" width="1300" height="709" alt="Chantier d'aménagement d'une terrasse en bois devant une maison en pierre" fetchpriority="high">
 <div class="wrap"><span class="eyebrow">Notre approche</span><h1>Vos idées d'abord, le savoir-faire ensuite</h1><p class="lead">Chaque jardin est différent. Nous partons de ce que vous imaginez pour le concrétiser avec méthode.</p></div>
</section>
<section class="sec" id="engagements">
 <div class="wrap eng">
  <div class="head"><span class="eyebrow">Nos engagements</span><h2>Ce sur quoi vous pouvez compter</h2><p>Une démarche d'artisan, simple et transparente, du premier échange à la dernière intervention.</p></div>
  <ul>
   <li>'''+ico(I_CHAT)+'''<div><h3>Une vraie écoute</h3><p>Faites-nous part de vos idées, même les plus originales : nous nous appliquons à les mettre en œuvre.</p></div></li>
   <li>'''+ico(I_RUL)+'''<div><h3>Les bonnes pratiques</h3><p>Chaque aménagement respecte les bonnes pratiques de l'architecture paysagère.</p></div></li>
   <li>'''+ico(I_SUN)+'''<div><h3>Le respect des saisons</h3><p>Vos arbres sont pris en charge au bon moment, en tenant compte de leur rythme.</p></div></li>
   <li>'''+ico(I_MED)+'''<div><h3>Une longue expérience</h3><p>Des prestations de qualité, appuyées sur une longue expérience de l'entretien de jardin.</p></div></li>
  </ul>
 </div>
</section>
<div class="band-wrap">
<section class="band" id="saisons"><div class="wrap split">
  <img src="images/taille-reduction.jpg" width="1000" height="545" loading="lazy" alt="Élagueur en hauteur dans un grand chêne après une taille de réduction">
  <div>
   <span class="eyebrow">Les arbres</span>
   <h2>Maîtriser la pousse, sans les brusquer</h2>
   <p>Un arbre bien taillé reste sain et sûr. Notre équipe intervient dans le respect des saisons, pour accompagner la croissance de vos arbres plutôt que la contrarier.</p>
   <a class="btn btn-p" href="prestations.html#elagage">Voir l'élagage</a>
  </div>
</div></section>
</div>
<section class="sec" id="acces" style="background:var(--cream)">
 <div class="wrap">
  <div class="head"><span class="eyebrow">Où nous trouver</span><h2>Un paysagiste près de chez vous</h2></div>
  <div class="loc">
   <div class="box"><h3>L'entreprise</h3><address>ARESPACE VERT<br>28 Rue du Pré Marot<br>78890 Garancières</address><a class="lk" href="https://www.google.com/maps/place/ARESPACE+VERT/@48.8220892,1.74393,17z" target="_blank" rel="noopener">Voir l'itinéraire sur Google Maps</a></div>
   <div class="box g"><h3>Besoin d'un conseil ?</h3><p>Appelez-nous : nous répondons à vos questions sur votre jardin, vos arbres ou vos allées.</p><a class="btn btn-p" href="tel:+33680898896">06 80 89 88 96</a></div>
  </div>
 </div>
</section>
<section class="bd-s"><div class="wrap"><div class="bd col"><h2>Racontez-nous votre jardin</h2><p>Quelques lignes suffisent pour démarrer : nous vous répondons rapidement.</p><a class="tel2" href="tel:+33680898896" style="color:#0f3d1e">06 80 89 88 96</a><a class="btn btn-d" href="contact.html">Écrire notre besoin</a></div></div></section>'''
page('approche.html','Notre approche – ARESPACE VERT, paysagiste à Garancières (78)','La démarche d\'ARESPACE VERT, paysagiste à Garancières : écoute, bonnes pratiques, respect des saisons et longue expérience de l\'entretien de jardin.','approche.html',main)

# ---------------- CONTACT
main='''<section class="ph slim"><div class="wrap"><span class="eyebrow">Contact</span><h1>Parlons de votre jardin</h1><p class="lead">Remplissez le formulaire, puis envoyez-nous votre demande par SMS en un geste, ou appelez-nous directement.</p></div></section>
<section class="sec" id="formulaire">
 <div class="wrap ct">
  <div class="form">
   <h2 style="font-size:1.7rem">Votre demande de devis</h2>
   <form id="devis" novalidate>
    <div class="fld"><label for="nom">Nom</label><input id="nom" name="nom" type="text" autocomplete="name" required aria-describedby="e-nom"><p class="err" id="e-nom" role="alert" hidden></p></div>
    <div class="fld"><label for="tel">Téléphone</label><input id="tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="e-tel"><p class="err" id="e-tel" role="alert" hidden></p></div>
    <div class="fld"><label for="commune">Commune</label><input id="commune" name="commune" type="text" autocomplete="address-level2" required aria-describedby="e-commune"><p class="err" id="e-commune" role="alert" hidden></p></div>
    <div class="fld"><label for="besoin">Votre besoin</label><select id="besoin" name="besoin" required aria-describedby="e-besoin"><option value="">Choisir…</option><option>Architecture paysagère</option><option>Entretien de jardin</option><option>Élagage</option><option>Aménagement d'allées</option><option>Autre demande</option></select><p class="err" id="e-besoin" role="alert" hidden></p></div>
    <div class="fld"><label for="message">Message <small>(facultatif)</small></label><textarea id="message" name="message" rows="4"></textarea></div>
    <button class="btn btn-g" type="submit">Préparer ma demande</button>
   </form>
   <div class="recap" id="recap" hidden>
    <h3 id="recap-h" tabindex="-1">Votre demande est prête</h3>
    <p class="ok">Il ne reste qu'à l'envoyer : le formulaire ne part pas tout seul.</p>
    <label for="recap-txt" style="font-weight:600">Récapitulatif</label>
    <textarea id="recap-txt" readonly></textarea>
    <div class="acts"><a class="btn btn-g" id="sms" href="sms:+33680898896">Envoyer par SMS</a><button class="btn btn-o" id="copy" type="button" style="border-color:var(--g700);color:var(--g700)">Copier</button><a class="btn btn-p" href="tel:+33680898896">Appeler</a></div>
    <p id="copy-ok" role="status" class="ok" style="margin:12px 0 0"></p>
   </div>
  </div>
  <aside class="side">
   <div class="box"><h3>Appelez-nous</h3><p>Pour une question ou un devis, le plus simple reste le téléphone.</p><a class="tel3" href="tel:+33680898896" style="color:var(--g300)">06 80 89 88 96</a></div>
   <div class="box l"><h3>L'entreprise</h3><address style="font-style:normal;margin-bottom:10px">ARESPACE VERT<br>28 Rue du Pré Marot<br>78890 Garancières</address><a href="https://www.google.com/maps/place/ARESPACE+VERT/@48.8220892,1.74393,17z" target="_blank" rel="noopener">Itinéraire sur Google Maps</a></div>
  </aside>
 </div>
</section>'''
page('contact.html','Contact et devis – ARESPACE VERT, paysagiste à Garancières (78)','Contactez ARESPACE VERT, paysagiste à Garancières (78) : formulaire de demande de devis, envoi par SMS et appel direct au 06 80 89 88 96.','contact.html',main)

# ---------------- MENTIONS
main='''<section class="ph slim"><div class="wrap"><span class="eyebrow">Informations légales</span><h1>Mentions légales</h1></div></section>
<section class="sec" style="min-height:0"><div class="wrap legal">
 <dl>
  <dt>Entreprise</dt><dd>ARESPACE VERT</dd>
  <dt>SIREN</dt><dd>818586174</dd>
  <dt>Adresse</dt><dd>28 Rue du Pré Marot, 78890 Garancières</dd>
  <dt>Téléphone</dt><dd><a href="tel:+33680898896">06 80 89 88 96</a></dd>
  <dt>Statut de ce site</dt><dd>Maquette de présentation, non référencée dans les moteurs de recherche.</dd>
 </dl>
</div></section>'''
page('mentions-legales.html','Mentions légales – ARESPACE VERT, Garancières (78)','Mentions légales du site d\'ARESPACE VERT, paysagiste à Garancières (78) : identification de l\'entreprise.','',main)
print('ok')
