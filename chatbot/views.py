from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = '' # put your api key here from https://platform.openai.com/account/api-keys
openai.api_key = openai_api_key


def ask_openai(message):
    respose = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
