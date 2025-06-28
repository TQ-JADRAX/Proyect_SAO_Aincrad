import subprocess
import os
from dotenv import load_dotenv
from openai import OpenAI

# RUTA ABSOLUTA al archivo .env 
load_dotenv("C:/Proyect_SAO_Aincrad/API-AI_Commits/Api-key.env")


api_key = os.getenv("OPENAI_API_KEY")

# Inicializar cliente OpenAI
client = OpenAI(api_key=api_key)

def obtener_commits(n=10):
    try:
        output = subprocess.check_output(
            ["git", "log", f"-n{n}", "--pretty=format:%s"],
            stderr=subprocess.DEVNULL,
            text=True
        )
        return output.strip().split("\n")
    except subprocess.CalledProcessError:
        print("❌ Error al ejecutar git log. ¿Estás en un repositorio Git?")
        return []

def filtrar_features(commits):
    return [c for c in commits if c.lower().startswith("feat:")]

def generar_anuncio(commits_filtrados):
    if not commits_filtrados:
        return "No se encontraron nuevas funcionalidades en los últimos commits."

    prompt = (
        "Genera un anuncio llamativo y breve en estilo de redes sociales (Discord o Twitter) "
        "basado en los siguientes commits de nuevas funcionalidades:\n\n"
        + "\n".join(commits_filtrados)
    )

    try:
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error al generar con OpenAI: {e}"

def main():
    commits = obtener_commits()
    features = filtrar_features(commits)
    anuncio = generar_anuncio(features)
    print("\n📢 Anuncio generado:\n")
    print(anuncio)

if __name__ == "__main__":
    main()