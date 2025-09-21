import streamlit as st
import plotly.express as px
import pandas as pd  
import plotly.io as pio
import plotly.graph_objects as go
st.title("MUMPS case visualization")
df = pd.read_csv("Mumps cleaned file.csv")
df.head()

#FIRST VISUALIZATION, LIVE SCATTER PLOT, Previous assignment
st.subheader("1) Trends of Mumps cases over regions in Lebanon over time")

scatter =px.scatter(
    df,
    x="Number of cases", y = "refArea", 
    color = "refArea", orientation= "h", 
    animation_frame = "refPeriod", animation_group = "refArea", 
    range_x= [0, df["Number of cases"].max()],
    color_discrete_sequence=px.colors.qualitative.Set1,
    title = "Number of recorded Mumps cases in Lebanese regions over time"
)
st.plotly_chart(scatter, use_container_width=True)
scatter.show()
with st.expander("Important insights"):
    st.write(f"""
- The live scatter plot allows us to oversee trends of mumps cases with the ability to identify outlier regions easily and follow their pattern.
- The scatter plot shows how Mumps disease breaks out in some regions like Beqaa or South constantly.
- Beirut had the lease recorded Mumps cases over time.
- The overall number of Mumps cases recorded has decreased to near zero levels in most Lebanese regions after June of 2016.
""")

#SECOND VISUALIZATION, PIE CHART, New 
st.subheader("2) Cases by governorate for a selected month")

periods = df["refPeriod"].unique()

first = periods[0]
df0 = df[df["refPeriod"] == first]

colors = px.colors.qualitative.Set3 
fig = go.Figure(data=[go.Pie(labels=df0["refArea"], values=df0["Number of cases"], marker=dict(colors=colors))])

buttons = []
for p in periods:
    dff =df[df["refPeriod"] == p]
    buttons.append(dict(
        label=p,
        method= "update",
        args=[{"labels":[dff["refArea"]], "values":[dff["Number of cases"]]},
              {"title": f"Distribution of cases among Lebanese regions in ({p})"}]
    ))


fig.update_layout(
    updatemenus=[dict(type="dropdown", x=0.02, y=1.1, buttons=buttons)],
    title=f"Distribution of cases among Lebanese regions in({first})"
)
st.plotly_chart(fig, use_container_width=True)
fig.show()
with st.expander("Important insights"):
    st.write(f"""
- The pie chart allows us to know the distribution of mumps cases across Lebanese regions.
- After observing trends in the live scatter plot and you identify a seasonal outbreak, you can select that reference period and compare the cases distribution.
- For example, in June of 2015 all regions reported Mumps cases, with Beqaa Valley recoding 46.7% of the total recorded Mumps cases.
- In November of 2018, three regions accounted for 100% of the Mumps cases, with South and North Lebanon accounting for 12.5% each (1 case each), while Mount Lebanon accounted for 75% (6 cases).
""")