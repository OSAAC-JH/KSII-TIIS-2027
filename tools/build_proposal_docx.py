# Usage: python tools/build_proposal_docx.py <unpacked TIIS_Template_final_2020.docx dir> <fig1.png> <output.docx>
# The TIIS template is not redistributed here; unzip your own copy of TIIS_Template_final_2020.docx first.
# Build the TIIS proposal draft on top of the TIIS template package.
# Keeps template styles/numbering/headers/footers/page setup; replaces the body.
import re, sys, shutil, zipfile, os
from xml.sax.saxutils import escape
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
TPL, FIG, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
WORK = "build_pkg"
shutil.rmtree(WORK, ignore_errors=True)
shutil.copytree(TPL, WORK)

# ---------------------------------------------------------------- references
DOI = {
 "R01": "10.1145/3715336.3735844", "R02": "10.1145/3802842.3802892", "R03": "10.3390/app15105408",
 "R04": "10.1145/3749496", "R05": "10.3390/electronics15061294", "R06": "10.1145/3800645.3812941",
 "R07": "10.1145/3664209", "R08": "10.3390/arts15110252", "R09": "10.1080/10447318.2026.2732483",
 "R10": "10.1007/s00146-026-03379-x", "R11": "10.1145/2893491", "R12": "10.20668/adada.29.2_45",
 "R13": "10.1016/j.edurev.2018.07.001", "R14": "10.1007/978-3-031-98197-5_39",
 "R15": "10.1080/14626268.2023.2174557", "R16": "10.3390/su16166973", "R17": "10.1145/3706598.3713281",
 "R18": "10.1080/14606925.2024.2303236", "R19": "10.1145/3772363.3798619", "R20": "10.1162/LEON_a_00603",
 "R21": "10.18653/v1/2026.acl-long.604", "R22": "10.1609/aaaiss.v6i1.36054", "R23": "10.1177/0887302X261487373",
 "R24": "10.1145/3706598.3714188", "R25": "10.1145/3746059.3747770", "R26": "10.3758/s13423-012-0333-8",
 "R27": "10.1177/1745691615569000", "R28": "10.1136/bmj.l6890", "R29": "10.3837/tiis.2026.04.027",
 "R30": "10.15187/adr.2022.11.35.4.73",
}
# text with *italic* segment for the venue
REF = {
 "R01": 'H. Ji, P. Hu, and D. EL-Zanfaly, “Reshaping Craft Learning: Insights from Designing an AI-Augmented MR System for Wheel-Throwing,” in *Proc. of the 2025 ACM Designing Interactive Systems Conference (DIS ’25)*, Madeira, Portugal, pp. 2549-2573, 2025.',
 "R02": 'T. Akbas, A. Glushkova, and S. Manitsaris, “Cross-Modal Retrieval-Augmented Generation for Craft Gestures Learning: Enabling Dialogue with Multimodal Pedagogical Contents,” in *Proc. of the 10th Int. Conf. on Movement and Computing (MOCO ’26)*, Montpellier, France, pp. 1-5, 2026.',
 "R03": 'X. Zabulis, N. Partarakis, V. Manikaki, I. Demeridou, A. Dubois, I. Moreno, V. Bartalesi, N. Pratelli, C. Meghini, S. Manitsaris, and G. Senteri, “A Digitally Enhanced Ethnography for Craft Action and Process Understanding,” *Applied Sciences*, vol. 15, no. 10, Art. no. 5408, May 2025.',
 "R04": 'X. Yu, L. Hu, B. Reichman, D. Chu, R. Chandrupatla, X. Zhang, L. Heck, and T. S. Rosing, “SensorChat: Answering Qualitative and Quantitative Questions during Long-Term Multimodal Sensor Interactions,” *Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.*, vol. 9, no. 3, pp. 1-35, Sep. 2025.',
 "R05": 'N. Partarakis, P. Koutlemanis, I. Demeridou, D. Zourarakis, A. Makris, A. Roussos, and X. Zabulis, “Externalizing Tacit Craft Knowledge Through Semantic Graphs and Real-Time VR Simulation,” *Electronics*, vol. 15, no. 6, Art. no. 1294, Mar. 2026.',
 "R06": 'S. Liu, H. C. S. Mok, L. Ling, T. Klein, and R. LC, “ClayScape: A GenAI-Supported Workflow for Designing Chinese Style Ceramics with Clay 3D Printing,” in *Proc. of the 2026 ACM Designing Interactive Systems Conference (DIS ’26)*, Singapore, pp. 2014-2036, 2026.',
 "R07": 'S. R. Elran and A. R. Zoran, “Probabilistic Craft—Materialization of Generated Images Using Digital and Traditional Craft,” *Proc. ACM Comput. Graph. Interact. Tech.*, vol. 7, no. 4, pp. 1-10, Jul. 2024.',
 "R08": 'S. Fışgın Korkmaz, “Ceramic Design and the Role of Generative AI: A Practice-Based Exploration,” *Arts*, vol. 15, no. 11, Art. no. 252, Oct. 2026.',
 "R09": 'H. Xu, J. Li, N. Hou, X. Ding, and G. Liu, “Result-Oriented Generation Meets Process-Oriented Creation: Understanding the Tension Between Generative AI and Craft Practice,” *Int. J. Hum.–Comput. Interact.*, pp. 1-24, Sep. 2026 (published online).',
 "R10": 'A. R. Zoran, “More than We Can Make: Generative AI, Artistic Forms, and Artistic Becoming,” *AI & Society*, Oct. 2026 (published online).',
 "R11": 'A. Zoran, “A Manifest for Digital Imperfection,” *XRDS: Crossroads, The ACM Magazine for Students*, vol. 22, no. 3, pp. 22-27, 2016.',
 "R12": 'S. Ahn, “Generative Restoration of Traditional Ceramics,” *International Journal of Asia Digital Art and Design Association*, vol. 29, no. 2, pp. 45-52, 2025.',
 "R13": 'B. H. Limbu, H. Jarodzka, R. Klemke, and M. Specht, “Using Sensors and Augmented Reality to Train Apprentices Using Recorded Expert Performance: A Systematic Literature Review,” *Educational Research Review*, vol. 25, pp. 1-22, Nov. 2018.',
 "R14": 'H.-C. Lin, “A Generative AI-Supported Flipped Classroom Model for Personalized Skill Training in Engineering Woodworking Education,” in *Innovative Technologies and Learning (ICITL 2025), Lecture Notes in Computer Science*, vol. 15914, Cham, Switzerland: Springer, pp. 366-376, 2025.',
 "R15": 'H. Vartiainen and M. Tedre, “Using Artificial Intelligence in Craft Education: Crafting with Text-to-Image Generative Models,” *Digital Creativity*, vol. 34, no. 1, pp. 1-21, 2023.',
 "R16": 'D. Jung and S. Suh, “Enhancing Soft Skills through Generative AI in Sustainable Fashion Textile Design Education,” *Sustainability*, vol. 16, no. 16, Art. no. 6973, Aug. 2024.',
 "R17": 'Y. Tao, X. Fu, J. Wu, Z. Bian, A. Zhu, Q. Bao, W. Zheng, Y. Wang, B. Zhu, C. Yang, and C. Zhou, “AIFiligree: A Generative AI Framework for Designing Exquisite Filigree Artworks,” in *Proc. of the 2025 CHI Conf. on Human Factors in Computing Systems (CHI ’25)*, Yokohama, Japan, pp. 1-18, 2025.',
 "R18": 'X. Wu and L. Li, “An Application of Generative AI for Knitted Textile Design in Fashion,” *The Design Journal*, vol. 27, no. 2, pp. 270-290, 2024.',
 "R19": 'K. Nie, Z. Wang, M. Guo, and H. Xiong, “DisCraft: Exploring the Dis-embodiment of Bamboo Weaving in Generative AI,” in *Extended Abstracts of the 2026 CHI Conf. on Human Factors in Computing Systems (CHI EA ’26)*, Barcelona, Spain, pp. 1-5, 2026.',
 "R20": 'A. Zoran, “Hybrid Basketry: Interweaving Digital Practice within Contemporary Craft,” *Leonardo*, vol. 46, no. 4, pp. 324-331, Aug. 2013.',
 "R21": 'P. Li, X. Huang, T. Hua, and N. V. Chawla, “CrochetBench: Can Vision-Language Models Move from Describing to Doing in Crochet Domain?,” in *Proc. of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, San Diego, CA, USA, pp. 13229-13251, 2026.',
 "R22": 'R. Dias and K. Karim, “Translation of User Crochet Patterns to CrochetPARADE Syntax Using Large Language Models,” *Proc. AAAI Symp. Ser.*, vol. 6, no. 1, pp. 200-208, Aug. 2025.',
 "R23": 'H. Park and S. Kim, “Development of an LLM-Based Multi-Agent System for Sewing Sequence Planning,” *Clothing and Textiles Research Journal*, Sep. 2026 (OnlineFirst).',
 "R24": 'C. Li, G. Wu, G. Y.-Y. Chan, D. G. Turakhia, S. Castelo Quispe, D. Li, L. Welch, C. Silva, and J. Qian, “Satori 悟り: Towards Proactive AR Assistant with Belief-Desire-Intention User Modeling,” in *Proc. of the 2025 CHI Conf. on Human Factors in Computing Systems (CHI ’25)*, Yokohama, Japan, pp. 1-24, 2025.',
 "R25": 'K. Pu, T. Zhang, N. Sendhilnathan, S. Freitag, R. Sodhi, and T. R. Jonker, “ProMemAssist: Exploring Timely Proactive Assistance Through Working Memory Modeling in Multi-Modal Wearable Devices,” in *Proc. of the 38th Annual ACM Symp. on User Interface Software and Technology (UIST ’25)*, Busan, Republic of Korea, pp. 1-19, 2025.',
 "R26": 'R. Sigrist, G. Rauter, R. Riener, and P. Wolf, “Augmented Visual, Auditory, Haptic, and Multimodal Feedback in Motor Learning: A Review,” *Psychon. Bull. Rev.*, vol. 20, no. 1, pp. 21-53, 2013.',
 "R27": 'N. C. Soderstrom and R. A. Bjork, “Learning Versus Performance: An Integrative Review,” *Perspect. Psychol. Sci.*, vol. 10, no. 2, pp. 176-199, Mar. 2015.',
 "R28": 'M. Campbell, J. E. McKenzie, A. Sowden, S. V. Katikireddi, S. E. Brennan, S. Ellis, J. Hartmann-Boyce, R. Ryan, S. Shepperd, J. Thomas, V. Welch, and H. Thomson, “Synthesis Without Meta-analysis (SWiM) in Systematic Reviews: Reporting Guideline,” *BMJ*, vol. 368, Art. no. l6890, Jan. 2020.',
 "R29": 'J. H. Lee and J. Lee, “Generative AI Features and Limitations in Support of Inclusive XR Immersive Learning Environments for Aging and Creative Community Applications,” *KSII Transactions on Internet and Information Systems*, vol. 20, no. 4, pp. [TBD], Apr. 2026.',
 "R30": 'J. H. Lee and H.-K. Lee, “A Study on the Strategic Collaboration System between Craftspeople and Enterprises for Sustainable Development in the Center of Creative Metropolitan City,” *Archives of Design Research*, vol. 35, no. 4, pp. 73-89, Nov. 2022.',
}

