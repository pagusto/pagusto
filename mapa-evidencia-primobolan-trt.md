# Mapa de evidencia: metenolona (Primobolan) junto a testosterona

**Qué es esto:** un mapa de afirmaciones contra evidencia. **No contiene un protocolo
recomendado** — el encargo lo prohibía explícitamente y el documento lo respeta.

**Fecha:** 2026-07-27

---

## 0. Procedencia de cada dato (léelo antes que nada)

Este informe se construyó bajo restricciones de red severas, y la honestidad sobre
*qué se verificó y qué no* es parte del producto. Tres niveles:

| Nivel | Significado | Qué cae aquí |
|---|---|---|
| **[V]** | **Verificado en esta sesión** contra fuente, con números leídos | Bhasin 2001, Liu 2006, Baggish 2017, Thompson 1989, lipasa hepática 2003, umbral Hct >54 %, tasas de falsificación |
| **[I]** | **Recuperado a nivel de índice/abstract** por agentes con búsqueda activa | Toda la farmacología de metenolona y el inventario de ensayos (§2, §3) |
| **[R]** | **Recuerdo no verificado** — pista para comprobar, no dato para citar | Parte de §6 (monitoreo) |

**Ningún texto completo pudo abrirse.** El proxy de egreso devolvió `403 CONNECT` para
PubMed, Europe PMC, Crossref, editoriales, y hasta Wikipedia. Donde un número vive en
una tabla y no en el abstract, se dice y **no se inventa el número**.

---

## 1. Fases 1–2 (afirmaciones de creadores): NO SE PUDIERON RESPONDER

Se intentó. Cinco agentes, 123 llamadas a herramientas. Resultado: **cero páginas
recuperadas.**

- **YouTube bloqueado** por política de egreso (`403` en CONNECT). `yt-dlp` se instaló
  y funciona, pero no hay ruta a YouTube. El flag `--no-check-certificates` sugerido
  en el encargo **no aplica**: no es un fallo de TLS sino una denegación de política, y
  el README del entorno prohíbe rodearla.
- **Todo lo demás también bloqueado**: el sitio propio de MPMD, MESO-Rx, Reddit,
  archive.org, Listennotes, Spotify, Apple Podcasts, Wikipedia.

Quedó solo el índice de búsqueda. Y ahí apareció un problema que invalida el uso de
esos resúmenes para atribuir afirmaciones: **el resumidor mezclaba contenido de los
creadores con SEO no relacionado** (Swolverine, CrazyBulk, ExcelMale, biomogging).
Varios agentes lo detectaron de forma independiente y se negaron a atribuir nada
mecanicista. Fue la decisión correcta.

### Lo único establecido

| Hallazgo | Nivel |
|---|---|
| Vigorous Steve tituló un vídeo *"Schering Oral Primobolan… **(Still Worse Than Anavar)**"* — el paréntesis es su propio veredicto editorial, y es desinflador | Título [I] |
| Vigorous Steve: *"Best Weekly Dose Of Primobolan **(Side-Effect Free Anabolic?)**"* — con interrogante, interroga la fama de suavidad | Título [I] |
| MPMD tiene un episodio *"Does Primobolan Act As An AI? Estradiol Blood Work Before And After"* (7 oct 2020) con analítica propia | Título [I] |
| Cortex Labs = Ryan Michael Ballow | [I] |
| MPMD: postura aparentemente favorable **pero condicionada a autenticidad del producto** | Fragmento sin verificar |

### Lo NO establecido, para ningún creador

Ni un solo **ratio test:primo**. Ni una dosis atribuible. Ni una afirmación mecanicista
citable. **Ni "% de runtime promocional"** — eso es imposible de calcular sin audio y no
se estimó.

> ⚠️ **Trampa de lectura:** circuló un dato de MPMD sobre **1200 mg/sem de metenolona**.
> Es él *reportando un ensayo clínico* (Kennedy 1968) **en mujeres posmenopáusicas con
> cáncer de mama metastásico**. No es una recomendación suya. Atribuírselo como dosis
> sugerida sería un error grave.

**Conclusión de esta sección:** la pregunta "¿en qué coinciden y en qué se contradicen
los creadores?" **no tiene respuesta desde este entorno**. Requiere ver los vídeos.

---

## 2. Farmacología de la metenolona — lo que hay y lo que no [I]

### Identidad estructural (no está en disputa)

