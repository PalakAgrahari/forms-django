from django.db import models

# CHOICES = (
#            ('dog','Dog'),
#            ('cat','Cat'),
#         )

# class signin(models.Model):
#     search-equipment = models.CharField(max_length=3,widget=models.Select(choices = CHOICES))


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

class formdata(models.Model):
    equipment_No =  models.IntegerField(null=False,blank = False),
    equipment = models.CharField(null=False,blank = False),
    eqp_description = models.CharField(null = False,blank = False,max_length = 50),
    Short_Name = models.CharField(null = False,blank = False,max_length = 50),
    shop_No = models.CharField(null=False,blank = False),
    bay = models.CharField(null=False,blank = False),
    column = models.CharField(null=False,blank = False),
    section = models.CharField(null=False,blank = False),
    sec_ELN = models.CharField(null=False,blank = False),
    eqpType = models.CharField(null=False,blank = False),
    mc_Se_No = models.CharField(null=False,blank = False),
    mc_Model = models.CharField(null=False,blank = False),
    Level1 = models.CharField(null=False,blank = False),
    level2 = models.CharField(null=False,blank = False),
    list1 = models.CharField(null=False,blank = False),
    list2 = models.CharField(null=False,blank = False),
    manufacturer_Code = models.CharField(null=False,blank = False),
    supplier_Code = models.CharField(null=False,blank = False),
    indian_Agent = models.CharField(null=False,blank = False),
    make = models.CharField(null=False,blank = False),
    cost_in_Rs_Lakh1 = models.CharField(null=False,blank = False),
    po_no = models.IntegerField(null=False,blank = False),
    

    pO_Date = models.DateField(null=False,blank = False),
    unit_Code = models.CharField(null=False,blank = False),
    cost = models.CharField(null=False,blank = False),
    cost_in_Lakh2 = models.IntegerField(null=False,blank = False),
    
    received_Date = models.DateField(null=False,blank = False),
    date_of_Commisioning = models.DateField(null=False,blank = False),
    pTC_Issued_Date = models.CharField(null=False,blank = False),
    warranty = models.CharField(null=False,blank = False),
    aMC = models.CharField(null=False,blank = False),
    type_of_AMC = models.CharField(null=False,blank = False),
    validity = models.CharField(null=False,blank = False),
    recovery_value = models.CharField(null=False,blank = False),
    age_availability = models.CharField(null=False,blank = False),
    specialization = models.TextField(null=False,blank = False), 
    machine_Picture = models.ImageField(upload_to=None, height_field=None, width_field=None),
    pO_Copy = models.ImageField(upload_to=None),
    accumulated_depreciation_till = models.CharField(null=False,blank = False),
    net_Book_Value1 = models.CharField(null=False,blank = False),  
    give_reference =  models.CharField(null=False,blank = False),  
    current_Market_value = models.CharField(null=False,blank = False),
    net_Book_Value2 = models.CharField(null=False,blank = False),
    whether_Surplus = models.CharField(null=False,blank = False),
    Remarks1 = models.CharField(null=False,blank = False),
    
    
    