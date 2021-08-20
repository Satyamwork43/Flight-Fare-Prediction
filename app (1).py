 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('/content/classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Airline,Source,Destination,Total_Stops,Additional_Info,Year_of_Journey,Month_of_Journey,Day_of_Journey,Dep_hour,Dep_minute,arrival_hour,arrival_minute):   
 
    # Pre-processing user input   

    

    if Airline == "IndiGo":
        Airline = 3
    elif Airline == "Air India":
      Airline = 1
    elif Airline == "Jet Airways":
      Airline = 4
    elif Airline == "SpiceJet":
      Airline = 8
    elif Airline == "Multiple carriers":
      Airline = 6
    elif Airline == "GoAir":
      Airline = 2
    elif Airline == "Vistara":
      Airline = 10

    elif Airline == "Air Asia":
      Airline = 0
    elif Airline == "Vistara Premium economy":
      Airline = 11
    elif Airline == "Jet Airways Business":
      Airline = 5
    elif Airline == "Multiple carriers Premium economy":
      Airline = 7
    elif Airline == "Trujet":
      Airline = 9

    if Destination == "Bangalore":
        Destination = 0
    elif Destination == "Cochin":
        Destination = 1
    elif Destination == "Delhi":
        Destination = 2
    elif Destination == "Hyderabad":
        Destination = 3
    elif Destination == "Kolkata":
        Destination = 4
    elif Destination == "New Delhi":
        Destination = 5
 
    if source == "Bangalore":
        source = 0
    elif source == "Chennai":
        source = 1
    elif source == "Delhi":
        source = 2
    elif source == "Kolkata":
        source = 3
    elif source == "Mumbai":
        source = 4
    
    if Total_Stops == "non-stop":
        Total_Stops = 4
    elif Total_Stops == "2 stops"
        Total_Stops = 1
    elif Total_Stops == "1 stops":
        Total_Stops = 0
    elif Total_Stops == "3 stops":
        Total_Stops = 2
    elif Total_Stops == "4 stops":
        Total_Stops = 3

    if Additional_Info == "No info":
        Additional_Info = 8
    elif Additional_Info == "In-flight meal not included"
        Additional_Info = 5
    elif Additional_Info == "No check-in baggage included":
        Additional_Info = 7
    elif Additional_Info == "1 Short layover":
        Additional_Info = 1
    elif Additional_Info == "No Info":
        Additional_Info = 6
    elif Additional_Info == "1 Long layover":
        Additional_Info = 0
    elif Additional_Info == "Change airports":
        Additional_Info = 4
    elif Additional_Info == "Business class":
        Additional_Info = 3
    elif Additional_Info == "Red-eye flight":
        Additional_Info = 9
    elif Additional_Info == "2 Long layover":
        Additional_Info = 2
 
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Airline,Source,Destination,Total_Stops,Additional_Info,Year_of_Journey,Month_of_Journey,Day_of_Journey,Dep_hour,Dep_minute,arrival_hour,arrival_minute]])
     
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Flight Price Prediction</h1> 
    </div> 
    """
      
    # display the front end aspect

    st.markdown(html_temp, unsafe_allow_html = True) 

    st.sidebar.subheader("Select Departure")
    m = pd.to_datetime("today").month
    d = pd.to_datetime("today").day
    y = pd.to_datetime("today").year
    
    dep = st.sidebar.date_input("Day" , datetime.date(y,m,d))
    if dep is not None:
        mon_d = dep.month
        day_d = dep.day
        dat_y = dep.year

        hour_1 = st.sidebar.selectbox("Hour", list(range(1,25)))
        minute_1 = st.sidebar.selectbox("Minute", list(range(0,61)))

    st.subheader("Departure Time :")
    x = "2020" + "/"  +str(mon_d) + "/" + str(day_d) + " " + str(hour_1) + ":" + str(minute_1)
    if x is not None:
        
        op = pd.to_datetime([x])
        if op is not None:
            st.write(op.item())
    

    st.sidebar.subheader("Select Arrival")
    arr = st.sidebar.date_input("Day." , datetime.date(y,m,d+1))
    if arr is not None:
    
        mon_a = arr.month
        day_a = arr.day
        
        

        hour_2 = st.sidebar.selectbox("Hour.", list(range(1,25)) ,2)
        minute_2 = st.sidebar.selectbox("Minute.", list(range(0,61)))

    st.subheader("Arrival Time :")
    x1 = "2020" + "/"  +str(mon_a) + "/" + str(day_a) + " " + str(hour_2) + ":" + str(minute_2)
    if x1 is not None:
        
        op1 = pd.to_datetime([x1] )
        if op1 is not None:
            st.write(op1.item())
      
    # following lines create boxes in which user can enter data required to make prediction 
    Airline = st.selectbox('Airline',('IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet')
    Destination = st.selectbox('Destination',('New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad')) 
    Source = st.selectbox('Source',('Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'))
    Total_Stops = st.selectbox('Total_Stops',('non-stop', '2 stops', '1 stop', '3 stops', '4 stops'))
    Additional_Info=st.selectbox('Additional_Info',('No info', 'In-flight meal not included',
       'No check-in baggage included', '1 Short layover', 'No Info',
       '1 Long layover', 'Change airports', 'Business class',
       'Red-eye flight', '2 Long layover'))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Airline,Source,Destination,Total_Stops,Additional_Info,Year_of_Journey,Month_of_Journey,Day_of_Journey,Dep_hour,Dep_minute,arrival_hour,arrival_minute) 
        st.success('Your Fare Price is {}'.format(result))
        st.write("*Happy and Safe Journey ...*")
    
     
if __name__=='__main__': 
    main()
