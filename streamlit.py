import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
st.set_page_config(layout="wide")
import plotly.graph_objects as go
import plotly.express as px

matplotlib.use('Agg')

# Reading and renaming of files for visualization
original = pd.read_csv("Datasets/mrsd_4_annl_emp_chg_by_ind_14032022.csv")
# original = original.drop(["industry1", "industry3"], axis=1).rename(
#     columns={"year": "Year", "industry2": "Industry", "employment_change": "Change"})

# Title and Sidebar information
st.title('Employment Change Dataset')
st.sidebar.subheader(' Filter ')
st.markdown("Tick the box on the side panel to explore the dataset.")

# Year slidebar to choose year range
start_year, end_year = st.select_slider(
    'Select the years to view',
    options=list(range(1991, 2022)),
    value=(1991, 2021))
st.write('You selected the year range of', start_year, 'and', end_year)
original = original[(original.year >= start_year) & (original.year <= end_year)]

# Selecting Of Columns For Display
columns = original.columns.values
columns_select = st.multiselect("Select The Columns To View", columns,
                         default=columns)
genre = st.sidebar.radio("Which Dataset To View",
    ('Employment Change', 'Employment By Gender and Education', 'Labour Force Status By Age Group'))

if genre == 'Employment Change':
        st.dataframe(original[columns_select], use_container_width=True)

explore = st.sidebar.radio("Data Filters", ("Employment Data", "Quick Look", "Show Columns", "Statistics"))

if explore == "Employment Data":
    st.subheader("Employment Data")


if explore == "Quick Look":
    st.subheader('Dataset Quick Look:')
    st.write(original[columns].head())

if explore == "Show Columns":
    st.subheader('Show Columns List')
    all_columns = original.columns.to_list()
    st.write(all_columns)

if explore == "Statistics":
    st.subheader('Statistical Data Descripition')
    st.write(original.describe())

st.download_button(
    label="Download data as CSV",
    data=original.to_csv(),
    file_name='large_df.csv')

df = original.replace("-", 0)
df.Year = df.Year.astype(int)
df.Industry = df.Industry.astype(str)
df.Change = df.Change.astype(float)

if st.sidebar.checkbox('Graphics'):
    st.subheader('Barplot')
    st.info("Please set a year range less than 5 years")
    columnX = st.sidebar.selectbox("X (Choose a column). Try Selecting Year:", df.columns)
    columnY = st.sidebar.selectbox("Y (Choose a column). Try Selecting Change", df.columns)
    hueopt = st.sidebar.selectbox("Hue (Choose a column). Try Selecting Industry", df.columns)
    fig = plt.figure(figsize=(15, 8))
    # sns.barplot(data=df, x="Year", y="Change", hue="Industry")
    sns.barplot(x=columnX, y=columnY, hue=hueopt, data=df, palette="Paired")
    st.pyplot(fig)

# Employment By Age and Education
df_age_edu = pd.read_csv("Datasets/employed_15_sex_edu_age_yr.csv").rename(columns={"year":"Year",
                                                                               "sex": "Sex",
                                                                               "age":"Age",
                                                                               "edu_1":"Education",
                                                                               "employed":"Employed"
                                                                               }).replace("-", 0)
df_age_edu.Employed = pd.to_numeric(df_age_edu.Employed)
df_age_edu = df_age_edu[(df_age_edu.Year >= 2017) & (df_age_edu.Year <= 2021) & (df_age_edu.Age != "15-19")]
df_age_edu = df_age_edu.groupby(["Year","Education"]).sum()
df_age_edu = df_age_edu.reset_index()


if st.sidebar.checkbox('Plotly'):
    st.subheader('Barplot')
    f1 = df_age_edu[df_age_edu['Year'] == 2017]
    f2 = df_age_edu[df_age_edu['Year'] == 2018]
    f3 = df_age_edu[df_age_edu['Year'] == 2019]
    f4 = df_age_edu[df_age_edu['Year'] == 2020]
    f5 = df_age_edu[df_age_edu['Year'] == 2021]

    edu = df_age_edu['Education'].unique().tolist()

    fig = go.Figure()
    colors = px.colors.qualitative.T10[0:5]

    fig.add_trace(go.Bar(x=edu, y=f1['Employed'], name="2017", marker_color=colors[0]))
    fig.add_trace(go.Bar(x=edu, y=f2['Employed'], name="2018", marker_color=colors[1]))
    fig.add_trace(go.Bar(x=edu, y=f3['Employed'], name="2019", marker_color=colors[2]))
    fig.add_trace(go.Bar(x=edu, y=f4['Employed'], name="2020", marker_color=colors[3]))
    fig.add_trace(go.Bar(x=edu, y=f5['Employed'], name="2021", marker_color=colors[4]))
    st.plotly_chart(fig, use_container_width=True)
