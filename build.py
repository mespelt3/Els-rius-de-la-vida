import re
import os

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 14. TÍTOL DEL DOCUMENT
html = re.sub(r'<title>.*?</title>', "<title>El riu de la vida | Docent | Recerca i acció 2026-27</title>", html)

# 1. CAPÇALERA I BADGE + 15. BADGE DOCENT A LA CAPÇALERA
html = re.sub(r'text-transform:\s*uppercase;', '', html)
html = html.replace("🧭 4t d'ESO · Orientació i Trajectòria Vital", "Recerca i acció - curs 2026-27")
badge_docent = """<div style="display: inline-flex; align-items: center; gap: 0.4rem; background: rgba(251,191,36,0.25); border: 1px solid rgba(251,191,36,0.4); padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 600; margin-bottom: 0.8rem;">
  📋 Versió docent · Materials pedagògics inclosos
</div>"""
html = html.replace('<div class="badge-hero">', badge_docent + '\n      <br>\n      <div class="badge-hero">')

# 2. PESTANYES
nav_html = """<nav class="main-nav no-print">
    <div class="nav-container">
      <button class="nav-btn active" onclick="switchTab('tab-metafora')">🌊 La metàfora</button>
      <button class="nav-btn" onclick="switchTab('tab-trams')">🗺️ Els 3 trams</button>
      <button class="nav-btn" onclick="switchTab('tab-docent')">📋 Eina docent</button>
      <button class="nav-btn" onclick="switchTab('tab-print')">🖨️ Materials imprimibles</button>
      <button class="nav-btn" onclick="switchTab('tab-referents')" style="display:none">🗣️ Converses amb referents</button>
    </div>
  </nav>"""
html = re.sub(r'<nav class="main-nav no-print">.*?</nav>', nav_html, html, flags=re.DOTALL)
html = html.replace('id="tab-metàfora"', 'id="tab-metafora"')

# 3. TÍTOLS — CAPITALITZACIÓ
# Not easily done with regex without false positives. I'll replace the main titles.
html = html.replace("El Riu de la Vida", "El riu de la vida")
html = html.replace("🌊 Sessió de Llançament: «Quin Riu ets Avui?»", "🌊 Sessió de llançament: «Quin riu ets avui?»")
html = html.replace("L'espurna d'autoconeixement: Els 10 Rius de la Vida", "L'espurna d'autoconeixement: els 10 rius de la vida")
html = html.replace("🗺️ El Diccionari Simbòlic del Riu", "🗺️ El diccionari simbòlic del riu")
html = html.replace("⚓ Dinàmica: «El meu Equipatge per Navegar»", "⚓ Dinàmica: «El meu equipatge per navegar»")
html = html.replace("🗺️ L'Arquitectura del Projecte: Els 3 Trams", "🗺️ L'arquitectura del projecte: els 3 trams")
html = html.replace("🌊 Tram 1: «El meu riu fins avui» (0 a 16 anys)", "🌊 Tram 1: «El meu riu fins avui» (0 a 16 anys)")
html = html.replace("🔭 Tram 2: «Mirada retrospectiva des dels 80 anys»", "🔭 Tram 2: «Mirada retrospectiva des dels 80 anys»")
html = html.replace("🔍 Tram 3: «La lupa a la Postobligatòria» (16 a 18/20 anys)", "🔍 Tram 3: «La lupa a la postobligatòria» (16 a 18/20 anys)")
html = html.replace("📋 Graella d'Observació Docent: Habilitats Socioemocionals", "📋 Graella d'observació docent: habilitats socioemocionals")
html = html.replace("🖨️ Zona d'Impressió: Kit de Treball per a l'Aula", "🖨️ Zona d'impressió: kit de treball per a l'aula")

# 4. TÍTOL INTERN PESTANYA 1
html = html.replace("🌊 Sessió de llançament: «Quin riu ets avui?»", "🌊 Quin riu ets avui?")

# 5. IMATGES DELS RIUS
imgs_800 = [
    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1547981609-4b6bfe67ca0b?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1551632436-cbf8dd35adfa?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1505118380757-91f5f5632de0?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1485470733090-0aae1788d5af?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1541701494587-cb58502866ab?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1491002052546-bf38f186af56?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1516912481808-3406841bd33c?auto=format&fit=crop&w=800&q=80"
]
html = re.sub(r'src="https://images.unsplash.com/photo-[^"]+?w=800&q=80"', lambda m, i=iter(imgs_800): f'src="{next(i)}"', html)

