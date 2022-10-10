import matplotlib
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

matplotlib.use('Agg')

# Title and Sidebar information
st.title('Employment Change Dataset')
st.sidebar.subheader(' Filter ')
data = st.radio("Which Dataset To View",
                 (
                     'Employment Change', 'Employment By Gender and Education',
                     'Labour Force Status By Age Group'))

if data == "Employment Change":
    file = "mrsd_39_annual_ emp_chng_by_ind_and_res_stat_29072022"

elif data == "Employment By Gender and Education":
    file = "employed_15_sex_edu_age_yr"

elif data == "Labour Force Status By Age Group":
    file = "pop_1_labourforce_status_age_yr"

# Reading and renaming of files for visualization
original = pd.read_csv("Datasets/" + file + ".csv").replace("-", 0)
df = original
columns = original.columns.values
# original = original.drop(["industry1", "industry3"], axis=1).rename(
#     columns={"year": "Year", "industry2": "Industry", "employment_change": "Change"})




explore = st.sidebar.radio("Data Filters", ("Employment Data", "Quick Look", "Columns"))


if explore == "Employment Data":
    st.subheader("Employment Data")
# Selecting Of Columns For Display
    columns_select = st.multiselect("Select The Columns To View",
                                    columns,default=columns)
# Year slidebar to choose year range
    start = int(min(original.year))
    end = int(max(original.year))
    start_year, end_year = st.select_slider('Select the years to view',
                                            options=list(range(start, end+1)),value=(start, end))
    st.write('You selected the year range of', start_year, 'and', end_year)

    original = original[(original.year >= start_year) & (original.year <= end_year)]
    if data == 'Employment Change':
        st.dataframe(original[columns_select], use_container_width=True)
    elif data == 'Employment By Gender and Education':
        st.dataframe(original[columns_select], use_container_width=True)
    elif data == 'Labour Force Status By Age Group':
        st.dataframe(original[columns_select], use_container_width=True)

    option = st.selectbox("Raw or Custom",
                          ("Raw", "Custom"))
    if option == "Custom":
        st.download_button(
            label="Download Customised Columns Data",
            data=original[columns_select].to_csv(), file_name=data + "_custom.csv")
    else:
        st.download_button(label="Download Raw Data",
                           data=original.to_csv(), file_name=data + ".csv")


elif explore == "Quick Look":
    st.subheader('Dataset Quick Look:')
    st.write(original.head())

elif explore == "Columns":
    st.subheader('Show Columns List')
    st.write(original.columns.to_list())


# if st.sidebar.checkbox('Graph'):
if data == "Employment Change":
    st.subheader(data + " Sunburst From 2017 To 2021")
    df = df[df.year >= 2017]
    df["employment_change"] = df["employment_change"].astype(float)
    fig = px.sunburst(df, path=['year', "res_stat",'industry1',"employment_change"],
                      color="employment_change",color_continuous_scale='RdBu')
    st.plotly_chart(fig)

elif data == "Employment By Gender and Education":
    st.subheader(data + ' Barplot From 2017 To 2021')
# st.info("Please set a year range less than 5 years")
# columnX = st.sidebar.selectbox("X (Choose a column). Try Selecting Year:", df.columns)
# columnY = st.sidebar.selectbox("Y (Choose a column). Try Selecting Change", df.columns)
# hueopt = st.sidebar.selectbox("Hue (Choose a column). Try Selecting Industry", df.columns)
#     fig = plt.figure(figsize=(15, 8))
# sns.barplot(data=df, x="Year", y="Change", hue="Industry")
#     sns.barplot(x=columnX, y=columnY, hue=hueopt, data=df, palette="Paired")
#     st.pyplot(fig)

# Employment By Age and Education
# df_age_edu = pd.read_csv("Datasets/employed_15_sex_edu_age_yr.csv").rename(columns={"year": "Year",
#                                                                                     "sex": "Sex",
#                                                                                     "age": "Age",
#                                                                                     "edu_1": "Education",
#                                                                                     "employed": "Employed"
#                                                                                     }).replace("-", 0)
    df.employed = pd.to_numeric(df.employed)
    df = df[(df.year >= 2017)& (df.age != "15-19")]
    df = df.groupby(["year", "edu_1"]).sum()
    df = df.reset_index()

    f1 = df[df['year'] == 2017]
    f2 = df[df['year'] == 2018]
    f3 = df[df['year'] == 2019]
    f4 = df[df['year'] == 2020]
    f5 = df[df['year'] == 2021]

    edu = df['edu_1'].unique().tolist()

    fig = go.Figure()
    colors = px.colors.qualitative.T10[0:5]

    fig.add_trace(go.Bar(x=edu, y=f1['employed'], name="2017", marker_color=colors[0]))
    fig.add_trace(go.Bar(x=edu, y=f2['employed'], name="2018", marker_color=colors[1]))
    fig.add_trace(go.Bar(x=edu, y=f3['employed'], name="2019", marker_color=colors[2]))
    fig.add_trace(go.Bar(x=edu, y=f4['employed'], name="2020", marker_color=colors[3]))
    fig.add_trace(go.Bar(x=edu, y=f5['employed'], name="2021", marker_color=colors[4]))
    st.plotly_chart(fig, use_container_width=True)

elif data == "Labour Force Status By Age Group":
    st.subheader(data + " Piechart From 2017 To 2021")

    labels = ["20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64"]

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=df["employed"][df.year == 2019], name="2019"),
                  1, 1)
    fig.add_trace(go.Pie(labels=labels, values=df["employed"][df.year == 2020], name="2020"),
                  1, 2)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(
        title_text="Age Group Of Employed People In The Labour Force",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='2019', x=0.175, y=0.5, font_size=20, showarrow=False),
                     dict(text='2020', x=0.825, y=0.5, font_size=20, showarrow=False)])
    st.plotly_chart(fig)
