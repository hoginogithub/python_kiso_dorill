class Greetings:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
         allowed = [
             'hello',
             'wake_up',
             'good_morning',
             'good_afternoon',
             'good_evening',
             'nice_to_meet_you',
             'good_night',
         ]

         def call(name=None):
             if attr in allowed:
                 greeting = attr.replace('_', ' ')
                 name = name or self.name
                 print(f'{greeting.capitalize()}, {name}')
             else:
                 msg = f'{name}, greeting: {attr}' 
                 raise ValueError(f'Invalid name or greeting. {msg}')

         return call

greeting = Greetings('Link')
greeting.wake_up()
greeting.hello(name='Princess')
greeting.nice_to_meet_you(name='Mister Bond')
greeting.hi()