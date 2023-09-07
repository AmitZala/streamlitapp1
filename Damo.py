import streamlit as st
import pandas as pd
st.title('AMIT ZALA PROJECT')
st.header('Home')
st.subheader('About')


st.write('This is my first project.')


st.markdown('''

### This is project List
- Machine Learning Project.
- Deep Learning Project.
- NLP Project
- PowerBI Dashboard

''')


st.code('''

def square(input):
    return square**2

x = square(2)

''')

st.latex("x^2 = 10")

st.write('DataFrame')

df = pd.DataFrame({
    "name":['amit','Renuka'],
    "marks":[50,60]
})
st.dataframe(df)

st.metric('Revenue','RS 3L','+10%')



st.json(
{
    "employee": {
        "name":       "sonoo",
        "salary":      56000,
        "married":    'true'
    }
}

)


st.image('unnamed.jpg')



st.sidebar.title('my sidebar')



