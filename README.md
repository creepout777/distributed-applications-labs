# Applications Distribuées — TP (Python)

Ce dépôt regroupe des **mini-projets Python pédagogiques** autour des systèmes distribués et de la cybersécurité appliquée aux APIs : communication client/serveur, fiabilité (timeout, retry, backoff), asynchronisme, sérialisation (JSON/XML/Protobuf) et validation défensive.

## Objectifs pédagogiques

- Comprendre les bases d’une communication distribuée avec la librairie standard Python.
- Mettre en œuvre des patterns de résilience côté client.
- Manipuler des formats de sérialisation avec validation stricte.
- Identifier les surfaces de risque courantes (input invalide, timeouts, désérialisation).

## Structure du dépôt

### Séance 5 — Concepts distribués (exemples Python)
- `ar-cs1-exemple-1-mini-client-serveur-http/`
  - `serveur.py`
  - `client.py`
- `ar-cs1-exemple-2-retry-backoff-exponentiel/`
  - `retry_backoff.py`
- `ar-cs1-exemple-3-appels-asynchrones-asyncio/`
  - `asyncio_appels.py`

### Séance 6 — APIs et fiabilité
- `ar-cs6-exemple-1-mini-api-http/`
  - `mini_api_server.py`
- `ar-cs6-exemple-2-client-urllib-timeout-request-id/`
  - `api_client.py`
- `ar-cs6-exemple-3-retry-backoff-exponentiel/`
  - `retry_backoff.py`

### Séance 7 — Sérialisation / marshalling
- `seance7-demo-1-json-robuste/`
  - `json_robuste.py`
- `seance7-demo-2-xml-parsing-securite/`
  - `xml_parsing.py`
- `seance7-demo-3-protobuf-python/`
  - `protobuf_encode_decode.py`
  - `protobuf_compat.py`

## Prérequis

- Python **3.10+** recommandé
- Dépendances externes uniquement pour la partie Protobuf :
  - `protobuf`
  - `protoc` (compilateur Protocol Buffers) si vous générez `document_pb2.py`

## Lancement rapide

Depuis la racine du dépôt :

```bash
# Séance 5 - exemple client/serveur HTTP
python ar-cs1-exemple-1-mini-client-serveur-http/serveur.py
# (dans un 2e terminal)
python ar-cs1-exemple-1-mini-client-serveur-http/client.py

# Séance 5 - retry/backoff
python ar-cs1-exemple-2-retry-backoff-exponentiel/retry_backoff.py

# Séance 5 - asynchronisme asyncio
python ar-cs1-exemple-3-appels-asynchrones-asyncio/asyncio_appels.py

# Séance 6 - mini API HTTP
python ar-cs6-exemple-1-mini-api-http/mini_api_server.py
# (dans un 2e terminal)
python ar-cs6-exemple-2-client-urllib-timeout-request-id/api_client.py

# Séance 6 - retry générique
python ar-cs6-exemple-3-retry-backoff-exponentiel/retry_backoff.py

# Séance 7 - JSON robuste
python seance7-demo-1-json-robuste/json_robuste.py

# Séance 7 - XML parsing défensif
python seance7-demo-2-xml-parsing-securite/xml_parsing.py
```

## Protobuf (séance 7)

Exemple minimal de génération du module Python :

```bash
pip install protobuf
protoc --python_out=. document.proto
```

Puis exécution :

```bash
python seance7-demo-3-protobuf-python/protobuf_encode_decode.py
python seance7-demo-3-protobuf-python/protobuf_compat.py
```

> Remarque : `protobuf_compat.py` illustre la lecture de champs compatibles à partir d’un objet déjà désérialisé.

## Notes

- Les scripts sont volontairement simples et orientés démonstration.
- Les trois supports de cours HTML d’origine ne font pas partie du contenu versionné de ce dépôt Git.
