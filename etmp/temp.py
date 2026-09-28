import pandas as pd
from scipy import stats
import numpy as np
def trimmed_average(df, name):
    col = df[name]
    col.sort()

def explanatory_analysis(charges_data_path, personal_data_path, plan_data_path):
    df_charges, df_personal, df_plan = pd.read_csv(charges_data_path), pd.read_csv(personal_data_path), pd.read_csv(plan_data_path)
    # write you solution here
    col = df_charges["monthlyCharges"]
    # Sort
    col = col.sort_values()
    #print(len(col))

    # find idx of 10th and 90th precentile
    print(len(col))
    start, end = round(len(col) * 0.1), round(len(col) * 0.9)
    ncol = col[start : end]

    # part 2
    monthly_charges_mean = round(ncol.mean())
    print(monthly_charges_mean)
    #print(col.isnull().sum())

    # fill col
    col = col.fillna(monthly_charges_mean)
    #print(col.isnull().sum())
    df_charges["monthlyCharges"] = col
    print(f'totalcharges nan: {df_charges["totalCharges"].isnull().sum()}')
    df_charges["totalCharges"] = (df_charges["totalCharges"]
                                  .fillna(df_charges["monthlyCharges"] * df_charges["tenure"]))
    print(f'totalcharges nan: {df_charges["totalCharges"].isnull().sum()}')

    # tenure binned

    df_charges["tenureBinned"] = pd.cut(
        df_charges['tenure'],
        bins=[0, 24, 48, 60, float('inf')],
        labels=['group1', 'group2', 'group3', 'group4'],
        include_lowest=True
    )

    # churn
    print((df_charges["churn"] == 'Yes').sum())
    print(len(df_charges['churn']))
    churn = (df_charges["churn"] == 'Yes').sum()
    churn_precent = round(churn / len(df_charges['churn']) * 100 )
    print(f'churn precent: {churn_precent}%')
    ndf = (df_charges
           .merge(df_personal, on= "customerID", how ="inner")
           .merge(df_plan, on= "customerID", how="inner"))
    n = len(ndf['customerID'])
    over60  = (ndf['age'] > 60).sum()
    print(f'over60 : {over60}')
    over60_precent = round(over60 / n * 100 )
    print(f'over60 precent: {over60_precent}%')

    internet_service_counts = ndf['internetService'].value_counts().to_dict()

    results = {
        "monthly_charges_mean" : monthly_charges_mean,
        "charges_data_updated" : df_charges,
        "churn_pct" : churn_precent,
        "data_merged" : ndf,
        "pct_age_above_60": over60_precent,
        "internet_service_counts" : internet_service_counts
    }
    return results

#explanatory_analysis("charges_data.csv", "personal_data.csv", "plan_data.csv")
