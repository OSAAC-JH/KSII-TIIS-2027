# Usage: python tools/check_dois.py data/seed_dois.txt data/crossref_check.json  (R12 is a JaLC DOI; Crossref returns 404 for it)
import json,sys,urllib.request,time
sys.stdout.reconfigure(encoding="utf-8")
dois=[l.split()[1] for l in open(sys.argv[1]) if l.strip()]
out={}
for line in open(sys.argv[1]):
    if not line.strip(): continue
    rid,doi=line.split()
    try:
        req=urllib.request.Request('https://api.crossref.org/works/'+doi,headers={'User-Agent':'reference-check/1.0'})
        m=json.load(urllib.request.urlopen(req,timeout=30))['message']
        out[rid]={'doi':doi,'ok':True,'title':m.get('title'),'author':[(a.get('given'),a.get('family'),a.get('name')) for a in m.get('author',[])],
          'container':m.get('container-title'),'short':m.get('short-container-title'),'vol':m.get('volume'),'issue':m.get('issue'),'page':m.get('page'),'article':m.get('article-number'),
          'issued':m.get('issued',{}).get('date-parts'),'type':m.get('type'),'event':(m.get('event') or {}).get('name'),'loc':(m.get('event') or {}).get('location'),'publisher':m.get('publisher'),'pub-loc':m.get('publisher-location')}
    except Exception as e:
        out[rid]={'doi':doi,'ok':False,'err':str(e)}
    time.sleep(0.3)
json.dump(out,open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,v in out.items(): print(k,v['ok'],v.get('title'),v.get('err',''))