order = []          # citation order of first appearance
def cite_nums(keys):
    for k in keys:
        if k not in order:
            order.append(k)
    nums = sorted(order.index(k) + 1 for k in keys)
    # compress ranges: [1]-[3], [5]
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(f"[{nums[i]}]" if j == i else (f"[{nums[i]}], [{nums[j]}]" if j == i + 1 else f"[{nums[i]}]-[{nums[j]}]"))
        i = j + 1
    return ", ".join(out)

# ---------------------------------------------------------------- rels
rels_path = f"{WORK}/word/_rels/document.xml.rels"
rels = open(rels_path, encoding="utf-8").read()
rid_n = [100]
def new_rel(typ, target, external=True):
    rid_n[0] += 1
    rid = f"rIdP{rid_n[0]}"
    global rels
    ext = ' TargetMode="External"' if external else ""
    rels = rels.replace("</Relationships>",
        f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/{typ}" Target="{escape(target)}"{ext}/></Relationships>')
    return rid

# ---------------------------------------------------------------- run builders
CAP = '<w:rStyle w:val="figtabletextboldblueChar"/>'
KWS = '<w:rStyle w:val="KeywordstitleChar"/>'
HL = re.compile(r"(\[TBD[^\]]*\])")
def run(text, rpr=""):
    out = []
    for part in HL.split(text):
        if not part:
            continue
        p = rpr + ('<w:highlight w:val="yellow"/>' if HL.fullmatch(part) else "")
        out.append(f'<w:r>{"<w:rPr>"+p+"</w:rPr>" if p else ""}<w:t xml:space="preserve">{escape(part)}</w:t></w:r>')
    return "".join(out)

TOK = re.compile(r"(\{[R0-9, ]+\}|\*\*.+?\*\*|\*[^*]+?\*)")
def rich(text, base="", in_table=False):
    out = []
    for tok in TOK.split(text):
        if not tok:
            continue
        if tok.startswith("{"):
            keys = [k.strip() for k in tok[1:-1].split(",")]
            size = '<w:sz w:val="20"/>' if in_table else ""
            out.append(run(cite_nums(keys), '<w:rStyle w:val="bodyreferencenumChar"/>' + size))
        elif tok.startswith("**"):
            out.append(run(tok[2:-2], base + "<w:b/><w:bCs/>"))
        elif tok.startswith("*"):
            out.append(run(tok[1:-1], base + "<w:i/><w:iCs/>"))
        else:
            out.append(run(tok, base))
    return "".join(out)

def P(style, text="", ppr_extra="", base=""):
    return f'<w:p><w:pPr><w:pStyle w:val="{style}"/>{ppr_extra}</w:pPr>{rich(text, base)}</w:p>'

body = []
def H1(t, page_break=False):
    br = '<w:r><w:br w:type="page"/></w:r>' if page_break else ""
    body.append(f'<w:p><w:pPr><w:pStyle w:val="heading1"/></w:pPr>{br}{run(t)}</w:p>')
    state["first"] = True
def H2(t):
    body.append(P("heading2", t)); state["first"] = True
state = {"first": True}
def para(t):
    body.append(P("body" if state["first"] else "body129", t)); state["first"] = False
def blank(style="body"):
    body.append(f'<w:p><w:pPr><w:pStyle w:val="{style}"/></w:pPr></w:p>')

TEXT_W = 8221
def table(caption_no, caption, header, rows, widths, align_left_cols=()):
    blank()
    body.append(f'<w:p><w:pPr><w:pStyle w:val="fig"/><w:keepNext/></w:pPr>'
                f'{run(f"Table {caption_no}. ", CAP)}{rich(caption)}</w:p>')
    total = sum(widths)
    b = lambda top, bottom: (f'<w:tcBorders><w:top w:val="{top}" w:sz="4" w:space="0" w:color="auto"/>'
        f'<w:left w:val="single" w:sz="4" w:space="0" w:color="auto"/><w:bottom w:val="{bottom}" w:sz="4" w:space="0" w:color="auto"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="auto"/></w:tcBorders>')
    x = ['<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="center"/><w:tblBorders>' % total +
         ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="auto"/>' for s in ["top","left","bottom","right","insideH","insideV"]) +
         '</w:tblBorders><w:tblLayout w:type="fixed"/><w:tblLook w:val="00A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="0"/></w:tblPr><w:tblGrid>' +
         ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths) + '</w:tblGrid>']
    x.append('<w:tr><w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>' + ''.join(
        f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{b("single","double")}<w:vAlign w:val="center"/></w:tcPr>'
        f'<w:p><w:pPr><w:pStyle w:val="tabletitle"/></w:pPr>{run(h)}</w:p></w:tc>' for h, w in zip(header, widths)) + '</w:tr>')
    for ri, r in enumerate(rows):
        top = "double" if ri == 0 else "single"
        cells = []
        for ci, (c, w) in enumerate(zip(r, widths)):
            jc = '<w:jc w:val="left"/>' if ci in align_left_cols else ""
            paras = c if isinstance(c, list) else [c]
            ps = "".join(f'<w:p><w:pPr><w:pStyle w:val="fig"/>{jc}</w:pPr>{rich(pt, in_table=True)}</w:p>' for pt in paras)
            cells.append(f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{b(top,"single")}<w:vAlign w:val="center"/></w:tcPr>{ps}</w:tc>')
        x.append('<w:tr><w:trPr><w:cantSplit/></w:trPr>' + "".join(cells) + '</w:tr>')
    x.append('</w:tbl>')
    body.append("".join(x))
    blank()
    state["first"] = True

def figure(path, no, caption, width_cm=14.0):
    rid = new_rel("image", "media/fig1.png", external=False)
    shutil.copy(path, f"{WORK}/word/media/fig1.png")
    w, h = Image.open(path).size
    cx = int(width_cm * 360000); cy = int(cx * h / w)
    blank()
    body.append(
        f'<w:p><w:pPr><w:pStyle w:val="bodycenter"/><w:keepNext/></w:pPr><w:r><w:drawing>'
        f'<wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="501" name="Figure {no}"/>'
        f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
        f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="501" name="fig{no}.png"/><pic:cNvPicPr/></pic:nvPicPr>'
        f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
        f'</a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>')
    body.append(f'<w:p><w:pPr><w:pStyle w:val="fig"/></w:pPr>'
                f'{run(f"Fig. {no}.  ", CAP)}{rich(caption)}</w:p>')
    blank()
    state["first"] = True

# ================================================================= CONTENT
TITLE = "Internet-Connected Generative AI for Human Making in Craft: A Critical Review of In-Process Feedback and Learning"
body.append(f'<w:p><w:pPr><w:pStyle w:val="11"/></w:pPr>{run(TITLE)}</w:p>')
body.append('<w:p/>')
sup = '<w:vertAlign w:val="superscript"/>'
body.append(f'<w:p><w:pPr><w:pStyle w:val="Author"/></w:pPr>{run("JooHyun Lee")}{run("1*", sup)}{run(" and Junheon Lee")}{run("2", sup)}</w:p>')
num = '<w:rStyle w:val="AffiliationnumChar"/>'
for n, lines in [("1", ["Division of Culture & Design Management, UIC, Yonsei University, 85, Songdogwahak-ro, Yeonsu-gu,",
                        "Incheon, 21983, South Korea", "[e-mail: joohyunlee01@yonsei.ac.kr]"]),
                 ("2", ["AI & Digital Division, KB Securities, 50, Yeouinaru-ro, Yeongdeungpo-gu,",
                        "Seoul, 07328, South Korea", "[e-mail: junheon.lee@kbfg.com]"])]:
    body.append(f'<w:p><w:pPr><w:pStyle w:val="Affiliation"/></w:pPr>{run(n, num)}{run(" " + lines[0])}</w:p>')
    for l in lines[1:]:
        body.append(f'<w:p><w:pPr><w:pStyle w:val="Affiliation"/></w:pPr>{run(l)}</w:p>')
body.append(f'<w:p><w:pPr><w:pStyle w:val="Affiliation"/></w:pPr>{run("*Corresponding author: JooHyun Lee")}</w:p>')
body.append(f'<w:p><w:pPr><w:pStyle w:val="Affiliation"/></w:pPr>{run("[TBD: author list, order, and corresponding author are carried over from TIIS-S1-2025-Nov-1354.R1 and must be confirmed for this paper]")}</w:p>')
body.append('<w:p/>'); body.append('<w:p/>')
body.append(P("Abstracttitle", "Abstract"))
body.append('<w:p/>')
ABSTRACT = ("Generative artificial intelligence now produces craft images, design variations, and making instructions, and recent systems "
 "deliver advice to people while they work with physical materials. Existing studies, however, test different abilities and report "
 "different outcomes, so it remains unclear what information such advice is based on and how it relates to the maker’s own judgment "
 "and learning. This proposed survey is a follow-up to our earlier review of generative artificial intelligence in inclusive extended "
 "reality learning environments, and it narrows that work to physical craft making. It examines what information internet-connected "
 "generative systems observe during making, what supports their feedback, how makers decide to correct, preserve, or extend a "
 "variation, and how studies evaluate changes in independent understanding, judgment, and skill. The review compares technical "
 "systems, physical craft cases, and education studies with a common extraction scheme that records the making context, information "
 "sources, model and internet use, feedback characteristics, human decisions, and learning measures. The expected results are an "
 "evidence map that links observed information to advice, maker decisions, and learning tests, together with design and evaluation "
 "items for state data, information sources, feedback timing, maker control, and learning.")
body.append(P("AbstractKeywordsText", ABSTRACT))
blank(); blank()
body.append(f'<w:p><w:pPr><w:pStyle w:val="AbstractKeywordsText"/></w:pPr>{run("Keywords:", KWS)}'
            f'{run(" Craft Making, Generative AI, In-Process Feedback, Learning Evaluation, Material Judgment, Wearable Interfaces")}</w:p>')

# ---- 1. Introduction
H1("1. Introduction", page_break=True)
H2("1.1 Background and Motivation")
para("Generative AI (GenAI) creates craft images and making instructions, and several recent systems deliver advice while a person "
     "is throwing clay on a wheel, working with glass, or following a craft procedure {R01, R02}. In craft, making is more than the "
     "production of an artifact: people observe, judge, and adjust materials during making. Makers read resistance, moisture, and "
     "deformation to choose the next action, and they assess both the functional effect of a variation and its relation to their "
     "artistic intent {R01, R08, R09}.")
para("On the system side, AI collects craft information from images, sensors, and expert records, and it uses these observations "
     "together with prior knowledge to generate explanations and suggested changes {R01, R03}. Whether such feedback is valid "
     "therefore depends on how it is linked to the information the system actually observed and to the making context. Studies to "
     "date, however, test different abilities and report different outcomes, which makes it difficult to judge what an AI system "
     "observes and what the maker decides. This proposal addresses that gap.")
H2("1.2 Relation to Our Previous TIIS Survey")
para("This proposal is a follow-up to our previous survey in KSII Transactions on Internet and Information Systems, “Generative AI "
     "Features and Limitations in Support of Inclusive XR Immersive Learning Environments for Aging and Creative Community "
     "Applications” (manuscript ID TIIS-S1-2025-Nov-1354.R1) {R29}. That survey examined how GenAI influences inclusive immersive "
     "learning built on Extended Reality (XR). It identified structural limitations of current generative models, namely reasoning "
     "inconsistency, contextual drift, multimodal desynchronization, strategic adaptation gaps, and ethical opacity, and it proposed a "
     "multidimensional evaluation model covering cross-modal fidelity, semantic integrity, cognitive stability, contextual continuity, "
     "and adaptive transparency {R29}.")
para("The present proposal carries this work into physical craft making along three lines, summarized in Table 1. First, the "
     "questions of multimodal alignment and feedback reliability raised in the previous survey are made concrete as the consistency "
     "between observed material states and AI advice {R29}. Second, research on the contributions of craftspeople to design and "
     "production {R30} motivates the question of who interprets materials and who controls changes. Third, the tension between "
     "result-focused generation and repeated, process-oriented making {R09} calls for comparing feedback functions with the "
     "evaluation evidence that each study provides. The new review thus connects technical reliability with material judgment in "
     "craft within a single analysis.")
table(1, "Link to prior research",
      ["Prior work", "Main issue", "Extension in this study"],
      [["GenAI and inclusive XR learning {R29}", "Multimodal alignment and feedback reliability", "Compare material states with AI advice"],
       ["Craftsperson roles and collaboration {R30}", "Craftsperson contributions to design and production", "Identify who interprets materials and controls changes"],
       ["GenAI and craft practice {R09}", "Result-focused generation and repeated making", "Compare feedback functions and evaluation evidence"]],
      [2600, 2800, 2800])
H2("1.3 Research Questions")
para("The review is organized around three research questions (RQs). Fig. 1 shows how they follow the evidence chain from observed "
     "information to AI advice, maker judgment, and learning evaluation.")
para("**RQ1 (Observation and representation).** How does AI observe and represent making actions, material states, and maker "
     "intent? {R01, R02, R03, R05}")
para("**RQ2 (Feedback and judgment).** What supports AI advice, and how does the maker decide to change, preserve, or extend a "
     "variation? {R01, R08, R09, R12, R23}")
para("**RQ3 (Performance and learning).** What changes in independent understanding, judgment, or skill do studies test after AI "
     "support, and how do they evaluate them? {R01, R05, R14, R15, R16, R27}")
figure(FIG, 1, "Analytical frame of the proposed review. Evidence is traced from the information an AI system observes, through the "
       "advice it generates and the maker’s judgment, to the evaluation of learning (RQ1–RQ3).")
H2("1.4 Contributions and Organization")
para("The unit of analysis is the feedback function that each study implements and the test of making or learning that it reports. "
     "For internet and information systems, the review analyzes the consistency between observed data and generated advice, and it "
     "relates source access, processing location, and latency to feedback. For craft making and learning, it analyzes decisions about "
     "materials, imperfection, and maker intent, and it distinguishes outcomes obtained with support from evidence of independent "
     "skill {R09, R13, R27, R28, R29, R30}.")
para("The remainder of this proposal is organized as follows. Section 2 defines the scope of the review and the roles of the "
     "literature. Section 3 describes the search, data extraction, and synthesis methods. Section 4 presents preliminary evidence from "
     "representative studies. Section 5 summarizes the expected results, and Section 6 concludes by relating the proposal to the "
     "outcomes of our previous survey. A proposed writing roadmap for the Editing Staff is attached after the references.")

# ---- 2. Scope
H1("2. Scope of the Review")
H2("2.1 Study Scope")
para("The review covers four areas, listed in Table 2. Wearables are analyzed as input and output devices, and physical human making "
     "remains at the center of the analysis {R01, R02, R05, R06, R09, R20, R24}.")
table(2, "Study scope",
      ["Area", "Objects of analysis", "Comparison basis"],
      [["Human making", "People work with physical materials and tools", "Current state, goal, and next action"],
       ["Feedback and learning", "Live guidance, questions, and expert videos", "Process timing and sources for advice"],
       ["Generation and materialization", "Makers turn images or 3D models into objects", "Process limits, changes, and human intervention"],
       ["Technical and conceptual context", "Sensing, knowledge, virtual training, and craftsmanship", "Evidence of implementation, making, and learning"]],
      [2300, 3000, 2900])
H2("2.2 Roles of the Literature")
para("The proposal stage identified 30 seed studies. Each study is assigned an analysis role according to the evidence it can "
     "provide (Table 3). The final size of the corpus after the systematic search is [TBD].")
table(3, "Roles of the literature",
      ["Analysis area", "Evidence to extract", "Studies"],
      [["Making and learning support", "Feedback functions and learning measures", "{R01, R02, R14, R15, R16}"],
       ["Observation and knowledge", "Sensing, expert records, and knowledge models", "{R03, R04, R05, R13}"],
       ["Design and materialization", "Appearance, procedures, and process limits", "{R06, R07, R08, R17, R18, R19}"],
       ["Craftsmanship and imperfection", "Material interpretation and maker control", "{R09, R10, R11, R12, R20}"],
       ["Procedures and interaction", "Execution tests and assistance timing", "{R21, R22, R23, R24, R25}"],
       ["Classification and synthesis", "Feedback, learning, and evidence synthesis", "{R26, R27, R28}"]],
      [2500, 3300, 2400])

# ---- 3. Methodology
H1("3. Review Methodology")
H2("3.1 Literature Search and Selection")
para("Studies will be searched in the ACM Digital Library, IEEE Xplore, Scopus, and Web of Science, and references in key papers "
     "and prior reviews will be traced {R13}. The search combines three concepts, craft × GenAI × feedback, learning, or making, with "
     "craft terms such as ceramic*, glassblow*, woodwork*, weav*, knit*, crochet*, filigree, and sewing. Studies are included when "
     "they connect GenAI with craft making, learning, or material judgment, and each included study is given a role according to the "
     "systems, cases, and evaluations it reports. For every search, the queries, the selection reasons, duplicate systems, and the "
     "data sources are recorded {R28}. The search period, the exact query string for each database, and the screening counts are "
     "[TBD].")
H2("3.2 Data Extraction")
para("A common extraction scheme with six data groups is applied to every study (Table 4) {R01, R02, R05, R08, R21}.")
table(4, "Data extraction scheme",
      ["Data group", "Fields to extract"],
      [["Task and making context", "Material, tool, goal, process phase, and physical or virtual making"],
       ["Information source", "Direct measures, self-reports, expert accounts, simulations, and model estimates"],
       ["AI and internet use", "Model, version, study date, API, corpus, source, and source location"],
       ["Feedback", "Target, content, timing, format, support, and uncertainty"],
       ["Human judgment", "Acceptance, changes, rejection, correction, preservation, extension, and reasons"],
       ["Evaluation and learning", "Sample unit, denominator, comparator, measure, timing, independent performance, retention, and transfer"]],
      [2600, 5600], align_left_cols=(1,))
H2("3.3 Cross-Study Synthesis")
para("Because the included studies use heterogeneous designs and measures, results are synthesized without meta-analysis: "
     "compatible outcomes are grouped and the comparison method is stated explicitly {R28}. Four syntheses are planned.")
para("**Observation and advice.** A source map from observation to representation and advice {R01, R02, R03, R04, R05}.")
para("**Imperfection and control.** A case matrix of causes, intent, responses, and decision makers {R01, R07, R08, R09, R12, R20}.")
para("**Making and validation.** A comparison of the abilities each study tests and the human interventions it reports "
     "{R06, R17, R18, R21, R22, R23}.")
para("**Performance and learning.** An evaluation map that separates performance with support from independent performance, "
     "retention, and transfer {R01, R05, R14, R16, R27}.")

# ---- 4. Preliminary evidence
H1("4. Preliminary Evidence from Representative Studies")
H2("4.1 Feedback during Making: Wheel Throwing")
para("An AI-augmented Mixed Reality (MR) system for wheel throwing illustrates the full feedback loop {R01}. An external camera "
     "captures the clay outline, a program compares the current shape with the target shape, an API generates advice from the shape "
     "information, and a Quest 3 headset delivers text, audio, and spatial guidance. Twenty participants (14 novices and 6 "
     "experienced users) made a vase in 30 minutes and rated the perceived feedback accuracy at 2.79 out of 5; they reported missing "
     "context such as water and hand pressure {R01}. The evaluation focused on session experience and subjective ratings. The review "
     "will analyze how shape observations support advice about materials.")
H2("4.2 Expert Knowledge and State Diagnosis")
para("A cross-modal retrieval-augmented generation system for glass craft links expert explanations to video segments, adjusts "
     "learner queries to the terms in the expert corpus, and retrieves sources and video segments to generate an answer {R02}. Its "
     "evaluation used four videos, four expert annotations, and 33 synthetic questions, and query refinement increased the mean "
     "query–document cosine similarity by 0.059 {R02}. Retrieval of expert records and observation of the learner’s current state "
     "should therefore be separated, and retrieval alignment and context-specific advice should be evaluated as separate targets "
     "{R02, R22}.")
para("Related systems show how observation errors can propagate. SensorChat separates question analysis, sensor queries, and answer "
     "generation, and it was evaluated on SensorQA and on records from eight users over one to three days {R04}. A desktop virtual "
     "metal-stippling system that links expert rules to a physical simulation reached correct-action rates of 74.2% with guidance and "
     "61.8% in examination mode among twelve novices {R05}; such virtual results must be separated from evidence of physical craft "
     "skill.")
H2("4.3 Tests of Making Feasibility")
para("Studies that generate designs or procedures test different abilities (Table 5). For example, CrochetBench contains 6,085 "
     "patterns across 55 categories and tests nine base models; its results show a gap between recognition and executable procedure "
     "generation {R21}. Translation of user crochet patterns into a formal language reached a best syntactic accuracy of 74%, with "
     "terminology and reference errors {R22}. Each measure must therefore be reported with the ability and scope that it tests.")
table(5, "Tests of making feasibility",
      ["Evaluation target", "Evaluation focus", "Sources"],
      [["Craft appearance", "Form, texture, and cultural expression", "{R17, R18, R19}"],
       ["Feasibility judgment", "Expert judgments of material and process limits", "{R08, R17, R23}"],
       ["Procedure validity", "Instruction syntax, structure, and execution", "{R21, R22}"],
       ["Physical making", "Changes and interventions for physical production", "{R06, R07, R08, R20}"],
       ["Independent learning", "Independent performance, retention, and transfer", "{R14, R27}"]],
      [2400, 3600, 2200])
H2("4.4 Material Judgment and Imperfection")
para("Craft cases show that a deviation from the target is not always an error to be corrected. Table 6 lists the decisions that "
     "the review will analyze. For each case, the cause, the functional effect, the maker’s intent, and the decision maker are coded "
     "together {R01, R08, R09, R11, R12, R20}.")
table(6, "Material judgment and imperfection",
      ["Case in the literature", "Decision to analyze", "Study"],
      [["Makers choose another form after missing the target", "Goal deviation and reinterpretation", "{R01}"],
       ["An instructor describes an intentional wave pattern", "Artistic intent and acceptance of variation", "{R01}"],
       ["The maker adjusts the design to material limits", "Feasibility and visual goals", "{R08}"],
       ["The study uses fracture edges for new forms", "Preservation and extension of material loss", "{R12}"]],
      [3400, 3300, 1500])
H2("4.5 Evaluation of Learning")
para("Performance during practice can differ from lasting learning {R27}. The review therefore separates four evaluation areas "
     "(Table 7) and synthesizes technical accuracy, satisfaction, making outcomes, and learning as separate results "
     "{R01, R05, R14, R15, R16, R27, R28}. The seed studies illustrate the range: a GenAI-supported woodworking course followed 32 "
     "university students for one semester {R14}; a textile design course recruited 35 students, of whom 27 completed the surveys "
     "{R16}; and a craft teacher-education workshop involved ten pre-service teachers and five teacher educators {R15}.")
table(7, "Evaluation of learning",
      ["Evaluation area", "Question about the learner", "Evidence to extract"],
      [["Performance with support", "Does AI support task completion?", "Accuracy, artifacts, time, and user experience"],
       ["Independent performance", "Can the learner repeat the task alone?", "Guidance conditions, actions, and error explanations"],
       ["Retention", "Does the learner retain the skill?", "Test delay and later performance"],
       ["Transfer", "Can the learner adapt to a new task?", "New tasks, conditions, and adaptation"]],
      [2400, 2900, 2900])
H2("4.6 Roles of Internet Access and Wearables")
para("The review separates sensing devices from feedback interfaces and traces the actual role of internet access in four "
     "information processes: observation and recording through camera, sensor, and expert video inputs {R01, R02, R03, R04}; "
     "inference and knowledge access through APIs, processing location, retrieval, and answer sources {R01, R02, R04}; feedback "
     "delivery through MR, audio, and text, together with response latency {R01, R24, R26}; and intervention in the task flow, "
     "including timing, deferral, rejection, and workload {R24, R25}. For example, a proactive AR assistant was compared with an "
     "expert-designed Wizard-of-Oz system by 16 participants {R24}, and a working-memory model for assistance timing was compared "
     "with an LLM baseline by 12 participants {R25}.")

# ---- 5. Expected results
H1("5. Expected Results and Contributions")
H2("5.1 Expected Results")
para("The review is expected to produce four results {R01, R02, R08, R09, R21, R27}.")
para("**Information and feedback map.** For each type of advice, the observations and expert sources on which it relies.")
para("**Classification of material decisions.** A comparison of the reasons and decision authority for correction, preservation, "
     "and extension.")
para("**Learning evidence map.** A distinction between outcomes obtained with support and evidence of independent performance, "
     "retention, and transfer.")
para("**Design and evaluation items.** Tests for state data, information sources, feedback timing, maker control, and learning.")
H2("5.2 Contributions")
para("For internet and information systems, the review contributes an analysis of the consistency between observed data and "
     "generated advice, and of how source access, processing location, and latency relate to feedback. For craft making and "
     "learning, it contributes an analysis of decisions about materials, imperfection, and maker intent, and a clear boundary "
     "between support outcomes and evidence of independent skill. Taken together, the review defines the scope of technical support "
     "and the tests that human craft making requires.")

# ---- 6. Conclusion
H1("6. Conclusion")
para("Our previous survey examined how GenAI influences inclusive immersive learning in XR environments, identified the structural "
     "limitations of current generative models, and proposed a multidimensional evaluation model together with an illustrative "
     "application scenario and a minimal experimental protocol {R29}. It concluded that future work should develop validated "
     "instruments or domain-specific benchmarks derived from these evaluation dimensions, and should examine how improvement "
     "technologies can support long-term learning trajectories and sustained creative production {R29}.")
para("The proposed review takes up these directions in one domain where they can be examined concretely: physical craft making by "
     "creative communities. The question of multimodal alignment becomes the question of whether AI advice is consistent with the "
     "material states that a system actually observes (RQ1). The concern with reliable and transparent feedback becomes an analysis of "
     "the sources, timing, and maker control of feedback, including decisions to correct, preserve, or extend a variation (RQ2). The "
     "interest in long-term learning becomes a distinction between performance with support and independent performance, retention, "
     "and transfer (RQ3) {R27}. The resulting evidence map and design and evaluation items are intended to provide the "
     "domain-specific grounding that our previous survey identified as the next step.")

# ---- Acknowledgement
H1("Acknowledgement")
para("[TBD: funding source and grant information.] [TBD: statement on the use of AI-assisted writing tools, following the TIIS "
     "policy in force at submission.]")

# ---- References
H1("References")
ref_start = len(body)
REF_PLACEHOLDER = "@@REFS@@"
body.append(REF_PLACEHOLDER)

# ---- Attachment: roadmap
H1("Attachment. Proposed Writing Roadmap for the Editing Staff", page_break=True)
para("[Not part of the manuscript.] This roadmap applies only if the proposal is accepted. It describes how the authors will write "
     "the full survey with AI assistance while remaining responsible for every claim and citation. Week numbers count from the "
     "acceptance notice; calendar dates and the submission deadline are [TBD].")
H2("A.1 Principles")
for t in [
 "**AI is a copilot, not the pilot.** The authors set the research questions, the taxonomy, and the conclusions. AI tools help with structuring, drafting, consistency checks, and citation verification.",
 "**No source the authors have not read.** A reference enters the corpus only after an author has read it. AI may synthesize the authors’ notes but may not add sources (“Do not add any sources I haven’t provided”).",
 "**Gaps are marked, not filled.** Where evidence is missing, the draft carries a [MATERIAL GAP] or [TBD] marker instead of invented text.",
 "**Continuity with TIIS-S1-2025-Nov-1354.R1.** The survey is framed as a follow-up to the authors’ previous TIIS survey, which is cited in the Introduction, revisited in the Conclusion, and listed in the References.",
 "**Delivery, not claims.** Prose-editing tools may change how a claim is worded, never what it says. Apparent scientific errors are flagged for the authors, not silently rewritten.",
 "**Transparent disclosure.** AI use is disclosed in the manuscript according to the TIIS and KSII policy in force at submission."]:
    para(t)
H2("A.2 Stage-by-Stage Roadmap")
para("Table A1 lists the stages. Each stage ends with an author checkpoint, and the output in the last column is the gate to the "
     "next stage.")
RM = [
 ["0. Kick-off", "W1", "Fix scope, RQs, and inclusion criteria from the accepted proposal; incorporate Editing Staff comments; confirm the page limit and deadline [TBD]; set the time budget (about 70% pre-writing, 10% drafting, 20% revision)", "Socratic planning (/ars-plan); sciwrite-process; review-article guidance in sciwrite-proposals", "Scope memo, RQ list, schedule"],
 ["1. Framing", "W1", "Rank three candidate framings by novelty and defensibility; list the strongest counter-argument to each", "Adversarial framing prompt", "Final framing and contribution statement"],
 ["2. Literature corpus", "W2–W3", "Systematic search as in Section 3.1, starting from the 30 seed studies; authors read sources and take structured notes", "PRISMA-style flow; Zotero; /ars-lit-review only to find gaps in the authors’ corpus", "Flow diagram, annotated corpus, query and provenance log"],
 ["2.5 Integrity gate I", "W3", "Check every candidate citation for existence and metadata", "DOI resolution (Crossref, JaLC); Semantic Scholar matching", "Verified bibliography (zero unverified items)"],
 ["3. Taxonomy and synthesis", "W3–W4", "Apply the extraction scheme (Table 4); build the four syntheses (Section 3.3); fix a controlled vocabulary for terms and acronyms", "Synthesis from author notes only; SWiM reporting items", "Taxonomy figure, comparison tables, glossary"],
 ["4. Section drafting", "W4–W6", "Figures and tables first, then body sections, then Introduction, Conclusion, and Abstract; one section per pass, no more than about 800–1,000 words, each reviewed before the next", "Paragraph-level outlines with purpose and evidence; sciwrite-manuscript (section order and tense, adapted to a survey); TIIS template; style calibration on the authors’ prior papers, including 1354.R1", "Full first draft in the TIIS template"],
 ["4.5 Integrity gate II", "W6", "Zero-tolerance re-check: fabricated citations, unsupported claims, and numbers not found in the sources (e.g., every figure carried over from the proposal slides)", "Claim-to-source audit; figure and table checklist", "Integrity report signed off by the authors"],
 ["5. Internal review", "W7", "Simulated peer review (editor, methodology, domain, and cross-disciplinary reviewers plus a devil’s advocate); logic-flow and Abstract/Conclusion consistency checks", "academic-paper-reviewer (0–100 rubric); hostile-reviewer prompt", "Prioritized revision list"],
 ["6. Revision and language", "W7–W8", "Revise; tighten wording without losing claims, numbers, or citations; run mechanical audits; human proofreading", "sciwrite-prose; prose_audit.py, keyword_consistency.py, numeric_consistency.py; tracked changes; professional proofreading", "Audit report with each flag resolved or justified"],
 ["7. Submission", "W8", "AI-use disclosure, cover letter, format check, authorship and similarity check; update online-first references", "TIIS submission checklist; sciwrite-publish; separate similarity checker", "Submitted manuscript"],
 ["8. Reviewer response", "Post-review", "Extract each comment; mark it Revise, Defend, or Needs analysis; draft neutral responses", "sciwrite-publish; traceability matrix (comment → change → location)", "Response letter and revised manuscript"],
]
table("A1", "Stage-by-stage writing roadmap",
      ["Stage", "Weeks", "Main activity", "Tools and techniques", "Output (gate)"],
      RM, [1250, 950, 2550, 2050, 1400], align_left_cols=(0, 2, 3, 4))
H2("A.3 Quality and Integrity Controls")
for t in [
 "**Citation checks.** Each reference is verified against its DOI or publisher page by an author. The 30 seed references in this proposal were checked against Crossref and JaLC on 22 November 2026; four entries are online-first or lack page numbers and must be updated before submission.",
 "**Number checks.** Every figure or statistic in the text is traced to a cited source.",
 "**Consistency checks.** The Abstract, contribution list, and Conclusion state the same claims. Script checks cover terms, acronyms, and numbers; their output is a list of candidates for the authors to judge, not automatic fixes.",
 "**Voice checks.** The authors rewrite AI-assisted passages in their own voice; raw AI output is not submitted.",
 "**Model use.** A mid-size model for routine drafting and editing, a stronger model for whole-manuscript consistency and multi-source synthesis, and fast models only for mechanical formatting, never for citations."]:
    para(t)
H2("A.4 How the Three Sources Divide the Work")
table("A2", "Division of work among the three sources",
      ["Source", "Main role in this roadmap", "Not covered"],
      [["ProofreaderPro guide [S1]", "Prompting techniques: framing, synthesis without added sources, section-by-section drafting, hostile-reviewer self-review", "Automated checks or a pipeline"],
       ["Academic Research Skills (ARS), as summarized in [S2]", "Research pipeline: literature search, citation verification, integrity gates, simulated peer review", "Sentence-level style; licensed CC BY-NC 4.0 (non-commercial use only)"],
       ["Scientific Writing Skills (sciwrite) [S3]", "Writing craft: process planning, section order and tense, prose editing, term and number consistency scripts, publication ethics", "Citation verification, plagiarism checks, judgment of scientific claims"]],
      [2300, 3700, 2200], align_left_cols=(0, 1, 2))
para("ARS checks that each citation exists and supports its claim; sciwrite checks that the text states it clearly and consistently. "
     "The two are complementary and are used at different stages.")
H2("A.5 Responsibilities and Requests to the Editing Staff")
para("**Authors:** research questions, source reading, taxonomy, interpretation, final wording, and all verification sign-offs. "
     "**AI tools:** structuring, first-pass drafting from author notes, consistency and integrity checks, and simulated review. "
     "**Editing Staff (requested):** feedback on scope and section structure at Stage 0 and on the draft outline before Stage 4; "
     "confirmation of the page limit for survey papers, the submission timeline, and the policy on disclosing AI-assisted writing.")
H2("A.6 Sources for This Roadmap")
for t in [
 "[S1] Moe, “Claude for Academic Research Writing: A Practical Guide” (in Korean), ProofreaderPro.ai, Aug. 10, 2026. [Online]. Available: https://proofreaderpro.ai/ko/blog/how-to-use-claude-for-research-writing",
 "[S2] 9bow, “Academic Research Skills: A Skill Collection for Academic Research and Paper Writing in Claude Code” (in Korean), PyTorch Korea User Group, May 28, 2026. [Online]. Available: https://discuss.pytorch.kr/t/academic-research-skills-claude-code/10385 (describes the repository https://github.com/Imbad0202/academic-research-skills)",
 "[S3] dvdsosa, Scientific Writing Skills (based on K. Sainani, Writing in the Sciences, Stanford University), GitHub repository. [Online]. Available: https://github.com/dvdsosa/scientific-writing-skills"]:
    body.append(P("body", t, '<w:ind w:left="426" w:hanging="426"/><w:jc w:val="left"/>'))

# ---- render references in citation order
missing = [k for k in REF if k not in order]
if missing:
    raise SystemExit(f"uncited references: {missing}")
refs_xml = []
for k in order:
    txt = REF[k]
    m = re.match(r"(.*?)\*(.+?)\*(.*)", txt)
    pre, ital, post = m.groups()
    rid = new_rel("hyperlink", "http://doi.org/" + DOI[k])
    link = (f'<w:hyperlink r:id="{rid}" w:history="1"><w:r><w:rPr><w:rStyle w:val="aa"/><w:color w:val="0000FF"/><w:szCs w:val="20"/></w:rPr>'
            f'<w:t>Article (CrossRef Link)</w:t></w:r></w:hyperlink>')
    refs_xml.append(f'<w:p><w:pPr><w:pStyle w:val="References"/><w:ind w:left="426" w:hanging="426"/></w:pPr>'
                    f'{run(pre)}{run(ital, "<w:i/><w:iCs/>")}{run(post + " ")}{link}</w:p>')
body[body.index(REF_PLACEHOLDER)] = "".join(refs_xml)

# ================================================================= assemble
doc = open(f"{WORK}/word/document.xml", encoding="utf-8").read()
head = doc[:doc.index("<w:body>") + len("<w:body>")]
sect = doc[doc.rindex("<w:sectPr"):]
sect = re.sub(r'<w:pgNumType w:start="\d+"/>', '<w:pgNumType w:start="1"/>', sect)
open(f"{WORK}/word/document.xml", "w", encoding="utf-8").write(head + "".join(body) + sect)
open(rels_path, "w", encoding="utf-8").write(rels)

# headers / footer text
def set_texts(path, mapping):
    x = open(path, encoding="utf-8").read()
    for a, b in mapping:
        if a not in x:
            raise SystemExit(f"{path}: '{a}' not found")
        x = x.replace(a, b, 1)
    open(path, "w", encoding="utf-8").write(x)
set_texts(f"{WORK}/word/header1.xml", [("<w:t>Hong</w:t>", "<w:t>J. H. Lee</w:t>"),
          ("<w:t>paper title</w:t>", "<w:t>Internet-Connected GenAI for Human Making in Craft</w:t>")])

# footer: rewrite the text paragraphs that follow the rule line
f = open(f"{WORK}/word/footer1.xml", encoding="utf-8").read()
paras = re.findall(r"<w:p [^>]*>.*?</w:p>", f, re.S)
txt_paras = [p for p in paras if "preliminary" in p or "ISSN" in p or "doi.org" in p or "research" in p]
fr = '<w:rPr><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>'
def fpara(text):
    return f'<w:p><w:pPr><w:jc w:val="both"/>{fr}</w:pPr>' + run(text, '<w:sz w:val="18"/><w:szCs w:val="18"/>') + '</w:p>'
new = [fpara("[TBD: funding acknowledgment; note any preliminary version of this work, if applicable.]"),
       fpara("http://doi.org/10.3837/tiis.20XX.XX.XXX                                                    ISSN : 1976-7277")]
# keep the first text paragraph if it also holds the drawing (rule line); otherwise replace
first = txt_paras[0]
if "<w:drawing>" in first or "mc:AlternateContent" in first:
    keep = re.match(r"(<w:p [^>]*>.*?</mc:AlternateContent></w:r>)", first, re.S).group(1)
    f = f.replace(first, keep + "</w:p>" + "".join(new), 1)
    for p in txt_paras[1:]:
        f = f.replace(p, "", 1)
else:
    f = f.replace(first, "".join(new), 1)
    for p in txt_paras[1:]:
        f = f.replace(p, "", 1)
open(f"{WORK}/word/footer1.xml", "w", encoding="utf-8").write(f)

# drop template comment parts not needed? keep package intact.
if os.path.exists(OUT):
    os.remove(OUT)
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(WORK):
        for fn in files:
            full = os.path.join(root, fn)
            arc = os.path.relpath(full, WORK).replace("\\", "/")
            z.write(full, arc)
print("refs in order:", ", ".join(f"[{i+1}]{k}" for i, k in enumerate(order)))
print("written", OUT)
