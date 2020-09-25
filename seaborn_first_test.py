#seaborn_first_test

# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot([0, 1, 2, 3, 4, 5])

# plt.show()

#------------------------------------

# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

# plt.show()

#------------------------------------

import seaborn as sns, numpy as np
sns.set_theme(); np.random.seed(0)
x = np.random.randn(100)
ax = sns.distplot(x)

#this last was failed!