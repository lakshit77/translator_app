from django.shortcuts import render
from googletrans import Translator
from .models import TranslationLog

def text_translation_func(original_text, language_initial):
    translater = Translator()
    output = translater.translate(text=original_text, dest=language_initial).text
    model_dict = {
        "input_text": original_text,
        "output_text": output,
        "language_used": language_initial
    }
    TranslationLog.objects.create(**model_dict)
    return output

# Create your views here.
def translatorView(request):

    all_translation = TranslationLog.objects.all().order_by("-created_at")
    context = {}
    if request.method == "POST":
        original_text = request.POST['my_textarea']
        language_initial = request.POST['language_initial']
        output = text_translation_func(original_text, language_initial)
        context["output_text"] = output
        context["original_text"] = original_text

    context["all_translation"] = all_translation
    return render(request, "index.html", context)