| | |
|---|---|
| Metenolona | 1-metil-5α-androst-1-en-17β-ol-3-ona = **1-metil-Δ¹-DHT** |
| Acetato (oral) | éster 17β-acetato · CAS 434-05-9 |
| Enantato (inyectable) | éster 17β-heptanoato · CAS 303-42-4 |
| Anillo A | **5α-saturado** (sin Δ⁴), más Δ¹ y **metilo en C1** |
| C17α | **hidrógeno — sin grupo alquilo** |

Ninguno de los dos ésteres es 17α-alquilado. La actividad oral del acetato viene del
metilo en C1 / Δ¹ que frena el metabolismo hepático, **no** de 17α-alquilación.

### ¿Aromatiza? — casi con certeza no, pero nadie lo ha medido

**Argumento estructural (fuerte):** la aromatasa (CYP19A1) requiere sustratos
Δ⁴-3-ceto. Un anillo A 5α-saturado elimina eso — es la misma razón por la que la DHT no
aromatiza.

**Segundo bloqueo, y es el dato más elegante del informe:** Schering — la misma empresa
que fabricó Primobolan — desarrolló **atamestano (1-metilandrosta-1,4-dien-3,17-diona)**,
donde la literatura afirma explícitamente que *"la introducción de un grupo metilo en C-1
fue concebida para **impedir la aromatización**"*. Atamestano acabó siendo un **inhibidor
competitivo de aromatasa (Kᵢ ≈ 2,5 × 10⁻⁷ mol/L)**. La metenolona lleva **ambos**: el
metilo en C1 y el anillo A saturado.

**Lo que NO existe:**
- **Ningún ensayo de aromatasa con metenolona como sustrato.** El assay es estándar y se
  ha corrido sobre otros andrógenos sintéticos cuando la duda se consideró abierta.
  Sobre metenolona, nadie lo hizo.
- **Ningún estudio humano que mida estradiol o estrona durante administración de
  metenolona.** Cero.
- **Ningún dato sobre si la metenolona inhibe la aromatasa.** Dado el precedente de
  atamestano es una hipótesis razonable. Está **completamente sin probar**.

> **Error documentado que conviene conocer:** la página "Metenolone — an overview" de
> ScienceDirect afirma que la metenolona es 17α-alquilada y que "tras aromatizarse a
> estrona y estradiol se une a receptores de estrógeno". **Ambas cosas son falsas.** Así
> es como un error se lava hasta parecer citable.

### Afinidad por el receptor de andrógenos

**Fuente única real:** Saartok, Dahlberg, Gustafsson. *Endocrinology* 1984;114(6):2100–2106.
PMID 6539197. Competición contra [³H]metiltrienolona en citosol de músculo esquelético
de rata, próstata ventral de rata y músculo de conejo.

- Orden: **MT > nandrolona > metenolona > testosterona > mesterolona**. La metenolona
  une AR **por encima de la testosterona**.
- **Ratio músculo:próstata ≈ 0,4–1,7** para casi todos los compuestos — esencialmente la
  unidad. **A nivel de unión al receptor no hay selectividad tisular.** Esto socava
  directamente la idea folclórica de que la "disociación anabólica:androgénica" del
  primobolán sea un fenómeno de afinidad.

**El número concreto no sobrevive a la verificación.** La RBA numérica vive en la tabla
del paper, no en el abstract, y no se pudo abrir. **No se da un número que no se leyó.**
Consecuencia práctica: cualquier fuente que cite "RBA del primo = X" debería tener que
señalar tabla y página.

**Matices que pesan mucho:**
- AR citosólico de rata/conejo, metodología de 1984 — **no es AR humano**.
- Unión ≠ transactivación. **No existe EC₅₀/Emax en AR humano para metenolona.**
- **3α-reducción:** el metabolito urinario dominante tras dosis oral es
  3α-hidroxi-1-metilen-5α-androstan-17-ona (Massé 1990), consistente con reducción 3α
  intensa in vivo. La 3α-HSD se expresa en músculo esquelético e inactiva andrógenos
  tipo DHT localmente. Es la explicación mecanicista más creíble del reporte persistente
  de que "el primo rinde menos de lo que su afinidad sugiere". **La medición en músculo
  humano no se ha hecho.**

### SHBG — la afirmación falla en el primer paso

Del mismo Saartok 1984, orden de afinidad por SHBG humana:

> mesterolona > DHT > testosterona > 3β-adiol > 3α-adiol = 17α-metiltestosterona >
> **metenolona** > metandienona > estanozolol

