# -*- coding: utf-8 -*-
import datetime
import string
import random
import hmac
import hashlib
import base64

from django.conf import settings
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import get_connection, EmailMultiAlternatives
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context_dict = {}
    return render(request,"index.html",context_dict)
