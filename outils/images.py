import sys
from PIL import Image
S='/mnt/user-data/uploads/Maquettes/Images/Paysagiste/'
D='/home/claude/arespace-vert/images/'
M={'terrasse-bois':('chantier terrasse en bois.jpg',1300),'allee-paves':('alléé pavés carrelage extérieure.jpg',1000),'taille-reduction':('Étêtage taille de réduction.jpg',1000),'tonte-robot':('robot tonte de pelouse.jpg',1000),'conception':('conception chantier.jpg',1000),'equipe-elagage':('Équipe et matériel elagage.jpg',1000),'allee-dallee':('chantier allée dallée.jpg',1000),'maconnerie':('maçonerie paysagère.jpg',1000),'taille-haies':('imgi_4_taille-haies.jpg',800)}
for k,(f,w) in M.items():
    im=Image.open(S+f).convert('RGB'); 
    if im.width>w: im=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
    q=82
    while True:
        im.save(D+k+'.jpg',quality=q,optimize=True,progressive=True)
        import os
        if os.path.getsize(D+k+'.jpg')<250000 or q<=70: break
        q-=3
    print(k,im.size,os.path.getsize(D+k+'.jpg')//1024,'Ko q',q)
names=['terrasse-bois','allee-paves','taille-reduction','tonte-robot','conception','equipe-elagage']
sheet=Image.new('RGB',(1200,600),'white')
for i,n in enumerate(names):
    t=Image.open(D+n+'.jpg'); t.thumbnail((400,300)); sheet.paste(t,((i%3)*400,(i//3)*300))
sheet.save('/tmp/w/sheet.jpg',quality=70)