imgs_1200 = [img.replace('w=800', 'w=1200') for img in imgs_800]
html = re.sub(r'img:\s*"https://images.unsplash.com/photo-[^"]+?w=1200&q=80"', lambda m, i=iter(imgs_1200): f'img: "{next(i)}"', html)

# 6. BOTÓ «AMPLIAR» — FIX
for i in range(10):
    html = re.sub(r'<span class="river-zoom-btn">🔍 Ampliar</span>', f'<span class="river-zoom-btn" onclick="event.stopPropagation(); openRiverModal({i})">🔍 Ampliar</span>', html, count=1)

# 12. PANELL DOCENT
nota_docent_1 = """
        <div style="background: #fef3c7; border-left: 4px solid #d97706; border-radius: 8px; padding: 1rem 1.5rem; margin-bottom: 1.5rem;">
          <h4 style="margin: 0 0 0.5rem; color: #92400e;">📋 NOTA DOCENT — Sessió 1 (1 hora)</h4>
          <p style="margin: 0; font-size: 0.9rem; color: #78350f;">Projecta els 10 rius a la pissarra digital. Dona temps a l'alumnat per explorar les fotos individualment (5-7 min). Després, en plenari, demana: «Qui ha triat el riu 3? I el 9?». Recull totes les triadesanonymament per veure la distribució de la classe. Evita jutjar cap tria.<br>
          Elements necessaris: Pissarra digital o projector · Fitxa de treball Tram 1 · Diari del viatge (quadern físic)</p>
        </div>
"""
html = html.replace('<div class="card-header">\n          <h2 class="card-title">🌊 Quin riu ets avui?</h2>', nota_docent_1 + '<div class="card-header">\n          <h2 class="card-title">🌊 Quin riu ets avui?</h2>')

nota_docent_2 = """
        <div style="background: #fef3c7; border-left: 4px solid #d97706; border-radius: 8px; padding: 1rem 1.5rem; margin-bottom: 1.5rem;">
          <h4 style="margin: 0 0 0.5rem; color: #92400e;">📋 NOTA DOCENT — Sessió 1 (2a part, 30-40 min)</h4>
          <p style="margin: 0; font-size: 0.9rem; color: #78350f;">Explica les 5 habilitats i mostra el mapa de comportaments. L'alumnat tria l'Àncora i el Timó individualment. És important que no es pressionin mútuament. Recorda'ls que no hi ha cap comportament millor que un altre — depèn del moment vital de cadascú. Pots demanar que comparteixin en parella la tria (però no en gran grup).<br>
          Pers: Imprimible «Targeta d'Equipatge» per penjar a l'agenda o carpeta.</p>
        </div>
"""
html = html.replace('<div class="behavior-selector-box">', nota_docent_2 + '<div class="behavior-selector-box">')

