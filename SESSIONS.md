# MANTLE — Journal de sessions

---

## J1 — P0-A : Session logger
**Date :** 09 mars 2026

**Accompli :**
- Environnement WSL Ubuntu 24.04 + VS Code opérationnel
- Repo GitHub initialisé : https://github.com/katssen4/Mantle
- `session_logger.py` : logger append-only en `.jsonl`, timestamp UTC, métadonnées
- `test_logger.py` : test sans API, validation écriture fichier
- `.gitignore` sécurisé pour `.env` et `.env.local`
- Premier push GitHub réussi, credential.helper configuré

**Concepts validés :**
- Format `.jsonl` vs `.json` — pourquoi append-only
- `timezone.utc` — obligatoire en contexte multi-fuseaux APAC/Europe
- Pattern observabilité : capturer input + output + timestamp + metadata
- Workflow VS Code + terminal WSL intégré
- Git init / remote / push depuis WSL

**Décisions d'architecture :**
- Fichiers Python créés dans VS Code directement (pas txt renommé)
- Terminal WSL dans VS Code via Ctrl+J
- Claude Code utilisé comme réviseur, pas auteur principal
- `SESSIONS.md` = journal de bord session par session (ce fichier)

**Prochaine étape — J2 :**
Connecter le logger à l'API Claude réelle. Un vrai appel, une vraie réponse, loggée automatiquement.