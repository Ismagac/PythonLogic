import subprocess
import sys
import os

def download_spotify_playlist(playlist_url, output_dir="downloads"):
    """
    Descarga una playlist de Spotify usando spotDL.
    
    Args:
      playlist_url (str): URL de la playlist de Spotify.
      output_dir (str): Carpeta donde se guardarán los MP3 (se crea si no existe).
    """
    # Asegurarnos de que la carpeta existe
    os.makedirs(output_dir, exist_ok=True)
    
    # Construir el comando para spotdl
    cmd = [
        sys.executable, "-m", "spotdl",
        "download", playlist_url,
        "--output", os.path.join(output_dir, "{artist} - {title}.{ext}")
    ]
    
    # Ejecutar el comando
    try:
        subprocess.check_call(cmd)
        print(f"✅ Descarga completada en '{output_dir}'")
    except subprocess.CalledProcessError as e:
        print("❌ Error al descargar la playlist:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python download_playlist.py <URL_DE_LA_PLAYLIST>")
        sys.exit(1)
    
    playlist_link = sys.argv[1]
    download_spotify_playlist(playlist_link)