import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.paths import DASHBOARD_DATA_DIR, STATE_MAPPING

import streamlit as st

st.set_page_config(
    page_title="US Hotel Prices, Winter 2024/25",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    [data-testid="stMetric"] {
    background-color: #393939;
    text-align: center;
    padding: 15px 0;
}

[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}

[data-testid="stMetricDeltaIcon-Up"] {
    position: relative;
    left: 40%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

[data-testid="stMetricDeltaIcon-Down"] {
    position: relative;
    left: 40%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}
    </style>
    """,
    unsafe_allow_html=True,
)

# LOAD AND PREPARE DATA
@st.cache_data
def load_data():
    return pd.read_csv(DASHBOARD_DATA_DIR / "dashboard_data.csv")

df = load_data()

averages = (
    df.groupby("state")[["price", "rating"]]
    .median()
    .reset_index()
    .sort_values("price")
    .reset_index(drop=True)
)

averages_weekend = (
    df.groupby(["state", "weekend"])[["price", "rating"]]
    .median()
    .reset_index()
    .sort_values("price")
    .reset_index(drop=True)
)

averages_month = (
    df.groupby(["state", "month"])[["price", "rating"]]
    .median()
    .reset_index()
    .sort_values("price")
    .reset_index(drop=True)
)

# Add missing data for RI
averages_weekend.loc[len(averages_weekend.index)] = ["RhodeIsland", 1, 94.0, 8.5]

averages['state_code'] = averages['state'].map(STATE_MAPPING)

weekend = df[['price', 'state', 'weekend']].copy()
weekend.loc[len(averages_weekend.index)] = [94.0, "RhodeIsland", 1]
midweek = weekend[weekend["weekend"] == 0].copy()
weekend = weekend[weekend['weekend'] == 1].copy()


# PLOTS
def make_choropleth(df, selected_state):

    choropleth = px.choropleth(
        df,
        locations="state_code",
        locationmode="USA-states",
        color="price",  # Continue using price for the main color scale
        scope="usa",
        labels={"price": "Price ($)", "state_code": "State"},
        color_continuous_scale=px.colors.sequential.Agsunset,
    )

    choropleth.update_traces(
        marker_line_color="black",
        marker_line_width=0.5,
        colorbar_thickness=200,
    )

    # Highlight selected state
    selected_state_code = STATE_MAPPING.get(selected_state)
    if selected_state_code in df["state_code"].values:
        selected_state_row = df[df["state_code"] == selected_state_code]
        highlight_trace = px.choropleth(
            selected_state_row,
            locations="state_code",
            locationmode="USA-states",
            color_discrete_sequence=["lightskyblue"], 
            scope="usa",
        )

        highlight_trace.update_traces(
            showlegend=False,
            marker_line_color="black",
            marker_line_width=1.0,
        )
        
        choropleth.add_trace(highlight_trace.data[0])

    choropleth.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        margin=dict(l=0, r=0, t=0, b=0),
        height=400,
        coloraxis_colorbar_tickfont=dict(size=18),
    )

    choropleth.update_coloraxes(
            colorbar=dict(
                thickness=40,
                len=0.8,
                title=dict(text="Price ($)", font=dict(size=20))
            )
        )

    return choropleth


def make_heatmap(df, state):

    df_pivot = df.pivot(index="weekend", columns="state", values="price").fillna(0)

    state_idx = df_pivot.columns.get_loc(state)

    # Mask for highlighting selected state
    mask = df_pivot.values.copy()
    mask[:, :] = None  
    mask[:, state_idx] = df_pivot.iloc[:, state_idx] 

    # Create heatmap
    heatmap = go.Figure(
        data=go.Heatmap(
            z=df_pivot.values, 
            x=df_pivot.columns,
            y=["Midweek" if w == 0 else "Weekend" for w in df_pivot.index], 
            colorscale=px.colors.sequential.Agsunset,
            xgap=1,
            ygap=1,
            showscale=False
        )
    )
    
    # Highlight selected state
    heatmap.add_trace(
        go.Heatmap(
            z=mask, 
            x=df_pivot.columns,
            y=["Midweek" if w == 0 else "Weekend" for w in df_pivot.index],
            colorscale=[[0, "lightskyblue"], [1, "lightskyblue"]],
            xgap=3,
            ygap=3,
            showscale=False,
            zmin=df_pivot.values.min(),
            zmax=df_pivot.values.max(),
            hoverinfo="skip",
        )
    )

    # Update layout for appearance
    heatmap.update_layout(
        xaxis_title="",
        yaxis_title="",
        width=900,
        xaxis=dict(
            tickfont=dict(size=16),
            categoryarray=averages["state"].values,
        ),
        yaxis=dict(tickfont=dict(size=20)),
    )

    return heatmap

def make_state_bar_chart(state):
    df = averages_month[averages_month["state"] == state][["month", "price"]]
    df["month"] = df["month"].map({"December": "Dec", "January": "Jan", "February": "Feb"})

    ordered_months = ["Dec", "Jan", "Feb"]

    barchart = px.bar(
        df,
        x="price",
        y="month",
        orientation="h",
        color="month",
        category_orders={"month": ordered_months},
    )

    cheapest_month = df.iloc[df["price"].argmin()]["month"]
    cheapest_month_idx = ordered_months.index(cheapest_month)
    
    # Highlight cheapest month
    barchart.data[cheapest_month_idx].marker.color = "lightskyblue" 
    barchart.data[cheapest_month_idx].marker.opacity = 1.0

    for i in range(len(barchart.data)):
        if i != cheapest_month_idx:
            barchart.data[i].marker.color = px.colors.sequential.Agsunset[
                len(px.colors.sequential.Agsunset) // 3
            ]
            barchart.data[i].marker.opacity = 0.2

    barchart.update_layout(
        yaxis_title=None,
        xaxis_title="Price ($)",
        xaxis=dict(
            tickfont=dict(size=20)
            ),
        yaxis=dict(
            tickfont=dict(size=20)
            ),
        bargap=0.4,
        height=400,
    )

    barchart.update_yaxes(tickangle=90)
    barchart.update_xaxes(title_font=dict(size=16))

    barchart.update_traces(
        showlegend=False, 
    )

    return barchart

def get_metrics(state):
    names = ["Average Rating", "Weekend Price", "Midweek Price"]

    avg_rating = averages[averages["state"] == state]["rating"].iloc[0]
    avg_price_weekend = weekend[weekend["state"] == state]["price"].iloc[0]
    avg_price_midweek = midweek[midweek["state"] == state]["price"].iloc[0]
    
    avgs = [
        avg_rating,
        avg_price_weekend,
        avg_price_midweek,
    ]
    
    avg_rating_all_states = averages["rating"].mean()
    avg_price_weekend_all_states = weekend.groupby("state")["price"].median().mean()
    avg_price_midweek_all_states = midweek.groupby("state")["price"].median().mean()

    diffs = [
        round(avg_rating - avg_rating_all_states, 1),
        round(avg_price_weekend - avg_price_weekend_all_states),
        round(avg_price_midweek - avg_price_midweek_all_states),
    ]

    return names, avgs, diffs

def display_metrics():

    names, avgs, diffs = get_metrics(selected_state)

    st.header(f"Metrics")
    st.metric(label=names[0], value=f"{avgs[0]} ⭐️", delta=f"{diffs[0]} ⭐️")
    
    st.metric(
        label=names[1],
        value=f"${avgs[1]}",
        delta=(f"${diffs[1]}" if diffs[1] > 0 else f"-${abs(diffs[1])}"),
        delta_color="inverse",
    )
    st.metric(
        label=names[2],
        value=f"${avgs[2]}",
        delta=(f"${diffs[2]}" if diffs[2] > 0 else f"-${abs(diffs[2])}"),
        delta_color="inverse",
    )

if "selected_state" not in st.session_state:
    st.session_state["selected_state"] = None

# SIDEBAR
with st.sidebar:
    st.title('US Hotel Prices, Winter 2024/25')

    states = sorted(df['state'].unique())
    selected_state = st.selectbox('Select a state', states)
    st.session_state["selected_state"] = selected_state

    st.info(
        """
        - :blue[**Data**]: Scraped from [booking.com](booking.com) in October 2024.
        - :blue[**Metrics**]: The average rating and midweek/weekend prices for the selected state. 
        The green/red values give the comparison to the US as a whole.
        - :blue[**Monthly Prices**]: Average monthly hotel prices for the selected state; the cheapest month  
        is highlighted in blue. 
        """
    )


# MAIN DASHBOARD
cols = st.columns((1, 4), gap="medium")

with cols[0]:

    metrics = get_metrics(selected_state)
    display_metrics()

    st.header(f"Monthly Prices")
    bar_chart = make_state_bar_chart(st.session_state["selected_state"])
    st.plotly_chart(bar_chart)

with cols[1]:
    st.header(f"{selected_state}")
    
    # Hack to reduce spacing
    st.markdown("<div style='margin-top: -1px;'></div>", unsafe_allow_html=True)
    
    choropleth = make_choropleth(averages, st.session_state['selected_state'])
    st.plotly_chart(choropleth, use_container_width=True)

    heatmap = make_heatmap(averages_weekend, st.session_state["selected_state"])
    st.plotly_chart(heatmap, use_container_width=True)
