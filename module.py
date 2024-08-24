# def detail(**data):
#     for key, value in data.items():
#         print(key, '-->', value)
#
#
# detail(name='Tej', std='9', city='npj', language='nepali')

def profile(**data):
    for key, value in data.items():
        print(key,'--.', value)
        print(data['name'], data['email'])


profile(id='101', name="John", address='ktm', mob=98767676, email='john@gmail.com')
