from openai import OpenAI
client = OpenAI(
     api_key = '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'
)

# exe 1
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{
#         "role": "system",
#         "content": "Write a one-sentence bedtime story about a unicorn."
#     }]
# )

# print(completion)

# exe 2
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{
#         "role": "system",
#         "content": "You are a helpful assistant."
#     },{
#           "role": "user",
#           "content": "Who is the owner of the meta?"
#     }]
# )

# print(completion)
# ChatCompletion(id='chatcmpl-BEzJmt3YkB3CRjOKwl7AxJQMclVEP', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Meta Platforms, Inc., formerly known as Facebook, Inc., is a publicly traded company and has various shareholders who own the company. Mark Zuckerberg is the founder and CEO of Meta Platforms, Inc.', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1742911998, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=40, prompt_tokens=25, total_tokens=65, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))


# exe 3
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{
#         "role": "system",
#         "content": "You are the CEO of meta company"
#     },
# #     {
# #           "role": "assistant",
# #           "content": "Mark Zuckerberg is the owner of the meta."
# #     },
#     {
#          "role": "user",
#           "content": "Where is located?"
#     }]
# )

# print(completion)
# ChatCompletion(id='chatcmpl-BEzNHKjRSOVUVHaJcAEvjEUg3AFAL', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="Meta's headquarters are located in Menlo Park, California, United States.", refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1742912215, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=16, prompt_tokens=34, total_tokens=50, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
# ChatCompletion(id='chatcmpl-BEzQ1wX45FWp8k92Lpp0YdbVidChg', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Meta company is headquartered in Silicon Valley, California, United States.', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1742912385, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=14, prompt_tokens=22, total_tokens=36, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))

# => temperature (0 to 2)

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     store=True,
#     messages=[{
#         "role": "system",
#         "content": "You are a helpful assistant."
#     },
#     {
#          "role": "user",
#           "content": "write 1 joke about the web developer."
#     }],
#     temperature= 1 # .5 (0 to 2)
# )
# print(completion.choices[0].message.content)
# ChatCompletion(id='chatcmpl-BEzUSAmLuCePL8E8eFLT1XHeXKXRI', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='1. Why was the web developer always calm? Because they knew how to handle stress(less) CSS!\n2. Why did the web developer go broke? Because they kept spending all their money on domain names!', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1742912660, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=44, prompt_tokens=26, total_tokens=70, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
# ChatCompletion(id='chatcmpl-BEzZbIDk2x9ggO5ey3rJ6x44Rhq4L', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='1. Why did the web developer go broke? Because he used up all his cache!\n2. How does a web developer fix a broken heart? By using JavaScript to console it!', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1742912979, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=38, prompt_tokens=26, total_tokens=64, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
# ChatCompletion(id='chatcmpl-BEzdf2cxGNiLLAHyyfLSgxmBzwMbg', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="Why did the web developer go broke?\nBecause he didn't know how to website his money!", refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1742913231, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=20, prompt_tokens=26, total_tokens=46, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
# ChatCompletion(id='chatcmpl-BEzlq6qsPb8gOCUKNc4IGbI0iA4rR', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Why did the web developer break up with the internet? \n\nBecause it had too many cookies!', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1742913738, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=20, prompt_tokens=26, total_tokens=46, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
# Why did the web developer stay up all night?

# Because he couldn't find the <body> to sleep!</body>
