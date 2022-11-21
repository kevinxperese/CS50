# Testing out using R to solve the ACS pandas exercise that Josh created...
library(tidyverse)

# Read in ACS data
ACS_data <- read_csv('\\\\cbo.gov\\shares\\PUBLIC_DATA\\ACS\\1-year\\2018\\psam_pusa.csv', n_max=1000)

# Take a peak at some summary stats
summary(ACS_data)

# Create a YEAR column, and then select a subset of columns to work with
ACS_subset <- ACS_data %>%
  mutate(YEAR = 2018) %>%
  select(YEAR, SERIALNO, ST, AGEP, SSP, RETP)

# Create means (for numeric columns, and removing NAs from the calculation)
ACS_subset %>%
  select(where(is.numeric)) %>%
  summarise(across(everything(), mean, na.rm=TRUE))

# Create dummy variable for age 50+
ACS_subset$AGE_50_PLUS <- ifelse(ACS_subset$AGEP >= 50, 1, 0)
