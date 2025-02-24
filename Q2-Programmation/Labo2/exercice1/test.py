import os
import dotenv

dotenv.load_dotenv()

key = os.getenv('KEY')

print(key)
