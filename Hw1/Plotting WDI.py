"""
Asa Guest
HW1 - World Development Indicators
Use API to download data (https://pypi.org/project/wbgapi/)
"""
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

wdi_df = pd.read_csv(r"./Data_Extract_From_World_Development_Indicators/N2O Data, India, Kenya, Thailand_Non Percent.csv")

IND = wdi_df.iloc[0, 4:].tolist()
KEN = wdi_df.iloc[1, 4:].tolist()
THA = wdi_df.iloc[2, 4:].tolist()

YOI = [1971+x for x, it in enumerate(IND)]

fig, ax = plt.subplots()

ax.plot(YOI, IND, '--')
ax.plot(YOI, KEN, 'o')
ax.plot(YOI, THA, '-')
ax.legend(['India', 'Kenya', 'Thailand'])
ax.set_ylabel('$N_{2}O$ ($10^{3}$ metric tons)')
ax.set_xlabel('Year')
ax.set_title('$N_{2}O$ Emissions in Energy Sector')
fig.savefig('N2O_v_mton')