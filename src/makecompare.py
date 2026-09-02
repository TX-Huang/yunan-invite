# -*- coding: utf-8 -*-
"""Build a side-by-side page: photo at the top (A) vs photo under the title (B)."""
import io

s = io.open("invite-cards.html", encoding="utf-8").read()

INJECT = """
<style>
  .grid{grid-template-columns:repeat(2,minmax(250px,1fr));max-width:820px;gap:22px}
  .grid>section.cmp{display:block}
  .grid>section.cmp .pick{display:flex}
  .send,.hint{display:none}
  /* B: photo sits between the title block and the greeting */
  .c2b .body{padding:26px 40px 24px}
  .c2b .c2-tree{width:44px;height:40px}
  .c2b .eyebrow{margin-top:8px}
  .c2b h2{font-size:29px;margin-top:0}
  .c2b .c2-sub{font-size:17px}
  .c2b .popout{margin:14px 0 58px}
  .c2b .guest-block{margin:2px 0 auto}
  .c2b .info{gap:6px}
  .c2b .cupline{margin-top:6px}
</style>
<script>
(function(){
  // this page always shows both cards, never the single-guest view
  document.body.classList.remove('solo');
  var qsName = new URLSearchParams(location.search).get('to') || '林小美';
  var CJK = /[㐀-鿿豈-﫿぀-ヿ]/;
  function name(root){
    root.querySelectorAll('.guest').forEach(function(e){ e.textContent = qsName; });
    root.querySelectorAll('.script').forEach(function(e){ e.classList.toggle('cjk', CJK.test(qsName)); });
  }
  var secs = document.querySelectorAll('main > section');
  var a = secs[1];
  a.classList.add('cmp');
  a.querySelector('.pick').innerHTML =
    '<span class="num">A</span><span class="style-name">照片在最上面</span><span class="tag">目前版本</span>';

  var b = a.cloneNode(true);
  b.classList.add('cmp');
  b.querySelector('.pick').innerHTML =
    '<span class="num">B</span><span class="style-name">照片在標題下面</span><span class="tag">新排法</span>';
  var card = b.querySelector('.card');
  card.classList.add('c2b');
  var pop = b.querySelector('.popout');
  b.querySelector('.c2-sub').after(pop);          // 畇安 週歲 / First Birthday Party 之後
  b.querySelector('.slot').setAttribute('aria-label', '放大看 B 版');
  a.after(b);
  name(a); name(b);

  // the page's own observer only watches the cards that existed at load
  var ro = new ResizeObserver(function(es){
    es.forEach(function(e){ e.target.style.setProperty('--s', (e.contentRect.width/360).toFixed(4)); });
  });
  document.querySelectorAll('.slot').forEach(function(sl){ ro.observe(sl); });
})();
</script>
"""
s = s.replace("</body>", INJECT + "</body>") if "</body>" in s else s + INJECT
io.open("compare.html", "w", encoding="utf-8").write(s)
print("compare.html written,", len(s) // 1024, "KB")
