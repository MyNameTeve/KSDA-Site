from django.core.management.base import BaseCommand, CommandError
from ksda.models import *
import datetime
from django.core.mail import send_mail

class Command(BaseCommand):

	args = '<>'
	def handle(self, *args, **options):
		#filter by free that day and active then order by units and order
		monday = Brother.objects.all().filter(active=True, waitsessionbrotherinfo__freeM = True).order_by("waitsessionbrotherinfo__units","-order")
		tuesday = Brother.objects.all().filter(active=True, waitsessionbrotherinfo__freeT = True).order_by("waitsessionbrotherinfo__units","-order")
		wednesday = Brother.objects.all().filter(active=True, waitsessionbrotherinfo__freeW = True).order_by("waitsessionbrotherinfo__units","-order")
		thursday = Brother.objects.all().filter(active=True, waitsessionbrotherinfo__freeH = True).order_by("waitsessionbrotherinfo__units","-order")
		friday = Brother.objects.all().filter(active=True, waitsessionbrotherinfo__freeF = True).order_by("waitsessionbrotherinfo__units","-order")
		
		
		assigned = {}
		for brother in Brother.objects.all():
			assigned[brother.order] = False
		defaultBrother = Brother.objects.get(order=69)
		# m = []
		# t = []
		# w = []
		# h = []
		# f = []
		# for b in monday:
		# 	m.append(b)
		# for b in tuesday:
		# 	t.append(b)
		# for b in wednesday:
		# 	w.append(b)
		# for b in thursday:
		# 	h.append(b)
		# for b in friday:
		# 	f.append(b)
		# days = [m,t,w,h,f]
		# days.sort()
		
		m_waitsession=None
		t_waitsession=None
		w_waitsession=None
		r_waitsession=None
		f_waitsession=None
		m_namelist = []
		t_namelist = []
		w_namelist = []
		r_namelist = []
		f_namelist = []
		
		count = -1	
		today = datetime.date.today()
		#set an offset to add to the current day to get to the closest sunday then add to 
		#get the desired day
		offset =  6 - datetime.date.today().weekday()
		#determine the date of the week for the different wait session days
		m = today + datetime.timedelta(days=(offset+1))
		t = today + datetime.timedelta(days=(offset+2))
		w = today + datetime.timedelta(days=(offset+3))
		h = today + datetime.timedelta(days=(offset+4))
		f = today + datetime.timedelta(days=(offset+5))
		#loop through all the brothers available for the given day and give them that waitsession
		#once 3 are assigned break out of the loop
		for b in monday:
			if (count >= 2):
				break
			elif (not assigned[b.order]):
				m_waitsession = Waitsession.objects.create(date=m, brotherinfo=b.waitsessionbrotherinfo)
				m_namelist.append(b.waitsessionbrotherinfo.brother.getName())
				assigned[b.order] = True
				m_waitsession.save()
				count += 1
		count = -1
		
	    	for b in tuesday:
			if (count >= 2):
				break
			elif (not assigned[b.order]):
				#if not already assigned, we assign
				t_waitsession = Waitsession.objects.create(date=t, brotherinfo=b.waitsessionbrotherinfo)
				t_namelist.append(b.waitsessionbrotherinfo.brother.getName())
				assigned[b.order] = True
				t_waitsession.save()
				count += 1
	    	count = -1			
	    	
		for b in wednesday:
			if (count >= 2):
				break
			elif (not assigned[b.order]):
				#if not already assigned, we assign
				w_waitsession = Waitsession.objects.create(date=w, brotherinfo=b.waitsessionbrotherinfo)
				w_namelist.append(b.waitsessionbrotherinfo.brother.getName())
				assigned[b.order] = True
				w_waitsession.save()
				count += 1
	    	count = -1			
	    	for b in thursday:
			if (count >= 2):
				break
			elif (not assigned[b.order]):
				#if not already assigned, we assign
				r_waitsession = Waitsession.objects.create(date=h, brotherinfo=b.waitsessionbrotherinfo)
				r_namelist.append(b.waitsessionbrotherinfo.brother.getName())
				assigned[b.order] = True
				r_waitsession.save()
				count += 1
	    	count = -1			
	    	for b in friday:
			if (count >= 2):
				break
			elif (not assigned[b.order]):
				#if not already assigned, we assign
				f_waitsession = Waitsession.objects.create(date=f, brotherinfo=b.waitsessionbrotherinfo)
				f_namelist.append(b.waitsessionbrotherinfo.brother.getName())
				assigned[b.order] = True
				f_waitsession.save()
				count += 1
	    	count = -1			
    	
		sendingList = Brother.objects.values_list('email', flat=True);
	
		endingList = ['AEKDB', 'Semper', 'Yours in Brotherhood', 'Interfraternally Yours']

		email_body ='''Brothers,
	
		The waitsessions for the week of %s are as follows:
	
		Monday: %s
	
		Tuesday %s
	
		Wednesday: %s
	
		Thursday: %s
	
		Friday %s
	
		Any vacancies will be filled by the House Manager.
	
		If you cannot make a waitsession, please go to the website, check availability for that day, and arrange a substitute.
	
		All concerns about the algorithm should be sent to the Admin.
	
		%s,
	
		Baldassare Cossa ''' % (today + datetime.timedelta(days=(offset)), m_namelist, t_namelist,
				w_namelist, r_namelist, f_namelist, 'AEKDB')
		
		print(email_body)
		
		send_mail(subject="Waitsession Assignments",
		          message=email_body,
		          from_email="DoNotReply@ksda.herokuapp.com",
		          recipient_list=sendingList)
    
    	
    	


    		

		