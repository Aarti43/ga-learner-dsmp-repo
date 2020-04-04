# --------------
import pandas as pd
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = ['int','float'])
print(numerical_var)




# --------------
banks= bank.drop(['Loan_ID'],axis=1)
banks.head()
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
# Fill the missing values with
banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount', aggfunc = np.mean)
print(avg_loan_amount)


# code ends here



# --------------
# code starts here

# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print("loan approved for self employed", loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print("loan approved for non self employed", loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
# print percentage of loan approved for self employed
print("percentage of loan approved for self employed", percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
#print percentage of loan for non self employed
print ("percentage of loan approved for non self employed",percentage_nse)

# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)
print("Conversion of months to year", loan_term)

big_loan_term = len(loan_term[loan_term>=25])
print("Tenuer More than 25 yrs", big_loan_term)
# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')

mean_values = loan_groupby.mean()
print(mean_values)

# code ends here


