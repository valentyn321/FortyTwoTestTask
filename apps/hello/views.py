from django.shortcuts import render


def return_developer(request):
    context = {
        'name': 'Valentyn',
        'last_name': 'Cherkasov',
        'birth': '03.02.2001',
        'bio': 'I am a student of Lviv Polytechnic National University. '
        'In my junior year, I have started to learn C/C++.  With time, '
        'I understood, that I new something new, without '
        ';  in the end of the line :)',
        'email': 'vcherkasov321@gmail.com',
        'jabber': 'valentyn17@42cc.co',
        'skype': 'tawervalik15',
        'other': '+380986418462'
    }

    return render(request, "hello/main.html", context)