La metenolona está **abajo**, por debajo de la testosterona. La mesterolona es la de
alta afinidad (~4× DHT). **La idea de que el primo desplaza testosterona de la SHBG y
sube la T libre no tiene dónde apoyarse: su afinidad es baja.**

---

## 3. Inventario completo de ensayos humanos de metenolona [I]

Esta es la sección más importante del informe.

| Pregunta | Respuesta |
|---|---|
| Estudios humanos identificables en literatura indexada | **~20 informes primarios**, 1962–2024 |
| Ensayos prospectivos **controlados** | **5** |
| Aleatorizados con desenlace clínico duro | **1** (Kennedy 1968, cáncer de mama) |
| Controlados con placebo, de cualquier tipo | **1** (Fowler 1965, hombres sanos — **nulo**) |
| **Dosis-respuesta en hombres sanos para composición corporal o rendimiento** | **CERO. Ninguno. Ni uno.** |
| **Ensayos de metenolona enantato inyectable en hombres sanos, a cualquier dosis** | **CERO** |
| Registros en ClinicalTrials.gov | **Ninguno** |
| Humanos documentados que hayan recibido metenolona, en total | ~**300–400** |
| Era de estudio clínico activo | **1962 – ~1980**, más goteo japonés residual |

> Toda esa base de evidencia global — 60 años, todas las indicaciones, todos los países —
> **es más pequeña que un solo ensayo fase II moderno.**

### El único ensayo en hombres sanos

**Fowler WM Jr, Gardner GW, Egstrom GH.** *Effect of an anabolic steroid on physical
performance of young men.* **J Appl Physiol 1965;20(5):1038–1040.**

- **n = 47.** Cuatro brazos: placebo (8), fármaco solo (9), placebo+ejercicio (15),
  fármaco+ejercicio (15)
- **Acetato de metenolona, 20 mg/día, ORAL, 16 semanas**
- Medidos: fuerza isométrica, rendimiento motor, capacidad de trabajo, capacidad vital,
  circunferencias, pliegues, peso
- **Resultado: ninguna diferencia significativa en NINGUNA medida.**

**Interpretación honesta, en ambas direcciones:** este nulo **no** prueba que la
metenolona no funcione. Prueba que *20 mg/día por vía oral de un éster no 17α-alquilado,
en 1965, no produjo nada medible*. Es la dosis baja de la etiqueta japonesa para
pacientes frágiles, no una dosis de rendimiento. El ensayo es a la vez (a) el único
placebo-controlado de composición corporal en hombres sanos que existe, y (b) poco
informativo sobre la vía y las dosis que la gente usa.

### La dosis clínica más alta jamás documentada

**Kennedy BJ, Yarbro JW.** *Cancer* 1968;21(2):197–201.
Aleatorizado. **Mujeres posmenopáusicas con cáncer de mama avanzado.**
**400–1.200 mg/sem IM, ≥3 meses.** n=43 metenolona (27 evaluables) vs 13 testosterona
propionato. Resultado: 48 % mejoría objetiva vs 0/13.

**Los propios autores no reclamaron el efecto** — lo atribuyeron a la dosis masiva, a un
defecto metodológico del protocolo en uso, al azar, o a diferencia biológica entre grupos.

Es el único dataset humano con dosis que solapan el uso actual. Población: mujeres con
cáncer metastásico. Desenlace: regresión tumoral, no masa magra.

### Lo más cercano a un ensayo "de músculo"

Okamoto et al. 2010 y 2011 (*Int J Neurosci*; *Am J Phys Med Rehabil*), pacientes con
ictus subagudo, **100 mg/sem IM × 6 semanas**. CSA de muslo +13,4 % parético / +14,5 %
no parético vs control +3,3 % / +5,2 % (p<0,05). **No aleatorizado, no placebo, n=25–26,
ancianos con daño neurológico, sin seguimiento más allá de 6 semanas.**

### Dosis: etiqueta vs ensayos vs uso real

| Contexto | Dosis |
|---|---|
| **Etiqueta japonesa, enantato depot** | **100 mg IM cada 1–2 semanas → 50–100 mg/sem** |
| Etiqueta japonesa, acetato oral | 10–20 mg/día → 70–140 mg/sem |
| Fowler 1965 (hombres sanos) | 20 mg/día oral |
| Okamoto (ictus) | 100 mg/sem IM |
| Knöbel 1975 (cirrosis) | 200 mg/sem IM |
| **Kennedy 1968 (cáncer, mujeres)** | **400–1.200 mg/sem IM** |
| **Uso entusiasta reportado en fuentes legas** | **400–600 mg/sem** |

