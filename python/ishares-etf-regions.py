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
    case 'Belgien'|'Deutschland'|'Dänemark'|'Finnland'|'Frankreich'|'Irland'|'Italien'|\
         'Niederlande'|'Norwegen'|'Portugal'|'Schweden'|'Schweiz'|'Spanien'|'Vereinigtes Königreich'|\
         'Österreich'|'Griechenland'|'Polen'|\
         'Tschechien'|'Türkei'|'Ungarn':
      return "Europa"
    case 'Israel'|'Kuwait'|'Qatar'|'Saudi-Arabien'|'Ver. Arabische Emirate':
      return "Vorderasien"
    case 'Vereinigte Staaten'|'Kanada':
      return "Nordamerika"
    case 'Brasilien'|'Chile'|'Kolumbien'|'Mexiko'|'Peru':
      return "Südamerika"
    case 'Japan'|'Australien'|'Hongkong'|'Neuseeland'|'Singapur'|'China'|'Indien'|'Indonesien'|\
         'Korea'|'Malaysia'|'Philippinen'|'Taiwan'|'Thailand':
      return "Asien-Pazifik"
    case 'Ägypten'|'Südafrika':
      return "Afrika"
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

market_value_etf = df.Marktwert.apply(conv_str_to_float).sum()
market_value_stocks = df[df.Anlageklasse == "Aktien"].Marktwert.apply(conv_str_to_float).sum()

print("Fondsfolumen",market_value_etf)
print("Fondsfolumen (Nur Aktien)",market_value_stocks)

# Calculate fraction for stocks only
df["value"] = df["Marktwert"].apply(conv_str_to_float)

# {:.1f}%'.format(val*100)
df["fraction"] = df["value"] / market_value_stocks * 100

# Print only rows with Anlagenklasse == Aktien
print(df[df.Anlageklasse == "Aktien"][["Anlageklasse","Standort","Gewichtung (%)", "fraction", "Marktwert", "value"]])
print("Summe fraction:", df[df.Anlageklasse == "Aktien"].fraction.sum())

# Create new dataframe for rows with Anlagenklasse == Aktien and calculate sums per location
df_aktien = df[df.Anlageklasse == "Aktien"].groupby(['Standort'])["fraction"].sum().reset_index()

# Create new region columns
df_aktien['msci_region'] = df_aktien.Standort.apply(get_msci_region)
print(df_aktien)

# Calculate sums per region
print(df_aktien.groupby(['msci_region'])["fraction"].sum().reset_index())
print("Summe fraction:", df_aktien.fraction.sum())