import pandas as pd

data = {
    'men': [7, 6, 8, 5],
    'women': [2, 1, 3, 4]
}

purchases = pd.DataFrame(data)
purchases = pd.DataFrame(data, index=['1 group', '2 group', '3 group', '4 group'])
purchases.loc['2 group']
print(purchases.loc['2 group'])