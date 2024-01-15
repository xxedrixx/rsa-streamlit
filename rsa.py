import streamlit as st  
import math  
from streamlit_option_menu import option_menu
import ast

selected = option_menu(
    menu_title=None,
    options=["Encryption","Cracking"],
    icons=["lock","key"],
    orientation="horizontal"
)

st.title("RSA Encryption")  
with st.sidebar:
    st.title("Info")

def prime(num):  
    if num < 2:  
        return False  
    for i in range(2, int(math.sqrt(num)) + 1):  
        if num % i == 0:  
            return False  
    return True  

# function to encrypt the message 
def encryption(): 
    for char in to_ascii: 
        encr = (char**r) % n 
        encrypted.append(encr) 
    st.info (f"Encrypted ASCII:  \n :orange[{encrypted}]") 

# function to decrypt the message 
def decryption(): 
    for char in encrypted: 
        decr = (char**s) % n 
        decrypted.append(decr) 
    st.info (f"Decrypted ASCII:  \n :orange[{decrypted}]") 

if selected == "Encryption":
    p = st.number_input('Enter p',min_value=0, max_value=4999)  
    if prime(int (p)):  
        st.write('p is ', p) 
        with st.sidebar:
            st.write("p =",p)
        q = st.number_input('Enter q',min_value=0, max_value=4999) 
        n = p*q  
        L = math.lcm(p-1,q-1) 

        if prime(int (q)):  
            st.write('q is ', q)
            with st.sidebar:
                st.write("q =",q)
                st.write("n = p*q  \n n =",n)
                st.write("L = lcm(p-1)(q-1)  \n L =", L )
            
            
            r = st.number_input('Enter r',min_value=0, max_value=4999)  
        
            if (math.gcd(r,L)) == 1:  
                s = pow (r, -1, L)  

                st.write('r is ', r)
                with st.sidebar:               
                    st.write("r =",r)
                    st.write("r*s [n] = 1   \ns =",s)

                message = st.text_area('Enter the message', '')  

                to_ascii = [ord(char) for char in message]  # convert every character to ascii  

                if message:
                    st.info (f"**:red[{message}]** to ascii:  \n :orange[{to_ascii}]")  


                    encrypted = [] 
                    decrypted = [] 
                    
                    #encrypt
                    encryption() 

                    #decrypt
                    decryption() 

                    to_string = ''.join(chr(value) for value in decrypted) # convert every ascii to character 

                    st.success(f"Decrypted message:  \n **:red[{to_string}]**") 

            else: 
                st.error(f"{r} and {L} are NOT coprime")  

        else: 
            st.error(f"{q} is NOT a prime number")  
    else: 
        st.error(f"{p} is NOT a prime number")    

else:
    n = st.number_input('Enter n',min_value=0) 
    

    def find_p_and_q(n):
        for i in range(math.isqrt(n) + 1):
            if prime(i) and n % i == 0:
                p = i
                q = n // i
                return p, q

    try:    
        p, q= find_p_and_q(n)
        with st.sidebar:
            st.write("p =",p)
            st.write("q =",q)
        try:
            r = st.number_input('Enter r',min_value=0, max_value=4999)
            L = math.lcm(p-1,q-1)
            s = pow (r, -1, L) 
            with st.sidebar:
                st.write("r =",r)
                st.write("L =",L)
                st.write("s =",s)

            input_ascii = st.text_area("Enter encrypted message", '')
            decrypted = []
            if input_ascii:
                if '[' in input_ascii and ']' in input_ascii:
                    encrypted = ast.literal_eval(input_ascii)
                else:
                    encrypted = [int(char) for char in input_ascii.split(',')]
                #decrypt
                decryption()
                to_string = ''.join(chr(value) for value in decrypted) # convert every ascii to character 

                st.success(f"Decrypted message:  \n **:red[{to_string}]**")
        except ValueError as ve:
            st.error(f"ValueError: {ve}")
        
                 
    except TypeError as e:
        st.error(f"TypeError: {e}")