# 7. MAPA DELS 35 COMPORTAMENTS
mapa_comportaments = """
        <!-- MAPA COMPORTAMENTS -->
        <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: white; border: 1px solid var(--border-color); border-radius: var(--radius-md);">
          <h3 style="margin-bottom: 1rem; color: var(--primary-deep);">Mapa dels 35 comportaments</h3>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            
            <div style="background: #dbeafe; border: 1px solid #93c5fd; padding: 1rem; border-radius: var(--radius-sm);">
              <h4 style="color: #1e40af; margin-bottom: 0.5rem; font-size: 0.95rem;">🔵 Responsabilitat</h4>
              <ul style="font-size: 0.8rem; padding-left: 1rem; margin: 0; color: #1e3a8a;">
                <li>C1: Treballa constant</li>
                <li>C2: Realitza tasques amb cura</li>
                <li>C3: Fa comentaris de tasca</li>
                <li>C4: Persevera</li>
                <li>C5: Respecta normes/material</li>
                <li>C6: Compleix terminis</li>
                <li>C7: Assumeix el rol</li>
              </ul>
            </div>

            <div style="background: #d1fae5; border: 1px solid #6ee7b7; padding: 1rem; border-radius: var(--radius-sm);">
              <h4 style="color: #065f46; margin-bottom: 0.5rem; font-size: 0.95rem;">🟢 Cooperació</h4>
              <ul style="font-size: 0.8rem; padding-left: 1rem; margin: 0; color: #064e3b;">
                <li>C8: Escolta activament</li>
                <li>C9: Fomenta participació</li>
                <li>C10: Presa decisions consens</li>
                <li>C11: Reconeix responsabilitats</li>
                <li>C12: Ajuda companys</li>
                <li>C13: Resolució conflictes</li>
                <li>C14: Incorpora aportacions</li>
              </ul>
            </div>

            <div style="background: #fef3c7; border: 1px solid #fcd34d; padding: 1rem; border-radius: var(--radius-sm);">
              <h4 style="color: #92400e; margin-bottom: 0.5rem; font-size: 0.95rem;">🟠 Autonomia</h4>
              <ul style="font-size: 0.8rem; padding-left: 1rem; margin: 0; color: #78350f;">
                <li>C15: Aporta idees noves</li>
                <li>C16: Fa preguntes pertinents</li>
                <li>C17: Decisions amb criteri</li>
                <li>C18: Argumenta i convenç</li>
                <li>C19: Treballa independent</li>
                <li>C20: Inicia canvis/millores</li>
                <li>C21: Gestiona temps</li>
              </ul>
            </div>

            <div style="background: #ffe4e6; border: 1px solid #fda4af; padding: 1rem; border-radius: var(--radius-sm);">
              <h4 style="color: #9f1239; margin-bottom: 0.5rem; font-size: 0.95rem;">🔴 Gestió Emocional</h4>
              <ul style="font-size: 0.8rem; padding-left: 1rem; margin: 0; color: #881337;">
                <li>C22: Tranquil·litat sota pressió</li>
                <li>C23: Controla en conflicte</li>
                <li>C24: Accepta propostes rebutjades</li>
                <li>C25: Actitud constructiva</li>
                <li>C26: Adequa to i llenguatge</li>
                <li>C27: Tolerància a l'error</li>
              </ul>
            </div>

            <div style="background: #ede9fe; border: 1px solid #c4b5fd; padding: 1rem; border-radius: var(--radius-sm);">
              <h4 style="color: #5b21b6; margin-bottom: 0.5rem; font-size: 0.95rem;">🟣 Pensament</h4>
              <ul style="font-size: 0.8rem; padding-left: 1rem; margin: 0; color: #4c1d95;">
                <li>C28: Relaciona sabers</li>
                <li>C29: Reflexiona profundament</li>
                <li>C30: Fa bones preguntes</li>
                <li>C31: Alternatives quan falla</li>
                <li>C32: Diferents perspectives</li>
                <li>C33: Planifica i prioritza</li>
                <li>C34: Curiositat/va més enllà</li>
                <li>C35: Dóna/rep feedback Austin</li>
              </ul>
            </div>

          </div>
        </div>
"""
html = html.replace('<div class="behavior-selector-box">', mapa_comportaments + '<div class="behavior-selector-box">')


nota_docent_3 = """
        <div style="background: #fef3c7; border-left: 4px solid #d97706; border-radius: 8px; padding: 1rem 1.5rem; margin-bottom: 1.5rem;">
          <h4 style="margin: 0 0 0.5rem; color: #92400e;">📋 NOTA DOCENT — Sessió 2 (1-2 hores)</h4>
          <p style="margin: 0; font-size: 0.9rem; color: #78350f;">Els alumnes comencen el dibuix del Tram 1 (0-16 anys). Et recomanem que facis una demostració breu: dibuixa el teu propi riu dels 0-18 amb 3 elements (font, afluent, roca). Això trenca el bloqueig del «no sé dibuixar». Recorda que no és un dibuix artístic sinó un mapa vital.<br>
          Papallona d'Austin: Dedica 10-15 min de la Sessió 3 a l'intercanvi de feedback entre parelles. Recorda els 3 criteris: Amable, Específic, Útil.<br>
          Critèri d'èxit: Cada alumne ha d'haver dibuixat com a mínim 4 elements simbòlics i una llegenda.</p>
        </div>
"""
html = html.replace('<div class="card-header">\n          <h3 class="card-title" style="color: var(--primary);">🌊 Tram 1: «El meu riu fins avui» (0 a 16 anys)</h3>', nota_docent_3 + '<div class="card-header">\n          <h3 class="card-title" style="color: var(--primary);">🌊 Tram 1: «El meu riu fins avui» (0 a 16 anys)</h3>')

