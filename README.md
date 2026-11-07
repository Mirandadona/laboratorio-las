# laboratorio-las

# Laboratorio: Seguridad en aplicaciones web, MTTD y MTTR

**Asignatura:** Lenguajes de Programación con Aspectos de Seguridad
**Unidad:** 3, Código Seguro y Modelo OWASP
**Estudiante:** Diego Alejandro Miranda Hernández

## Estructura del proyecto

```
laboratorio-las/
├── app.py           
├── crearDB.py       
├── detector.py      
├── usuarios.db
├── eventos.log      
├── respuesta.log    
└── templates/
    ├── registro.html
    └── login.html
```

## Cómo ejecutarlo

```bash
python -m venv venv
venv\Scripts\activate
pip install flask
python crearDB.py
python app.py          # terminal 1
python detector.py     # terminal 2
```

## Controles de seguridad aplicados

- Validación y saneamiento de entradas (usuario 4–20 caracteres alfanuméricos/guion bajo, correo válido, contraseña ≥ 8).
- Consultas parametrizadas en todas las operaciones SQL (prevención de SQL Injection).
- Contraseñas almacenadas con hash (`generate_password_hash` / `check_password_hash`).
- Rechazo de usuarios o correos duplicados.
- Registro de eventos de autenticación en `eventos.log`.
- Detección de 3 o más intentos fallidos y bloqueo simulado en `respuesta.log`.

## Resultados MTTD y MTTR

| Prueba | Usuario    | MTTD (s) | MTTR (s) |
|--------|------------|----------|----------|
| 1      | Diego      | 11       | 71       |
| 2      | usuario_02 | 10       | 41       |
| 3      | usuario_03 | 13       | 13       |

**MTTD promedio** = (11 + 10 + 13) / 3 = **11.33 segundos**
**MTTR promedio** = (71 + 41 + 13) / 3 = **41.67 segundos**


