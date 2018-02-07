from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Ports
from ipware import get_client_ip
from .forms import PortCheckerForm
import nmap
nm = nmap.PortScanner()

class HomePageView(TemplateView):
    form_class = PortCheckerForm
    initial = {'key': 'value'}
    template_name = 'portchecker/home.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        client_ip, is_routable = get_client_ip(request)
        args = {'form': form, 'client_ip': client_ip}
        return render(request, self.template_name, args)

    def post(self, request):
        form = self.form_class(request.POST)
        client_ip, is_routable = get_client_ip(request)
        if form.is_valid():
            text = form.cleaned_data['Port_to_check']

            #return HttpResponseRedirect('/success/')

        port_number = getattr(text, 'number')
        port_string = repr(port_number)
        nm.scan(client_ip, port_string)
        #TODO add support for UDP
        nmap_result = nm[client_ip]['tcp'][port_number]['state']
        context = {'client_ip': client_ip, 'text': text, 'form': form, 'port_string': port_string, 'nmap_result': nmap_result}
        return render(request, self.template_name, context)