**El uso entusiasta típico corre a 4–6× la dosis máxima de etiqueta, por una vía
(inyectable en hombres sanos) que nunca se ha ensayado.**

### Hepatotoxicidad — el punto que más contradice al folclore

- **PMID 8334198** (*Ann Hematol* 1993): **muerte por fallo hepático** en varón de 75
  años tras acetato de metenolona; histopatología compatible con daño hepático inducido
  por fármaco.
- **PMID 7615051** (1995): efecto adverso grave con acetato de metenolona.
- **PMDA (Japón), 19 marzo 2012:** revisión de precauciones que añade **trastorno de la
  función hepática e ictericia** como reacción adversa grave **para ambos ésteres —
  acetato Y enantato**.
- La etiqueta japonesa exige **pruebas hepáticas periódicas** en uso prolongado.

### El número de las ovejas

El efecto más impresionante de la metenolona en la literatura (**+79,97 % de masa** en
dorsal ancho vs +11,07 % control) es en **24 ovejas**, con el músculo bajo **estimulación
eléctrica crónica** para cardiomioplastia (*Ann Thorac Surg* 1995, PMID 7695425). **No
tiene contraparte humana.** Un motor de búsqueda ya intentó presentarlo como dato humano
durante esta investigación.

---

## 4. Adjudicación de afirmaciones

Afirmaciones que **circulan** en el ambiente. **No se atribuyen a ninguna persona
concreta** — no se recuperó ninguna transcripción.

| # | Afirmación | Veredicto |
|---|---|---|
| 1 | No aromatiza → puedo subir carga androgénica sin subir E2 | **PARCIAL → EXTRAPOLADO** |
| 2 | Baja el estrógeno / actúa como IA | **NO SOPORTADO** (hipótesis interesante, sin probar) |
| 3 | Desplaza T de la SHBG → sube T libre | **CONTRADICHO** |
| 4 | Es "suave", de los más seguros | **EXTRAPOLADO** (y parcialmente contradicho) |
| 5 | El inyectable no es hepatotóxico → sin monitoreo hepático | **CONTRADICHO** |
| 6 | Alta afinidad AR → potente por mg | **PARCIAL, pero engañoso** |
| 7 | Buen añadido de bajo riesgo a TRT | **NO SOPORTADO** |
| 8 | Necesita 600 mg+ porque es débil | **NO SOPORTADO** |
| 9 | Vida media ~10,5 días → 1×/semana basta | **NO SOPORTADO** |
| 10 | Bueno para definición / preserva magro en déficit | **NO SOPORTADO** |
| 11 | Derivado de DHT → sin retención ni ginecomastia | **PARCIAL, incompleto** |
| 12 | Seguro a largo plazo / todo el año | **NO SOPORTADO** |

### Las que más importan, desarrolladas

**#3 — CONTRADICHO.** Falla en la premisa: Saartok 1984 sitúa la afinidad de la
metenolona por SHBG **por debajo de la testosterona**. La que tiene afinidad alta es la
mesterolona (~4× DHT). No hay mecanismo que sostenga el desplazamiento.

**#5 — CONTRADICHO.** El razonamiento "no es 17α-alquilado, luego no es hepatotóxico" es
estructuralmente atractivo y empíricamente falso. Hay una **muerte publicada** por fallo
hepático, y en 2012 el regulador japonés añadió disfunción hepática e ictericia a la
etiqueta **del enantato inyectable también**, no solo del oral.

**#6 — PARCIAL pero engañoso.** Sí, une AR por encima de testosterona. Pero: (a) es AR de
rata/conejo de 1984, no humano; (b) unión ≠ transactivación, y no existe dato de
transactivación humana; (c) la 3α-reducción intensa in vivo probablemente lo inactiva en
músculo; (d) el ratio músculo:próstata ≈ 1 elimina la base de la supuesta selectividad
tisular. La afinidad alta **no se traduce** en potencia demostrada.

**#8 — NO SOPORTADO, y es el vacío más grande.** Para afirmar que 600 mg es el umbral de
eficacia hace falta una curva dosis-respuesta. **No existe ninguna, a ninguna dosis, en
ninguna población sana.** La cifra es puro consenso de ambiente.

