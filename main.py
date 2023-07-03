import os
import openai
from openai import CompletionRequest, OpenAiServce

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


def is_spam(msg: str) -> bool:
	completion_request = CompletionRequest.builder().prompt(msg + "\n--\nLabel:\n").maxTokens(4).n(1).model("ada:ft-x x-1.15.0").echo(False).build()
	service = OpenAiServce(OPENAI_API_KEY)
	choices = service.create_completion(completion_request).getChoices()
	if choices is not None and len(choices) > 0:
		return choices[0].getText().startswith("spam")
	return False

def is_spam_2(msg: str) -> bool:
	completion = openai.Completion.create(
		model="FINE_TUNE_MODEL_ID",
		prompt=msg + "\n--\nLabel:\n",
		max_tokens=4,
		n=1,
		echo=False,
	)

	if completion is not None and len(completion.choices) > 0:
		return completion.choices[0].text.startswith("spam")
	return False


if "__name__" == "__main__":
	while True:
		msg = input("Enter message: ")
		if is_spam(msg):
			print("Spam")
		else:
			print("Not Spam")