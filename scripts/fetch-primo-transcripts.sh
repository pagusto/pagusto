#!/usr/bin/env bash
# Fase 1 del mapa de evidencia Primobolan/TRT: recolección de transcripciones.
#
# Ejecuta esto EN TU MÁQUINA (no en el contenedor de Claude Code, que tiene
# YouTube bloqueado por política de egreso).
#
#   chmod +x fetch-primo-transcripts.sh
#   ./fetch-primo-transcripts.sh
#
# Salida: ./transcripts/{canal}_{videoid}.txt  + metadata.csv
# Después súbeme la carpeta y hago las Fases 2-4 completas.

set -uo pipefail

OUT="./transcripts"
META="$OUT/metadata.csv"
PER_QUERY="${PER_QUERY:-8}"   # vídeos por término de búsqueda

command -v yt-dlp >/dev/null || { echo "Falta yt-dlp:  pip install -U yt-dlp"; exit 1; }
mkdir -p "$OUT"

# Nota: NO se usa --no-check-certificates. Si tu red necesitara algo así,
# lo correcto es apuntar al bundle de CA, no desactivar la verificación.
COMMON=(--ignore-errors --no-warnings --skip-download
        --write-auto-sub --write-sub --sub-lang "en.*" --sub-format vtt
        --sleep-requests 1 --retries 3)

echo "video_id,channel,title,upload_date,duration_s,view_count,url" > "$META"

collect() {   # $1 = target (ytsearchN:... o URL de canal)
  yt-dlp "${COMMON[@]}" \
    -o "$OUT/%(channel)s_%(id)s.%(ext)s" \
    --print-to-file "%(id)s,\"%(channel)s\",\"%(title)s\",%(upload_date)s,%(duration)s,%(view_count)s,https://youtu.be/%(id)s" "$META" \
    "$1" 2>&1 | grep -viE "^\[download\]|Deleting" || true
}

echo "== Términos de búsqueda =="
for q in "primobolan TRT" \
         "metenolone TRT add-on" \
         "primo test ratio" \
         "DHT derivatives TRT" \
         "primobolan estrogen control" \
         "primobolan bloodwork estradiol"; do
  echo "  -> $q"
  collect "ytsearch${PER_QUERY}:${q}"
done

echo "== Canales =="
# Añade o quita canales aquí. Se cogen los 25 vídeos más recientes y se filtra
# por título; sube el número si quieres barrer más atrás en el historial.
for ch in "https://www.youtube.com/@MorePlatesMoreDates/videos" \
          "https://www.youtube.com/@VigorousSteve/videos" \
          "https://www.youtube.com/@CortexLabsChannel/videos"; do
  echo "  -> $ch"
  collect "$(printf '%s' "$ch")" --playlist-end 25 \
    --match-filter "title~=(?i)(primo|metenolone|methenolone|DHT|estrogen|estradiol)"
done

echo "== Convirtiendo VTT a texto plano =="
for f in "$OUT"/*.vtt; do
  [ -e "$f" ] || continue
  # quita cabeceras, timestamps, tags inline y líneas duplicadas consecutivas
  sed -E '/^(WEBVTT|Kind:|Language:|NOTE)/d; /^[0-9]{2}:[0-9]{2}:[0-9]{2}/d; /^$/d; s/<[^>]*>//g' "$f" \
    | awk '!seen[$0]++' > "${f%.*}.txt"
  rm -f "$f"
done

echo
echo "Listo. $(ls -1 "$OUT"/*.txt 2>/dev/null | wc -l) transcripciones en $OUT/"
echo "Metadata en $META"
echo "Súbeme la carpeta completa y sigo con las Fases 2-4."
