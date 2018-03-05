from django.shortcuts import render
from django.shortcuts import redirect
from django.template import Context
from django.core.mail import EmailMessage
from django.template.loader import get_template
from dog.forms import ContactForm,UserForm,UserProfileForm,AddCottageForm
from .models import Cottage
from django.contrib import messages
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


################
# DOG BNB views
################

#####################################################
# STUFF TO DO. SEND BACK MESSAGES TO CONTACT TEMPLATE
#####################################################

# INDEX [HOME]
def index(request):
    
    return render(request, 'dog/index.html', {})

# ABOUT US
def about(request):

    return render(request, 'dog/about.html', {})

# CONTACT US
def contact(request):
    
    form_class = ContactForm
    
    # Process form
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email details
            template = get_template('dog/contact_template.txt')
            context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
            }

            content = template.render(context)

            # Email message
            email = EmailMessage(
                
                "New contact form submission",
                content,
                "Website" +'', ['youremail@gmail.com'], headers = {'Reply-To': contact_email }
            )

            # Send email
            email.send()
            
            # Send a message back to the user
            messages.success(request, ('Your email was succcessfully sent.'))
            return redirect('contact')

    return render(request, 'dog/contact.html', {'form': form_class,})

# REGISTER [caters for both a Guest and a host]
def register(request):

    registered = False
    
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            
            print(user_form.errors, profile_form.errors)
    else:
        
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'dog/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

# LATEST COTTAGES
#  - Gets the latest cottages from the database
def latestcottages(request):

    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Get the lastest cottages
    # Need to decide how many to retrieve [maybe just get 10 and sort by name]
    cottages_list = Cottage.objects.all()

    return render(request, 'dog/latest-cottages.html', locals())

# ADD A COTTAGE
# - Form to add a cottage
def addcottage(request):

    add_cottage = AddCottageForm()

    return render(request, 'dog/add-cottage.html', {'add_cottage': add_cottage,})

# page 124
#@login_required
def user_logout(request):
    
    logout(request)
    
    return HttpResponseRedirect(reverse('index'))

# SEARCH RESULTS
def search_results(request):

    return render(request, 'dog/search-results.html', {})

# ACCOUNT
# - Caters for Tourist, Host, and Admin
# - Checks logged in user to decide which options to display
def search_results(request):

    return render(request, 'dog/search-results.html', {})