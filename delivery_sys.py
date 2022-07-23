from requests import session
import streamlit as st

f1 = open('Data.txt','r')
elements = eval(f1.read())


st.header("Vinayaga Supermarket")

st.title("Welcome to Vinayaga Supermarket")
#st.subheader("address and phone number")

sidebar = st.sidebar.radio('Navigation',['Home','My Cart','Billing','Checkout'])
confirm = False
if sidebar == 'Home':
    st.title("Supermarket")
    col1,col2, col3=st.columns(3)


    with col1:
        st.subheader("Fruits")
        st.write("")
        st.write("Mangoes: 150")
        st.write("Apple: 75")
        st.write("Pomegranates: 80")
        st.write("Cherries: 500")
        st.write("Soursop: 450")
        st.write("Watermelon: 11")
        st.write("Fresh Dates: 300")
        st.write("Durian Fruit: 750")
        st.write("Dragon Fruit: 250")

    with col2:
        st.subheader("Vegetables")
        st.write("")
        st.write("Onion: 25")
        st.write("Carrot: 63")
        st.write("Coriander Leaves: 60")
        st.write("Beans French: 80")
        st.write("Beetroot: 60")
        st.write("Brinjal: 40")
        st.write("Cucumber: 40")
        st.write("Fresh Cauliflower: 40")
        st.write("Fresh Spinach: 20")
        st.write("Garlic: 400")
        st.write("Ladies Finger: 120")

    with col3:
        st.subheader("Chocolates")
        st.write("")
        st.write("Blueberry chocolate: 500")
        st.write("Teenage Solid Milk Compound: 180")
        st.write("Valentina Dark Round Chocolate: 350")
        st.write("Plain Milk Chocolate: 660")
        st.write("Crown Choclate Sauce: 130")
        st.write("Multiple Multicolor Gems: 150")
        st.write("Mr. Kool Chocospread Chocolate: 260")
        st.write("Blossom Dark Chocolate Spread: 351")
        
    col4,col5,col6=st.columns(3)

    with col4:
        st.subheader("Grains")
        st.write("")
        st.write("Wheat Flour: 27")
        st.write("India Gate Classic Basmati Rice: 210")
        st.write("Daawat Basmati Rice - Brown: 165")
        st.write("Organic - Besan: 140")
        st.write("bb Royal Black Pepper: 1000")
        st.write("Chicken Fillets: 260")
        st.write("White Steel Cut Oats: 75")
        st.write("Natural White Rolled Oats: 95")
        st.write("Rolled Jumbo Oats: 120")

    with col5:
        st.subheader("Household")
        st.write("")
        st.write("Harpic Disinfectant Toilet Cleaner: 187")
        st.write("BB Home Disinfectant Bathroom Cleaner: 195")
        st.write("Vim Anti Bac Dishwashing Liquid: 365")
        st.write("Nimyle Herbal Floor Cleaner: 126")
        st.write("Colin Glass & Surface Cleaner: 140")

    with col6:
        st.subheader("Beverages")
        st.write("")
        st.write("Coca Cola: 40")
        st.write("Mirinda: 38")
        st.write("Pepsi: 38")
        st.write("Sprite: 40")
        st.write("Limca: 37")
        st.write("7 Up: 38")
        st.write("Mountain Dew: 41")
        st.write("Appy: 55")
        st.write("Fanta: 40")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    options = st.multiselect(
        'Choose your products please',
        [i for i in elements]
        )
    for j in options:
        if j not in st.session_state:
            st.session_state[j] = j

    



    if st.button('Confrim order'):
        if 'cart_done' not in st.session_state:
            st.session_state['cart_done'] = True

     
        

if sidebar =='My Cart' and st.session_state['cart_done']:

    st.title("Your Cart")
    col1,col2, col3=st.columns(3)

    with col1:
        st.header("Cart items")
        st.write("")
        
        for i in st.session_state:
            if i in elements:
                st.subheader(i)
                st.write("")
                st.write("")
                st.write("")


    with col2:
        st.header("Price")
        st.write("")
        
        for i in st.session_state:
            if i in elements:
                st.subheader(elements[i])
                st.write("")
                st.write("")
                st.write("")

    
    with col3:
        st.header("Quantity")
        quant = []
        for i in st.session_state:
            quant.append(st.number_input("",min_value=0, max_value=15,key=i))
            del st.session_state[i]
            if i not in st.session_state:
                st.session_state[i]={i:quant.pop()}

        st.write("")
        st.write("")
        st.write("")
        st.write("")    
    
    if st.button("Checkout"):
        if 'checkout' in st.session_state:
            st.session_state['checkout'] = True



elif sidebar == 'My Cart':
    st.write("Please fill in a cart")
    st.write("Refresh the page")

else:
    pass

if sidebar == 'Billing':
    col1,col2 = st.columns(2)
    bill =0
    for i in st.session_state:
        
        if i in elements:
            bill+= (st.session_state[i][i]*elements[i])
    if bill <=1000:
        st.write("Sorry your order was below 1000")
    else:
        with col1:
            st.write("Total bill")
            st.write("items cost")
            st.write("GST (18%)")
            st.write("sales tax")
            st.write("")
            st.write("")
            st.write("")
            st.write("Total")
        with col2:
            st.write(" ")
            st.write("")
            st.write(bill)
            st.write(18*bill/100)
            st.write(5*bill/100)
            st.write("")
            st.write("")
            st.write("")
            st.write(bill+(18*bill/100)+(5*bill/100))
    if st.button("Proceed"):
        if 'Proceed' in st.session_state:
            st.session_state['Proceed'] = True
    



                    




