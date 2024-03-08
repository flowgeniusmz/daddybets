# Daddy Bets

## Utils
- Utils contains functions that are not executed as part of the DaddyBets app
- Utils are utilities to be used by developers or testers to execute code - such as create a file id for openai

## All Other Directories and Modules
1. _**Root Directory Files**_
- **Home.py**: The initial and home page of the DaddyBets app
- **requirements.txt**: Contains the python packages that are already or will be installed
- **README.md**: This current page containing app details
- **.gitignore**: Contains the modules that exist in codespace but will not be officially pulled into main branch (i.e. .streamlit/secrets.toml)

2. _**Config**_
- **pagesetup.py**: Contains predefined page elements such as title, overview, page_links, and more to ensure consistency across the app
- **sessionstate.py**: Contains all session_state initialization functions - including initialize_all and individual functions grouping st.session_state variables together
- **style.css**: Contains custom styling information used in this app 

3. _**Connections**_
- **connection_supabase.py**: Creates a Supabase client using authorization information in st.secrets that can be used globally 
- **N/A**:  
- **N/A**: 

4. _**Data**_
- **message_log.csv**: Logs all OpenAI assistant chat messages including both user prompts and assistant responses - with additional metadata. Data from all sessions is contained here. NOTE: Each time the app is rebuilt, this file will be blank.
- **dk_regionlist.csv**:  Contains a list of all DraftKings regions and api metadata
- **dk_sportlist.csv**: Contains a list of all DraftKings sports and api metadata
- **dk_teamlist.csv**: Contains a list of all DraftKings teams and api metadata
- **users.csv**: Backup of Supabase users table containing login information for paid users.

5. _**Assets**_
- **terms_and_conditions.md**: Contains the Terms and Conditions presented when any user first comes to the app 
- **N/A**:  
- **N/A**: 

6. _**Form**_
- **form_betting.py**: Contains predefined page elements such as title, overview, page_links, and more to ensure consistency across the app
- **form_login.py**:  
- **from_terms.py**: 

7. _**Config**_
- **sessionstate.py**: 
- **sessionstate.py**:  
- **sessionstate.py**: 

8. _**Config**_
- **sessionstate.py**: 
- **sessionstate.py**:  
- **sessionstate.py**: 

9. _**Config**_
- **sessionstate.py**: 
- **sessionstate.py**:  
- **sessionstate.py**: 

10. _**Config**_
- **sessionstate.py**: 
- **sessionstate.py**:  
- **sessionstate.py**: 

11. _**Config**_
- **sessionstate.py**: 
- **sessionstate.py**:  
- **sessionstate.py**: 