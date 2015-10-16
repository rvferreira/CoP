from django.shortcuts import render
from django.http import HttpResponse

import PIL
from matplotlib import pylab
from pylab import *
import StringIO

def test_matplotlib(request):
	x = [1, 2, 3, 4, 5]
	y = [2, 7, 4, 3, 9]
	plot(x, y, linewidth=2)

	xlabel = 'xaxis'
	ylabel = 'yaxis'
	title('test')
	grid(True)

	buffer = StringIO.StringIO()
	canvas = pylab.get_current_fig_manager().canvas
	canvas.draw()
	graphIMG = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
	graphIMG.save(buffer, "PNG")
	pylab.close()

	return HttpResponse(buffer.getvalue(), content_type='image/png')

# 	return HttpResponse(OPENID_LOGO_BASE_64.decode('base64'), content_type='image/png')
# # Logo from http://openid.net/login-bg.gif
# # Embedded here for convenience; you should serve this as a static file
# OPENID_LOGO_BASE_64 = """
# R0lGODlhEAAQAMQAAO3t7eHh4srKyvz8/P5pDP9rENLS0v/28P/17tXV1dHEvPDw8M3Nzfn5+d3d
# 3f5jA97Syvnv6MfLzcfHx/1mCPx4Kc/S1Pf189C+tP+xgv/k1N3OxfHy9NLV1/39/f///yH5BAAA
# AAAALAAAAAAQABAAAAVq4CeOZGme6KhlSDoexdO6H0IUR+otwUYRkMDCUwIYJhLFTyGZJACAwQcg
# EAQ4kVuEE2AIGAOPQQAQwXCfS8KQGAwMjIYIUSi03B7iJ+AcnmclHg4TAh0QDzIpCw4WGBUZeikD
# Fzk0lpcjIQA7
# """


# Create your views here.
def index(request):
	context = {
	'page_title':'Evolutives Report',
	}
	
	if request.GET.get('fitness-selection'):
		request.session['fitness-selection'] = request.GET.get('fitness-selection')
	else:
		return render(request, 'report.html', context)

