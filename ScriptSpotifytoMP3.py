import subprocess
import sys

# URL de tu playlist
spotify_link = "https://open.spotify.com/playlist/37i9dQZF1E8UXBoz02kGID"

# Llamamos al mismo intérprete de Python para ejecutar el módulo de spotDL
subprocess.check_call([
    sys.executable, "-m", "spotdl", "download", spotify_link
])
