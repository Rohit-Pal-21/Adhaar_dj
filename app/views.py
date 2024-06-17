# app/views.py
from django.shortcuts import render, redirect
from .models import AdhaarCardDetail
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from googletrans import Translator

from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def index_view(request):
    context = {
        "States":["Maharashtra","Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam",
                    "Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu",
                    "Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir",
                    "Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Pradesh","Manipur",
                    "Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu",
                    "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"
                ],
        
        "Gender": ["Male", "Female"],
        
        "Language": ["en","bn","hi","mr","ta","ur","gu","te",
            "kn","or","pa","ml"],
    }
    
    if request.method == 'POST':
        adhaar_no = request.POST.get('adhaar_no')
        profile_img = request.FILES.get('profile_img')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        father_name = request.POST.get('father_name')
        date_of_birth = request.POST.get('date_of_birth')
        house_no = request.POST.get('house_no')
        locality = request.POST.get('locality')
        post_office = request.POST.get('post_office')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        state = request.POST.get('state')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        local_gender = request.POST.get('local_gender')
        address_local = request.POST.get('address_local')
        fullname  =request.POST.get('fullname')
        local_fullname=request.POST.get("local_fullname")
        full_father_name_local=request.POST.get("full_father_name_local")
        so_do=request.POST.get("so_do")
        
        
        
        print(adhaar_no)
        
        def separate_string(input_string):
            # Remove any existing spaces
            input_string = input_string.replace(" ", "")
    
            # Insert spaces after every 4 characters
            separated_string = ' '.join([input_string[i:i+4] for i in range(0, len(input_string), 4)])
            return separated_string
        

        adhaarcard=AdhaarCardDetail.objects.create(adhaar_no=separate_string(adhaar_no),profile_img=profile_img,
                                        name=name,father_name=father_name,surname=surname,
                                        house_no=house_no,locality=locality,post_office=post_office,
                                        state=state,city=city,pincode=pincode,date_of_birth=date_of_birth,
                                        gender=gender,local_gender=local_gender,address=address,
                                        address_local=address_local,fullname=fullname,local_fullname=local_fullname,
                                        full_father_name_local=full_father_name_local, so_do=so_do )
        
        if isinstance(adhaarcard,AdhaarCardDetail):return redirect("/adhaar_card_list")

    return render(request, "adhaar_card_form.html", context=context)



from django.http import JsonResponse
from translate import Translator

def translate_function(request):
    if request.method == 'POST':
        data = request.POST
        language = data.get('Language')
        gender = data.get('gender')
        address = data.get('address')
        fullname = data.get('fullname')
        full_father_name_local = data.get('full_father_name_local')
        

        language_map = {"hi": "Hindi","en": "English","mr":"Marathi",
                        "bn":"Bengali","gu":"Gujarati","ta":"Tamil",
                        'ml':"Malayalam",'ur':'Urdu','or':'Oriya',
                        'pa':'Punjabi','te':'Telugu','kn':'Kannada'}
        
        for target_language, name in language_map.items():
            if language == target_language:
                global lang
                lang = name
                break
        # print(lang)
        # print(name)
        # print(target_language)

        # translator = Translator(to_lang=language)
        # local_gender = translator.translate(gender)
        # local_address = translator.translate(address)
        # local_fullname = translator.translate(fullname)
        # full_father_name_local = translator.translate(full_father_name_local)
        # local_language = translator.translate(lang) # needed for translating the  language itself
        
        tr = GoogleTranslator(source='en', target=target_language)
        local_gender = tr.translate(gender)
        local_address = tr.translate(address)
        local_fullname = tr.translate(fullname)
        full_father_name_local = tr.translate(full_father_name_local)
        local_language = tr.translate(lang) 
        
        print(local_language)
        

        return JsonResponse({
            'local_gender': local_gender,
            'local_address': local_address,
            'local_language': local_language,
            'local_fullname':local_fullname,
            'full_father_name_local':full_father_name_local,
            
        })
    else:
        return JsonResponse({'error': 'Invalid request'})

@login_required
def adhaar_list_view(request):
    adhaar_cards = AdhaarCardDetail.objects.filter(is_deleted=False)
    context={'data':adhaar_cards}
    return render(request,"adhaar_card_list.html",context=context)


@csrf_exempt
def delete_adhaar_card(request, id):
    if request.method == 'POST':
        adhaar_card = get_object_or_404(AdhaarCardDetail, pk=id)
        adhaar_card.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)


@login_required
def adhaar_card_detail(request, id):
    adhaar_card = get_object_or_404(AdhaarCardDetail, pk=id)
    context = {'adhaar_card': adhaar_card}
    return render(request, 'adhaar_card.html', context)
