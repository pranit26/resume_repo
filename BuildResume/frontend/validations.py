from django.core.validators import validate_email



def data_validator(data):
    candidate_registration_error = 'Candidate registration failed.'
    skills=["python","java","ruby","docker","node","js"]
    if not data.get('name'):
        return False,f"{candidate_registration_error} Candidate name is required."   
    
    if not isinstance(data.get('name'),str):
        return False,f"{candidate_registration_error} Candidate name must be a string."
    
    if len(data.get('name'))>=250:
        return False, f"{candidate_registration_error} Candidate name must in upto 250 character."
    
    if not data.get('address'):
        return False, f"{candidate_registration_error} Address is required."
    
    if not isinstance(data.get('address'),str):
        return False,f"{candidate_registration_error} Address must be a string."
    
    if len(data.get('address'))>=250:
        return False, f"{candidate_registration_error} Address must in upto 250 character."
    
    if not data.get('contact_number'):
        return False,f"{candidate_registration_error} Contact number is required."
    
    if not isinstance(data.get('contact_number'),int):
        return False,f"{candidate_registration_error} Contact number must be a integer."
    
    if len(str(data.get('contact_number')))!=10:
        return False, f"{candidate_registration_error} Contact number must be upto 10 character."
    
    if not data.get('email'):
        return False,f"{candidate_registration_error} Email is required." 
    
    if not isinstance(data.get('email'),str):
        return False,f"{candidate_registration_error} Email must be a string."
    
    if len(data.get('email'))>=100:
        return False, f"{candidate_registration_error} Email must in upto 100 character."
    
    try:
        validate_email(data.get("email"))
    except Exception as e:
        return False, f"{candidate_registration_error} Please enter valid email address."
    
    if not data.get('location'):
        return False,f"{candidate_registration_error} Location is required." 
    
    if not isinstance(data.get('location'),str):
        return False,f"{candidate_registration_error} Location must be a string."
    
    if len(data.get('location'))>=100:
        return False, f"{candidate_registration_error} Location must in upto 100 character."
    
    if not data.get('tech_skills'):
        return False,f"{candidate_registration_error} Tech skills is required." 
    
    if not isinstance(data.get('tech_skills'),list):
        print(data.get('tech_skills'),type(data.get('tech_skills')))
        return False,f"{candidate_registration_error} Tech skills must be a string in list."
    
    if len(data.get('tech_skills'))>=250:
        return False, f"{candidate_registration_error} Tech skills must in upto 250 character."
    
    for skil in data.get('tech_skills'):
        if skil.lower() not in skills:
            return False,f"{candidate_registration_error} Tech skills must be a in python,java,ruby,docker,node,js."
               
    return True, "Validation successful." 



def validate_list(data):
    if data.get('showAll'):
        if not isinstance(data.get('showAll'), bool):
            return False, 'showAll field must be true or false.'

    if data.get('recordsPerPage'):
        if not isinstance(data.get('recordsPerPage'), int):
            if isinstance(data.get('recordsPerPage'), str):
                if data.get('recordsPerPage').isalpha():
                    return False, "recordsperpage field should only contain Numbers"

    if data.get('rowNumber'):
        if isinstance(data.get('rowNumber'), int):
            if data.get('rowNumber') < 1:
                return False, "rowNumber Should be greater than Zero"
        elif isinstance(data.get('rowNumber'), str):
            if data.get('rowNumber').isalpha():
                return False, "rowNumber field should only contain Numbers"
            if int(data.get('rowNumber')) < 1:
                return False, "rowNumber Should be greater than Zero"

    if data.get('sortOrder'):
        if not isinstance(data.get('sortOrder'), str):
            return False, 'sortOrder field must be string.'
        if data.get('sortOrder') != 'asc' and data.get('sortOrder') != 'desc':
            return False, 'sortOrder must be asc or desc only.'

    if data.get('sortBy'):
        if not isinstance(data.get('sortBy'), str):
            return False, "sortby field must be string"

    if data.get("search"):
        if not isinstance(data.get("search"), str):
            return False, "search field must be string"
    return True, 'Validation successful.'
      


    



    

    


    

 