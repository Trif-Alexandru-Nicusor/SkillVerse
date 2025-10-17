from nicegui.ui import page, button, header, row, card, input, add_head_html, column, label, checkbox, expansion, element

@page(path='/home')
def home_page():
    
    add_head_html('<link rel="stylesheet" href="/css/home.css">')

    with header().classes('flex justify-between items-center px-4l').style('background-color: white'):
        
        button(text='SkillVerse').props('flat text-color=black').style('text-transform: none; font-size: 20px; font-family: Times New Roman')
        
        with row().style('gap: 10px;'):
            
            button(text='Log In', icon = 'login').props('flat text-color=black').style('text-transform: none; font-size: 20px; font-family: Times New Roman')
            button(text='Sign Up', icon = 'person_add').props('flat text-color=black').style('text-transform: none; font-size: 20px; font-family: Times New Roman')
    
        
    with column().style('align-self: center; width: 90%'):
        
        with row().style('align-self: center; width: 100%'):
            
            input(label = 'Key Words').props('outlined').style('flex: 1')
            
            input(label = 'City').props('outlined').style('flex: 1')
            
            button(text = 'Search for jobs', icon = 'search')
        
        with row().style('width: 100%'):
                            
            with column():
                
                with expansion(text = 'Filters', value = True).style('width: 250px; background-color: #444444'):
                    
                    pass
                                
                with expansion(text = 'Job Type', value = True).style('width: 250px; background-color: #444444'):
                                    
                    checkbox(text = 'Internship')
                    
                    checkbox(text = 'Part-time')
                    
                    checkbox(text = 'Full-time')
                    
                with expansion(text = 'Departments', value = True).style('width: 250px; background-color: #444444'):
                    
                    pass
                                
                with expansion(text = 'Level of Studies', value = True).style('width: 250px; background-color: #444444'):
                                    
                    checkbox(text = 'Unqualified')
                    
                    checkbox(text = 'Qualified')
                    
                    checkbox(text = 'Student')
                    
                    checkbox(text = 'Graduate')
                    
                with expansion(text = 'Career Level', value = True).style('width: 250px; background-color: #444444'):
                    
                    checkbox(text = 'No Experience')
                    
                    checkbox(text = 'Entry-Level (<2 years)')
                    
                    checkbox(text = 'Mid-Level (2-5 years)')
                    
                    checkbox(text = 'Senior-Level (>5 years)')
                    
                    checkbox(text = 'Manager/Executive')

            with element(tag = 'div').style('flex: 1; display: flex; justify-content: center;'):
                
                with card().style('width: 50%'):
                        
                    with row():
                            
                        label(text = 'Job Title + image')
                            
                    with row():
                            
                        label('Location: ')
                            
                        button(icon = 'favorite').props('flat text-color=wite')