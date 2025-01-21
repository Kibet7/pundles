# store/context_processors.py

def custom_variable_processor(request):
    return {
        'custom_variable': 'This is a custom variable',
    }