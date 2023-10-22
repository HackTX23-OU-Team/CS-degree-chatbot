prompt = """Instructions for Training GPT-5 on Recognizing and Rendering College Course Information

Introduction:
We are training GPT-5 to understand and properly format user inputs related to college courses. The goal is to extract key information such as course codes, course names, credit hours, and other relevant details, and then render this information in a structured format.

1. Dataset Collection:
   a. The training dataset should include a variety of user inputs related to college courses, such as:
      - Questions about specific courses.
      - Requests for course recommendations.
      - Inquiries about course prerequisites.
      - Queries regarding course credits and descriptions.

   b. Include a diverse set of course codes and names from different departments, universities, and programs. You can use data from different institutions to ensure a wide coverage.

2. Annotate the Dataset:
   a. Annotate the dataset with structured information, such as:
      - Course code (e.g., "C S 2334").
      - Course name (e.g., "Programming Structures and Abstractions").
      - Credit hours (e.g., "4").
      - User intent (e.g., "Request for course information").

3. Training Prompt:
   a. Use the following prompt to train GPT-5 for this task:

      "Given a user input related to college courses, extract and render the relevant course information. The user input may include course code, course name, and any other relevant details. Your response should be in the following format:

      - Course Code: [Course Code]
      - Course Name: [Course Name]
      - Credit Hours: [Credit Hours]

      For example, if the user input is 'Can you tell me about C S 2334?' your response should be:
      - Course Code: C S 2334
      - Course Name: Programming Structures and Abstractions
      - Credit Hours: 4"

4. Fine-tuning GPT-5:
   a. Use the training data and the provided prompt to fine-tune GPT-5. Make sure to use a suitable fine-tuning method and specify the number of training steps.

5. Testing and Validation:
   a. After fine-tuning, test GPT-5 with a wide range of user inputs related to college courses. Ensure it can accurately recognize and render course information.

6. Deployment:
   a. Once GPT-5 is successfully fine-tuned and tested, deploy it for use in applications like the chatbot provided in previous code examples.

7. Monitoring and Refinement:
   a. Continuously monitor the performance of GPT-5 and refine its training if needed to improve accuracy.

8. Privacy and Security:
   a. Ensure that user data privacy and security are maintained throughout the training and deployment of GPT-5.

By following these instructions, you will train GPT-5 to understand and format user inputs related to college courses, providing valuable information in a structured way. This can enhance the functionality of the chatbot and similar applications."""
