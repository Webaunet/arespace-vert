import re,os
t=open('/home/claude/arespace-vert/index.html',encoding='utf8').read()
head=re.search(r'<head>(.*)</head>',t,re.S).group(1)
body=re.search(r'<body>(.*)</body>',t,re.S).group(1)
head=re.sub(r'<meta charset[^>]*>|<meta name="viewport"[^>]*>','',head)
os.makedirs('/tmp/w/art',exist_ok=True)
open('/tmp/w/art/index.html','w',encoding='utf8').write(head+body)
