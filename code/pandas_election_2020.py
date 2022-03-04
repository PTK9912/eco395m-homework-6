from dataclasses import replace
import os
import pandas as pd

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report_pandas.csv")

if __name__ == "__main__":
    df = pd.read_csv(IN_PATH)
    
    
    df1=df.loc[df.year==2020]
    df2=df1.groupby(by=["year","state_po","candidate"])["candidatevotes"].sum().reset_index()
    df3=df2.sort_values(by=["state_po","candidatevotes"],ascending=[True,False])
    df3['candidatevotes'] = df3['candidatevotes'].astype(int)
    df3.rename(columns={"state_po":"state_code","candidatevotes":"votes"},inplace=True)
    df3.to_csv(OUTPUT_PATH,index=False)