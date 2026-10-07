import streamlit as st
import pandas as pd
import requests


"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)

"""
## Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin. We need to know all the inputs required by our model to make a prediction.

1. Let's ask for:
- island (the location where the penguin lives: Biscoe, Dream or Torgersen)
- bill length (in mm)
- bill depth (in mm)
- flipper length (in mm)
- body mass (in g)
- sex ("Male" or "Female")
"""
island_list = ['Dream', 'Biscoe', 'Torgersen']

island = st.selectbox('Island', island_list)
bill_length_mm = st.number_input('Bill Length (mm)')
bill_depth_mm = st.number_input('Bill Depth (mm)')
flipper_length_mm = st.number_input('Flipper Length (mm)')
body_mass_g = st.number_input('Body Mass (g)')
sex = st.selectbox('Sex', ['Male', 'Female'])

st.write(f"The penguin is from {island}" + "  " + "\n"
        + f"Has a bill length of {bill_length_mm}" + "  " + "\n"
        + f"Has a bill depth of {bill_depth_mm}" + "  " + "\n"
        + f"Has a flipper length of {flipper_length_mm}" + "  " + "\n"
        + f"Has a body mass of {body_mass_g}" + "  " + "\n"
        +f"Is a {sex} penguin")


"""
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?

1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""

api_url = st.secrets['API_URL']

api_dict = {
    "island": island,
    "bill_length_mm": bill_length_mm,
    "bill_depth_mm": bill_depth_mm,
    "flipper_length_mm": flipper_length_mm,
    "body_mass_g": body_mass_g,
    "sex": sex
}

res = requests.get(api_url, params=api_dict)
st.write(res.url)
prediction = res.json()['prediction']
st.write(f"The penguin is most likely a {prediction}")
