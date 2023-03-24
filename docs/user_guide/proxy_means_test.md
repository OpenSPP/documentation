# Proxy Mean Test

## Introduction

The Proxy Means Test (PMT) is a statistical method used to determine the poverty status of a household, using a set of indicators that are correlated with household income or consumption. The PMT is often used to identify beneficiaries who are eligible for support.

Here are some typical criteria that may be used to calculate the Proxy Means Test:

- **Household assets**: The PMT may consider household assets such as land, livestock, or other durable goods as an indicator of household income or consumption. The value of these assets may be used as a proxy for the household's overall economic status.
- **Housing conditions**: The PMT may consider housing conditions such as the type of dwelling, access to water and sanitation facilities, and other indicators of living standards as proxies for household income or consumption.
- **Education and occupation**: The PMT may consider the education level and occupation of household members as proxies for income or consumption, as these factors can be correlated with higher income levels.
- **Demographic characteristics**: The PMT may consider demographic characteristics such as household size, age, and gender composition as proxies for income or consumption. For example, households with larger numbers of children or elderly members may be considered more vulnerable to poverty.

Overall, the specific criteria used to calculate the PMT may vary depending on the context and objectives of the social protection program. It is important to select indicators that are relevant and meaningful in the local context and that accurately reflect household income or consumption levels.

## How to configure a proxy mean test

### Exemple

Here's a simple example of a PMT formula using the following indicators: household size, education level, and assets:

PMT score = (0.5 x household size) + (0.3 x education level) + (0.2 x asset value)

In this example, the PMT score is calculated using three indicators: household size, education level, and asset value. Each indicator is assigned a weight based on its perceived importance in reflecting household income or consumption. The weights are then multiplied by the value of each indicator and added together to produce the PMT score. In this case, household size is given a weight of 0.5, education level is given a weight of 0.3, and asset value is given a weight of 0.2.

For example, if a household has a size of 4, an education level of 12 (out of a possible 20), and assets worth $5,000, the PMT score would be calculated as follows:

PMT score = (0.5 x 4) + (0.3 x 12) + (0.2 x 5000) = 2 + 3.6 + 1000 = 1005.6

In this example, the PMT score for the household is 1005.6. This score can then be used to determine the household's poverty status and eligibility for social protection programs.

### Implementation

TODO