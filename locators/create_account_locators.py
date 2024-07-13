class CreateAccountLocators:
    field_name_page = "//span[text()='Create New Customer Account']"

    input_email = "//input[@id='email_address']"
    error_email = "#email_address-error"

    button_create = "//button[@class='action submit primary']"

    input_password = "#password"
    error_password = "#password-error"