nota_docent_4 = """
        <div style="background: #fef3c7; border-left: 4px solid #d97706; border-radius: 8px; padding: 1rem 1.5rem; margin-bottom: 1.5rem;">
          <h4 style="margin: 0 0 0.5rem; color: #92400e;">📋 NOTA DOCENT — Sessió 3-4 (2 hores)</h4>
          <p style="margin: 0; font-size: 0.9rem; color: #78350f;">El Tram 2 (80→18 anys) es fa DESPRÉS de les converses amb referents. Guia l'alumnat perquè primerament reflecteixin el que han après de les converses i llavors projecin el seu riu futur. El Tram 3 (16→18/20) es fa en la Sessió 5-6: és la recerca concreta de les opcions postobligatòries amb els 3 plans (A, B, C).</p>
        </div>
"""
html = html.replace('<div class="card-header">\n          <h2 class="card-title">🗺️ L\'arquitectura del projecte: els 3 trams</h2>', nota_docent_4 + '<div class="card-header">\n          <h2 class="card-title">🗺️ L\'arquitectura del projecte: els 3 trams</h2>')

# 8. PAPALLONA D'AUSTIN AMPLIADA
papallona_html = """
            <div style="background: #fffbeb; border: 1px solid #fef3c7; border-left: 5px solid #f59e0b; padding: 1.5rem; border-radius: var(--radius-sm); margin: 1.5rem 0;">
              <h3 style="color: #92400e; display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">🦋 La papallona d'Austin: com donar feedback que faci créixer</h3>
              <div style="display: grid; grid-template-columns: 1fr; gap: 1rem;">
                <div style="background: white; border: 1px solid #fde68a; padding: 1rem; border-radius: 6px;">
                  <h4 style="color: #d97706; margin-bottom: 0.25rem;">1. Amable</h4>
                  <p style="font-size: 0.85rem; color: #78350f; margin: 0;">Destaca primer allò que funciona molt bé o t'agrada de la feina de l'altre. <em>Exemple: «M'agrada molt com has representat l'afluent de quan vas canviar d'institut.»</em></p>
                </div>
                <div style="background: white; border: 1px solid #fde68a; padding: 1rem; border-radius: 6px;">
                  <h4 style="color: #d97706; margin-bottom: 0.25rem;">2. Específic</h4>
                  <p style="font-size: 0.85rem; color: #78350f; margin: 0;">Assenyala un punt exacte que no quedi clar o pugui millorar, sense generalitzar. <em>Exemple: «Entre els 10 i els 12 anys no s'acaba d'entendre per què l'aigua es torna més fosca.»</em></p>
                </div>
                <div style="background: white; border: 1px solid #fde68a; padding: 1rem; border-radius: 6px;">
                  <h4 style="color: #d97706; margin-bottom: 0.25rem;">3. Útil</h4>
                  <p style="font-size: 0.85rem; color: #78350f; margin: 0;">Proposa una acció clara i directa que la persona pugui aplicar per millorar. <em>Exemple: «Si afegeixes una petita etiqueta al costat de la roca negra, s'entendrà de seguida què va passar.»</em></p>
                </div>
              </div>
              <p style="font-size: 0.85rem; color: #92400e; margin-top: 1rem; font-style: italic;">Nota: El feedback és un regal. Quan te'l donen, només has de dir «gràcies» i decidir què hi fas.</p>
            </div>
"""
html = re.sub(r'<div class="butterfly-box">.*?</ul>\s*</div>', papallona_html, html, flags=re.DOTALL)

# 9. INSTRUCCIONS TRAM 1
instruccions_1 = """
            <ol style="margin-left: 1.2rem; font-size: 1.05rem; line-height: 2.0;">
              <li><strong>Pluja d'idees inicial:</strong> Escriu en brut 3 moments feliços (ex. viatge familiar), 2 dificultats superades (ex. canvi d'escola), 2 persones afluents (ex. una tieta) i 1 afició constant (ex. bàsquet).</li>
              <li><strong>El curs del riu (Suport A3 o digital):</strong> Dibuixa un riu que comenci a un extrem (naixement) i arribi fins a l'altre (4t d'ESO). Fes que el riu s'eixampli en moments d'energia i s'estrenyi en moments de dubte.</li>
              <li><strong>Afegeix la simbologia:</strong> Dibuixa afluents amb noms de persones o aficions, roques amb etiquetes de dificultats superades, i gorgs de reflexió.</li>
              <li><strong>La Llegenda:</strong> Crea a una cantonada una llegenda que expliqui els colors de l'aigua i els símbols emprats (ex. color verd = alegria, roca = examen suspès).</li>
            </ol>
"""
html = re.sub(r'<ol style="margin-left: 1.2rem; font-size: 0.9rem; line-height: 1.7;">.*?</ol>', instruccions_1, html, flags=re.DOTALL)


