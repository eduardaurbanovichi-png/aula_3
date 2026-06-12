
#------  COISA ALEATORIA ------

# import streamlit as st
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# st.header("Previsão de Vendas")
# dados_vendas = pd.DataFrame({'investimento': [100, 200, 300, 400, 500, 600],'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
# })

#------ TIPO 1 - CRIADO --------#

# import numpy as np
# from sklearn.tree import DecisionTreeClassifier
# # TEMPO DE USO DE UM PRODUTO x RECLAMAÇÃO
# # y = f(x)


# X = np.array([
#     [3,0],
#     [2,0],
#     [3,3],
#     [4,1],
#     [5,1],     
# ])


# y = np.array([1,0,0,0,0])
# modelo = DecisionTreeClassifier()
# modelo.fit(X,y)


#investimento de marketing


# import numpy  as np
# from sklearn.linear_model import LinearRegression
# # investimento em mkt 1mil
# X = np.array([[1],[2],[4],[5],[3]])
# # vendas 
# y =  np.array([2,8,4,6,5])



# modelo = LinearRegression()


# modelo.fit(X, y)



# print(modelo.predict([[6]]))


#----------------EXERCICIO-------------

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

st.scatter_chart(dados_vendas, x= 'investimento', y= 'faturamento')

modelo_mkt = LinearRegression()
modelo_mkt.fit(dados_vendas[['investimento']], dados_vendas[['faturamento']])

mkt_dados = st.slider('investimento', 3400,3000,5200)
faturamento_final = modelo_mkt.predict([[mkt_dados]])
print(faturamento_final)

st.metric('Seu faturamento seria', f'R$ {faturamento_final[0][0]:,.2f}')







