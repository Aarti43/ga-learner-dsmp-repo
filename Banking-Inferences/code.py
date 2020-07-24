# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

#Reading file
data=pd.read_csv(path)

#Sampling the dataframe
data_sample = data.sample(n=sample_size, random_state=0)

#Finding the mean of the sample
sample_mean = data_sample['installment'].mean()

#Finding the standard deviation of the sample
sample_std = data_sample['installment'].std()

#Finding the margin of error
margin_of_error = z_critical * (sample_std/math.sqrt(sample_size))

#Finding the true mean
true_mean=data['installment'].mean()
print(("True mean: {}".format(true_mean)))

#Finding the confidence interval
confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)  

print("Confidence interval:\n", confidence_interval)

#Code starts here

if true_mean not in confidence_interval:
    print('The population mean falls in the range of confidence interval')
else:
    print('The population mean does not fall in the range of confidence interval')



# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig ,axes = plt.subplots(nrows = 3 , ncols = 1)
for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        m.append((data_sample['installment'].sample(n=sample_size[i])).mean())
    mean_series = pd.Series(m)
    axes[i].hist(mean_series)
plt.show()


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
# To change the percentage value into float
data['int.rate'] = data['int.rate'].str.rstrip('%').astype('float') / 100.0

# To Find Z-statistics
z_statistic, p_value = ztest(x1 = data[data['purpose']=='small_business']['int.rate'], value = data['int.rate'].mean(), alternative='larger')

print('Z-Statistics is', z_statistic)
print('P-Value is',  p_value)

if p_value < 0.05:
    print('Interest rate being given to people with purpose as small_business is higher than the average interest rate')
else:
    print('There is no difference in interest rate being given to people with purpose as small_business')






# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic, p_value = ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2=data[data['paid.back.loan']=='Yes']['installment'])

print('Z_statistic is', z_statistic )
print('P-Value is', p_value)

if p_value < 0.05:
    print('There is difference in installments being paid by loan defaulters and loan non defaulters')
else:
    print('There is no difference in installments being paid by loan defaulters and loan non defaulters')


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()
no = data[data['paid.back.loan'] == 'No']['purpose'].value_counts()
observed = pd.concat([yes.transpose(), no.transpose()], keys=['Yes','No'], axis=1)
chi2, p, dof, ex = stats.chi2_contingency(observed)
if chi2 > critical_value:
    print('Distribution of purpose for loan defaulters and non defaulters is different.')
else:
    print('Distribution of purpose across all customers is same.')



