from django.shortcuts import render
from django.views.generic.base import View

from .models import OrgDict

# Create your views here.


class InfoView(View):
    def get(self, request, org_id):
        middle = []
        primary = []
        kindergarten = []
        org = OrgDict.objects.get(id=int(org_id))
        all_orgs = OrgDict.objects.all()
        for each_org in all_orgs:
            if each_org.sort == "middle":
                middle.append(each_org)
            elif each_org.sort == "primary":
                primary.append(each_org)
            elif each_org.sort == "kindergarten":
                kindergarten.append(each_org)
        return render(request, "content.html", {"middle": sorted(middle, key=lambda middle: middle.id),
                                                "primary": sorted(primary, key=lambda primary: primary.id),
                                                "kindergarten": sorted(kindergarten, key=lambda kindergarten: kindergarten.id),
                                                "org": org,
                                                "title": org.name+"概况", 
                                                "bread": org.name+"概况",
                                                "add_time": org.add_time.strftime('%Y-%m-%d %H:%M:%S'), 
                                                "desc": org.desc})


class LeaderInfoView(View):
    def get(self, request, leader_id):
        pass