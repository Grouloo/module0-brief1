## Démarrer

### Lancer le serveur HTTP

```bash
uvicorn main:app --host 0.0.0.0 --port 8
```

L'API sera ensuite disponible à l'adresse http://0.0.0.0/

## Endpoints

### Analyser un texte

```
POST /analyse_sentiment
```

#### Body

```json
{
  "text": "string"
}
```

#### Réponse

```json
{
  "raw": {
    "neg": "float",
    "neu": "float",
    "pos": "float",
    "compound": "float"
  },
  "interpretation": {
    "label": "string",
    "emoji": "string"
  }
}
```
