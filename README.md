
# Assignment

This assignment having two microservice, Frontend microservice and Backend microservice. 
Frontend microservice used to :
* Build webapp APIs which will list interview candidate’s details on a
      portal.
* App allow the super adminadmin to add entries of candidates into its DB.
* App retain data in a MYSQL DB.
 Backend microservice
* Backend service independent of frontend app based on event driven architecture.
* Service able to auto-generate resumes for newly added candidates and store it in S3.
* It also classify and tag resumes based on candidate skills and years of experience.


## API Reference: From Frontend Service.Backend service feature are dependent on Fronted API's.

#### List All Items with pagination of page size of 10 records.

```http
  POST /frontend/get_candidate_list/
```

* Parameter 

  `{"showAll":Bool,"recordsPerPage":Integer,"rowNumber": Integer, "search":"      {\"filter\":\"<search_field>\",\"field\":\"<column_name>\"}","sortBy":"id",    "sortOrder":"desc" or "aesc"}` 



#### Save one or multiple candidate records.

```http
  POST /frontend/create/
```

* Parameter
`{"data":[{"name":string,"address":string,"contact_number":Integer,"email":string,"location":string,"tech_skills":List_of_String,"experience":Integer}]}`

#### Download resume from S3



```http
  GET /frontend/download_resume/
```
* Parameter : None




## Deployment

To deploy this project run

```bash
  pip install -r requirements.txt
```


## Screenshots

![Screenshot from 2024-01-16 00-56-26](https://github.com/pranit26/resume_repo/assets/156698113/79b272f6-d8ac-4739-9175-2d0c7fa2c6be)

![Screenshot from 2024-01-16 01-04-26](https://github.com/pranit26/resume_repo/assets/156698113/580b0411-ca7b-4ec8-a1fd-54e244d037b1)


![Screenshot from 2024-01-16 01-06-06](https://github.com/pranit26/resume_repo/assets/156698113/2a4b068a-b3d1-4b0f-85b1-fb1c7cfd5343)


![Screenshot from 2024-01-16 01-10-35](https://github.com/pranit26/resume_repo/assets/156698113/ac8a603b-7893-4202-a3d4-f4c6dfccbf92)


![Screenshot from 2024-01-16 01-16-16](https://github.com/pranit26/resume_repo/assets/156698113/5f15feff-da54-4c16-ae7e-41094f06ae57)
## Tech Stack

Python,Django,MySQL,SQS,S3
