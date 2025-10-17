from nicegui.ui import page, button, label, card, row, input, column, add_head_html, link


@page(path = '/sign_up/candidate')
def sign_up_candidate_page():
    
    add_head_html('<link rel="stylesheet" href="/css/global.css">')
    
    skillverse_button = button(text = 'SkillVerse')
    skillverse_button.props('flat text-color=white').style('text-transform: none; font-family: Times New Roman; font-size: 30px')
    
    ### Big Screen ###
    with card(align_items = 'center').style('align-self: center').classes('max-sm:hidden'):
        
        label(text = 'Create your candidate account').style('font-size: 26px; font-family: Times New Roman')
        
        with column(align_items = 'center'):
            
            with row():
                
                input(label = 'First Name').props('outlined')
                
                input(label = 'Last Name').props('outlined')
                
            input(label = 'E-mail').props('outlined').style('width: 100%')
            
            input(label = 'Password', password = True, password_toggle_button = 'True').props('outlined').style('width: 100%')
            
            input(label = 'City of Residence').props('outlined').style('width: 100%')
            
            button(text = 'Sign Up').props('text-color=black color=white').style('text-transform: none; font-family: Times New Roman; font-size: 16px; font-weight: bold; width: 150px')
             
            link(text = 'Already have an account ? Log in to your account !').style('font-size: 20px; font-family: Times New Roman; text-decoration: none; color: white')
            
    ### Small Screen ###
    
    with card(align_items = 'center').style('align-self: center').classes('sm:hidden'):
        
        label(text = 'Create your candidate account').style('font-size: 26px; font-family: Times New Roman')
        
        with column(align_items = 'center'):
            
            input(label = 'First Name').props('outlined').style('width: 100%')
                
            input(label = 'Last Name').props('outlined').style('width: 100%')
                
            input(label = 'E-mail').props('outlined').style('width: 100%')
            
            input(label = 'Password', password = True, password_toggle_button = 'True').props('outlined').style('width: 100%')
            
            input(label = 'City of Residence').props('outlined').style('width: 100%')
            
            button(text = 'Sign Up').props('text-color=black color=white').style('text-transform: none; font-family: Times New Roman; font-size: 16px; font-weight: bold; width: 150px')
               
            link(text = 'Already have an account ?').style('font-size: 20px; font-family: Times New Roman; text-decoration: none; color: white')
            
            link(text = 'Log in to your account !').style('font-size: 20px; font-family: Times New Roman; text-decoration: none; color: white')
