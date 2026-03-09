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

## J2 — P0-A : Premier appel API réel
**Date :** 09 mars 2026
**Accompli :**
- Dépendances installées : `anthropic`, `python-dotenv` (--break-system-packages)
- `.env` créé et sécurisé avec la clé API Anthropic
- `api_test.py` : premier appel réel à claude-haiku-4-5-20251001
- Réponse reçue, 64 tokens, loggée automatiquement dans `session_log.jsonl`
- Résolution : `python` → `python3` sur Ubuntu 24.04
- Résolution : mismatch `log_session` → `log_exchange` (nom réel dans session_logger.py)

**Concepts validés :**
- Mécanique de base d'un appel API LLM : model, max_tokens, messages, content
- `response.usage` : input_tokens + output_tokens — ce qui se paie
- `response.content[0].text` — pourquoi `[0]` : un LLM peut retourner plusieurs blocs
- `.env` + `load_dotenv()` : pattern sécurité, la clé n'est jamais dans le code
- Append-only confirmé : deux entrées dans le `.jsonl`, deux modèles différents

**Décisions d'architecture :**
- Modèle de dev = `claude-haiku-4-5-20251001` — suffisant pour apprendre, coût minimal
- Champ `tokens` ajouté aux métadonnées du logger dès J2

**Prochaine étape — J3 :**
Explorer la mécanique des tokens : input vs output, ce qui fait varier le compteur,
et toucher la limite qui rend le RAG nécessaire.