from django.shortcuts import render, HttpResponse
from django.shortcuts import render
# Create your views here.

#html_base = """
 #   <h1>Mi Web Personal</h1>
  #  <ul>
   #     <li><a href="/">Portada</a></li>
    #    <li><a href="/about/">Acerca de</a></li>
    #</ul>
#"""

#def home(request):
 #   return HttpResponse(html_base + """
  #      <h2>Bienvenidos</h2>
   #     <p>Esto es la portada.</p>
    #""")

#def about(request):
 #   return HttpResponse(html_base + """
  #      <h2>Acerca de</h2>
   #     <p>Me llamo Sherlin y me encanta Django!</p>
    #""")

#def contact(request):
    #return HttpResponse(html_base + """
        #<h2>Contacto</h2>
        #<p>Email y redes sociales:</p>
        #<ul>
         #   <li><a href="sherlintp09@gmail.com">Email</a></li>
          #  <li><a href="https://github.com/Sherlin09?tab=repositories">Github</a></li>
   # """)

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portafolio(request):
    return render(request, "core/portafolio.html")

def contact(request):
    return render(request, "core/contact.html")