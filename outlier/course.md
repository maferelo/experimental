# Outlier Scale AI tasks

## Writer/Attempter

1. Prompt

### Clarity of intent

"In Python, how would you use the threading module to concurrently run three functions, 'task1()', 'task2()', and 'task3()', and ensure that the main program waits for all these tasks to complete before continuing execution."

### Contextual Grounding

"How would the output differ if depth-first search was used instead?"

### Specificity

"What measures can I take to ensure my function is thread safe?"

### Feasability

"What is a popular example of a dynamic programming algorithm?"

### Complexity

"Evaluate the positive and negative effects of database sharding on scaling a micro-service."

### Spelling & Grammar

"Implement a user class that is initialized with first name, last name, email, and password values."

### Safety

"How can technology be used to enhance public safety without infringing on privacy?"

1. Evaluate

Evaluation is between 1 and 8. 1, response 1 is better than 2 and 2, reponse 2 is better than 1

1. Identify Deviations

Look for responses 1, 2, 7 or 8.

a. Reasoning & Quality
a. Style & Formatting: Does the AI's solution adhere to proper styling and formatting guidelines? Does it convey the point concisely without excess fluff? 
a. Functionality & Performance: Does the AI's solution compile and run, and is it efficient? Does the code compile, run and generate the expected results or outputs?
a. Relevance & Completeness
a. Trust & Safety: Is the AI steering clear of sensitive or inappropriate content?
a. Security: Does the AI's solution expose security vulnerabilities?

if one of the model responses still excels in other dimensions/areas (e.g., formatting, explanation, markdown), it still counts as a deviation.

## Rater/Reviewer

### Justification

a. Conclusion: The overall claim that the justification makes as to which response is better
a. Supporting Claims: The key supporting points that the justification makes to defend its conclusion.
a. Specific Evidence: The precise examples or evidence in the text used to support each supporting point.
a. Analysis: The explanation(s) of how the evidence for each response defends the supporting claim

#### Examples of good justifications

“Response 1 is better since the code in Response 2 crashes due to type errors and unhandled promise rejections. Functionality & Performance: Response 2, on line 3, tries to extract `sentenceToWords` and `getDefinitions` which do not exist within the word-definition package. The code crashes on lines 15 & 16, producing type errors since `sentenceToWords` and `getDefinitions` are not functions. On the other hand, Response 1 does not crash since it attempts to get the word definitions within a try-catch block from lines 27 to 32.”

“Response 1 is better than response 2 - Functionality and Performance: After installing the necessary libraries (python and system libraries), response 1 compiles perfectly. It saves an image with transcribed information to the same local path. The associated IDE environment does not allow the code to run due to specified system needs (such as the installation of FFmpeg and a specific font). On the other hand, response 2's code fails to execute because line 11 includes an invalid argument error. Response 1 is functional, and this turn presents a straightforward deviation.”

“Response 2 is better than Response 1 because its code executes without error, and Response 2 provides meaningful code documentation. Functionality & Performance: Response 1 throws a `TypeError` in its `get_available_units`, `get_available_units_by_floor`, and `get_available_units_by_price` functions because it misunderstands its `buildings` data dictionary and uses dictionaries as list indices instead of integers or slices. In contrast, Response 2 executes without error. Reasoning Quality: Response 2 provides meaningful docstrings in its code functions, which improves understanding of how the code functions. In contrast, Response 1 only provides two categorical comments.”

"Response 1 is better than Response 2 in terms of Functionality & Performance. Response 2's code does not compile and will throw an error on line 21. This is because line 10 is not properly formatted in datetime format, so `dt()` will not work properly. Additionally, the list of zoos provided by Response 2 is also subpar compared to Response 1 because Response 2's list of zoos is just city names such as 'San Diego' and 'Tokyo' and is not realistic.”

## After completing task

https://app.outlier.ai/en/expert/course?id=662077f6d2a29b678d34b368

Key video points:

Leave a comment on the prompt in which turn's prompt was low quality, copied, or the wrong model was selected.
Properly mark the task (in the questions) that the prompt was low quality/copied or the wrong model response was selected.
The following prompts can be marked any way you want -- however these will have to be redone anyways.


IF YOU PLAN ON REJECTING A TASK AND SENDING IT BACK (SBQ) THERE ARE ONLY 4 WAYS TO DO SO:

You grade/mark any PROMPT in the conversation as <= 2 (low complexity or low originality). 
You mark that instructions were not followed. 
You mark the prompt was copied off the internet for any turn.
You mark that the wrong response was selected for any turn in the conversation.


Safety: Does the response include sensitive or inappropriate content? 
The model should rarely generate responses that have trust and safety concerns unless you ask them safety related prompts, which is not encouraged by the project. However, if such responses do arise, please clearly indicate the reasons for concern.  
If one does and the other one does not, a more extreme score (1, 2, 7, 8) should be chosen
Instruction Following: Does the response follow the prompt and address all aspects/requirements of the prompt? 
If yes, call out that the response follows the prompt and provide the detail
If not, call out the parts where the model fails to follow the prompt
If one does and the other one does not, a more extreme score (1, 2, 7, 8) should be chosen
Correctness: Does the code compile and run without errors and exceptions? 
If yes, call out that you have run the code (and the test input, if applicable), and the model doesn’t crash or throw exceptions. 
If not, call out under what circumstances would an error or exception occur, and describe the error or exception. Bonus point if you can include how to fix the issue. 
If one does and one does not, you don’t necessarily have to choose a more extreme score (1, 2, 7, 8). For example, if one compiles and runs without errors and exceptions but has bugs in the output, it is not necessarily better than the other one that doesn’t compile. 
Output: Does the code compile and run and generate the expected results or outputs? 
If yes / no, call out how you set up the environment, test the program, the test cases you used, the result you are expecting, and if the output is the same as your expectation. Bonus point if you can include how to fix the issue. 
If one does and the other one does not, a more extreme score (1, 2, 7, 8) should be chosen
Security: Does the code expose security vulnerabilities such as not validating API request input?  
If yes, call out how it exposes security vulnerabilities. Bonus point if you can include how to fix the issue. 
If one does and the other one does not, a more extreme score (1, 2, 7, 8) should be chosen
Truthfulness: Is all the non-code explanation factual and truthful? 
If not, call out which part is not factual and truthful 
If one does and the other one does not, a more extreme score (1, 2, 7, 8) should be chosen
Helpfulness: Is all the non-code explanations helpful ? 
If not, call out which part is more helpful than the other one 
If one does and the other one does not, a more extreme score (1, 2, 7, 8) should be chosen
Reasoning: Are the model’s explanations for why they came up with their solution fully justified? 
If not, call out why the explanation is not fully justified or why one explanation is better than the other
If one does and the other one does not, a more extreme score (1, 2, 7, 8) should be chosen
Style: Does the model’s response adhere to proper styling and formatting guidelines? Does it convey the point concisely without excess fluff?
If not, call out which part the response doesn’t follow the styling and formatting guidelines
If one does and the other one does not, you don’t necessarily have to choose a more extreme score (1, 2, 7, 8), because styling and formatting are sometimes subjective, unless one is clearly malformed 


Reasoning Quality: 📝 Are the AI’s explanations for why they came up with their solution fully justified?


Style and Formatting: 🌟 Does the AI's solution adhere to proper styling and formatting guidelines? Does it convey the point concisely without excess fluff? 


Functionality and Performance: 💻 Does the AI's solution compile and run, and is it efficient? Does the code compile, run and generate the expected results or outputs?


Relevance and Completeness: 🎯 Does the AI's solution follow the prompt and instruction and address all aspects/requirements of the prompt?


Trust and Safety: 🛡️ Is the AI steering clear of sensitive or inappropriate content?


Security: 🔒 Does the AI's solution expose security vulnerabilities?