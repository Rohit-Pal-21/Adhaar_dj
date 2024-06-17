from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class BaseModel(models.Model):
    created_on =models.DateTimeField(auto_now_add=True)
    updated_on =models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

States =[('Andaman and Nicobar Islands','Andaman and Nicobar Islands'), ('Andhra Pradesh','Andhra Pradesh'),
         ('Arunachal Pradesh','Arunachal Pradesh'), 
         ('Assam','Assam'), ('Bihar','Bihar'), ('Chandigarh','Chandigarh'), ('Chhattisgarh','Chhattisgarh'), 
         ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'), 
         ('Daman and Diu','Daman and Diu'), ('Delhi','Delhi'), ('Goa','Goa'), ('Gujarat','Gujarat'), 
         ('Haryana','Haryana'), ('Himachal Pradesh','Himachal Pradesh'), 
         ('Jammu and Kashmir','Jammu and Kashmir'), ('Jharkhand','Jharkhand'),('Karnataka','Karnataka'), 
         ('Kerala','Kerala'), ('Ladakh','Ladakh'), ('Lakshadweep','Lakshadweep'), 
         ('Madhya Pradesh','Madhya Pradesh'), ('Maharashtra','Maharashtra'), ('Manipur','Manipur'), 
         ('Meghalaya','Meghalaya'), ('Mizoram','Mizoram'), ('Nagaland','Nagaland'), ('Odisha','Odisha'), 
         ('Puducherry','Puducherry'), ('Punjab','Punjab'), 
         ('Rajasthan','Rajasthan'), ('Sikkim','Sikkim'),('Tamil Nadu','Tamil Nadu'), ('Telangana','Telangana'), 
         ('Tripura','Tripura'), ('Uttar Pradesh','Uttar Pradesh'), ('Uttarakhand','Uttarakhand'), ('West Bengal','West Bengal')]


Gender=[('Male','Male'),('Female','Female'),('Transgender','Transgender')]

class AdhaarCardDetail(BaseModel):
    adhaar_no       =models.CharField(max_length=14)
    so_do           =models.CharField(max_length=14)
    profile_img     =models.ImageField(upload_to="profile_images/")
    name            =models.CharField(max_length=1000)
    father_name     =models.CharField(max_length=1000)
    full_father_name_local  =models.CharField(max_length=1000)
    surname         =models.CharField(max_length=1000)
    fullname        =models.CharField(max_length=1000)
    date_of_birth   =models.DateField()
    house_no        =models.CharField(max_length=1000)
    locality        =models.CharField(max_length=1000)
    post_office     =models.CharField(max_length=1000)
    state           =models.CharField(max_length=1000,choices=States)
    city            =models.CharField(max_length=1000)
    pincode         =models.CharField(max_length=6)
    gender          =models.CharField(max_length=50,choices=Gender)
    address         =models.TextField(max_length=1000)
    local_fullname  =models.CharField(max_length=1000)
    local_gender    =models.CharField(max_length=1000)
    address_local   =models.TextField(max_length=1000)
    
    
    is_deleted          =models.BooleanField(default=False)
 
    def __str__(self) -> str:
        return f"{str(self.adhaar_no)}--{str(self.fullname)}"
    
    class Meta:
        ordering= ['-created_on']
        db_table='AdhaarCardDetails'

    def save(self,*args,**kwargs):
        super(AdhaarCardDetail,self).save()
        return self