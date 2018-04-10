########### from here is working ##########
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# import requests
# import json
#
#
# import httplib2
# import os
# import sys
#
#
#
# def home(request):
#     redirect(request, 'https://gaming.youtube.com/watch?v=FsWPwNnJXxE')




############# to here is working ############

from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



import httplib2
import os
import sys

from apiclient.errors import HttpError
from oauth2client.tools import argparser
from apiclient.discovery import build
import json
import sys
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = 'AIzaSyBSoMymH7ZLs_0nbOhqHeWiq9FaLNcLFXM'

def home(request):
    return render(request, 'registration/home.html')
    # return redirect(request, 'https://gaming.youtube.com/watch?v=FsWPwNnJXxE')













