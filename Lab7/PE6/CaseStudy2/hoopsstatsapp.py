"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

import pandas as pd
from hoopstatsview import *
def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    HoopStatsView(frame)
    hoop_stats_view = HoopStatsView(frame)
    hoop_stats_view.mainloop()

if __name__ == "__main__":
    main()



def cleanStats(df):
    df[['FGM', 'FGA']] = df['FG'].str.split('-', expand=True).astype(int)
    df.drop(columns=['FG'], inplace=True)

    df[['3PM', '3PA']] = df['3PT'].str.split('-', expand=True).astype(int)
    df.drop(columns=['3PT'], inplace=True)

    df[['FTM', 'FTA']] = df['FT'].str.split('-', expand=True).astype(int)
    df.drop(columns=['FT'], inplace=True)

    return df