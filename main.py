import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sheets = {
    "1": "England",
    "2": "Wales",
    "3": "NI",
    "4": "Scotland",
}

fpath = "leadingcausesofdeath.xlsx"

df = pd.DataFrame()
for table, country in sheets.items():
    tmp = pd.read_excel(fpath, sheet_name=f"Table {table}", skiprows=15)

    if "cause" in list(tmp)[0]:
        cause_col = "Leading cause (ICD-10 code)"
    else:
        cause_col = "Leading Cause (ICD-10 code)"

    tmp[cause_col] = [x.rstrip() for x in tmp[cause_col].values]

    tmp.columns = [str(x).rstrip() for x in tmp.columns]
    for col in list(tmp):
        if type(col) is str:
            if "Unnamed" in col:
                tmp.drop(columns=[col], inplace=True)

    tmp = tmp.set_index(cause_col).T
    tmp["country"] = country
    df = df.append(tmp)


df = df.reset_index()
df.pivot(['index', 'country'], columns="Cerebrovascular diseases (I60-I69)")

# https://www.kaggle.com/jrmistry/plotly-how-to-change-plot-data-using-dropdowns
import plotly.graph_objects as go

fig = go.Figure()
for col in df.columns.to_list():
    fig.add_trace(go.Scatter(x=df.index, y=df[col], name=col))


fig.show()
sns.lineplot(x=df.index, y="Cerebrovascular diseases (I60-I69)", hue="country", data=df)
plt.show()

# xls = pd.read_excel(, sheet_name=None)
# xls = pd.ExcelFile("leadingcausesofdeath.xlsx")

# with open()
