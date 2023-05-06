import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.markdown("# NBA Fantasy ")
st.sidebar.markdown("# NBA data for seasons 1996-2021")
@st.cache_data

st.subheader('Content')
st.text(' In recent years the NBA has seen an explosive growth in popularity.\n Along with the growth in popularity of the NBA, NBA fantasy has becoming more and more popular. \n NBA Fantasy is a game where fans can create their own league with friends and then draft their own fantasy teams with players of NBA Players. \n The fans then earn points each week for how each of their players perform week. \n They compete against each other in weekly matchups to see who created the best fantasy team.')

player_info, boxscore, gamescore, coaches, salaries = st.tabs(
    ['Player Information', 'Box Score', 'Game Score', 'Coaches', 'Player Salaries'])
with player_info:
    tabpi1, tabpi2, tabpi3 = st.tabs(
        ['Player Height', 'Player Weights', 'Player Position'])
    with tabpi1:
        player_ht = pd.read_csv("data/player_info.csv")
        st.write('## Players Height ')
        st.write(player_ht)
        top20player_ht = player_ht.head(20)

        Barplayer_ht = alt.Chart(top20player_ht).mark_bar().encode(
            x=alt.Y('playerName'),
            y=alt.Y('Ht', sort='-x'),
            tooltip=['Ht'],
            color='Ht',
            order=alt.Order('playerName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(Barplayer_ht, use_container_width=True)
    with tabpi2:
        player_wt = pd.read_csv("data/player_info.csv")
        st.write('## Players Weight ')
        st.write(player_wt)
        top20player_wt = player_wt.head(20)

        Barplayer_wt = alt.Chart(top20player_wt).mark_bar().encode(
            x=alt.Y('playerName'),
            y=alt.Y('Wt', sort='-x'),
            tooltip=['Wt'],
            color='Wt',
            order=alt.Order('playerName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(Barplayer_wt, use_container_width=True)
    with tabpi3:
        player_pos = pd.read_csv("data/player_info.csv")
        st.write('## Players Position ')
        st.write(player_pos)
        top20player_pos = player_pos.head(50)

        Scaplayer_pos = alt.Chart(top20player_pos).mark_circle(size=60).encode(
            x=alt.Y('playerName'),
            y=alt.Y('Pos', sort='-x'),
            tooltip=['Pos'],
            color='Pos',
            order=alt.Order('playerName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(Scaplayer_pos, use_container_width=True)

with boxscore:
    tabbs1, tabbs2, tabbs3, tabbs4, tabbs5 = st.tabs(
        ['Player MP Scores', 'Player FGA Scores', 'Player 3P Scored ', 'Player 3Pointers Attempted', 'Players PTS'])
    with tabbs1:
        boxscoreMP = pd.read_csv(r"data/boxscore.csv")
        st.write('## Players Height ')
        st.write(boxscoreMP)
        top20boxscoreMP = boxscoreMP.head(20)

        BarboxscoreMP = alt.Chart(top20boxscoreMP).mark_bar().encode(
            x=alt.Y('playerName'),
            y=alt.Y('MP', sort='-x'),
            tooltip=['MP'],
            color='MP',
            order=alt.Order('playerName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(BarboxscoreMP, use_container_width=True)
    with tabbs2:
        boxscoreFGA = pd.read_csv(r"data/boxscore.csv")
        st.write('## Players FGA ')
        st.write(boxscoreFGA)
        top20boxscoreFGA = boxscoreFGA.head(20)

        BarboxscoreFGA = alt.Chart(top20boxscoreFGA).mark_bar().encode(
            x=alt.Y('playerName'),
            y=alt.Y('FGA', sort='-x'),
            tooltip=['FGA'],
            color='FGA',
            order=alt.Order('playerName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(BarboxscoreFGA, use_container_width=True)
    with tabbs3:
        boxscore3P = pd.read_csv(r"data/boxscore.csv")
        st.write('## Players 3P ')
        st.write(boxscore3P)
        top20boxscore3P = boxscore3P.head(20)

        Barboxscore3P = alt.Chart(top20boxscore3P).mark_bar().encode(
            x=alt.Y('playerName'),
            y=alt.Y('3P', sort='-x'),
            tooltip=['3P'],
            color='3P',
            order=alt.Order('playerName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(Barboxscore3P, use_container_width=True)
    with tabbs4:
        boxscore3Pointers = pd.read_csv(r"data/boxscore.csv")
        st.write('## Players 3Pointers ')
        st.write(boxscore3Pointers)
        top20boxscore3Pointers = boxscore3Pointers.head(20)

        Barboxscore3Pointers = alt.Chart(top20boxscore3Pointers).mark_bar().encode(
            x=alt.Y('playerName'),
            y=alt.Y('3PA', sort='-x'),
            tooltip=['3PA'],
            color='3PA',
            order=alt.Order('playerName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(Barboxscore3Pointers, use_container_width=True)
    with tabbs5:
        boxscorePTS = pd.read_csv(r"data/boxscore.csv")
        st.write('## Players PTS ')
        st.write(boxscorePTS)
        top20boxscorePTS = boxscorePTS.head(20)

        BarboxscorePTS = alt.Chart(top20boxscorePTS).mark_bar().encode(
            x=alt.Y('playerName'),
            y=alt.Y('PTS', sort='-x'),
            tooltip=['PTS'],
            color='PTS',
            order=alt.Order('playerName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(BarboxscorePTS, use_container_width=True)
with gamescore:
    tabgs1, tabgs2 = st.tabs(
        ['Away Team Season Stats', 'Home Team Season Stats'])
    with tabgs1:
        gamesA = pd.read_csv(r"data/games.csv")
        st.write('## Away Team Season Stats')
        df = gamesA.groupby(['awayTeam', 'seasonStartYear']).size().unstack()
        st.write(df)
    with tabgs2:
        gamesA = pd.read_csv(r"data/games.csv")
        st.write('## Home Team Season Stats')
        df = gamesA.groupby(['homeTeam', 'seasonStartYear']).size().unstack()
        st.write(df)
with coaches:
    tabcs1, tabcs2, tabcs3 = st.tabs(
        ['Coach Age', 'Coach Type', 'Coach Finish'])
    with tabcs1:
        coachesT = pd.read_csv(r"data/coaches.csv")
        st.write('## Coach team ')
        coachesT['coachName'].unique()
        st.write(coachesT)
        top20coachesT = coachesT.head(200)

        Bartop20coachesT = alt.Chart(top20coachesT).mark_circle(size=60).encode(
            x=alt.Y('coachName'),
            y=alt.Y('Age', sort='-x'),
            tooltip=['Age'],
            color='coachName',
            order=alt.Order('coachName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(Bartop20coachesT, use_container_width=True)
    with tabcs2:
        coachesTp = pd.read_csv(r"data/coaches.csv")
        st.write('## Coach Type ')
        coachesTp['coachName'].unique()
        st.write(coachesTp)
        top20coachesTp = coachesT.head(200)

        Bartop20coachesTp = alt.Chart(top20coachesTp).mark_bar().encode(
            x=alt.Y('coachName'),
            y=alt.Y('coachType', sort='-x'),
            tooltip=['coachType'],
            color='coachName',
            order=alt.Order('coachName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(Bartop20coachesTp, use_container_width=True)
    with tabcs3:
        coachesTpf = pd.read_csv(r"data/coaches.csv")
        st.write('## Coach Finish ')
        coachesTpf['coachName'].unique()
        st.write(coachesTpf)
        top20coachesTpf = coachesTpf.head(200)

        Bartop20coachesTpf = alt.Chart(top20coachesTpf).mark_bar().encode(
            x=alt.Y('coachName'),
            y=alt.Y('Finish', sort='-x'),
            tooltip=['Finish', 'seasonStartYear'],
            color='coachName',
            order=alt.Order('coachName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(Bartop20coachesTpf, use_container_width=True)
with salaries:
    tabs1, tabs2 = st.tabs(
        [' Player Salary', 'Player Adjusted Salary'])
    with tabs1:
        player_s = pd.read_csv("data/salaries.csv")
        st.write('## Players Salary ')
        player_s['playerName'].unique()
        st.write(player_s)
        top20player_s = player_s.head(20)

        Bartop20player_s = alt.Chart(top20player_s).mark_circle(size=60).encode(
            x=alt.Y('playerName'),
            y=alt.Y('salary', sort='-x'),
            tooltip=['salary', 'seasonStartYear'],
            color='salary',
            order=alt.Order('playerName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(Bartop20player_s, use_container_width=True)
    with tabs2:
        player_s = pd.read_csv("data/salaries.csv")
        st.write('## Players Adjusted Salary ')
        player_s['playerName'].unique()
        st.write(player_s)
        top20player_s = player_s.head(20)

        Bartop20player_s = alt.Chart(top20player_s).mark_bar().encode(
            x=alt.Y('playerName'),
            y=alt.Y('inflationAdjSalary', sort='-x'),
            tooltip=['inflationAdjSalary', 'seasonStartYear'],
            color='inflationAdjSalary',
            order=alt.Order('playerName',
                            sort='ascending'
                            )
        ).interactive()
        st.altair_chart(Bartop20player_s, use_container_width=True)
