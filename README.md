___
<h1 align="center">📈 API Indicadores Económicos de Chile — Python Wrapper para mindicador.cl</h1>

<p align="center">
  <strong>Consulta indicadores económicos de Chile, genera gráficos y obtén datos por día, mes, año o fecha específica.</strong><br>
  Ideal para bots (Telegram, Discord), dashboards o análisis financieros en Python.
</p>

<hr>

<h2>📌 Descripción General</h2>
<p>
Este proyecto es una implementación simple pero extensible de la API pública 
<a href="https://mindicador.cl" target="_blank">mindicador.cl</a>.
Proporciona funciones en Python para:
</p>

<ul>
  <li>Consultar los valores actuales de todos los indicadores disponibles.</li>
  <li>Obtener series históricas de los últimos 30 días con gráficos automáticos.</li>
  <li>Consultar un indicador en una fecha exacta.</li>
  <li>Consultar series completas de un indicador para un año específico.</li>
  <li>Generar output listo para bots (ej: mensajes para Telegram).</li>
</ul>

<p>
Todos los resultados se devuelven como diccionarios o textos listos para enviar desde un bot, y los gráficos se generan como imágenes PNG.
</p>

<hr>

<h2>🧰 Tecnologías Utilizadas</h2>
<ul>
  <li>Python 3.10+</li>
  <li>Requests</li>
  <li>Pandas</li>
  <li>Matplotlib</li>
  <li>Seaborn</li>
  <li>API mindicador.cl</li>
</ul>

<hr>

<h2>📙 Indicadores Disponibles</h2>
<p>La API soporta los siguientes indicadores:</p>

<pre><code>[
  "uf", "ivp", "dolar", "dolar_intercambio", "euro", 
  "ipc", "utm", "imacec", "tpm",
  "libra_cobre", "tasa_desempleo", "bitcoin"
]
</code></pre>

<p>
Para más detalles, consulta <a href="https://mindicador.cl" target="_blank">mindicador.cl</a>.
</p>

<hr>

<h2>📦 Instalación</h2>

<h3>1. Clonar el repositorio</h3>
<pre><code>git clone https://github.com/tu_usuario/indicadores-chile-api.git
cd indicadores-chile-api
</code></pre>

<h3>2. Instalar dependencias</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>3. Estructura del Proyecto</h3>
<pre><code>
/indicadores-chile-api
│── indicadores.py     # Archivo principal con las funciones
│── README.html        # Documentación
│── requirements.txt   # Dependencias
│── examples/          # Scripts de ejemplo
</code></pre>

<hr>

<h2>🚀 Uso Rápido</h2>

<h3>🔹 Obtener todos los indicadores del día</h3>

```python
from indicadores import indicadoresDiarios

print(indicadoresDiarios())

____
```

<hr>

<h2 align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg"
       width="30"
       height="30"
       style="vertical-align: middle; margin-right: 8px;">
  Bot de Telegram en desarrollo
</h2>

<p align="center">
  Este proyecto está siendo integrado con un bot de Telegram que permitirá consultar 
  los indicadores económicos directamente desde la aplicación, además de enviar 
  gráficos y reportes en tiempo real.
</p>



