$(document).ready(function(){
    htmlStr = category_name.replace(/&#39;/g , "\"");
    htmlStr = htmlStr.replace(/&lt;/g , "");	 
    htmlStr = htmlStr.replace(/&gt;/g , "");     
    htmlStr = htmlStr.replace(/&quot;/g , "\"");  
    htmlStr = htmlStr.replace(/&amp;/g , "");
    console.log(htmlStr)   
    console.log(JSON.parse(htmlStr))
    category_name = JSON.parse(htmlStr)

    function myFunction(value, index, array) {
        txt += '<option value="' +value.category_name+'">'+ value.category_name + "</option>"; 
    }
    
    let txt = '<select class="btn" style="height: 4rem;">';
    category_name.forEach(myFunction);
    txt += '</select>';

    console.log(txt)

    

    // Components
    $(".add-new").click(function(){
        $(this).attr("disabled", "disabled");
        var index = $(".table-component tbody tr:last-child").index();
        
        $('[data-toggle="tooltip"]').tooltip();
        var actions = $(".table-component td:last-child").html();
        var row = '<tr id="somerow">'+
                    '<td> <input style= "width: 100%;" id="category" data-name="category" class="category" data-type="text" required ></td>'+
                    '<td> <input style= "width: 100%;" id="component_title" data-name="component_title" class="component_title" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="description" data-name="description" class="description" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="useful_life" data-name="useful_life" class="useful_life" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="remaining_useful_life" data-name="remaining_useful_life" class="remaining_useful_life" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="current_replacement_cost" data-name="current_replacement_cost" class="current_replacement_cost" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="assessment" data-name="assessment" class="assessment" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="fund_component" data-name="fund_component" class="fund_component" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="notes" data-name="notes" class="notes" data-type="text" required></td>'+
                    '<td>' + actions + '</td>' +
                    '</tr>';
        $(".table-component").append(row); 
        $(".table-component tbody tr").eq(index + 1).find(".add, .edit, .delete").toggle();
        $('[data-toggle="tooltip"]').tooltip();
 
    });

    $(document).on("click", ".add", function(){
        var empty = false;
        var input = $(this).parents("tr").find('input[data-type="text"]');
        input.each(function(){
            if(!$(this).val()){
                $(this).addClass("error");
                empty = true;
            } else{
                $(this).removeClass("error");
            }
        });

        var category = $("#category").val();
        var component_title =$("#component_title").val();
        var description = $("#description").val();
        var useful_life = $("#useful_life").val();
        var remaining_useful_life = $("#remaining_useful_life").val();
        var current_replacement_cost = $("#current_replacement_cost").val();
        var assessment = $("#assessment").val();
        var fund_component = $("#fund_component").val();
        var notes = $("#notes").val();

        $.post("/ajax_add", { category: category, component_title: component_title, description: description, useful_life:useful_life, remaining_useful_life:remaining_useful_life, current_replacement_cost:current_replacement_cost, assessment:assessment, fund_component:fund_component, notes:notes}, function(data) {
            $("#displaymessage").html(data);
            $("#displaymessage").show();
        });
        $(this).parents("tr").find(".error").first().focus();
        if(!empty){
            input.each(function(){
                $(this).parent("td").html($(this).val());
            });   
            $(this).parents("tr").find(".delete").toggle();
            $(".add-new").removeAttr("disabled");
        } 
    });

    $(document).ready(function(){
        var dataTable = $('#sample_data').DataTable();

        $('#sample_data').editable({
            container:'body',
            selector:'td.category',
            url:'/updateemployee',
            title:'Category',
            tpl: txt,
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data').editable({
            container:'body',
            selector:'td.component_title',
            url:'/updateemployee',
            title:'Component Title',
            type:'select',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data').editable({
            container:'body',
            selector:'td.description',
            url:'/updateemployee',
            title:'Description',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data').editable({
            container:'body',
            selector:'td.useful_life',
            url:'/updateemployee',
            title:'Useful Life (years)',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data').editable({
            container:'body',
            selector:'td.remaining_useful_life',
            url:'/updateemployee',
            title:'Remaining Useful Life (years)',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data').editable({
            container:'body',
            selector:'td.current_replacement_cost',
            url:'/updateemployee',
            title:'Current Replacement Cost',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data').editable({
            container:'body',
            selector:'td.assessment',
            url:'/updateemployee',
            title:'Assessment',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data').editable({
            container:'body',
            selector:'td.fund_component',
            url:'/updateemployee',
            title:'Fund Component',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data').editable({
            container:'body',
            selector:'td.notes',
            url:'/updateemployee',
            title:'Notes',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        }); 
    

    // Loans or Other Expenditures
    $(".add-new-loan").click(function(){
        $(this).attr("disabled", "disabled");
        var index = $(".table-loan tbody tr:last-child").index();
        
        $('[data-toggle="loantooltip"]').tooltip();
        var actions_loan = $(".table-loan td:last-child").html();
       
        var row = '<tr>'+
                    '<td> <input style= "width: 100%;" id="year" data-name="year" class="year" data-type="text" required ></td>'+
                    '<td> <input style= "width: 100%;" id="amount_due" data-name="amount_due" class="amount_due" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="description" data-name="description" class="description" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="fund_component" data-name="fund_component" class="fund_component" data-type="text" required></td>'+
                    '<td>' + actions_loan + '</td>' +
                    '</tr>';
        $(".table-loan").append(row); 
        $(".table-loan tbody tr").eq(index + 1).find(".add-loan, .delete-loan").toggle();
        $('[data-toggle="loantooltip"]').tooltip();
    });

    $(document).on("click", ".add-loan", function(){
        var empty = false;
        var input = $(this).parents("tr").find('input[data-type="text"]');
        input.each(function(){
            if(!$(this).val()){
                $(this).addClass("error");
                empty = true;
            } else{
                $(this).removeClass("error");
            }
        });
        var year = $("#year").val();
        var amount_due = $("#amount_due").val()
        var description = $("#description").val()
        var fund_component = $("#fund_component").val()
        $.post("/addother", {year:year, amount_due:amount_due, description: description, fund_component:fund_component}, function(data) {
            $("#displaymessage").html(data);
            $("#displaymessage").show();
        });
        $(this).parents("tr").find(".error").first().focus();
        if(!empty){
            input.each(function(){
                $(this).parent("td").html($(this).val());
            });   
            $(this).parents("tr").find(".add-loan, .delete-loan").toggle();
            $(".add-new-loan").removeAttr("disabled");
        } 
    });
    
    $(document).ready(function(){
        var dataTable = $('#sample_data_loan').DataTable();
        $('#sample_data_loan').editable({
            container:'body',
            selector:'td.year',
            url:'/updateloan',
            title:'Year',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data_loan').editable({
            container:'body',
            selector:'td.amount_due',
            url:'/updateloan',
            title:'Amount Due',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data_loan').editable({
            container:'body',
            selector:'td.description',
            url:'/updateloan',
            title:'Description',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#sample_data_loan').editable({
            container:'body',
            selector:'td.fund_component',
            url:'/updateloan',
            title:'Fund Component',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        });
    
    // Enter Initial Parameters
    $(document).on("click", ".add-initial", function(){
        var empty = false;
        var input = $(this).parents("tr").find('input[data-type="text"]');
        input.each(function(){
            if(!$(this).val()){
                $(this).addClass("error");
                empty = true;
            } else{
                $(this).removeClass("error");
            }
        });

        var fiscal_year_start = $("#fiscal_year_start").val()
        var fiscal_year_end = $("#fiscal_year_end").val()
        var starting_balance = $("#starting_balance").val()
        var current_yearly_reserve_contribution = $("#current_yearly_reserve_contribution").val()
        var proposed_yearly_reserve_contribution = $("#proposed_yearly_reserve_contribution").val()
        var inflation = $("#inflation").val()
        var number_of_units = $("#number_of_units").val()
        var default_interest_rate = $("#default_interest_rate").val()
        var total_assessment_amount_per_month = $("#total_assessment_amount_per_month").val()
        $.post("/initialparameter", {fiscal_year_start:fiscal_year_start, fiscal_year_end:fiscal_year_end,
            starting_balance: starting_balance, current_yearly_reserve_contribution:current_yearly_reserve_contribution,
            proposed_yearly_reserve_contribution:proposed_yearly_reserve_contribution, inflation:inflation, number_of_units:number_of_units,
            default_interest_rate:default_interest_rate, total_assessment_amount_per_month:total_assessment_amount_per_month}, function(data) {
            $("#displaymessage").html(data);
            $("#displaymessage").show();
        });
        $(this).parents("tr").find(".error").first().focus();
        if(!empty){
            input.each(function(){
                $(this).parent("td").html($(this).val());
            });   
            $(this).parents("tr").find(".add-initial").toggle();
            $(this).parents("tr").find(".edit-initial").toggle();
        } 
    });

    $(document).on("click", ".edit-initial", function(){  
        $(this).parents("tr").find("td:not(:last-child)").each(function(i){
            if (i=='0'){
                var idname = 'fiscal_year_start';
                $(this).html('<input type="date" data-type="text" name="updaterec" id="' + idname + '" data-name="' + idname + '" class="' + idname + '" value="' + $(this).text() + '" style="width: 100%;">');
            }else if (i=='1'){
                var idname = 'fiscal_year_end';
                $(this).html('<input type="date" data-type="text" name="updaterec" id="' + idname + '" data-name="' + idname + '" class="' + idname + '" value="' + $(this).text() + '" style="width: 100%;">');
            }else if (i=='2'){
                var idname = 'starting_balance';
                $(this).html('<input type="text" data-type="text" name="updaterec" id="' + idname + '" data-name="' + idname + '" class="' + idname + '" value="' + $(this).text() + '" style="width: 100%;">');
            }else if (i=='3'){
                var idname = 'current_yearly_reserve_contribution';
                $(this).html('<input type="text" data-type="text" name="updaterec" id="' + idname + '" data-name="' + idname + '" class="' + idname + '" value="' + $(this).text() + '" style="width: 100%;">');
            }else if (i=='4'){
                var idname = 'proposed_yearly_reserve_contribution';
                $(this).html('<input type="text" data-type="text" name="updaterec" id="' + idname + '" data-name="' + idname + '" class="' + idname + '" value="' + $(this).text() + '" style="width: 100%;">');
            }else if (i=='5'){
                var idname = 'inflation';
                $(this).html('<input type="text" data-type="text" name="updaterec" id="' + idname + '" data-name="' + idname + '" class="' + idname + '" value="' + $(this).text() + '" style="width: 100%;">');
            }else if (i=='6'){
                var idname = 'number_of_units';
                $(this).html('<input type="text" data-type="text" name="updaterec" id="' + idname + '" data-name="' + idname + '" class="' + idname + '" value="' + $(this).text() + '" style="width: 100%;">');
            }else if (i=='7'){
                var idname = 'default_interest_rate';
                $(this).html('<input type="text" data-type="text" name="updaterec" id="' + idname + '" data-name="' + idname + '" class="' + idname + '" value="' + $(this).text() + '" style="width: 100%;">');
            }else if (i=='8'){
                var idname = 'total_assessment_amount_per_month';
                $(this).html('<input type="text" data-type="text" name="updaterec" id="' + idname + '" data-name="' + idname + '" class="' + idname + '" value="' + $(this).text() + '" style="width: 100%;">');
            }else {}
            
        });  
        $(this).parents("tr").find(".add-initial, .edit-initial").toggle();
        $(this).parents("tr").find(".add-initial").removeClass("add-initial").addClass("update-initial"); 
    });

    $(document).on("click", ".update-initial", function(){
        var empty = false;
        var input = $(this).parents("tr").find('input[data-type="text"]');
        input.each(function(){
            if(!$(this).val()){
                $(this).addClass("error");
                empty = true;
            }else{
                $(this).removeClass("error");
            }
        });
        var id = $(this).attr("id");
        var string = id;
        var fiscal_year_start = $("#fiscal_year_start").val();
        var fiscal_year_end = $("#fiscal_year_end").val();
        var starting_balance = $("#starting_balance").val();
        var current_yearly_reserve_contribution = $("#current_yearly_reserve_contribution").val();
        var proposed_yearly_reserve_contribution = $("#proposed_yearly_reserve_contribution").val();
        var inflation = $("#inflation").val();
        var number_of_units = $("#number_of_units").val();
        var default_interest_rate = $("#default_interest_rate").val();
        var total_assessment_amount_per_month = $("#total_assessment_amount_per_month").val();
        $.post("/updateinitial", { string: string,fiscal_year_start: fiscal_year_start, fiscal_year_end: fiscal_year_end, starting_balance: starting_balance,
            current_yearly_reserve_contribution:current_yearly_reserve_contribution, proposed_yearly_reserve_contribution:proposed_yearly_reserve_contribution,
            inflation:inflation, number_of_units:number_of_units, default_interest_rate:default_interest_rate, total_assessment_amount_per_month:total_assessment_amount_per_month}, function(data) {
            $("#displaymessage").html(data);
            $("#displaymessage").show();
        });
        $(this).parents("tr").find(".error").first().focus();
        if(!empty){
            input.each(function(){
                $(this).parent("td").html($(this).val());
            });   
            $(this).parents("tr").find(".update-initial").removeClass("update-initial").addClass("add-initial"); 
            $(this).parents("tr").find(".add-initial, .edit-initial").toggle();
        }    
    });

    // Units if Variable
    $(".add-unit-variable").click(function(){
        $(this).attr("disabled", "disabled");
        var index = $(".table-unit tbody tr:last-child").index();
        
        $('[data-toggle="unittooltip"]').tooltip();
        var actions_loan = $(".table-unit td:last-child").html();
       
        var row = '<tr>'+
                    '<td> <input style= "width: 100%;" id="unit" data-name="unit" class="unit" data-type="text" required ></td>'+
                    '<td> <input style= "width: 100%;" id="building" data-name="building" class="building" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="address" data-name="address" class="address" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="square_footage" data-name="square_footage" class="square_footage" data-type="text" required></td>'+
                    '<td> <input style= "width: 100%;" id="percentage" data-name="percentage" class="percentage" data-type="text" required></td>'+
                    '<td>' + actions_loan + '</td>' +
                    '</tr>';
        $(".table-unit").append(row); 
        $(".table-unit tbody tr").eq(index + 1).find(".add-unit, .delete-unit").toggle();
        $('[data-toggle="unittooltip"]').tooltip();
    });

    $(document).on("click", ".add-unit", function(){
        var empty = false;
        var input = $(this).parents("tr").find('input[data-type="text"]');
        input.each(function(){
            if(!$(this).val()){
                $(this).addClass("error");
                empty = true;
            } else{
                $(this).removeClass("error");
            }
        });
        var unit = $("#unit").val();
        var building = $("#building").val()
        var address = $("#address").val()
        var square_footage = $("#square_footage").val()
        var percentage = $("#percentage").val()
        $.post("/addunit", {unit:unit, building:building, address: address, square_footage:square_footage,percentage:percentage}, function(data) {
            $("#displaymessage").html(data);
            $("#displaymessage").show();
        });
        $(this).parents("tr").find(".error").first().focus();
        if(!empty){
            input.each(function(){
                $(this).parent("td").html($(this).val());
            });   
            $(this).parents("tr").find(".add-unit, .delete-unit").toggle();
            $(".add-unit-variable").removeAttr("disabled");
        } 
    });

    $(document).ready(function(){
        var dataTable = $('#unit_variable').DataTable();
        $('#unit_variable').editable({
            container:'body',
            selector:'td.unit',
            url:'/updateunit',
            title:'Unit',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#unit_variable').editable({
            container:'body',
            selector:'td.building',
            url:'/updateunit',
            title:'Building',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#unit_variable').editable({
            container:'body',
            selector:'td.address',
            url:'/updateunit',
            title:'Address',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#unit_variable').editable({
            container:'body',
            selector:'td.square_footage',
            url:'/updateunit',
            title:'Square Footage',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
        $('#unit_variable').editable({
            container:'body',
            selector:'td.percentage',
            url:'/updateunit',
            title:'Percentage',
            type:'POST',
            validate:function(value){
                if($.trim(value) == '')
                {
                    return 'This field is required';
                }
            }
        });
    });

    // Scenarios Management
    // $(document).ready(function(){
    //     var dataTable = $('#scenario-data').DataTable();
    // });
});