$(document).ready(function() {
    $('#cpart1').hide();
    $('#cpart2').hide();
    $('#cpart3').hide();
    $('#cpart4').hide();

    var num_parts = parseInt($("#number_parts option:selected").val());
    switch (num_parts) {
        case 0:
            break;
        case 1:
            $('#cpart1').show();
            break;
        case 2:
            $('#cpart1').show();
            $('#cpart2').show();
            break;
        case 3:
            $('#cpart1').show();
            $('#cpart2').show();
            $('#cpart3').show();
            break;
    }

    $("#number_parts").change(function() {
        var count_parts = parseInt($("#number_parts option:selected").val());
        if (count_parts == 0) {
            $('#cpart1').hide();
            $('#cpart2').hide();
            $('#cpart3').hide();
        } else if (count_parts ==1) {
            $('#cpart1').show();

            $('#cpart2').hide();
            $('#cpart3').hide();
        } else if (count_parts ==2) {
            $('#cpart1').show();
            $('#cpart2').show();

            $('#cpart3').hide();
        } else if (count_parts ==3) {
            $('#cpart1').show();
            $('#cpart2').show();
            $('#cpart3').show();
        }
    });

    $("#question_type").change(function(){
        if ($("#question_type option:selected").val() == "EX") {
            $('#paper').show();
        } else {
            $('#paper').hide();
        }
    });
} );
