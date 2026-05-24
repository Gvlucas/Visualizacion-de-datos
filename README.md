# Visualización de datos- Proyecto final
# 📊 Dashboard de Ventas

Dashboard interactivo desarrollado con **Streamlit** para el análisis y visualización de datos de ventas. Desarrollado como práctica final de Visualización de Datos.

---

## 📁 Estructura del proyecto

```
├── app.py              # Aplicación principal
├── parte_1.csv         # Dataset de ventas (parte 1)
├── parte_2.csv         # Dataset de ventas (parte 2)
├── requirements.txt    # Dependencias del proyecto
└── README.md
```

---

## 🚀 Instalación y uso

**1. Clona el repositorio:**
```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
```

**2. Instala las dependencias:**
```bash
pip install -r requirements.txt
```

**3. Ejecuta la aplicación:**
```bash
streamlit run app.py
```

---

## 📌 Funcionalidades

El dashboard se organiza en cuatro pestañas:

**Análisis global**
- Métricas generales: tiendas, productos, estados, meses y ventas totales
- Top 10 productos más vendidos (en términos medios)
- Distribución de ventas por tienda
- Top 10 tiendas con ventas en promoción
- Estacionalidad: ventas por día de la semana, semana del año y mes

**Análisis por tienda**
- Selector interactivo de tienda
- Ventas totales por año
- Total de productos vendidos y productos vendidos en promoción

**Análisis por estado**
- Selector interactivo de estado
- Transacciones por año
- Ranking de tiendas con más ventas
- Producto más vendido en el estado

**Insights estratégicos**
- Estados con mayor volumen de ventas
- Evolución anual de ventas por estado (Top 5)
- Evolución del ticket medio por año

---

## 🛠️ Tecnologías

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
