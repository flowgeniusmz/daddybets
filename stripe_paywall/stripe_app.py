import streamlit as st
import stripe

def create_checkout_session():
    session = stripe.checkout.Session.create(
        api_key = st.secrets.stripe_api_key_test,
        line_items=[{"price": 'price_1OtiMoDvYq7iSz1pPiR80fVV', "quantity": 1}],
        mode="payment",
        ui_mode="hosted",
        success_url="https://dev.daddybetsgpt.com/return.html?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="https://dev.daddybetsgpt.com/"
    )
    
    st.session_state.stripe_session = session
    ss.update_sessionstate_checkout_creation(varCheckoutSessionId=session.id, varCheckoutSessionURL=session.url)
    print(session)
    return session
