#test_search_stock
#link of tutorial: https://www.kaggle.com/alvarob96/tutorial-on-data-retrieval-using-investpy
#UNSUCESSFUL

#####################################################################
# importing libraries
#####################################################################

import investpy
import pandas as pd
import random
from pprint import pprint


#####################################################################
# declarations
#####################################################################



#####################################################################
# execution
#####################################################################

available_equities = investpy.get_equities_list(country='brazil')
pprint(available_equities)