# ZLECENIE GLOWNE 82 - Permissions-Policy dla API

## Cel

Dodac naglowek `Permissions-Policy` (dawniej Feature-Policy) do API response. Blokuje dostep do API przegladarki (geolocation, camera, microphone, accelerometer), ktore nie sa uzywane przez API.

## Polityka

```http
Permissions-Policy: geolocation=(), camera=(), microphone=(), accelerometer=(), magnetometer=(), gyroscope=(), payment=(), usb=()
```

## Uwaga

Permissions-Policy jest dodatkowa warstwa obrony (defense-in-depth). API nie uzywa tych features, ale atakujacy moze probowac exploitowac API do dostepu do tych zasobow np. poprzez XSS lub content injection.

## Status

TODO — low priority.