**#9 — NO SOPORTADO.** No existe **ningún estudio de farmacocinética humana del enantato
de metenolona**. Los estudios antidopaje (Massé 1990) son acetato oral, dosis única de
50 mg. El "10,5 días" se repite en obras de referencia sin ensayo detrás.

**#1 — PARCIAL → EXTRAPOLADO.** La no aromatización está bien fundada estructuralmente
(§2). El salto está en el "por tanto": la **base de testosterona sigue aromatizando**, y
la carga androgénica total tiene costes que no pasan por el estrógeno (hematocrito,
lípidos, tejido cardíaco). "No sube E2" ≠ "es gratis".

---

## 5. Lo que estas discusiones sistemáticamente omiten

1. **Que no hay curva dosis-respuesta de metenolona a ninguna dosis.** Todo el debate de
   ratios se libra sobre un vacío. No es que la evidencia sea débil: es que no existe.
2. **Que "suave" confunde tolerabilidad subjetiva con riesgo orgánico medido.** Un
   compuesto puede *sentirse* bien y estar dañando lípidos y ventrículo en silencio.
   Ausencia de síntomas ≠ ausencia de daño.
3. **Que la ausencia de evidencia de daño para la metenolona es ausencia de ESTUDIO, no
   evidencia de seguridad.** Es la inversión lógica más costosa del ambiente.
4. **Que el riesgo cardíaco escala con dosis-años acumulados**, no con el ciclo actual
   (Baggish 2017 [V]). Un ciclo aislado no es la unidad de riesgo relevante.
5. **Que dos ésteres largos significan inicio lento Y salida lenta.** Si algo va mal, no
   hay freno rápido: se tarda semanas en bajar.
6. **Riesgo de identidad del producto.** La metenolona es cara → incentivo económico
   directo a falsificarla. Análisis por GC-MS de mercado negro: **~36 % sin el principio
   activo esperado** (Musshoff & Daldrup), **~42 % falsificados** (Neves & Caldas 2017),
   con **65 % de las soluciones oleosas** falsificadas [V]. Primobolan aparece entre los
   más sustituidos — por nandrolona o testosterona más baratas.
7. **Que los análisis rutinarios están confundidos en hombres musculados.** Creatinina
   sube por masa muscular → eGFR subestimada. ALT/AST y CK suben por entrenamiento →
   "daño hepático" que no lo es (y al revés: enmascaramiento).
8. **Polifarmacia.** Casi nadie corre un compuesto solo. Las interacciones no están
   estudiadas para ninguna de estas combinaciones.

---

## 6. Marcadores que la literatura usa y el consejo lego omite

> ⚠️ Sección mayormente **[R]** — el agente de monitoreo no pudo verificar fuentes.
> Trátese como lista de comprobación a validar, no como citas.

| Marcador | Por qué importa | Confusor |
|---|---|---|
| **Apolipoproteína B** | Cuenta partículas aterogénicas; mejor que LDL-C cuando las partículas son pequeñas y densas — exactamente lo que hacen los andrógenos | — |
| **Lp(a)** | Los andrógenos la **bajan** — complica el relato de "todo malo" y merece medirse | Genéticamente determinada |
| **Cistatina C** | Función renal **sin** el sesgo de masa muscular de la creatinina | Alterada por tiroides/corticoides |
| **Hematocrito + volumen plasmático** | El Hct sube en parte por contracción plasmática, no solo por eritrocitosis real | Hidratación, postura al extraer |
| **Ecocardiografía con strain** | Detecta disfunción sistólica subclínica antes que la FE | Requiere operador con experiencia |
| **NT-proBNP / troponina hs** | Estrés y daño miocárdico subclínico | Sube con ejercicio intenso reciente |
| **Cinética de PSA (velocidad)** | Más informativa que un valor aislado | Eyaculación, ciclismo, prostatitis |
| **Cribado de apnea del sueño** | Los andrógenos la empeoran; retroalimenta eritrocitosis e hipertensión | Infradiagnosticada de base |
| **GGT junto a ALT/AST** | Ayuda a separar señal hepática de daño muscular por entrenamiento | Alcohol |
| **Evaluación de ánimo** | Efectos psiquiátricos son de los más reportados y de los menos medidos | Nunca se objetiva |

