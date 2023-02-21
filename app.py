import streamlit as st
import pandas as pd
import preprocessor, helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
from PIL import Image
from streamlit_option_menu import option_menu

img = Image.open('imgLogo.png')
st.set_page_config(page_title='Olympics WebApp', page_icon="https://api.iconify.design/simple-icons/apachesolr.svg?color=red&width=16&height=16&flip=vertical")

hide_footer = """
<style>
Button:hover {
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  width: 100%;
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  # padding: 30px 32px;
  # text-align: center;
  text-decoration: none;
  # display: inline-block;
  font-size: 16px;
}


footer {visibility: hidden;
}
    footer:after{
    visibility: visible;
    
    content:'Copyright @ 2023: Streamlit WebApp ';
    word-spacing:3rem;
    content:'Creators: Supriya_Mishra   Suraj_Mishra   Ravi_Verma   Yogesh_Tilawath';
    display:block;
    
    
    
  left: 0;
  bottom: 0;
  width: 100%;
  length:600%;
  background-color: #40A42C;
  color: white;
  padding:3px;
  margin:500;
  text-align: center;




    position:relative;
   

}

</style>

"""
ButtonDisable = """
<style>
#css-1x8cf1d edgvbvh10{
visibility: hidden;


}



</style>

"""
st.markdown(hide_footer, unsafe_allow_html=True)
page_bg_img = """
<style>
button{
color:'blue',

}
[data-testid="stAppViewContainer"]{
# background-color: #e5e5f7;
# opacity: 0.8;
# background-image: radial-gradient(#444cf7 0.5px, #e5e5f7 0.5px);
# background-size: 10px 10px;

# background-color: #e5e5f7;
# opacity: 1.5;
# background-image: radial-gradient(#a8f745 0.7000000000000001px, #e5e5f7 0.7000000000000001px);
# background-size: 14px 14px

# website used-https://www.magicpattern.design/tools/css-backgrounds
background-color: #e5e5f7;
opacity: 1.8;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #e5e5f7 14px ), repeating-linear-gradient( #a8f74555, #a8f745 );


}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df, region_df)
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col6:
    Exit_btn1 = st.button("Exit Page", disabled=False)

if Exit_btn1:

    st.markdown(ButtonDisable, unsafe_allow_html=True)
    st.title('Thankyou for using the webapp')
    st.image('https://cdn.pixabay.com/photo/2016/08/11/14/50/ground-1585817__480.jpg')
    # btn2=st.button("Go back")
    col1, col2, col3 = st.columns(3)
    with col2:
        Back_btn2 = st.button("Go Back")





else:
    # st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuplB3TKDEweocWi5XsXDFFyFFXgmzlgfnIg&usqp=CAU',
    #          width=500)
    st.title('Olympics Analysis Web App')
    st.write('This is a Olympics Analysis Web App which is able to analyse  120 years of the Olympics. ')
    st.image(
        'https://images.unsplash.com/photo-1569517282132-25d22f4573e6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8b2x5bXBpY3N8ZW58MHx8MHx8&auto=format&fit=crop&w=600&q=60',
        width=600)
    st.sidebar.title("Olympics Analysis")
    st.sidebar.image(
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuplB3TKDEweocWi5XsXDFFyFFXgmzlgfnIg&usqp=CAU')
    # user_menu = st.sidebar.radio(
    #     'Select an Option',
    #     ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
    # )
    with st.sidebar:
        user_menu = option_menu(
            menu_title='Main Menu',
            options=['Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete wise Analysis'],
            icons=['bullseye', 'bar-chart-line-fill', 'flag-fill', 'graph-up'],
            menu_icon='cast',
        )

    if user_menu == 'Medal Tally':
        st.sidebar.header("Medal Tally")
        years, country = helper.country_year_list(df)

        selected_year = st.sidebar.selectbox("Select Year", years)
        selected_country = st.sidebar.selectbox("Select Country", country)

        medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
        if selected_year == 'Overall' and selected_country == 'Overall':
            st.title("Overall Tally")
        if selected_year != 'Overall' and selected_country == 'Overall':
            st.title("Medal Tally in " + str(selected_year) + " Olympics")
        if selected_year == 'Overall' and selected_country != 'Overall':
            st.title(selected_country + " overall performance")
        if selected_year != 'Overall' and selected_country != 'Overall':
            st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
        st.table(medal_tally)

    if user_menu == 'Overall Analysis':
        editions = df['Year'].unique().shape[0] - 1
        cities = df['City'].unique().shape[0]
        sports = df['Sport'].unique().shape[0]
        events = df['Event'].unique().shape[0]
        athletes = df['Name'].unique().shape[0]
        nations = df['region'].unique().shape[0]

        st.title("Top Statistics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Editions")
            st.title(editions)
        with col2:
            st.header("Hosts")
            st.title(cities)
        with col3:
            st.header("Sports")
            st.title(sports)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Events")
            st.title(events)
        with col2:
            st.header("Nations")
            st.title(nations)
        with col3:
            st.header("Athletes")
            st.title(athletes)

        nations_over_time = helper.data_over_time(df, 'region')
        fig = px.line(nations_over_time, x="Edition", y="region")
        st.title("Participating Nations over the years")
        st.plotly_chart(fig)

        events_over_time = helper.data_over_time(df, 'Event')
        fig = px.line(events_over_time, x="Edition", y="Event")
        st.title("Events over the years")
        st.plotly_chart(fig)

        athlete_over_time = helper.data_over_time(df, 'Name')
        fig = px.line(athlete_over_time, x="Edition", y="Name")
        st.title("Athletes over the years")
        st.plotly_chart(fig)

        st.title("No. of Events over time(Every Sport)")
        fig, ax = plt.subplots(figsize=(20, 20))
        x = df.drop_duplicates(['Year', 'Sport', 'Event'])
        ax = sns.heatmap(
            x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
            annot=True)
        st.pyplot(fig)

        st.title("Most successful Athletes")
        sport_list = df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0, 'Overall')

        selected_sport = st.selectbox('Select a Sport', sport_list)
        x = helper.most_successful(df, selected_sport)
        st.table(x)

    if user_menu == 'Country-wise Analysis':
        st.sidebar.title('Country-wise Analysis')

        country_list = df['region'].dropna().unique().tolist()
        country_list.sort()

        selected_country = st.sidebar.selectbox('Select a Country', country_list)

        country_df = helper.yearwise_medal_tally(df, selected_country)
        fig = px.line(country_df, x="Year", y="Medal")
        st.title(selected_country + " Medal Tally over the years")
        st.plotly_chart(fig)

        st.title(selected_country + " excels in the following sports")
        pt = helper.country_event_heatmap(df, selected_country)
        fig, ax = plt.subplots(figsize=(20, 20))
        ax = sns.heatmap(pt, annot=True)
        st.pyplot(fig)

        st.title("Top 10 athletes of " + selected_country)
        top10_df = helper.most_successful_countrywise(df, selected_country)
        st.table(top10_df)

    if user_menu == 'Athlete wise Analysis':
        athlete_df = df.drop_duplicates(subset=['Name', 'region'])

        x1 = athlete_df['Age'].dropna()
        x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
        x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
        x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

        fig = ff.create_distplot([x1, x2, x3, x4],
                                 ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                                 show_hist=False, show_rug=False)
        fig.update_layout(autosize=False, width=1000, height=600)
        st.title("Distribution of Age")
        st.plotly_chart(fig)

        x = []
        name = []
        famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                         'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                         'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                         'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                         'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                         'Tennis', 'Golf', 'Softball', 'Archery',
                         'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                         'Rhythmic Gymnastics', 'Rugby Sevens',
                         'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
        for sport in famous_sports:
            temp_df = athlete_df[athlete_df['Sport'] == sport]
            x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
            name.append(sport)

        fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
        fig.update_layout(autosize=False, width=1000, height=600)
        st.title("Distribution of Age wrt Sports(Gold Medalist)")
        st.plotly_chart(fig)

        sport_list = df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0, 'Overall')

        st.title('Height Vs Weight')
        selected_sport = st.selectbox('Select a Sport', sport_list)
        temp_df = helper.weight_v_height(df, selected_sport)
        fig, ax = plt.subplots()
        x = temp_df['Weight']
        y = temp_df['Height']
        ax = plt.scatter(x, y, s=60)
        st.pyplot(fig)

        st.title("Men Vs Women Participation Over the Years")
        final = helper.men_vs_women(df)
        fig = px.line(final, x="Year", y=["Male", "Female"])
        fig.update_layout(autosize=False, width=700, height=400)
        st.plotly_chart(fig)
