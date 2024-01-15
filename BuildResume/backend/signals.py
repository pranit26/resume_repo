import io
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
from frontend.models import Candidates
from .models import Resume
from .messaging import notify_backend,upload_to_s3

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

@receiver(post_save, sender=Candidates)
def candidate_created(sender, instance, **kwargs):
    resume_content = f"Name: {instance.name}\nAddress: {instance.address}\nContact: {instance.contact_number}\nEmail: {instance.email}\nYears_of_Experience:{instance.experience}"
      
    resume=None
    file_name="-".join((instance.tech_skills))+str(instance.experience)
    try:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=f"{file_name}_resume.pdf"'
        pdf = canvas.Canvas(response,pagesize=A4)
        pdf.drawString(10, 700, resume_content)
        pdf.save()
    
        resume = Resume.objects.create(candidate=instance)
        resume.resume_file.save(f"{file_name}_resume.pdf", ContentFile(response.content), save=True)
        pdf_resume_file_path = resume.resume_file.path

        notify_backend(instance.candidate_id,resume_content={"Name":{'StringValue':instance.name,'DataType':'String'},"Address":{'StringValue':instance.address,'DataType':'String'},"Contact":{'StringValue':str(instance.contact_number),'DataType':'String'},"Email":{'StringValue':instance.email,'DataType':'String'},"Years_of_Experience":{'StringValue':str(instance.experience),'DataType':'Number'},"Location":{'StringValue':instance.location,'DataType':'String'}})

        with open(pdf_resume_file_path, 'rb') as pdf_file:
            pdf_content_binary = pdf_file.read()

        upload_to_s3(pdf_content_binary,f"resumes/{file_name}_resume.pdf")
    except Exception as e:
        print(e)    
    
    return "Message Sent successfully"

