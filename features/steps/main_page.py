from behave import given, when


@given('Open the main page.')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click on “off plan” at the left side menu.')
def click_off_plan_menu(context):
    context.app.main_page.click_off_plan_menu()


@when('Click on “off plan” in the bottom menu.')
def click_off_plan_menu_mobile(context):
    context.app.main_page.click_off_plan_menu_mobile()
