from PIL import Image, ImageDraw, ImageFont
W,H=2400,800
im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
F='C:/Windows/Fonts/'
fb=ImageFont.truetype(F+'arialbd.ttf',42); fr=ImageFont.truetype(F+'arial.ttf',35); fl=ImageFont.truetype(F+'arialbd.ttf',40)
boxes=[("Observed information",["Images, sensors,","expert records","(state, action, intent)"]),
       ("AI advice",["Sources, content,","timing, format,","uncertainty"]),
       ("Maker judgment",["Accept / modify / reject;","correct / preserve /","extend a variation"]),
       ("Learning evaluation",["With support vs.","independent performance,","retention, transfer"])]
bw,bh,gap,y0=530,360,60,200
x0=(W-(4*bw+3*gap))//2
X=lambda i:x0+i*(bw+gap)
cols=['#E8EEF8','#EAF4EA','#FBF1E2','#F3E8F5']
P='#6A1B9A'
for i,(t,lines) in enumerate(boxes):
    x=X(i)
    d.rounded_rectangle([x,y0,x+bw,y0+bh],radius=24,fill=cols[i],outline='#333333',width=4)
    tw=d.textlength(t,font=fb); d.text((x+(bw-tw)/2,y0+40),t,font=fb,fill='black')
    for j,l in enumerate(lines):
        lw=d.textlength(l,font=fr); d.text((x+(bw-lw)/2,y0+135+j*54),l,font=fr,fill='#222222')
    if i<3:
        ax=x+bw+6; ay=y0+bh/2
        d.line([ax,ay,ax+gap-20,ay],fill='#333333',width=6)
        d.polygon([(ax+gap-10,ay),(ax+gap-30,ay-16),(ax+gap-30,ay+16)],fill='#333333')
def top(xa,xb,label):
    y=y0-40; d.line([xa,y+28,xa,y,xb,y,xb,y+28],fill=P,width=5)
    lw=d.textlength(label,font=fl); d.text(((xa+xb)/2-lw/2,y-58),label,font=fl,fill=P)
def bot(xa,xb,label):
    y=y0+bh+40; d.line([xa,y-28,xa,y,xb,y,xb,y-28],fill=P,width=5)
    lw=d.textlength(label,font=fl); d.text(((xa+xb)/2-lw/2,y+16),label,font=fl,fill=P)
top(X(0)+20,X(1)+bw-20,"RQ1  Observation and representation")
bot(X(1)+20,X(2)+bw-20,"RQ2  Feedback and judgment")
top(X(3)+20,X(3)+bw-20,"RQ3  Performance and learning")
im.save('fig1.png',dpi=(300,300))
# trim surrounding whitespace (same crop as used for the submitted draft)
im = Image.open('fig1.png'); im.crop((0, 40, 2400, 700)).save('fig1.png', dpi=(300, 300))
