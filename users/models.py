from django.db import models
from django.utils import timezone
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
    equipment_No =  models.IntegerField(null=True,blank=True,default=1)
    equipment = models.CharField(max_length=500,null=True,blank=True,default="")
    eqp_description = models.CharField(max_length=500,null = False,blank = False,default="")
    Short_Name = models.CharField(max_length=500,null = False,blank = False,default="")
    shop_No = models.CharField(max_length=500,null=True,blank=True,default="")
    bay = models.CharField(max_length=500,null=True,blank=True,default="")
    column = models.CharField(max_length=500,null=True,blank=True,default="")
    section = models.CharField(max_length=500,null=True,blank=True,default="")
    sec_ELN = models.CharField(max_length=500,null=True,blank=True,default="")
    eqpType = models.CharField(max_length=500,null=True,blank=True,default="")
    mc_Se_No = models.CharField(max_length=500,null=True,blank=True,default="")
    mc_Model = models.CharField(max_length=500,null=True,blank=True,default="")
    Level1 = models.CharField(max_length=500,null=True,blank=True,default="")
    level2 = models.CharField(max_length=500,null=True,blank=True,default="")
    list1 = models.CharField(max_length=500,null=True,blank=True,default="")
    list2 = models.CharField(max_length=500,null=True,blank=True,default="")
    manufacturer_Code = models.CharField(max_length=500,null=True,blank=True,default="")
    supplier_Code = models.CharField(max_length=500,null=True,blank=True,default="")
    indian_Agent = models.CharField(max_length=500,null=True,blank=True,default="")
    make = models.CharField(max_length=500,null=True,blank=True,default="")
    cost_in_Rs_Lakh1 = models.CharField(max_length=500,null=True,blank=True,default="")
    po_no = models.IntegerField(default=1)
    

    pO_Date = models.DateField(null=True,blank=True,default=timezone.now())
    unit_Code = models.CharField(max_length=500,null=True,blank=True,default="")
    cost = models.CharField(max_length=500,null=True,blank=True,default="")
    cost_in_Lakh2 = models.IntegerField(default=1)
    
    received_Date = models.DateField(null=True,blank=True,default="")
    date_of_Commisioning = models.DateField(null=True,blank=True,default="")
    pTC_Issued_Date = models.CharField(max_length=500,null=True,blank=True,default="")
    warranty = models.CharField(max_length=500,null=True,blank=True,default="")
    aMC = models.CharField(max_length=500,null=True,blank=True,default="")
    type_of_AMC = models.CharField(max_length=500,null=True,blank=True,default="")
    validity = models.CharField(max_length=500,null=True,blank=True,default="")
    recovery_value = models.CharField(max_length=500,null=True,blank=True,default="")
    age_availability = models.CharField(max_length=500,null=True,blank=True,default="")
    specialization = models.TextField(null=True,blank=True,default="")
    machine_Picture = models.ImageField(upload_to="images/machine", height_field=None, width_field=None,default="")
    pO_Copy = models.ImageField(upload_to="images/po_copy",default="")
    accumulated_depreciation_till = models.CharField(max_length=500,null=True,blank=True,default="")
    net_Book_Value1 = models.CharField(max_length=500,null=True,blank=True,default="") 
    give_reference =  models.CharField(max_length=500,null=True,blank=True,default="") 
    current_Market_value = models.CharField(max_length=500,null=True,blank=True,default="")
    net_Book_Value2 = models.CharField(max_length=500,null=True,blank=True,default="")
    whether_Surplus = models.CharField(max_length=500,null=True,blank=True,default="")
    Remarks1 = models.CharField(max_length=500,null=True,blank=True,default="")
    
    
    