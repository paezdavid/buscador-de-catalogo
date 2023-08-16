# Catálogo Virtual de Bibliotecas del Estudiante

Motor de búsqueda local para chequear la disponibilidad de artículos, papers y/o monografías en las bibliotecas de la Universidad Nacional de Asunción.

El presente proyecto fue construido con el objetivo de mejorar la interfaz y la experiencia de usuario de sitios web ya existentes con las mismas (en incluso mejores) funcionalidades. Al mismo tiempo, fue desarrollado con fines educativos y buscando la mejora de los servicios dispuestos a los estudiantes de la Universidad Nacional de Asunción.
Se busca la colaboración de más personas para que el proyecto crezca y mejore en los aspectos donde se encuentra limitado (por ej., un filtro de búsqueda avanzada).

De momento, el proyecto funciona solamente de forma local, pero su instalación es bastante sencilla. En el futuro se espera desplegarlo con su propio dominio y servidor en la nube :)

## Inicializar el proyecto de forma local
### Ubuntu
```git
git clone https://github.com/paezdavid/buscador-de-catalogo.git
cd buscador-de-catalogo
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
flask run
```

### Windows
```git
git clone https://github.com/paezdavid/buscador-de-catalogo.git
cd buscador-de-catalogo
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
flask run
```

## UI
![buscador](https://github.com/paezdavid/buscador-de-catalogo/assets/69438782/a70da938-1212-4250-9fee-f48809345bac)
![detalles](https://github.com/paezdavid/buscador-de-catalogo/assets/69438782/1007fa70-f291-4bb4-b989-c5c16a9dabbb)

