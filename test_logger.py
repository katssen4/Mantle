from session_logger import log_exchange

# Simule un échange sans toucher l'API
entry = log_exchange(
    prompt="Qu'est-ce qu'un orchestrateur IA ?",
    response="Un orchestrateur coordonne des agents spécialisés vers un objectif commun.",
    metadata={"session": "J1", "phase": "P0-A"}
)

print("Entrée loggée :")
print(entry)

# Vérifie que le fichier existe
with open("sessions/session_log.jsonl") as f:
    lines = f.readlines()
    print(f"\nNombre d'entrées dans le log : {len(lines)}")