# 10. DIARI DEL TEU VIATGE (blocs metacognició integrats)
# Bloc explicatiu al principi de tab-metafora (verd)
bloc_verd = """
        <div style="background: #dcfce7; border: 1px solid #86efac; border-radius: 8px; padding: 1rem 1.5rem; margin-bottom: 1.5rem;">
          <h4 style="margin: 0 0 0.5rem; color: #166534;">📝 El Diari del teu Viatge</h4>
          <p style="margin: 0; font-size: 0.9rem; color: #14532d;">Al llarg d'aquesta pàgina trobaràs blocs de reflexió per anotar les teves idees. Això substitueix el Quadern de Bitàcola original per integrar-ho en l'experiència.</p>
        </div>
"""
html = html.replace('<div class="card">\n        <div class="card-header">\n          <h2 class="card-title">🌊 Sessió de llançament: «Quin riu ets avui?»</h2>', bloc_verd + '<div class="card">\n        <div class="card-header">\n          <h2 class="card-title">🌊 Sessió de llançament: «Quin riu ets avui?»</h2>')

bloc_1 = """
        <div style="background: #f3f4f6; border-left: 4px solid #6b7280; padding: 1.5rem; margin-top: 1.5rem; border-radius: 0 8px 8px 0;">
          <h4 style="color: #374151; margin-bottom: 0.8rem;">📝 Diari del viatge: Aturada 1</h4>
          <label style="display: block; font-size: 0.85rem; font-weight: bold; margin-bottom: 0.4rem;">1. Quina és la primera paraula o emoció que et ve al cap quan penses en el curs vinent?</label>
          <input type="text" style="width: 100%; padding: 0.5rem; margin-bottom: 1rem; border: 1px solid #d1d5db; border-radius: 4px;" placeholder="Ex: Incertesa, il·lusió, mandra, curiositat...">
          <label style="display: block; font-size: 0.85rem; font-weight: bold; margin-bottom: 0.4rem;">2. Quin riu has triat a la dinàmica inicial i per què creus que representa el teu moment actual?</label>
          <textarea rows="3" style="width: 100%; padding: 0.5rem; border: 1px solid #d1d5db; border-radius: 4px;" placeholder="Explica com et sents a 4t d'ESO..."></textarea>
        </div>
"""
html = html.replace('<div id="selected-river-feedback"', bloc_1 + '\n        <div id="selected-river-feedback"')

bloc_2 = """
          <div style="background: #f3f4f6; border-left: 4px solid #6b7280; padding: 1.5rem; margin-top: 1.5rem; border-radius: 0 8px 8px 0;">
            <h4 style="color: #374151; margin-bottom: 0.8rem;">📝 Diari del viatge: Aturada 2</h4>
            <label style="display: block; font-size: 0.85rem; font-weight: bold; margin-bottom: 0.4rem;">Quin és el teu comportament «Timó» i quin compromís concret adoptes a l'aula?</label>
            <input type="text" style="width: 100%; padding: 0.5rem; border: 1px solid #d1d5db; border-radius: 4px;" placeholder="El meu timó és... i faré...">
          </div>
"""
html = html.replace('<span id="equipatge-status" style="font-size: 0.85rem; color: var(--color-coop); font-weight: 600;"></span>\n          </div>', '<span id="equipatge-status" style="font-size: 0.85rem; color: var(--color-coop); font-weight: 600;"></span>\n          </div>' + bloc_2)

