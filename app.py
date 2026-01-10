import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Ventas", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #DADEB1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3, tab4 = st.tabs(["Análisis global","Análisis por tienda","Análisis por estado","Gráficos para analizar los datos"])

df1 = pd.read_csv("parte_1.csv", low_memory=False)
df2 = pd.read_csv("parte_2.csv", low_memory=False)
df=pd.concat([df1, df2], ignore_index=True)
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
df["sales"] = pd.to_numeric(df["sales"], errors="coerce").fillna(0)
df["onpromotion"] = pd.to_numeric(df["onpromotion"], errors="coerce").fillna(0)
df["transactions"] = pd.to_numeric(df["transactions"], errors="coerce").fillna(0)

st.title("Dashboard de Ventas - Visualización de Datos: Práctica Final")
with tab1:
    st.header("Visualización global")
    n_tiendas = df["store_nbr"].nunique()
    n_productos = df["family"].nunique()
    n_estados = df["state"].nunique()
    meses_disp = df[["year", "month"]].drop_duplicates().shape[0]
    ventas_totales = df["sales"].sum()

    st.metric("Tiendas", f"{n_tiendas}")
    st.metric("Productos", f"{n_productos}")
    st.metric("Estados", f"{n_estados}")
    st.metric("Meses", f"{meses_disp}")
    st.metric("Ventas totales", f"{ventas_totales:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    st.subheader("Análisis en términos medios")

    
    st.markdown("Top 10 productos más vendidos")
    top_prod = (df.groupby("family")["sales"].mean().sort_values(ascending=False).head(10))
    st.dataframe(top_prod.reset_index().rename(columns={"family": "producto", "sales": "ventas_medias"}), use_container_width=True)
    st.bar_chart(top_prod,color="#7B8A20")

    st.divider()

    
    st.markdown("Distribución de las ventas por tiendas")
    ventas_tienda_media = (df.groupby("store_nbr")["sales"].mean().sort_index())
    st.bar_chart(ventas_tienda_media,color="#7B8A20")

    st.divider()

    
    st.markdown("Top 10 tiendas con ventas en productos en promoción")

    
    df_promo = df[df["onpromotion"] > 0].copy()

    top_tiendas_promo = (df_promo.groupby("store_nbr")["sales"].mean().sort_values(ascending=False).head(10))

    st.dataframe(top_tiendas_promo.reset_index().rename(columns={"store_nbr": "tienda", "sales": "ventas_medias_en_promo"}),use_container_width=True)
    st.bar_chart(top_tiendas_promo,color="#7B8A20")
    
    st.divider()
    st.subheader("Análisis de la estacionalidad de las ventas")

    
    st.markdown("Día de la semana con más ventas")

    orden_dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    ventas_dia = (df.groupby("day_of_week")["sales"].mean())

    
    ventas_dia = ventas_dia.reindex([d for d in orden_dias if d in ventas_dia.index])

    dia_max = ventas_dia.idxmax()
    valor_max = ventas_dia.max()

    
    st.bar_chart(ventas_dia,color="#7B8A20")

    st.divider()

    
    st.markdown("Volumen de ventas medio por semana del año")

    ventas_semana = (
        df.groupby("week")["sales"]
        .mean()
        .sort_index()
    )

    st.bar_chart(ventas_semana,color="#7B8A20")

    st.divider()

    
    st.markdown("Volumen de ventas medio por mes")

    ventas_mes = (df.groupby("month")["sales"].mean().sort_index())

    st.bar_chart(ventas_mes,color="#7B8A20")

with tab2:
    st.header("Análisis por tienda")

    
    tiendas = sorted(df["store_nbr"].dropna().unique())
    tienda_sel = st.selectbox("Selecciona la tienda (store_nbr):", tiendas)

    
    df_t = df[df["store_nbr"] == tienda_sel].copy()

    st.subheader("Número total de ventas por año")
    ventas_por_ano = (df_t.groupby("year")["sales"].sum().sort_index())
    st.bar_chart(ventas_por_ano,color="#7B8A20")

    st.divider()

    st.subheader("Número total de productos vendidos")
    total_productos_vendidos = df_t["sales"].sum()
    st.metric("Total productos vendidos (unidades)", f"{total_productos_vendidos:,.0f}".replace(",", "."))


    st.divider()

    st.subheader("Número total de productos vendidos que estaban en promoción")
    vendidos_en_promo = df_t.loc[df_t["onpromotion"] > 0, "sales"].sum()
    st.metric("Total productos vendidos en promoción (unidades)", f"{vendidos_en_promo:,.0f}".replace(",", "."))

    

with tab3:
    st.header("Análisis por estado")

    
    estados = sorted(df["state"].dropna().unique())
    estado_sel = st.selectbox("Selecciona el estado:", estados)

    
    df_s = df[df["state"] == estado_sel].copy()

    
    st.subheader("Número total de transacciones por año")

    trans_por_ano = (df_s.groupby("year")["transactions"].sum().sort_index())

    st.bar_chart(trans_por_ano,color="#7B8A20")

    st.divider()

    
    st.subheader("Ranking de tiendas con más ventas")

    ranking_tiendas = (df_s.groupby("store_nbr")["sales"].sum().sort_values(ascending=False))

    st.dataframe(ranking_tiendas.reset_index().rename(columns={"store_nbr": "tienda", "sales": "ventas_totales"}),use_container_width=True)
    st.bar_chart(ranking_tiendas,color="#7B8A20")

    st.divider()

    
    st.subheader("Producto más vendido")

    ventas_por_producto = (df_s.groupby("family")["sales"].sum().sort_values(ascending=False))

    producto_top = ventas_por_producto.index[0]
    valor_top = ventas_por_producto.iloc[0]

    st.metric("Producto más vendido", producto_top)
    st.metric("Unidades vendidas", f"{valor_top:,.0f}".replace(",", "."))

    
    st.caption("Top 10 productos en este estado")
    st.bar_chart(ventas_por_producto.head(10),color="#7B8A20")

with tab4:
    st.header("Insights estratégicos")

    
    st.divider()

    
    st.subheader("Estados con mayor volumen de ventas")

    ventas_estado = (df.groupby("state")["sales"].sum().sort_values(ascending=False).head(5))

    st.bar_chart(ventas_estado,color="#7B8A20")
    st.divider()

    
    st.subheader("Evolución anual de las ventas por estado")

    ventas_estado_ano = (df.groupby(["year", "state"])["sales"].sum().reset_index())

    # Top 5 estados por ventas totales
    top_estados = (
        df.groupby("state")["sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .index
    )

    ventas_estado_ano["state"] = ventas_estado_ano["state"].apply(
        lambda x: x if x in top_estados else "Otros"
    )

    ventas_estado_ano = (ventas_estado_ano.groupby(["year", "state"])["sales"].sum().reset_index())

    pivot = ventas_estado_ano.pivot(index="year", columns="state", values="sales")

    st.line_chart(pivot)

    

    st.divider()

    st.subheader("Evolución del ticket medio por año")

    ticket_medio = (df.groupby("year").apply(lambda x: x["sales"].sum() / x["transactions"].sum() if x["transactions"].sum() > 0 else 0))

    st.line_chart(ticket_medio,color="#7B8A20")

    

    

