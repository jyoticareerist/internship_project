from behave import then


@then('Verify the three options of visualization are “architecture”, “interior”, “lobby”')
def verify_visualization_options(context):
    context.app.product_details_page.verify_visualization_options()


@then('Verify the visualization options are clickable.')
def verify_visualization_clickable(context):
    context.app.product_details_page.verify_visualization_clickable()