**Fertilidad / eje HPG [V]:** Liu 2006 (*Lancet* 367:1412), análisis integrado de 30
estudios: mediana de recuperación a 20 M/ml = **3,4 meses**; probabilidad **67 % a 6
meses, 90 % a 12, 96 % a 16, 100 % a 24**. Advertencia: dosis moderadas, duración corta,
supervisado — **es el mejor caso**, no el escenario de dosis alta prolongada.

---

## 7. Corrección importante al informe previo (PR #6)

Un agente levantó una objeción metodológica válida que **debilita un argumento que hice
antes** y que conviene registrar:

En el informe anterior usé Thompson 1989 (testosterona −9 % HDL vs estanozolol −33 %)
para sostener que *la no aromatización* explica por qué un compuesto como la metenolona
presionaría más el HDL. **El contraste no aísla esa variable.** El estanozolol es **oral
y 17α-alquilado**; el enantato de testosterona es **inyectable y no alquilado**. Vía y
alquilación **co-varían** con la aromatización, y el paso hepático de primer orden de un
17αα tiene efecto propio sobre lipasa hepática y HDL.

La metenolona enantato es **inyectable y no 17α-alquilada** — está del lado "limpio" en
esas dos variables. Así que Thompson **no puede** transferirse directamente a ella. La
dirección del efecto sigue siendo mecanicísticamente plausible; la **magnitud tomada del
estanozolol no es transferible**.

Corolario: **no existe ninguna medición del efecto de la metenolona sobre HDL/LDL en
humanos.** Ni una.

---

## 8. Lo que no sabemos, ordenado por cuánto pesa

1. **Qué hace la metenolona en un hombre sano a dosis suprafisiológica.** Sin ensayo. A
   ninguna dosis. Por ninguna vía.
2. **Su farmacocinética humana.** No existe. El "10,5 días" no tiene ensayo detrás.
3. **Su efecto sobre lípidos en humanos.** No medido nunca.
4. **Si inhibe la aromatasa.** Hipótesis razonable por el precedente de atamestano.
   Sin probar.
5. **Qué hace la combinación** de dos ésteres largos a volumen alto crónico. Ningún
   ensayo ha combinado nada de esto.
6. **Si el frasco contiene lo que dice.** Entre ~36 % y ~42 % de los productos analizados
   no lo contenían [V].

---

## Fuentes

**Verificadas en esta sesión [V]:**
- Bhasin S, et al. *Testosterone dose-response relationships in healthy young men.* Am J Physiol Endocrinol Metab 2001;281:E1172–E1181.
- Liu PY, et al. *Rate, extent and modifiers of spermatogenic recovery after hormonal male contraception.* Lancet 2006;367:1412–1420.
- Baggish AL, et al. *Cardiovascular toxicity of illicit anabolic-androgenic steroid use.* Circulation 2017;135:1991–2002.
- Thompson PD, et al. *Contrasting effects of testosterone and stanozolol on serum lipoprotein levels.* JAMA 1989;261:1165–1168.
- Herbst KL, et al. *Testosterone administration to men increases hepatic lipase activity…* Am J Physiol Endocrinol Metab 2003;284:E1112–E1118.
- Bhasin S, et al. *Testosterone therapy in men with hypogonadism: an Endocrine Society clinical practice guideline.* JCEM 2018;103:1715–1744.
- Musshoff F, Daldrup T. *Black market in anabolic steroids.* · Neves DBJ, Caldas ED. Forensic Sci Int 2017;275:272–281.

**Recuperadas a nivel de índice [I]:**
- Saartok T, Dahlberg E, Gustafsson JÅ. Endocrinology 1984;114(6):2100–2106. PMID 6539197.
- Fowler WM Jr, Gardner GW, Egstrom GH. J Appl Physiol 1965;20(5):1038–1040.
- Kennedy BJ, Yarbro JW. Cancer 1968;21(2):197–201.
- Okamoto S, et al. Am J Phys Med Rehabil 2011;90(2):106–111. PMID 21173687.
- Okamoto S, et al. Int J Neurosci 2010;120(9):617–624. PMID 20707637.
- Massé R, Bi H, Ayotte C, Dugal R. *Identification of new urinary metabolites of methenolone acetate.* 1990.
- *Ann Hematol* 1993 — muerte por fallo hepático con acetato de metenolona. PMID 8334198.
- *Ann Thorac Surg* 1995 — cardiomioplastia en ovejas. PMID 7695425.
- PMDA Japón, 19 marzo 2012 — revisión de precauciones, ambos ésteres.

---

*Este documento mapea evidencia. No recomienda un protocolo, por diseño.*
