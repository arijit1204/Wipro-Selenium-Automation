def before_scenario(context, scenario):
    context.application = None

def after_scenario(context, scenario):
    if context.application:
        context.application.stop()
