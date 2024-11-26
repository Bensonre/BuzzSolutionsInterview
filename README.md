# BuzzSolutionsInterview
A simple rest API gateway with a Python lambda function sitting behind it that talks to an no-sql Dyanmo DB database Table with unstructured data repersenting resumes.

The following info is required for posts

# Test It
Currently running at https://mfi4hzvye4.execute-api.us-east-1.amazonaws.com/BuzzSolutionsInterview/Resume with an API key required.
I have created one public key for Interviewer use: `PLujDP8faG93WdJcNlX1h63blWcLPDG73sHtlpCM`.

## Credit 
This is built using the existing python API Library https://github.com/vincentsarago/lambda-proxy/ that works similiar to Flask but dedicated to AWS API Gateways with lambda integration.
