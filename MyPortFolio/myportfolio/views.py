from django.views.generic import TemplateView
from aboutme.models import AboutMe
from slinks.models import Slinks
from myskill.models import Myskill
from education.models import Education
from portfolio.models import PortFolio
from testimonial.models import Testimonial
from django.views.generic import DetailView, ListView

class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['about'] = AboutMe.objects.get(id=1)
        data['slink'] = Slinks.objects.get(id=1)
        data['skill_list'] = Myskill.objects.all()
        data['educate'] = Education.objects.all().order_by('-id')
        data['portfolio_list'] = PortFolio.objects.all()
        data['testimonial'] = Testimonial.objects.all()
        return data
    
class PortFolioListView(ListView):
    model = PortFolio
    queryset = PortFolio.objects.all()
    template_name = "portfolio-details.html"

class PortFolioDetailView(DetailView):
    model = PortFolio
    queryset = PortFolio.objects.all()
    template_name = "portfolio-details.html"