# frontend/views.py
import json
from rest_framework.decorators import api_view
from rest_framework import status
import traceback
from .response import Response
from django.http.response import JsonResponse
from .validations import data_validator,validate_list
from .models import Candidates
from django.db.models import Q
import boto3
import os


error_string = "Something seems to have  gone wrong. Try again later?"


@api_view(['POST'])
def create_candidate(request):
    responseObj=Response(request=request)
    try:
        
        data_request=request.data.get('data')
        print(data_request,type(data_request))
        for data in data_request:
            print(data)
            is_valid, message = data_validator(data)
            if not is_valid:
                message={"message":message,"status":status.HTTP_406_NOT_ACCEPTABLE}
                return JsonResponse(message,status=status.HTTP_406_NOT_ACCEPTABLE,safe=False)  
                      
            try:
                existing_name=list(Candidates.objects.filter(Q(name=data['name']) | Q(email=data['email'])).values()) 
                print(existing_name)  
            except Exception as e:
                print(traceback.format_exc(e))    

            if len(existing_name) > 0:
                message = {
                "message": "Candidate already exist with same name or same mail id.", "status": 406}
                return JsonResponse(message, status=status.HTTP_406_NOT_ACCEPTABLE)  
            
            candidate = Candidates.objects.create(
                        name=data['name'],
                        address=str(data['address']),
                        contact_number=data["contact_number"],
                        location=data["location"],
                        email=data["email"],
                        tech_skills=data["tech_skills"],
                        experience=data['experience']
                    )
            candidate.save()
        message={"message":"Candidate data saved successfully"}
        payload={item['name']: {'name': item['name'], 'tech_skills': item['tech_skills']} for item in data_request}
        return responseObj.createResponse(message,payload,status_code=200)
    except Exception as e:
        print(traceback.format_exc())
        message = {"message": "Unable to store Candidate data.", "status": 406}
        return responseObj.createResponse(message,payload={},status_code=406) 
    
    
@api_view(['POST'])
def get_candidate_list(request):
    responseObj = Response(request=request)
    try:
        data = request.data
        search = json.loads(data.get('search'))
        filter_data = search.get("filter")
        field = search.get("field")
        recordsPerPage = int(data.get('recordsPerPage'))
        recordsPerPage = 10 if recordsPerPage > 10 else recordsPerPage
        is_valid, message = validate_list(data=data)
        if not is_valid:
            return responseObj.createResponse(message,paylaod={},status_code=406)

        record_head = int(data.get('rowNumber')) - \
            1 if data.get('rowNumber') else 0
        record_tail = recordsPerPage + \
            record_head if recordsPerPage else None
        order = data.get('sortOrder') if data.get('sortOrder') else ""
        order = "" if order == "asc" else "-"
        sortBy = data.get('sortBy') if data.get('sortBy') else "created_at"
        results = get_filtered_results(field=field, filter_data=filter_data, order=order,                                   sortBy=sortBy, record_head=record_head, record_tail=record_tail)
        filtered_records = results[record_head:record_tail]
        pager = {
            "sortField": sortBy,
            "sortOrder": "ASC" if order == "asc" else "DESC",
            "rowNumber": record_head,
            "recordsPerPage": recordsPerPage,
            "totalRecords": len(results),
            "filteredRecords": len(filtered_records)
        }
        response = {'pager': pager, "payload": filtered_records,
                    'message': 'Candidates Fetched Successfully.'}
        return responseObj.createResponse(message=error_string,payload=response,status_code=200)
    except Exception as e:
        print(traceback.format_exc())
        return responseObj.createResponse(message=error_string,payload={},status_code=406)
    


def get_filtered_results(field, filter_data, order, sortBy, record_head, record_tail):
    if field == "name":
        data = list(Candidates.objects.filter(name__contains=filter_data).order_by(order+sortBy).values())
        return data
    elif field == "address":
        data = list(Candidates.objects.filter(address__contains=filter_data).order_by(order+sortBy).values())
        return data
    elif field == "location":
        data = list(Candidates.objects.filter(location__contains=filter_data).order_by(order+sortBy).values())
        return data
    elif field == "contact_number":
        data = list(Candidates.objects.filter(contact_number__contains=filter_data).order_by(order+sortBy).values())
        return data
    elif field == "email":
        data = list(Candidates.objects.filter(email__contains=filter_data).order_by(order+sortBy).values())
        return data
    elif field == "tech_skills":
        data = list(Candidates.objects.filter(tech_skills__contains=filter_data).order_by(order+sortBy).values())
        return data
    else:
        data = list(Candidates.objects.filter(
            Q(name__contains=filter_data) | Q(address__contains=filter_data) | Q(location__contains=filter_data) | Q(contact_number__contains=filter_data) | Q(email__contains=filter_data) | Q(email__contains=filter_data) | Q(tech_skills__contains=filter_data)).order_by(order + sortBy).values())
        return data       
    



@api_view(['GET'])
def download_resume(request):
    
    responseObj=Response(request)
    s3_resource = boto3.client('s3',aws_access_key_id="AKIAZ4B6NTNZ7CBSEBYO",aws_secret_access_key="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")

    try:        
        bucket_name="resumebucket14"
        list_files=s3_resource.list_objects(Bucket=bucket_name)['Contents']
        root_path=os.getcwd()
        for key in list_files:
            download_file_path = os.path.join(root_path,"downloads",key['Key'])
            s3_resource.download_file(Bucket=bucket_name,Key=key['Key'],Filename=key['Key'])

        message = {"message": "Download completes.", "status": 200}
        return responseObj(message,payload={}, status_code=200) 
    except Exception as e:
        print(traceback.format_exc())
        return responseObj.createResponse(message=error_string,payload={},status_code=404)


