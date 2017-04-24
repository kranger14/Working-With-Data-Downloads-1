import pandas as pd

data = pd.read_csv("/home/dq/scripts/data/CRDC2013_14.csv", encoding="Latin-1")

data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
headers = data.columns.values
enr_cols = dict()

for header in headers:
    if header[:7] != "SCH_ENR":
        continue
    total = data[header].sum()
    enr_cols[header] = total

all_enrollment = data["total_enrollment"].sum()
for key, value in enr_cols.items():
    newvalue = float(value)/all_enrollment
    newvalue = str(round(newvalue,2))
    enr_cols[key] = newvalue

print(enr_cols)