import requests
import time
import os
import sys
import urllib3

# Technical Debt 1: Disable SSL warnings globally (security risk)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Technical Debt 2: Global variables scattered throughout
global_url = "https://www.kapook.com"
global_timeout = 30
global_headers = {"User-Agent": "Mozilla/5.0"}
global_response = None
global_status_code = 0

# Technical Debt 3: Hardcoded values and magic numbers
def make_request():
    # Technical Debt 4: No proper error handling, just try-except with bare except
    try:
        # Technical Debt 5: Using requests without session (inefficient for multiple requests)
        response = requests.get(
            global_url, 
            headers=global_headers, 
            timeout=global_timeout,
            verify=False  # Technical Debt 6: Disable SSL verification
        )
        
        # Technical Debt 7: Global variable mutation
        global global_response, global_status_code
        global_response = response
        global_status_code = response.status_code
        
        # Technical Debt 8: Inefficient string concatenation in loop
        result = ""
        for i in range(len(response.text)):
            result = result + response.text[i]
        
        return result
        
    except:
        # Technical Debt 9: Bare except clause, no specific error handling
        print("Error happened")
        return None

# Technical Debt 10: Function with side effects and no return type hints
def process_response():
    if global_response is None:
        print("No response available")
        return
    
    # Technical Debt 11: Inconsistent variable naming
    content = global_response.text
    status = global_status_code
    
    # Technical Debt 12: Hardcoded print statements instead of logging
    print("Status Code: " + str(status))
    print("Content Length: " + str(len(content)))
    
    # Technical Debt 13: Inefficient string operations
    if len(content) > 100:
        # Technical Debt 14: Magic number and inefficient slicing
        display_content = content[0:100] + "..."
    else:
        display_content = content
    
    # Technical Debt 15: No encoding handling
    print("Content Preview:")
    print(display_content)

# Technical Debt 16: Main execution without proper main guard
print("Starting request to kapook.com...")

# Technical Debt 17: No input validation or configuration
result = make_request()

# Technical Debt 18: Inconsistent spacing and formatting
if result != None:
    process_response()
else:
    print("Failed to get response")

# Technical Debt 19: Unused imports and variables
unused_var = "this is never used"
time.sleep(0)  # Technical Debt 20: Unnecessary sleep

print("Request completed.")xxxxxx
