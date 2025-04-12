#
# This script is designed to calculate MSCI region fractions for iShares ETFs
#

import pandas as pd
import sys

def conv_str_to_float(val):
  if type(val) == type(float(0)):
    return val
  
  val = val.replace('.','')
  val = val.replace(',','.')
  return float(val)

def get_msci_region(val):
  match val:
    case 'Belgien'|'Deutschland'|'Dänemark'|'Finnland'|'Frankreich'|'Irland'|'Israel'|'Italien'|\
         'Niederlande'|'Norwegen'|'Portugal'|'Schweden'|'Schweiz'|'Spanien'|'Vereinigtes Königreich'|\
         'Österreich'|'Griechenland'|'Kuwait'|'Polen'|'Qatar'|'Saudi-Arabien'|'Südafrika'|\
         'Tschechien'|'Türkei'|'Ungarn'|'Ver. Arabische Emirate'|'Ägypten':
      return "EMEA"
    case 'Vereinigte Staaten'|'Kanada'|'Brasilien'|'Chile'|'Kolumbien'|'Mexiko'|'Peru':
      return "Amerika"
    case 'Japan'|'Australien'|'Hongkong'|'Neuseeland'|'Singapur'|'China'|'Indien'|'Indonesien'|\
         'Korea'|'Malaysia'|'Philippinen'|'Taiwan'|'Thailand':
      return "Asia-Pazifik"
    case _:
      return "Sonstige"


if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  filename = "EUNL_holdings.csv"

print('Reading file:', filename)

df = pd.read_csv(filename, skiprows = 2)

print(df)
print(df.describe())

# Calculate fraction
df["fraction"] = df["Gewichtung (%)"].apply(conv_str_to_float)
df["value"] = df["Marktwert"].apply(conv_str_to_float)

# Print only rows with Anlagenklasse == Aktien
print(df[df.Anlageklasse == "Aktien"][["Anlageklasse","Standort","Gewichtung (%)", "fraction", "Marktwert", "value"]])

# Create new dataframe for rows with Anlagenklasse == Aktien and calculate sums per location
df_aktien = df[df.Anlageklasse == "Aktien"].groupby(['Standort'])["fraction"].sum().reset_index()

# Create new region columns
df_aktien['msci_region'] = df_aktien.Standort.apply(get_msci_region)
print(df_aktien)

# Calculate sums per region
print(df_aktien.groupby(['msci_region'])["fraction"].sum().reset_index())