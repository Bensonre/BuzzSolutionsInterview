# BuzzSolutionsInterview
A simple rest API gateway with a Python lambda function sitting behind it that talks to an no-sql Dyanmo DB database Table with unstructured data repersenting resumes.

The following info is required for posts

## Test It
Currently running at https://mfi4hzvye4.execute-api.us-east-1.amazonaws.com/BuzzSolutionsInterview/Resume with an API key required.
I have created one public key for Interviewer use: `PLujDP8faG93WdJcNlX1h63blWcLPDG73sHtlpCM`.
curls:
Read All
`
curl --location 'https://mfi4hzvye4.execute-api.us-east-1.amazonaws.com/BuzzSolutionsInterview/Resume' \
--header 'x-api-key: PLujDP8faG93WdJcNlX1h63blWcLPDG73sHtlpCM'
`
Read 1
`
curl --location 'https://mfi4hzvye4.execute-api.us-east-1.amazonaws.com/BuzzSolutionsInterview/Resume/1' \
--header 'x-api-key: PLujDP8faG93WdJcNlX1h63blWcLPDG73sHtlpCM'
`
Create
`
curl --location 'https://mfi4hzvye4.execute-api.us-east-1.amazonaws.com/BuzzSolutionsInterview/Resume/' \
--header 'Content-Type: application/json' \
--header 'x-api-key: PLujDP8faG93WdJcNlX1h63blWcLPDG73sHtlpCM' \
--data '{
    "Role": {
        "S": "Jedi"
    },
    "Elevator Pitch": {
        "S": "Trained the chosen one"
    },
    "Experiance": {
        "M": {
            "Role and Responsibilities": {
                "M": {
                    "Jedi": {
                        "S": "Trained the Chosen One, General in the clone wars."
                    },
                    "Padawan": {
                        "S": "Trained under Quicon Gin"
                    }
                }
            },
            "Title": {
                "S": "Jedi and War General"
            },
            "Company": {
                "S": "Jedi Order"
            },
            "Durration": {
                "S": "A long time ago"
            }
        }
    },
    "FullName": {
        "S": "General Kenobi"
    }
}'
`
Update
`
curl --location 'https://mfi4hzvye4.execute-api.us-east-1.amazonaws.com/BuzzSolutionsInterview/Resume/5' \
--header 'Content-Type: application/json' \
--header 'x-api-key: PLujDP8faG93WdJcNlX1h63blWcLPDG73sHtlpCM' \
--data '{
    "Role": {
        "S": "Martial Artist"
    },
    "Elevator Pitch": {
        "S": "Savior of the world, OG goat"
    },
    "Experiance": {
        "M": {
            "Role and Responsibilities": {
                "M": {
                    "Sayain": {
                        "S": "Super powered Alien race."
                    },
                    "Super Sayain": {
                        "S": "Over Powered Alien race."
                    }
                }
            },
            "Title": {
                "S": "Martial Artist"
            },
            "Company": {
                "S": "Turtle School of Martial Arts"
            },
            "Durration": {
                "S": "1990-Present"
            }
        }
    },
    "FullName": {
        "S": "Son Goku"
    }
}'
`
Delete
`
curl --location --request DELETE 'https://mfi4hzvye4.execute-api.us-east-1.amazonaws.com/BuzzSolutionsInterview/Resume/5' \
--header 'x-api-key: PLujDP8faG93WdJcNlX1h63blWcLPDG73sHtlpCM'
`


## Credit 
This is built using the existing python API Library https://github.com/vincentsarago/lambda-proxy/ that works similiar to Flask but dedicated to AWS API Gateways with lambda integration.
