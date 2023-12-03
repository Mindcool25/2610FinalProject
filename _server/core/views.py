from django.views import View
from django.shortcuts import render
from django.conf  import settings
from django.http import HttpResponse
import json
import os
from django.contrib.auth.decorators import login_required

# Load manifest when server launches
MANIFEST = {}
if not settings.DEBUG:
    f = open(f"{settings.BASE_DIR}/core/static/manifest.json")
    MANIFEST = json.load(f)

# Create your views here.
@login_required
def index(req):
    context = {
        "asset_url": os.environ.get("ASSET_URL", ""),
        "debug": settings.DEBUG,
        "manifest": MANIFEST,
        "js_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["file"],
        "css_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["css"][0]
    }
    return render(req, "core/index.html", context)

class Post(View):
    # Return error, get not allowed
    def get(self, request):
        return
    # Create a new post
    def post(self, request):
        return

class GetPost(View):
    # Get given post
    def get(self, request):
        return
    # Edit given post (If correct user)
    def post(self, request):
        return

class GetImage(View):
    # Get given image 
    def get(self, request):
        return
    # Remove given image (if logged in)
    def post(self, request):
        return

class Topic(View):
    # Return all topics
    def get(self, request):
        return
    # Create a new topic
    def post(self, request):
        return

class GetTopic(View):
    # Return given topic
    def get(self, request):
        return
    # Edit given topic (If logged in)
    def post(self, request):
        return

class Images(View):
    # Get an image
    def get(self, request):
        return
    # Save an image
    def post(self, request):
        return
