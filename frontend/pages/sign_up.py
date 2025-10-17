from nicegui.ui import page, label, column, image, button, row, card

@page(path = '/sign_up')
def sign_up_page():
          
    skillverse_button = button(text = 'SkillVerse')
    skillverse_button.props('flat text-color=white').style('text-transform: none; font-family: Times New Roman; font-size: 30px')
        
    with column(align_items = 'center').style('align-self: center'):
        
        label(text = 'Create a new account').style('font-size: 26px; font-family: Times New Roman')
        
        label(text = 'Choose the right account type for you').style('font-size: 24px; font-family: Times New Roman')
       
    ### Big Screen ### 
    with row(align_items = 'center').style('align-self: center').classes('max-sm:hidden'):
        
        with card(align_items = 'center').style('width: 300px; height: 300px'):
            
            label(text = 'Candidate account').style('font-size: 22px; font-family: Times New Roman')
            
            image(source = r'images\job_hunt.png').style('width: 150px; height: 150px')
            
            candidate_account_button = button(text = 'I want to get hired')
            candidate_account_button.props('text-color=black color=white').style('text-transform: none; font-family: Times New Roman; font-size: 16px; font-weight: bold')

        with card(align_items = 'center').style('width: 300px; height: 300px'):
            
            label(text = 'Company Account').style('font-size: 22px; font-family: Times New Roman')
            
            image(source = r'images\job_offers.png').style('width: 150px; height: 150px')
            
            company_account_button = button(text = 'I want to hire')
            company_account_button.props('text-color=black color=white').style('text-transform: none; font-family: Times New Roman; font-size: 16px; font-weight: bold; width: 150px')
    
    ### Small Screen ###        
    with column(align_items = 'center').style('align-self: center').classes('sm:hidden'):

        with card(align_items = 'center').style('min-width: 350px'):
            
            label(text = 'Candidate account').style('font-size: 22px; font-family: Times New Roman')
            
            image(source = r'images\job_hunt.png').style('width: 150px; height: 150px')
            
            candidate_account_button = button(text = 'I want to get hired')
            candidate_account_button.props('text-color=black color=white').style('text-transform: none; font-family: Times New Roman; font-size: 16px; font-weight: bold')

        with card(align_items = 'center').style('min-width: 350px'):
            
            label(text = 'Company Account').style('font-size: 22px; font-family: Times New Roman')
            
            image(source = r'images\job_offers.png').style('width: 150px; height: 150px')
            
            company_account_button = button(text = 'I want to hire')
            company_account_button.props('text-color=black color=white').style('text-transform: none; font-family: Times New Roman; font-size: 16px; font-weight: bold; width: 150px')