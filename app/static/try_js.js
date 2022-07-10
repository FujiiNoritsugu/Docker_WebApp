let is_red = true;

function change_table(){
    table_obj = document.getElementById('table_id');
    if (is_red){
        table_obj.style.backgroundColor = "red";
        is_red = false;
    }else{
        table_obj.style.backgroundColor = "";
        is_red = true;
    }
}

function change_by_select(){
    select_obj = document.getElementById('select_id');
    table_obj = document.getElementById('table_id');
    table_obj.style.backgroundColor = select_obj.value;
}
