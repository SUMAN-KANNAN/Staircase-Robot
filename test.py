from pathlib import Path
import os 

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__name__).resolve().parent.parent
# BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
# TEMPLATE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('templates')))
# print(TEMPLATE_DIR)

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')  # Assuming 'templates' directory is located inside BASE_DIR

# Define the static directory path
STATIC_DIR = os.path.join(BASE_DIR, 'carcontrol','static')
print(STATIC_DIR)
