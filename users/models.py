from django.db import models
from datetime import datetime
# CHOICES = (
#            ('dog','Dog',default=""),
#            ('cat','Cat',default=""),
#         ,default="")

# class signin(models.Model,default=""):
#     search-equipment = models.CharField(max_length=500,max_length=3,widget=models.Select(choices = CHOICES,default=""),default="")


    # equipment No.= 
    # eqp.description = 
    # Short Name = 
    # shop No. = 
    # bay = 
    # column = 
    # section = 
    # sec.ELN = 
    # eqp.Type = 
    # m/c Se.No.Alloted by Mgf = 
    # m/c Model No. =
    # critical Level-1 = 
    # list = 
    # level-2 = 
    # manufacturer Code = 
    # supplier Code = 
    # indian Agent = 
    # make = 
    # cost in Rs. Lakh = 
    # # shop No. = 
    # # pO Date = 
    # received Date = 
    # date of Commisioning = 
    # pTC Issued Date = 
    # warranty = 
    # aMC = 
    # type of AMC = 
    # date of Commisioning =
    # pTC Issued Date = 
    # age availability = 
    # specialization = 
    # machine Picture = 
    # pO Copy  =
    # accumulated_depreciation_till = 
    # net_Book_Value_as_on_dt = 
    # give_reference_of_the_vaiable = 
    # current_Market_value = 
    # net_Book_Value_as_on_dt = 
    # whether_Surplus = 
    # accumulated_depreciation_till = 

class Machine(models.Model):
    equipment_No =  models.IntegerField(null=False,blank = False,default=1)
    equipment = models.CharField(max_length=500,null=False,blank = False,default="")
    eqp_description = models.CharField(max_length=500,null = False,blank = False,default="")
    Short_Name = models.CharField(max_length=500,null = False,blank = False,default="")
    shop_No = models.CharField(max_length=500,null=False,blank = False,default="")
    bay = models.CharField(max_length=500,null=False,blank = False,default="")
    column = models.CharField(max_length=500,null=False,blank = False,default="")
    section = models.CharField(max_length=500,null=False,blank = False,default="")
    sec_ELN = models.CharField(max_length=500,null=False,blank = False,default="")
    eqpType = models.CharField(max_length=500,null=False,blank = False,default="")
    mc_Se_No = models.CharField(max_length=500,null=False,blank = False,default="")
    mc_Model = models.CharField(max_length=500,null=False,blank = False,default="")
    Level1 = models.CharField(max_length=500,null=False,blank = False,default="")
    level2 = models.CharField(max_length=500,null=False,blank = False,default="")
    list1 = models.CharField(max_length=500,null=False,blank = False,default="")
    list2 = models.CharField(max_length=500,null=False,blank = False,default="")
    manufacturer_Code = models.CharField(max_length=500,null=False,blank = False,default="")
    supplier_Code = models.CharField(max_length=500,null=False,blank = False,default="")
    indian_Agent = models.CharField(max_length=500,null=False,blank = False,default="")
    make = models.CharField(max_length=500,null=False,blank = False,default="")
    cost_in_Rs_Lakh1 = models.CharField(max_length=500,null=False,blank = False,default="")
    po_no = models.IntegerField(null=False,blank = False,default=1)
    

    pO_Date = models.DateField(null=False,blank = False,default=datetime.now())
    unit_Code = models.CharField(max_length=500,null=False,blank = False,default="")
    cost = models.CharField(max_length=500,null=False,blank = False,default="")
    cost_in_Lakh2 = models.IntegerField(null=False,blank = False,default=1)
    
    received_Date = models.DateField(null=False,blank = False,default="")
    date_of_Commisioning = models.DateField(null=False,blank = False,default="")
    pTC_Issued_Date = models.CharField(max_length=500,null=False,blank = False,default="")
    warranty = models.CharField(max_length=500,null=False,blank = False,default="")
    aMC = models.CharField(max_length=500,null=False,blank = False,default="")
    type_of_AMC = models.CharField(max_length=500,null=False,blank = False,default="")
    validity = models.CharField(max_length=500,null=False,blank = False,default="")
    recovery_value = models.CharField(max_length=500,null=False,blank = False,default="")
    age_availability = models.CharField(max_length=500,null=False,blank = False,default="")
    specialization = models.TextField(null=False,blank = False,default="")
    machine_Picture = models.ImageField(upload_to=None, height_field=None, width_field=None,default="")
    pO_Copy = models.ImageField(upload_to=None,default="")
    accumulated_depreciation_till = models.CharField(max_length=500,null=False,blank = False,default="")
    net_Book_Value1 = models.CharField(max_length=500,null=False,blank = False,default="") 
    give_reference =  models.CharField(max_length=500,null=False,blank = False,default="") 
    current_Market_value = models.CharField(max_length=500,null=False,blank = False,default="")
    net_Book_Value2 = models.CharField(max_length=500,null=False,blank = False,default="")
    whether_Surplus = models.CharField(max_length=500,null=False,blank = False,default="")
    Remarks1 = models.CharField(max_length=500,null=False,blank = False,default="")
    
    
    