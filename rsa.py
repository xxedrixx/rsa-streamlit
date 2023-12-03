import streamlit as st  
import math  

st.title("RSA Encryption")  

def prime(num):  
    if num < 2:  
        return False  
    for i in range(2, int(math.sqrt(num)) + 1):  
        if num % i == 0:  
            return False  
    return True  

p = st.number_input('Enter p',min_value=0,max_value=100)  
if prime(int (p)):  
    st.write('p is ', p) 
    q = st.number_input('Enter q',min_value=1,max_value=100)  
    if prime(int (q)):  
        st.write('q is ', q) 

        L = math.lcm(p-1,q-1)  

        r = st.number_input('Enter r',min_value=0,max_value=100)  

        st.write('r is ', r)  

        if (math.gcd(r,L)) == 1:  
            n = p*q  
            s = pow (r, -1, L)  

            message = st.text_input('Enter the message', '')  

            to_ascii = [ord(char) for char in message]  # convert every character to ascii  

            st.write (f"{message} to ascii: {to_ascii}")  


            encrypted = [] 
            decrypted = [] 
            # function to encrypt the message 
            def encryption(): 
                for char in to_ascii: 
                    encr = (char**r) % n 
                    encrypted.append(encr) 
                st.write (f"Encrypted ASCII: {encrypted}") 
            encryption() 

            # function to decrypt the message 
            def decryption(): 
                for char in encrypted: 
                    decr = (char**s) % n 
                    decrypted.append(decr) 
                st.write (f"Decrypted ASCII: {decrypted}") 
            decryption() 

            to_string = ''.join(chr(value) for value in decrypted) # convert every ascii to character 

            st.write(f"Decrypted message: {to_string}") 

        else: 
            st.error(f"{r} and {L} are NOT coprime")  

    else: 
        st.error(f"{q} is NOT a prime number")  
else: 
    st.error(f"{p} is NOT a prime number")  

 
 
 
 

 