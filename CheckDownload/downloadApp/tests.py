#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CheckDownload.settings")
from downloadApp.models import *
# Create your tests here.

print RegisterPhone.objects.all().count();