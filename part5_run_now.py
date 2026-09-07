import csv
import pandas as pd

stare = pd.read_csv("OD_STARE_FIRMA.csv", sep="^", encoding="utf-8",
                     quoting=csv.QUOTE_NONE)
stare = stare.drop_duplicates(subset="COD_INMATRICULARE", keep="last")

firme = pd.read_csv("OD_FIRME.csv", sep="^", encoding="utf-8",
                     usecols=["DENUMIRE", "CUI", "COD_INMATRICULARE"],
                     dtype={"CUI": str},
                     quoting=csv.QUOTE_NONE)

firme = firme.merge(stare, on="COD_INMATRICULARE", how="left")

COD_ACTIV = 1048
firme_active = firme[firme["COD"] == COD_ACTIV].copy()

fin = pd.read_csv("web_uu_an2024.txt", sep=",", encoding="utf-8",
                   usecols=["CUI", "CAEN"],
                   dtype={"CUI": str},
                   quoting=csv.QUOTE_NONE)

firme_active["CUI"] = firme_active["CUI"].str.strip()
fin["CUI"] = fin["CUI"].str.strip()

cui_cu_filing = set(fin["CUI"])
caen_per_cui = fin.drop_duplicates(subset="CUI").set_index("CUI")["CAEN"]

firme_active["are_filing"] = firme_active["CUI"].isin(cui_cu_filing)

total_active = len(firme_active)
total_proxy = int(firme_active["are_filing"].sum())
procent = 100 * total_proxy / total_active

cui_cu_proxy = firme_active.loc[firme_active["are_filing"], "CUI"]
top3 = caen_per_cui.reindex(cui_cu_proxy).value_counts().head(3)

print("=" * 50)
print("REZULTATE PARTEA 5")
print("=" * 50)
print(f"Firme active (cod stare = {COD_ACTIV}): {total_active:,}")
print(f"Firme unde proxy-ul functioneaza (au depus bilant 2024): {total_proxy:,}")
print(f"Procent din firmele active: {procent:.1f}%")
print("Top 3 coduri CAEN printre ele:")
print(top3)
