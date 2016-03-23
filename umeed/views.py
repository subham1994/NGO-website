from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib import messages
from .forms import NewUserForm, LoginForm
from .models import UmeedNews, UmeedUsers, UsersPayment
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render_to_response, render


def home(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/home/')
        else:
                context = {}
                context.update(csrf(request))
                context['loginform'] = LoginForm()
                context['form'] = NewUserForm()
                return render_to_response('index1.html', context, context_instance=RequestContext(request))


def signup(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/home/')
        if request.method == 'POST':
                form = NewUserForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        user = User.objects.create_user(username=username, email=form.cleaned_data['email'],
                                                        password=password)
                        umeeduser = UmeedUsers(user=user, name=form.cleaned_data['name'])
                        umeeduser.save()
                        user = auth.authenticate(username=username, password=password)
                        if umeeduser is not None:
                                auth.login(request, user)
                        return HttpResponseRedirect('/home/')
                else:
                        return render_to_response('index1.html', {'form': form, 'loginform': LoginForm()},
                                                  context_instance=RequestContext(request))
        context = {}
        context.update(csrf(request))
        context['form'] = NewUserForm()
        context['loginform'] = LoginForm()
        return render_to_response('index1.html', context, context_instance=RequestContext(request))


def loginRequest(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/home/')
        if request.method == 'POST':
                loginform = LoginForm(request.POST)
                if loginform.is_valid():
                        username = loginform.cleaned_data['username']
                        password = loginform.cleaned_data['password']
                        umeeduser = auth.authenticate(username=username, password=password)
                        if umeeduser is not None:
                                auth.login(request, umeeduser)
                                return HttpResponseRedirect('/home/')
                        else:
                                messages.add_message(request, messages.WARNING, 'invalid username or password !!')
                                return render_to_response('index1.html',
                                                          {'loginform': loginform, 'form': NewUserForm()},
                                                          context_instance=RequestContext(request))
                else:
                        return render_to_response('index1.html', {'loginform': loginform, 'form': NewUserForm()},
                                                  context_instance=RequestContext(request))
        else:
                context = {}
                context.update(csrf(request))
                context['loginform'] = LoginForm()
                context['form'] = NewUserForm()
                return render_to_response('index1.html', context, context_instance=RequestContext(request))


def profile(request):
        umeeduser = None
        loggedin = True
        if not request.user.is_authenticated():
                loggedin = False
        else:
                umeeduser = UmeedUsers.objects.get(user=request.user)
        context = {'umeeduser': umeeduser, 'articles': UmeedNews.objects.all().order_by("-pub_date"),
                   'loggedin': loggedin}
        return render_to_response('articles.html', context, context_instance=RequestContext(request))


def logout(request):
        auth.logout(request)
        return HttpResponseRedirect('/main/')


def article(request, article_id=1):
        umeeduser = None
        loggedin = False
        if request.user.username != '' and request.user.is_authenticated():
                loggedin = True
                umeeduser = UmeedUsers.objects.get(user=request.user)
        context = {'umeeduser': umeeduser, 'article': UmeedNews.objects.get(id=article_id), 'loggedin': loggedin}
        return render_to_response('article.html', context, context_instance=RequestContext(request))


def memberSection(request, member_id):
        umeeduser = None
        loggedin = False
        if request.user.username != '' and request.user.is_authenticated():
                loggedin = True
                umeeduser = UmeedUsers.objects.get(user=request.user)
                if not umeeduser.coremember:
                        return HttpResponseRedirect('/main/')
        else:
                return HttpResponseRedirect('/main/')
        context = {'umeeduser': umeeduser, 'loggedin': loggedin}
        return render_to_response('members_panel.html', context, context_instance=RequestContext(request))


def getUsers(request):
        umeedusers = UmeedUsers.objects.all()
        showtable = False
        umeeduser = None
        loggedin = False
        if request.user.username != '' and request.user.is_authenticated():
                loggedin = True
                showtable = True
                umeeduser = UmeedUsers.objects.get(user=request.user)
                if not umeeduser.coremember:
                        return HttpResponseRedirect('/main/')
        else:
                return HttpResponseRedirect('/main/')
        context = {'umeeduser': umeeduser, 'loggedin': loggedin, 'umeedusers': umeedusers, 'showtable': showtable}
        return render_to_response('members_panel.html', context, context_instance=RequestContext(request))


def getPaymentData(request):
        umeeduser = None
        showPaymentData = False
        umeeduserPayment = None
        loggedin = False
        if request.user.username != '' and request.user.is_authenticated():
                loggedin = True
                umeeduser = UmeedUsers.objects.get(user=request.user)
                q = request.POST.get('paymentData')
                if q:
                        umeeduserPayment = UsersPayment.objects.filter(
                                Q(umeeduser__name__icontains=q) | Q(umeeduser__user__username__icontains=q))
                        if not umeeduserPayment:
                                messages.add_message(request, messages.WARNING, 'No Results to display !!')
                        else:
                                showPaymentData = True
                else:
                        messages.add_message(request, messages.WARNING, 'Field cannot be left blank')
        context = {'umeeduserPayments': umeeduserPayment, 'loggedin': loggedin, 'showPaymentData': showPaymentData,
                   'umeeduser': umeeduser}
        return render_to_response('members_panel.html', context, context_instance=RequestContext(request))


def imageGallery(request):
        umeeduser = None
        loggedin = False
        if request.user.username != '' and request.user.is_authenticated():
                loggedin = True
                umeeduser = UmeedUsers.objects.get(user=request.user)
        context = {'umeeduser': umeeduser, 'loggedin': loggedin}
        return render_to_response('image_gallery.html', context, context_instance=RequestContext(request))
