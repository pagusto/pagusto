#!/usr/bin/env bash
# Exporta tus datos de Oura de los últimos 14 días a un solo archivo.
#
#   1. Consigue el token: app Oura → Oura Developer → Personal Access Tokens
#   2. chmod +x oura-export.sh
#   3. OURA_TOKEN='tu_token' ./oura-export.sh
#   4. Mándame SOLO el archivo oura-export.json — nunca el token.

set -uo pipefail

: "${OURA_TOKEN:?Falta el token. Uso: OURA_TOKEN='xxx' ./oura-export.sh}"

END=$(date -u +%Y-%m-%d)
START=$(date -u -d '14 days ago' +%Y-%m-%d 2>/dev/null || date -u -v-14d +%Y-%m-%d)
OUT="oura-export.json"

echo "Rango: $START → $END"
echo "{" > "$OUT"

first=1
for ep in daily_activity daily_readiness daily_sleep daily_stress; do
  [ $first -eq 0 ] && echo "," >> "$OUT"
  first=0
  echo "  Descargando $ep…"
  printf '"%s": ' "$ep" >> "$OUT"
  curl -sS -H "Authorization: Bearer ${OURA_TOKEN}" \
    "https://api.ouraring.com/v2/usercollection/${ep}?start_date=${START}&end_date=${END}" \
    >> "$OUT" || echo 'null' >> "$OUT"
done

echo "}" >> "$OUT"

echo
echo "Listo → $OUT"
echo
echo "Resumen rápido:"
python3 - "$OUT" <<'PY' 2>/dev/null || echo "(instala python3 para ver el resumen; el archivo está igual)"
import json,sys
d=json.load(open(sys.argv[1]))
act=(d.get("daily_activity") or {}).get("data",[])
rdy=(d.get("daily_readiness") or {}).get("data",[])
slp=(d.get("daily_sleep") or {}).get("data",[])
print(f"{'fecha':<12}{'kcal tot':>9}{'kcal act':>9}{'pasos':>8}{'ready':>7}{'sleep':>7}")
rd={r['day']:r.get('score') for r in rdy}
sd={s['day']:s.get('score') for s in slp}
for a in act[-14:]:
    day=a['day']
    print(f"{day:<12}{a.get('total_calories','—'):>9}{a.get('active_calories','—'):>9}"
          f"{a.get('steps','—'):>8}{rd.get(day,'—'):>7}{sd.get(day,'—'):>7}")
ac=[a.get('active_calories') for a in act if a.get('active_calories')]
tc=[a.get('total_calories') for a in act if a.get('total_calories')]
if tc: print(f"\nMedia kcal TOTAL: {sum(tc)//len(tc)}   ← este es tu TDEE medido")
if ac: print(f"Media kcal activas: {sum(ac)//len(ac)}")
PY
