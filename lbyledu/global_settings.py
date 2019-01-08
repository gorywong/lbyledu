from django.conf import settings

def global_settings(request):
    return {"EDU_INFO": settings.EDU_INFO,
            "RESEARCH": settings.RESEARCH,
            "RESOURCE": settings.RESOURCE,
            "AFFAIRS": settings.AFFAIRS,
            "POLICY": settings.POLICY,
            "SHOW": settings.SHOW,}