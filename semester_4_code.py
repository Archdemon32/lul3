import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt

githubpath = './data/'
df_c = pd.read_excel(githubpath + 'my_shop_data.xlsx', sheet_name="customers")
df_o = pd.read_excel(githubpath + 'my_shop_data.xlsx', sheet_name="order")
df_e = pd.read_excel(githubpath + 'my_shop_data.xlsx', sheet_name="employee")
df_p = pd.read_excel(githubpath + 'my_shop_data.xlsx', sheet_name="products")

df_e['emp_name']=df_e['firstname'] + ' ' + df_e['lastname']
# df_p['productname']=df_p['productname']
df_o['Sales']=df_o['unitprice']*df_o['quantity']
# df_m=pd.merge(df_o, df_p, on='product_id')

salesdict={}
for i in range(1,11):
    salesdict[i]=df_o.loc[df_o['employee_id']==i]['Sales'].sum()
for i in range(1,11):
    name=df_e.loc[df_e['employee_id']==i]['emp_name']
    salesdict[name[i-1]]=salesdict[i]
    del salesdict[i]

dash_app = dash.Dash(__name__)
app = dash_app.server

app.layout = html.Div([
    html.H4('Sales Data'),
    dcc.Graph(id="graph"),
    html.P("ID:"),
    dcc.Dropdown(id='employee_id',
        options=['Product_ID','employee_id'],
        value='employee_id', clearable=False),

    html.P("Sales:"),
    dcc.Dropdown(id='Sales',
        options=['Sales'],
        value='Sales', clearable=False),])

@app.callback(Output("graph", "figure"), Input("employee_id", "Sales")

def generate_chart(employee_id, Sales):
    df = px.data.tips(new)
    fig = px.pie(df, values=values, names=names, hole=.3)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
# salesprod={}
# for i in range(1,21):
#     salesprod[i]=df_o.loc[df_o['product_id']==i]['Sales'].sum()
# for i in range(1,21):
#     name=df_e.loc[df_m['product_id']==i]['productname']
#     salesprod[name[i-1]]=salesprod[i]
#     del salesprod[i]
#
# Products = []
# Total_Sales2 = []
#
# for key in salesproducts:
#     Products.append(key)
#     Total_Sales2.append(salesdict[key])
#
# plt.pie(Total_Sales2, labels=Products)
#
# plt.axis('equal')
# plt.show()
