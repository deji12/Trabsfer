from django.contrib.sites.shortcuts import get_current_site
from .models import SiteInformation

def site_information(request):
    current_site = get_current_site(request)
    
    # Use get_or_create to retrieve or create the SiteInformation object
    site_information, created = SiteInformation.objects.get_or_create(site=current_site, defaults={
        'site_name': 'Default Site Name',  # You can provide default values for other fields here
        'facebook_link': '',
        'twitter_link': '',
        'instagram_link': '',
        'whatsapp_link': '',
        'contact_email': '',
        'contact_number': '',
        'footer_message': '',
        'contact_page_message': '',
    })

    return {'site_information': site_information}
