# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------
# APP CONFIG
# ---------------------------
st.set_page_config(
    page_title="EPL Data Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #38003c;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #38003c;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🏆 Advanced EPL Analytics Dashboard</h1>', unsafe_allow_html=True)
st.markdown("**Interactive analysis with predictive insights and advanced visualizations**")

# ---------------------------
# DATA LOADING
# ---------------------------
@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    if 'MatchDate' in df.columns:
        df['MatchDate'] = pd.to_datetime(df['MatchDate'])
    return df

# Sidebar for file upload
with st.sidebar:
    st.header("🔧 Configuration")
    uploaded_file = st.file_uploader("Upload EPL Dataset", type=["csv"])
    
    if uploaded_file:
        df = load_data(uploaded_file)
    else:
        try:
            df = load_data("data/epl_cleaned.csv")
        except FileNotFoundError:
            st.error("Please upload a CSV file to continue.")
            st.stop()

# ---------------------------
# ADVANCED FILTERS
# ---------------------------
with st.sidebar:
    st.header("🔍 Advanced Filters")
    
    # Team filter with multiselect
    all_teams = sorted(set(df['HomeTeam']).union(df['AwayTeam']))
    selected_teams = st.multiselect("Select Teams", all_teams, default=all_teams[:5])
    
    # Season filter
    if 'Season' in df.columns:
        seasons = sorted(df['Season'].unique())
        selected_seasons = st.multiselect("Select Seasons", seasons, default=seasons)
    
    # Date range filter
    if 'MatchDate' in df.columns:
        min_date = df['MatchDate'].min().date()
        max_date = df['MatchDate'].max().date()
        date_range = st.date_input("Select Date Range", 
                                 value=(min_date, max_date),
                                 min_value=min_date,
                                 max_value=max_date)
    
    # Goals filter
    min_goals, max_goals = st.slider("Total Goals Range", 
                                   0, 
                                   int(df['FullTimeHomeGoals'].max() + df['FullTimeAwayGoals'].max()),
                                   (0, 10))

# Apply filters
filtered_df = df.copy()
if selected_teams:
    filtered_df = filtered_df[
        (filtered_df['HomeTeam'].isin(selected_teams)) | 
        (filtered_df['AwayTeam'].isin(selected_teams))
    ]

if 'Season' in df.columns and selected_seasons:
    filtered_df = filtered_df[filtered_df['Season'].isin(selected_seasons)]

if 'MatchDate' in df.columns and len(date_range) == 2:
    filtered_df = filtered_df[
        (filtered_df['MatchDate'].dt.date >= date_range[0]) &
        (filtered_df['MatchDate'].dt.date <= date_range[1])
    ]

filtered_df['TotalGoals'] = filtered_df['FullTimeHomeGoals'] + filtered_df['FullTimeAwayGoals']
filtered_df = filtered_df[
    (filtered_df['TotalGoals'] >= min_goals) & 
    (filtered_df['TotalGoals'] <= max_goals)
]

# ---------------------------
# MAIN DASHBOARD WITH TABS
# ---------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "🏆 League Table", "📈 Analytics", "🔮 Predictions", "🎯 Team Deep Dive"])

# TAB 1: OVERVIEW
with tab1:
    # Key metrics row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    total_matches = len(filtered_df)
    total_goals = filtered_df['TotalGoals'].sum()
    avg_goals = filtered_df['TotalGoals'].mean()
    home_wins = len(filtered_df[filtered_df['FullTimeResult'] == 'H'])
    away_wins = len(filtered_df[filtered_df['FullTimeResult'] == 'A'])
    
    with col1:
        st.metric("Total Matches", total_matches)
    with col2:
        st.metric("Total Goals", total_goals)
    with col3:
        st.metric("Avg Goals/Match", f"{avg_goals:.2f}")
    with col4:
        st.metric("Home Win %", f"{(home_wins/total_matches*100):.1f}%")
    with col5:
        st.metric("Away Win %", f"{(away_wins/total_matches*100):.1f}%")
    
    # Interactive charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Goals distribution
        fig_hist = px.histogram(filtered_df, x='TotalGoals', 
                              title="Goals Distribution",
                              labels={'TotalGoals': 'Total Goals per Match'})
        fig_hist.update_layout(showlegend=False)
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Results pie chart
        result_counts = filtered_df['FullTimeResult'].value_counts()
        result_labels = {'H': 'Home Win', 'A': 'Away Win', 'D': 'Draw'}
        fig_pie = px.pie(values=result_counts.values, 
                        names=[result_labels.get(x, x) for x in result_counts.index],
                        title="Match Results Distribution")
        st.plotly_chart(fig_pie, use_container_width=True)

# TAB 2: ENHANCED LEAGUE TABLE
with tab2:
    st.subheader("📊 Interactive League Table")
    
    # Calculate league table
    league_table = []
    teams_to_show = selected_teams if selected_teams else all_teams
    
    for team in teams_to_show:
        home = filtered_df[filtered_df['HomeTeam'] == team]
        away = filtered_df[filtered_df['AwayTeam'] == team]
        
        played = len(home) + len(away)
        if played == 0:
            continue
            
        wins = len(home[home['FullTimeResult'] == 'H']) + len(away[away['FullTimeResult'] == 'A'])
        draws = len(home[home['FullTimeResult'] == 'D']) + len(away[away['FullTimeResult'] == 'D'])
        losses = played - wins - draws
        gf = home['FullTimeHomeGoals'].sum() + away['FullTimeAwayGoals'].sum()
        ga = home['FullTimeAwayGoals'].sum() + away['FullTimeHomeGoals'].sum()
        gd = gf - ga
        points = wins * 3 + draws
        
        league_table.append({
            'Position': 0,
            'Team': team,
            'Played': played,
            'Wins': wins,
            'Draws': draws,
            'Losses': losses,
            'GF': gf,
            'GA': ga,
            'GD': gd,
            'Points': points,
            'Points per Game': round(points/played, 2) if played > 0 else 0
        })
    
    league_df = pd.DataFrame(league_table).sort_values(by=['Points', 'GD'], ascending=False).reset_index(drop=True)
    league_df['Position'] = range(1, len(league_df) + 1)
    
    # Add color coding for positions
    def color_positions(row):
        if row['Position'] <= 4:
            return ['background-color: #d4edda'] * len(row)  # Champions League (green)
        elif row['Position'] <= 6:
            return ['background-color: #fff3cd'] * len(row)  # Europa League (yellow)
        elif row['Position'] >= len(league_df) - 2:
            return ['background-color: #f8d7da'] * len(row)  # Relegation (red)
        else:
            return [''] * len(row)
    
    styled_df = league_df.style.apply(color_positions, axis=1)
    st.dataframe(styled_df, use_container_width=True)
    
    # Top performers
    col1, col2, col3 = st.columns(3)
    with col1:
        top_scorer = league_df.loc[league_df['GF'].idxmax()]
        st.metric("🥅 Top Scoring Team", top_scorer['Team'], f"{top_scorer['GF']} goals")
    with col2:
        best_defense = league_df.loc[league_df['GA'].idxmin()]
        st.metric("🛡️ Best Defense", best_defense['Team'], f"{best_defense['GA']} conceded")
    with col3:
        most_efficient = league_df.loc[league_df['Points per Game'].idxmax()]
        st.metric("⚡ Most Efficient", most_efficient['Team'], f"{most_efficient['Points per Game']} PPG")

# TAB 3: ADVANCED ANALYTICS
with tab3:
    st.subheader("📈 Advanced Analytics")
    
    # Home vs Away performance
    col1, col2 = st.columns(2)
    
    with col1:
        # Home advantage analysis
        home_stats = filtered_df.groupby('HomeTeam').agg({
            'FullTimeHomeGoals': 'mean',
            'FullTimeAwayGoals': 'mean'
        }).reset_index()
        home_stats['Goal_Difference'] = home_stats['FullTimeHomeGoals'] - home_stats['FullTimeAwayGoals']
        
        fig_home = px.scatter(home_stats, x='FullTimeHomeGoals', y='FullTimeAwayGoals',
                            text='HomeTeam', title="Home Performance: Goals For vs Against",
                            labels={'FullTimeHomeGoals': 'Goals Scored at Home',
                                   'FullTimeAwayGoals': 'Goals Conceded at Home'})
        fig_home.add_shape(type="line", x0=0, y0=0, x1=4, y1=4, 
                          line=dict(color="red", dash="dash"))
        st.plotly_chart(fig_home, use_container_width=True)
    
    with col2:
        # Goals over time
        if 'MatchDate' in filtered_df.columns:
            monthly_goals = filtered_df.groupby(filtered_df['MatchDate'].dt.to_period('M'))['TotalGoals'].mean().reset_index()
            monthly_goals['MatchDate'] = monthly_goals['MatchDate'].astype(str)
            
            fig_trend = px.line(monthly_goals, x='MatchDate', y='TotalGoals',
                              title="Average Goals per Match Over Time")
            fig_trend.update_xaxes(tickangle=45)
            st.plotly_chart(fig_trend, use_container_width=True)
    
    # Correlation heatmap
    st.subheader("🔥 Performance Correlations")
    numeric_cols = ['FullTimeHomeGoals', 'FullTimeAwayGoals', 'HalfTimeHomeGoals', 'HalfTimeAwayGoals']
    available_cols = [col for col in numeric_cols if col in filtered_df.columns]
    
    if len(available_cols) >= 2:
        corr_matrix = filtered_df[available_cols].corr()
        fig_heatmap = px.imshow(corr_matrix, text_auto=True, aspect="auto",
                               title="Performance Metrics Correlation")
        st.plotly_chart(fig_heatmap, use_container_width=True)

# TAB 4: PREDICTIONS
with tab4:
    st.subheader("🔮 Predictive Analytics")
    
    # Simple prediction model based on historical performance
    st.write("**Next Match Outcome Predictor**")
    
    col1, col2 = st.columns(2)
    with col1:
        home_team = st.selectbox("Home Team", all_teams, key="pred_home")
    with col2:
        away_team = st.selectbox("Away Team", all_teams, key="pred_away")
    
    if st.button("Predict Match Outcome"):
        # Calculate team strengths based on recent performance
        home_data = filtered_df[filtered_df['HomeTeam'] == home_team]
        away_data = filtered_df[filtered_df['AwayTeam'] == away_team]
        
        if len(home_data) > 0 and len(away_data) > 0:
            home_avg_scored = home_data['FullTimeHomeGoals'].mean()
            home_avg_conceded = home_data['FullTimeAwayGoals'].mean()
            away_avg_scored = away_data['FullTimeAwayGoals'].mean()
            away_avg_conceded = away_data['FullTimeHomeGoals'].mean()
            
            # Simple prediction logic
            home_strength = home_avg_scored - home_avg_conceded
            away_strength = away_avg_scored - away_avg_conceded
            
            if home_strength > away_strength + 0.5:
                prediction = "Home Win"
                confidence = min(95, 60 + abs(home_strength - away_strength) * 10)
            elif away_strength > home_strength + 0.5:
                prediction = "Away Win"
                confidence = min(95, 60 + abs(away_strength - home_strength) * 10)
            else:
                prediction = "Draw"
                confidence = 50
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Predicted Outcome", prediction)
            with col2:
                st.metric("Confidence", f"{confidence:.0f}%")
            with col3:
                predicted_goals = max(0, (home_avg_scored + away_avg_scored) / 2)
                st.metric("Expected Goals", f"{predicted_goals:.1f}")
        else:
            st.warning("Not enough data for these teams in the selected filters.")

# TAB 5: TEAM DEEP DIVE
with tab5:
    st.subheader("🎯 Team Performance Deep Dive")
    
    selected_team_analysis = st.selectbox("Select Team for Analysis", all_teams, key="analysis_team")
    
    # Team-specific metrics
    team_home = filtered_df[filtered_df['HomeTeam'] == selected_team_analysis]
    team_away = filtered_df[filtered_df['AwayTeam'] == selected_team_analysis]
    team_all = pd.concat([team_home, team_away])
    
    if len(team_all) > 0:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            home_record = f"{len(team_home[team_home['FullTimeResult'] == 'H'])}-{len(team_home[team_home['FullTimeResult'] == 'D'])}-{len(team_home[team_home['FullTimeResult'] == 'A'])}"
            st.metric("Home Record (W-D-L)", home_record)
        
        with col2:
            away_record = f"{len(team_away[team_away['FullTimeResult'] == 'A'])}-{len(team_away[team_away['FullTimeResult'] == 'D'])}-{len(team_away[team_away['FullTimeResult'] == 'H'])}"
            st.metric("Away Record (W-D-L)", away_record)
        
        with col3:
            goals_scored = team_home['FullTimeHomeGoals'].sum() + team_away['FullTimeAwayGoals'].sum()
            st.metric("Total Goals Scored", goals_scored)
        
        with col4:
            goals_conceded = team_home['FullTimeAwayGoals'].sum() + team_away['FullTimeHomeGoals'].sum()
            st.metric("Total Goals Conceded", goals_conceded)
        
        # Performance timeline
        if 'MatchDate' in team_all.columns:
            team_all_sorted = team_all.sort_values('MatchDate')
            
            # Calculate rolling performance
            def get_team_result(row, team):
                if row['HomeTeam'] == team:
                    if row['FullTimeResult'] == 'H': return 3
                    elif row['FullTimeResult'] == 'D': return 1
                    else: return 0
                else:
                    if row['FullTimeResult'] == 'A': return 3
                    elif row['FullTimeResult'] == 'D': return 1
                    else: return 0
            
            team_all_sorted['Points'] = team_all_sorted.apply(lambda x: get_team_result(x, selected_team_analysis), axis=1)
            team_all_sorted['Cumulative_Points'] = team_all_sorted['Points'].cumsum()
            
            fig_timeline = px.line(team_all_sorted, x='MatchDate', y='Cumulative_Points',
                                 title=f"{selected_team_analysis} - Cumulative Points Over Time")
            st.plotly_chart(fig_timeline, use_container_width=True)

# ---------------------------
# REAL-TIME UPDATES
# ---------------------------
if st.sidebar.button("🔄 Refresh Data"):
    st.cache_data.clear()
    st.rerun()

# ---------------------------
# EXPORT FUNCTIONALITY
# ---------------------------
with st.sidebar:
    st.header("📥 Export Options")
    if st.button("Download Filtered Data"):
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"epl_filtered_data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Data Period:**")
    if 'MatchDate' in df.columns:
        st.write(f"{df['MatchDate'].min().strftime('%Y-%m-%d')} to {df['MatchDate'].max().strftime('%Y-%m-%d')}")
with col2:
    st.markdown("**Total Records:**")
    st.write(f"{len(df):,} matches")
with col3:
    st.markdown("**Last Updated:**")
    st.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit & Plotly | Advanced EPL Analytics Dashboard")