from behave import when


@when('Click on the first product.')
def click_first_product(context):
    context.app.off_plan_page.click_first_product()

