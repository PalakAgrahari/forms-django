from django.shortcuts import render,HttpResponse
from users.models import Machine
from .forms import signinForm

from datetime import datetime


def saveForm(request):
    if request.method == "POST":
        emp_no = request.POST.get('equipment_No') or 1
        equipment = request.POST.get('equipment', "")
        Short_Name = request.POST.get('Short_Name', "")
        shop_No = request.POST.get('shop_No', "")
        bay = request.POST.get('bay', "")
        column = request.POST.get('column', "")
        section = request.POST.get('section', "")
        sec_ELN = request.POST.get('sec_ELN', "")
        eqpType = request.POST.get('eqpType', "")
        mc_Se_No = request.POST.get('mc_Se_No', "")
        mc_Model = request.POST.get('mc_Model', "")
        Level1 = request.POST.get('Level1', "")
        level2 = request.POST.get('level2', "")
        list1 = request.POST.get('list1', "")
        list2 = request.POST.get('list2', "")
        manufacturer_Code = request.POST.get('manufacturer_Code', "")
        supplier_Code = request.POST.get('supplier_Code', "")
        indian_Agent = request.POST.get('indian_Agent', "")
        make = request.POST.get('make', "")
        cost_in_Rs_Lakh1 = request.POST.get('cost_in_Rs_Lakh1', "")
        po_no = request.POST.get('po_no', 1) or 1

        pO_Date_str = request.POST.get('pO_Date', "")
        pO_Date = datetime.strptime(pO_Date_str, '%Y-%m-%d').date() if pO_Date_str else None

        unit_Code = request.POST.get('unit_Code', "")
        cost = request.POST.get('cost', "")
        cost_in_Lakh2 = request.POST.get('cost_in_Lakh2', 1) or 1

        received_Date_str = request.POST.get('received_Date', "")
        received_Date = datetime.strptime(received_Date_str, '%Y-%m-%d').date() if received_Date_str else None

        date_of_Commisioning_str = request.POST.get('date_of_Commisioning', "")
        date_of_Commisioning = datetime.strptime(date_of_Commisioning_str, '%Y-%m-%d').date() if date_of_Commisioning_str else None

        pTC_Issued_Date = request.POST.get('pTC_Issued_Date', "")
        warranty = request.POST.get('warranty', "")
        aMC = request.POST.get('aMC', "")
        type_of_AMC = request.POST.get('type_of_AMC', "")
        validity = request.POST.get('validity', "")
        recovery_value = request.POST.get('recovery_value', "")
        age_availability = request.POST.get('age_availability', "")
        specialization = request.POST.get('specialization', "")
        
        machine_Picture = request.FILES.get('machine_Picture', "")
        pO_Copy = request.FILES.get('pO_Copy', "")

        accumulated_depreciation_till = request.POST.get('accumulated_depreciation_till', "")
        net_Book_Value1 = request.POST.get('net_Book_Value1', "")
        give_reference = request.POST.get('give_reference', "")
        current_Market_value = request.POST.get('current_Market_value', "")
        net_Book_Value2 = request.POST.get('net_Book_Value2', "")
        whether_Surplus = request.POST.get('whether_Surplus', "")
        Remarks1 = request.POST.get('Remarks1', "")

        en = Machine(
            equipment_No=emp_no, equipment=equipment, Short_Name=Short_Name, shop_No=shop_No, bay=bay,
            column=column, section=section, sec_ELN=sec_ELN, eqpType=eqpType, mc_Se_No=mc_Se_No,
            mc_Model=mc_Model, Level1=Level1, level2=level2, list1=list1, list2=list2,
            manufacturer_Code=manufacturer_Code, supplier_Code=supplier_Code, indian_Agent=indian_Agent,
            make=make, cost_in_Rs_Lakh1=cost_in_Rs_Lakh1, po_no=po_no, pO_Date=pO_Date, unit_Code=unit_Code,
            cost=cost, cost_in_Lakh2=cost_in_Lakh2, received_Date=received_Date,
            date_of_Commisioning=date_of_Commisioning, pTC_Issued_Date=pTC_Issued_Date, warranty=warranty,
            aMC=aMC, type_of_AMC=type_of_AMC, validity=validity, recovery_value=recovery_value,
            age_availability=age_availability, specialization=specialization, machine_Picture=machine_Picture,
            pO_Copy=pO_Copy, accumulated_depreciation_till=accumulated_depreciation_till,
            net_Book_Value1=net_Book_Value1, give_reference=give_reference,
            current_Market_value=current_Market_value, net_Book_Value2=net_Book_Value2,
            whether_Surplus=whether_Surplus, Remarks1=Remarks1
        )
        en.save()
        return render(request, "index.html")

    # return render(request,"index.html")

def about(request):
    return HttpResponse("This is about")

def Details(request):
    return render(request,"index.html")

def home(request):
    return render(request,"main/home.html")

def signin_data(request):
    if request.method == 'POST':
        form = signinForm(request.POST,request = FILES)
        if form.is_valid():
            
            equipment = form.cleaned_data['SearchEquipment']
            equipment_no = form.cleaned_data['EquipmentNo']
            eqpdescription = form.cleaned_data['EqpDescription']
            short_name = form.cleaned_data['Short_Name']
            salary = form.cleaned_data['emp_salary']

            emp = formdata.objects.create(
                SearchEquipment = equipment,
                EquipmentNo = equipment_no,
                EqpDescription = eqpdescription,
                
                Short_Name = short_name,
                emp_salary=salary,
                
            )
            emp.save()
            return HttpResponse("The data is saved in database")
    form = signinForm()
    return render(request, "main/signin.html", {'form':form})




def services(request):
    return HttpResponse("this is services page") 