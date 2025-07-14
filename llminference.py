import requests
import json
#
# import argparse
#
# parser = argparse.ArgumentParser(description="Accept a string as an argument")
# parser.add_argument("input_string", type=str, help="The string you want to pass")
# args = parser.parse_args()
#
# print("You entered:", args.input_string)
#


def llm_inference(text):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json",
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>",  # Optional. Site title for rankings on openrouter.ai.
        },
        data=json.dumps(
            {
                "model": "mistralai/ministral-3b",
                "messages": [
                    {
                        "role": "user",
                        "content": f"Summarize the following text in a paragraph.{text}",
                    },
                ],
            }
        ),
    )
    # print the response text for debugging purposes
    # print the response we got from the API
    return response.json()["choices"][0]["message"]["content"]
