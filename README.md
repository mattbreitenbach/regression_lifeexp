# regression_lifeexp

During the course "Estatística Econômica" (economic statistics) i learned using the Wooldridge textbook about cross-sectional econometrics. With the help of my classmates AUGUSTO ARTHUR SCHEEREN, CAETANO ZIMMER DA SILVA, LUCAS CUBATELI TARGA, and MATEUS MARTINELLI KOCH, we did a final project for this class about life expectancy.

This repository is a re-interpretation of this final project, in the end, I got a similar result.

In the data folder, you will encounter some folders to retrieve data from WHO (world health organization) API, and WB (World Bank) lib. I also treat that data and saved it in a .csv file called "merged_data.csv"

In the file "regression_analysis.ipynb" you will find the regression analysis of the data, I did the F-test, RESET-test, BP-test, QQ-plot, and JARQUE/BERA-TEST. Unfortunately, the model presents heteroscedasticity, thus it should not be used as an inference tool.