bloc_3 = """
        <div style="background: #f3f4f6; border-left: 4px solid #6b7280; padding: 1.5rem; margin-top: 1.5rem; border-radius: 0 8px 8px 0;">
          <h4 style="color: #374151; margin-bottom: 0.8rem;">📝 Diari del viatge: Aturada 3</h4>
          <label style="display: block; font-size: 0.85rem; font-weight: bold; margin-bottom: 0.4rem;">1. Mirant el teu riu fins avui, quina pedra o dificultat que semblava molt gran ara veus que et va fer madurar?</label>
          <textarea rows="3" style="width: 100%; padding: 0.5rem; margin-bottom: 1rem; border: 1px solid #d1d5db; border-radius: 4px;"></textarea>
          <label style="display: block; font-size: 0.85rem; font-weight: bold; margin-bottom: 0.4rem;">2. Quin feedback útil i concret vas rebre del teu company/a (Papallona d'Austin) i com vas millorar el dibuix?</label>
          <textarea rows="3" style="width: 100%; padding: 0.5rem; border: 1px solid #d1d5db; border-radius: 4px;"></textarea>
        </div>
"""
html = html.replace('</div>\n        </div>\n      </div>\n\n      <!-- TRAM 2 DETAIL -->', '</div>\n        </div>\n' + bloc_3 + '\n      </div>\n\n      <!-- TRAM 2 DETAIL -->')

# 11. ELIMINAR BITÀCOLA
html = re.sub(r'<!-- TAB 4: QUADERN DE BITÀCOLA \(METACOGNICIÓ\) -->.*?<!-- ============================================================= -->\n    <!-- TAB 5: EINA DOCENT', '<!-- TAB 5: EINA DOCENT', html, flags=re.DOTALL)
html = re.sub(r'function saveBitacola\(\) \{.*?\}\n', '', html, flags=re.DOTALL)
html = re.sub(r'function loadBitacola\(\) \{.*?\}\n', '', html, flags=re.DOTALL)
html = re.sub(r'function showAturada\(num\) \{.*?\}\n', '', html, flags=re.DOTALL)
html = html.replace('loadBitacola();', '')

# 13. SECCIÓ EINA DOCENT (GRAELLA D'OBSERVACIÓ) — MILLORADA
nota_dades = """
        <div style="background: #fff1f2; border: 1px solid #fecdd3; border-left: 4px solid #e11d48; border-radius: 8px; padding: 1rem 1.5rem; margin-bottom: 1.5rem;">
          <h4 style="margin: 0 0 0.5rem; color: #9f1239;">⚠️ On es guarden les dades?</h4>
          <p style="margin: 0; font-size: 0.9rem; color: #881337;">Totes les observacions es guarden ÚNICAMENT al localStorage d'aquest navegador i dispositiu. No surten a cap servidor extern i ningú extern hi pot accedir. Si obres el fitxer en un altre ordinador o navegador, la graella serà buida. Exporta regularment el CSV per no perdre les dades.<br>
          💡 <strong>Recomanació:</strong> Desa el CSV al final de cada sessió i guarda'l a la carpeta del projecte.</p>
        </div>
"""
html = html.replace('<div class="card-header">\n          <h2 class="card-title">📋 Graella d\'observació docent: habilitats socioemocionals</h2>', nota_dades + '<div class="card-header">\n          <h2 class="card-title">📋 Graella d\'observació docent: habilitats socioemocionals</h2>')

# Buida inicialment i canvia saveDocentData
html = re.sub(r'let docentStudents = \[.*?\];', 'let docentStudents = [];', html, flags=re.DOTALL)
html = html.replace('function loadDocentData() {', 'function loadDocentData() {\n      docentStudents = [];')

save_docent_new = """function saveDocentData() {
      localStorage.setItem('riu_docent_students', JSON.stringify(docentStudents));
      const status = document.getElementById('docent-save-status');
      if (status) {
        status.textContent = '✓ Observacions desades al navegador.';
        setTimeout(() => { status.textContent = ''; }, 3000);
      }
    }"""
html = re.sub(r'function saveDocentData\(\) \{.*?\}', save_docent_new, html, flags=re.DOTALL)
html = html.replace('<button class="btn btn-primary" onclick="saveDocentData()">💾 Desar observacions</button>', '<button class="btn btn-primary" onclick="saveDocentData()">💾 Desar observacions</button>\n            <span id="docent-save-status" style="font-size: 0.85rem; color: var(--color-coop); font-weight: 600;"></span>')

# 16. FOOTER
footer = """
  <footer style="text-align: center; padding: 2rem; color: var(--text-muted); font-size: 0.85rem; border-top: 1px solid var(--border-color); margin-top: 3rem;">
    El riu de la vida · Recerca i acció 2026-27 · Versió docent | Les dades de la graella d'observació es guarden localment al teu navegador (localStorage)
  </footer>
"""
html = html.replace('</main>', '</main>' + footer)

with open("index_docent.html", "w", encoding="utf-8") as f:
    f.write(html)
