from nicegui.ui import page, button, label, card, row, input, column, add_head_html, link, icon, image, select, separator

@page(path = '/sign_up/company')
def sign_up_company_page():
    
    add_head_html('<link rel="stylesheet" href="/css/sign_up_company.css">')
     
    skillverse_button = button(text = 'SkillVerse')
    skillverse_button.props('flat text-color=white').style('text-transform: none; font-family: Times New Roman; font-size: 30px')
        
    ### Big Screen ###
    with card(align_items = 'center').style('align-self: center').classes('max-sm:hidden'):
        
        with column():
            
            label(text = 'Crate a new account').style('font-size: 24px; font-family: Times New Roman')
            
        
        with row():
            
            image('icons/clarify.svg').style('width: 30px; height: 30px')
            
            label(text = 'Company Details').style('font-size: 20px; font-family: Times New Roman')
            
        with row().style('width: 100%'):
            
            select(options = ['RO'], value = 'RO').props('outlined')
            
            input(label = 'VAT Number (CUI/CRN)').props('outlined').style('flex: 1')
            
        input(label = 'Trade Registration Number').props('outlined').style('width: 100%')
        
        input(label = 'Company Name').props('outlined').style('width: 100%')
        
        separator()
        
        with row():
            
            icon(name = 'location_on', size = '30px')
            
            label(text = 'Social seat address').props('outlined').style('font-size: 20px; font-family: Times New Roman')
        
        input(label = 'Street, number ...').props('outlined').style('width: 100%')
        
        with row().style('width: 100%'):
            
            input(label = 'City').props('outlined').style('flex: 1')
            
            select(label = 'Country', options = []).props('outlined').style('flex: 1')
            
        separator()
        
        with row():
            
            icon(name = 'badge', size = '30px')
            
            label(text = 'Login credentials').style('font-size: 20px; font-family: Times New Roman')
        
        input(label = 'Username').props('outlined').style('width: 100%')
        
        input(label = 'Password', password = True, password_toggle_button = True).props('outlined').style('width: 100%')
        
        button(text = 'Sign Up').props('text-color=black color=white').style('text-transform: none; font-family: Times New Roman; font-size: 16px; font-weight: bold; width: 150px')
        
        link(text = 'Already have an account ? Log in to your account !').style('font-size: 20px; font-family: Times New Roman; text-decoration: none; color: white')
        
    ### Small Screen ###
    with card(align_items = 'center').style('align-self: center').classes('sm:hidden'):
        
        with column():
            
            label(text = 'Crate a new account').style('font-size: 24px; font-family: Times New Roman')
            
        
        with row():
            
            image('icons/clarify.svg').style('width: 30px; height: 30px')
            
            label(text = 'Company Details').style('font-size: 20px; font-family: Times New Roman')
            
        with row().style('width: 100%'):
            
            select(options = ['RO'], value = 'RO').props('outlined').style('flex: 1')
            
            input(label = 'VAT Number (CUI/CRN)').props('outlined').style('flex: 1')
            
        input(label = 'Trade Registration Number').props('outlined').style('width: 100%')
        
        input(label = 'Company Name').props('outlined').style('width: 100%')
        
        separator()
        
        with row():
            
            icon(name = 'location_on', size = '30px')
            
            label(text = 'Social seat address').props('outlined').style('font-size: 20px; font-family: Times New Roman')
        
        input(label = 'Street, number ...').props('outlined').style('width: 100%')
        
        with row().style('width: 100%'):
            
            input(label = 'City').props('outlined').style('flex: 1')
            
            select(label = 'Country', options = []).props('outlined').style('flex: 1')
            
        separator()
        
        with row():
            
            icon(name = 'badge', size = '30px')
            
            label(text = 'Login credentials').style('font-size: 20px; font-family: Times New Roman')
        
        input(label = 'Username').props('outlined').style('width: 100%')
        
        input(label = 'Password', password = True, password_toggle_button = True).props('outlined').style('width: 100%')
        
        button(text = 'Sign Up').props('text-color=black color=white').style('text-transform: none; font-family: Times New Roman; font-size: 16px; font-weight: bold; width: 150px')
        
        link(text = 'Already have an account ?').style('font-size: 20px; font-family: Times New Roman; text-decoration: none; color: white')
            
        link(text = 'Log in to your account !').style('font-size: 20px; font-family: Times New Roman; text-decoration: none; color: white')