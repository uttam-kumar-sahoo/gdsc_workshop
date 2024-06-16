import streamlit as st 
import pickle 

pickle_in=open('model.pkl',"rb")
model=pickle.load(pickle_in)

def predict_species_flower(sepal_length,sepal_width,Petal_length,Petal_width):
    prediction=model.predict([[sepal_length,sepal_width,Petal_length,Petal_width]])
    print(prediction)
    return prediction



def main():
    st.title("Iris Flower Classification")

    sepal_length=st.text_input("Sepal_length","")
    sepal_width=st.text_input("Sepal_width","")
    Petal_length=st.text_input("Petal_length","")
    Petal_width=st.text_input("Petal_width","")

    result=""

    if st.button("Predict"):
        result=predict_species_flower(sepal_length,sepal_width,Petal_length,Petal_width)
        st.success("The Species is {}".format(result))


if __name__=='__main__':
    main()    
