"""Yeni sürüm yayınlarken çalıştırılır: surumler.json'daki son kaydı uygulamaya işler.

Kullanım: surumler.json'a yeni kaydı ekle, sonra `python3 tools/surum.py`.
Her kayıtta: n (sürüm numarası), date, text (teknik not, sadece yönetici görür)
ve isteğe bağlı public (oyunculara gösterilecek not).
"""
import json, re, time, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
J = lambda x: json.dumps(x, ensure_ascii=False, separators=(",", ":"))
c = json.loads((R / "surumler.json").read_text(encoding="utf-8"))
last = c[-1]
v = {"n": last["n"], "date": last["date"]}
allc = [{"n": x["n"], "date": x["date"], "text": x["text"]} for x in reversed(c)][:8]
pubc = [{"n": x["n"], "date": x["date"], "text": x["public"]} for x in reversed(c) if x.get("public")][:5]
s = (R / "index.html").read_text(encoding="utf-8")
s = re.sub(r"window\.ZELVO_VERSION = \{[^}]*\};", "window.ZELVO_VERSION = " + J(v) + ";", s, count=1)
s = re.sub(r"window\.ZELVO_CHANGES = \[.*?\];", "window.ZELVO_CHANGES = " + J(allc) + ";", s, count=1, flags=re.S)
if "window.ZELVO_PUBLIC_CHANGES = " in s:
    s = re.sub(r"window\.ZELVO_PUBLIC_CHANGES = \[.*?\];", "window.ZELVO_PUBLIC_CHANGES = " + J(pubc) + ";", s, count=1, flags=re.S)
else:
    s = s.replace("window.ZELVO_CHANGES = ", "window.ZELVO_PUBLIC_CHANGES = " + J(pubc) + ";\nwindow.ZELVO_CHANGES = ", 1)
(R / "index.html").write_text(s, encoding="utf-8")
(R / "version.json").write_text(J(v), encoding="utf-8")
w = (R / "sw.js").read_text(encoding="utf-8")
w = re.sub(r'const VERSION = "zelvo-s\d+-\d+";', f'const VERSION = "zelvo-s{last["n"]}-{time.strftime("%Y%m%d%H%M%S")}";', w)
(R / "sw.js").write_text(w, encoding="utf-8")
md = (R / "README.md").read_text(encoding="utf-8")
row = f"| {last['n']} | {last['date']} | {last['text']} |\n"
if row not in md:
    md = md.replace("| --- | --- | --- |\n", "| --- | --- | --- |\n" + row, 1)
(R / "README.md").write_text(md, encoding="utf-8")
print("Sürüm", last["n"], "işlendi")
