import os
from dotenv import load_dotenv
from bardapi import Bard
load_dotenv()
os.environ['_BARD_API_KEY'] = os.getenv("BARD_API_KEY")
bard = Bard()
print('\n','*'*50,'Terminal Chat with BARD','*'*50, '\n')
try:
    while True:
        user_input = input('\U0001F464 You: ')
        print('')
        print('\U0001F916 Bard:', bard.get_answer(user_input.strip())['content'])
        print('-'*100, "\n")
except KeyboardInterrupt:
    print('Ended Chat!')
except:
    print('Ended Chat!')

