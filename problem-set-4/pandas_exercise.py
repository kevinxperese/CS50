import pandas as pd


ACS_data = pd.read_csv("\\\\cbo.gov\\shares\\PUBLIC_DATA\\ACS\\1-year\\2018\\psam_pusa.csv", nrows=1000)
print(f'ACS_data has {ACS_data.shape[0]} rows and {ACS_data.shape[1]} columns.\n')

ACS_data['YEAR'] = 2018

# Could use .copy() up here to avoid the SettingWithCopyWarning
# ACS_subset = ACS_data[['YEAR', 'SERIALNO', 'ST', 'AGEP', 'SSP', 'RETP']].copy()
ACS_subset = ACS_data[['YEAR', 'SERIALNO', 'ST', 'AGEP', 'SSP', 'RETP']]
print('Head of ACS_subset:')
print(ACS_subset.head(10), '\n')

print('Means of ACS_subset:')
print(ACS_subset.mean(), '\n')


# With copy to avoid SettingWithCopyWarning
print(id(ACS_subset))
ACS_subset = ACS_subset.copy()
print(id(ACS_subset))
ACS_subset['AGE_50_PLUS'] = (ACS_subset.loc[:, 'AGEP'] >= 50).astype(int)
print('Head of ACS_subset with `AGE_50_PLUS` dummy variable')
print(ACS_subset.head(10), '\n')

# With .assign() method, which also avoids the SettingWithCopyWarning
ACS_subset = ACS_subset.assign(AGE_LT_50 = (ACS_subset.loc[:, 'AGEP'] < 50).astype(int))
print('Head of ACS_subset with `AGE_LT_50` dummy variable:')
print(ACS_subset.head(10), '\n')
