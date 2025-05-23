def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "Result:- You did not provide anything"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result:-{formated_f_name} {formated_l_name}"
print(format_name(input("Enter Your First Name:-\n"),input("Enter your Last Name:-\n")))